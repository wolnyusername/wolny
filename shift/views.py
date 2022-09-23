from django.shortcuts import render, redirect
from . import models
import datetime
from .models import Shift, Worker
from django.views.generic.base import TemplateView


#def index(request):
    #from pdb import set_trace;set_trace()
#    context = {}
#   context['logged'] = False
#   if request.method == 'POST':
#       user = models.Worker.objects.filter(login=request.POST.get('login'))
#       if len(user) == 0:
#           context['wrong_user'] = True
#        else:
#            if user[0].password == request.POST.get('password'):
 #               request.session['user'] = user[0].pk
  #              request.session['logged'] = True
   #             context['logged'] = True
    #            if Shift.objects.filter(worker=request.session.get('user'), end_time=None).count() == 0:
     #               context['shift_started'] = False
      #          else:
       #             context['shift_started'] = True
        #        return redirect('home')
         #   else:
          #      context['wrong_password'] = True
   # return render(request, 'shift/index.html', context=context)
class ContextView(TemplateView):
    context = {'logged': False}
    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        if "user" in request:
            context['logged'] = True
            if Shift.objects.filter(worker=request.get('user'), end_time=None).count() == 0:
                context['shift_started'] = False
            else:
                context['shift_started'] = True
        return context


class LoginView(ContextView):
    template_name = 'index.html'
    def post(self, request):
        user = models.Worker.objects.filter(login=request.POST.get('login'))
        if len(user) == 0:
            self.context['wrong_user'] = True
        else:
            if user[0].password == request.POST.get('password'):
                request.session['user'] = user[0].pk
                request.session['logged'] = True
                return redirect('home')
            else:
                self.context['wrong_password'] = True

class HomeView(ContextView):
    def get(self, request):
        if request.session['logged'] is True:
            self.context['logged'] = True
            if Shift.objects.filter(worker=request.session.get('user'), end_time=None).count() == 0:
                self.context['shift_started'] = False
            else:
                self.context['shift_started'] = True
        else:
            return redirect('login')
        return render(request, 'shift/home.html', context=self.context)


#def home(request):
 #   context = {}
  #  if request.session['logged'] is True:
   #     context['logged'] = True
    #    if Shift.objects.filter(worker=request.session.get('user'), end_time=None).count() == 0:
     #       context['shift_started'] = False
      #  else:
       #     context['shift_started'] = True
#    else:
 #       return redirect('login')
  #  return render(request, 'shift/home.html', context=context)

#def user_start_shift(request):
 #   user_id = request.session.get('user')
  #  new_shift = Shift(worker=Worker.objects.get(id=user_id))
   # new_shift.save()
    #return redirect(request.META['HTTP_REFERER'])

class UserStartShiftView(ContextView):
    def get(self, request):
        user_id = request.session.get('user')
        new_shift = Shift(worker=Worker.objects.get(id=user_id))
        new_shift.save()
        return redirect(request.META['HTTP_REFERER'])

class UserEndShiftView(ContextView):
    def get(self, request):
        user_id = request.session.get('user')
        Shift.objects.filter(worker=Worker.objects.get(id=user_id), end_time=None).update(
            end_time=datetime.datetime.now())
        return redirect(request.META['HTTP_REFERER'])

#def user_end_shift(request):
 #   user_id = request.session.get('user')
  #  Shift.objects.filter(worker=Worker.objects.get(id=user_id), end_time=None).update(end_time=datetime.datetime.now())
   # return redirect(request.META['HTTP_REFERER'])

#def log_out(request):
 #   request.session.flush()
  #  return redirect('login')

class LogOutView(ContextView):
    def get(self, request):
        request.session.flush()
        self.context.clear()
        return redirect('login')

