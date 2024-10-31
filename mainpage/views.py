from django.shortcuts import render
from django.shortcuts import render, redirect

from . import models
from . import forms
from datetime import datetime
from datetime import timedelta

def index(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/index.html', 
        context={ 
        } 
    )# Create your views here.

def contacts(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/contacts.html', 
        context={ 
        } 
    )# Create your views here.
    
def about_us(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/about_us.html', 
        context={ 
        } 
    )# Create your views here.
    
def menu(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/menu.html', 
        context={ 
        } 
    )# Create your views here.
    
def services(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/services.html', 
        context={ 
        } 
    )# Create your views here.
    

# timeslots = {
#    '10:00': {
#            'time': '10:00',
#            'weekdays': [
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#            ]
#        }
# }
def newWeek(dt):
    work_starts = 10   # 10:00 утра
    slots_per_day = 23  # 12 по полчаса
    # Создадим слоты
    timeslots = {}
    s = datetime(dt.year, dt.month, dt.day, work_starts)
    while s < dt + timedelta(7):  # next week
        wd = []
        for i in range(7):
            wd.append({
                'free': True
            })
        tm = s.strftime('%H:%M')
        timeslots[tm] = {
            'time': tm,
            'weekdays': wd,
            'datetime': s.strftime('%Y-%m-%dT%H:%M'),
        }
        s += timedelta(seconds=1800)  # 3600 = 60*60 - это час в секундах
        if s.hour > work_starts + slots_per_day / 2:
            s += timedelta(1)
            s = datetime(s.year, s.month, s.day, work_starts)
    return timeslots


def create_visit(request, dtstr=''):
    if request.method == "POST":
        print(request.POST)
        form = forms.VisitForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #form.save()
    form = forms.VisitForm(initial={'start_time': dtstr})
    return render(
        request,                    # Запрос
	    'mainpage/visit.html',   # путь к шаблону
        {
            'visitform': form,
            'currtime': 'default'
        }                     # подстановки
    )  

def calender(request, dtstr=''):
    dt = datetime.now()
    try:
        dt = datetime.strptime(dtstr, '%Y%m%d')
    except:
        return redirect(dt.strftime('/calender/%Y%m%d'))
    if dt.weekday():  # 0 - понедельник
        return redirect((dt - timedelta(dt.weekday())).strftime('/calender/%Y%m%d'))
    dt_next = dt + timedelta(7)  # next week
    timeslots = newWeek(dt)
    # Все задачи на эту неделю
    visits = models.Visit.objects.filter(  # Достаточно фильтровать по одному параметру, если все слоты умещаются в текущие сутки и никто заполночь не работает
        start_time__gte=dt.strftime('%Y-%m-%d')
    ).filter(end_time__lte=dt_next.strftime('%Y-%m-%d'))
    print(visits)
    for t in visits:
        tm = t.start_time.strftime('%H:%M')
        #print(t.description, t.softline, tm)
        #print(timeslots[tm])
        if tm in timeslots:
            s = timeslots[tm]['weekdays'][t.start_time.weekday()]
            s['free'] = False
            s['task'] = t
    # Превращаем в список, чтобы потом не мучиться упорядочиваением
    timeslots_list = []
    for key in sorted(list(timeslots.keys())):
        timeslots_list.append(timeslots[key])
    context = {
        'prev_week': (dt - timedelta(7)).strftime('%Y%m%d'),
        'curr_week': (dt).strftime('%Y%m%d'),
        'next_week': (dt + timedelta(7)).strftime('%Y%m%d'),
        'timeslots': timeslots_list,
    }
    return render(
        request,                    # Запрос
	    'mainpage/calender.html',   # путь к шаблону
        context                     # подстановки
    )     
    
  
    
