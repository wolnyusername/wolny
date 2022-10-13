import datetime

from django import template
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import View
from django.views.generic.base import TemplateView

from . import models
from .models import Shift, Worker


class ContextView(TemplateView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if "user_id" in self.request.session:
            context['logged'] = True
            if Shift.objects.filter(worker=self.request.session.get('user_id'), end_time=None).count() == 0:
                context['shift_started'] = False
            else:
                context['shift_started'] = True
        return context

class LoginView(ContextView):
    template_name = 'shift/index.html'
    def post(self, request):
        user = models.Worker.objects.filter(login=request.POST.get('login'))
        if models.Worker.objects.filter(login=request.POST.get('login')).count() == 0:
            self.context['wrong_user'] = True
        else:
            if user[0].password == request.POST.get('password'):
                request.session['user_id'] = user[0].id
                request.session['logged'] = True
                return redirect('home')
            else:
                self.context['wrong_password'] = True

class HomeView(ContextView):
    template_name = 'shift/home.html'

class UserStartShiftView(View):
    def get(self, request):
        new_shift = Shift(worker=models.Worker.objects.get(id=request.session['user_id']))
        new_shift.save()
        return redirect(request.META['HTTP_REFERER'])

class UserEndShiftView(View):
    def get(self, request):
        Shift.objects.filter(worker=Worker.objects.get(id=request.session['user_id']), end_time=None).update(
            end_time=timezone.now())
        return redirect(request.META['HTTP_REFERER'])

class LogOutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')

class DeleteShiftView(View):
    def post(self,request):
        shift_list = request.POST.getlist('shift_id')
        for i in shift_list:
            Shift.objects.filter(id=i).delete()
        return redirect(request.META['HTTP_REFERER'])

class ShiftListView(ContextView):
    template_name = 'shift/listofshift.html'
    def get_context_data(self,**kwargs):
        #import pdb; pdb.set_trace()
        context = super().get_context_data(**kwargs)
        sort = self.request.GET.get('sorting_field') or 'start_time'
        q = Shift.objects.filter(worker=self.request.session.get('user_id'))
        direction = self.request.GET.get('direction')
        print(self.request.GET)
        q = q.order_by(sort)
        if direction != "asc":
            q=q.reverse()
        p = Paginator(q, 20)
        context['shift_list'] = p.page(self.request.GET.get('page') or 1)
        context['sorting_field'] = sort
        context['direction'] = direction
        return context

    def get(self,request):
        sorting_values = {"start_time", "end_time"}
        if request.GET.get('sorting_field'):
            if request.GET.get('sorting_field') not in sorting_values:
                return redirect('list_of_shifts')
        return super(ShiftListView, self).get(request)

