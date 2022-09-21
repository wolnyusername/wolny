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
                request.session['logged'] = True
                return redirect('home')
            else:
                context['wrong_password'] = True
    return render(request, 'shift/index.html', context=context)

def home(request):
    user_shifts = list(Shift.objects.filter(worker=request.session.get('user'), end_time=None))
    context = {}
    if request.session['logged'] is True:
        if len(user_shifts) == 0:
            context['shift_started'] = False
        else:
            context['shift_started'] = True
        if context['shift_started'] is False:
            return redirect('user_start_shift')
        else:
            return redirect('user_end_shift')
    else:
        return redirect('index')

def user_start_shift(request):
    user_id = request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('start') == 'start':
            new_shift = Shift(worker=Worker(id=user_id))
            new_shift.save()
            return redirect('home')
        if request.POST.get('logout') == 'logout':
            request.session.flush()
            return redirect('index')
    return render(request, 'shift/home.html')

def user_end_shift(request):
    user_id = request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('end') == 'end':
            Shift.objects.filter(worker=Worker(id=user_id), end_time=None).update(end_time=datetime.datetime.now())
            return redirect('home')
        if request.POST.get('logout') == 'logout':
            request.session.flush()
            return redirect('index')
    return render(request, 'shift/home.html')