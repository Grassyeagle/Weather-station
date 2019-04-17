from django.shortcuts import render
from api.models import Temperature , H , Bp


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
    }
)


   