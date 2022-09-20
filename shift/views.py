from django.shortcuts import render, redirect
from . import models
import datetime

from .models import Shift, Worker


def index(request):
    #from pdb import set_trace;set_trace()
    context = {}
    if request.method == 'POST':
        log = models.Worker.objects.filter(login=request.POST.get('login'))
        if len(log) == 0:
            context['wrong_user'] = True
        else:
            if log[0].password == request.POST.get('password'):
                request.session['user'] = log[0].pk
                return redirect('home')
            else:
                context['wrong_password'] = True
    return render(request, 'shift/index.html', context=context)


def home(request):
    context = {}
    z = list(request.session.values())
    if request.method == 'POST':
        if request.POST.get('start') == 'start':
            s = Shift.objects.filter(worker=z[0], end_time=None)
            if len(s) > 0:
                context['shift_already_started'] = True
            else:
                work = Worker.objects.get(id=z[0])
                temp = Shift(worker=work)
                temp.save()
        if request.POST.get('end') == 'end':
            s=Shift.objects.filter(end_time=None)
            if len(s) <= 0:
                context['shift_not_started'] = True
            else:
                Shift.objects.filter(end_time=None).update(end_time=datetime.datetime.now())
        if request.POST.get('logout') == 'logout':
            request.session.clear()
            return redirect('index')
    return render(request, 'shift/home.html', context=context)
