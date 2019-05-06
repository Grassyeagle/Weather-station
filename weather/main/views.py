from django.shortcuts import render
from api.models import Temperature , H , Bp
from datetime import datetime, timedelta
from django.db.models import Max, Min

def c2f(celsius):
    return ((celsius*9/5)+32)
# Create your views here.
def home(request):
    # Find the newest single temperature
    temp =   Temperature.objects.order_by('-record_time').first()
    # Gather the total number of temperature readings gathered.
    tcount = Temperature.objects.count()
    # Find the first temperature entry recorded
    tfirst = Temperature.objects.order_by('record_time').first()
     # Find the newest single temperature
    h =   H.objects.order_by('-record_time').first()
    # Gather the total number of temperature readings gathered.
    Hcount = H.objects.count()
    # Find the first temperature entry recorded
    Hfirst = H.objects.order_by('record_time').first()
    p =   Bp.objects.order_by('-record_time').first()
    # Gather the total number of temperature readings gathered.
    Pcount = Bp.objects.count()
    # Find the first temperature entry recorded
    Pfirst = Bp.objects.order_by('record_time').first()
    now = datetime.now()
    some_time_ago = now - timedelta(days=7)
    tmax = c2f(Temperature.objects.filter(record_time__range=(some_time_ago, now)).aggregate(Max('celsius'))['celsius__max'])
    hmax = H.objects.filter(record_time__range=(some_time_ago, now)).aggregate(Max('rh'))['rh__max']
    pmax = Bp.objects.filter(record_time__range=(some_time_ago, now)).aggregate(Max('p'))['p__max']
    hmin = H.objects.filter(record_time__range=(some_time_ago, now)).aggregate(Min('rh'))['rh__min']
    pmin = Bp.objects.filter(record_time__range=(some_time_ago, now)).aggregate(Min('p'))['p__min']
    tmin = c2f(Temperature.objects.filter(record_time__range=(some_time_ago, now)).aggregate(Min('celsius'))['celsius__min'])
    return render(request, 'home.html', {
        'temp': temp,
         'tcount': tcount, 
         'tfirst': tfirst.record_time ,
         'h': h,
         'Hcount': Hcount, 
         'Hfirst': Hfirst.record_time,
         'p': p ,
         'Pcount': Pcount, 
         'Pfirst': Pfirst.record_time,
         'tmax':tmax,
         'hmax':hmax,
         'pmax':pmax,
         'tmin':tmin,
         'hmin':hmin,
         'pmin':pmin,
    }
)


   