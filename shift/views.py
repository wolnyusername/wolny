from django.shortcuts import render, redirect
from . import models
import datetime
from .models import Shift, Worker


def index(request):
    #from pdb import set_trace;set_trace()
    context = {}
    if request.method == 'POST':
        user = models.Worker.objects.filter(login=request.POST.get('login'))
        if len(user) == 0:
            context['wrong_user'] = True
        else:
            if user[0].password == request.POST.get('password'):
                request.session['user'] = user[0].pk
                user_shifts = list(Shift.objects.filter(worker=request.session.get('user'), end_time=None))
                if len(user_shifts) == 0:
                    return redirect('user_start_shift')
                else:
                    return redirect('user_end_shift')
            else:
                context['wrong_password'] = True
    return render(request, 'shift/index.html', context=context)

def home(request):
    user_shifts = list(Shift.objects.filter(worker=request.session.get('user'), end_time=None))
    user_id = request.session.get('user')

    return render(request, 'shift/home.html')

def user_start_shift(request):
    context = {}
    user_shifts = list(Shift.objects.filter(worker=request.session.get('user'), end_time=None))
    user_id = request.session.get('user')
    if len(user_shifts) == 0:
        context['shift_not_started'] = True
        if request.method == 'POST':
            new_shift = Shift(worker=Worker(id=user_id))
            new_shift.save()
    return render(request, 'shift/home.html', context=context)

def user_end_shift(request):
    context = {}
    user_shifts = list(Shift.objects.filter(worker=request.session.get('user'), end_time=None))
    user_id = request.session.get('user')
    if len(user_shifts) > 0:
        context['shift_already_started'] = True
        if request.method == 'POST':
            Shift.objects.filter(worker=Worker(id=user_id), end_time=None).update(end_time=datetime.datetime.now())
    return render(request, 'shift/home.html', context=context)

def user_logout(request):
    if request.POST.get('logout') == 'logout':
        request.session.flush()
        return redirect('index')
    return render(request, 'shift/home.html', context=context)