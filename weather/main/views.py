from django.shortcuts import render
from api.models import Temperature

# Create your views here.
def home(request):
    # Find the newest single temperature
    temp =   Temperature.objects.order_by('-record_time').first()
    # Gather the total number of temperature readings gathered.
    tcount = Temperature.objects.count()
    # Find the first temperature entry recorded
    tfirst = Temperature.objects.order_by('record_time').first()
    
    return render(request, 'home.html', {
        'temp': temp,
         'tcount': tcount, 
         'tfirst': tfirst.record_time}
)