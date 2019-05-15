from django.shortcuts import render
from api.models import Temperature , H , Bp
from datetime import datetime, timedelta
from django.db.models import Max, Min, F
from chartjs.views.lines import BaseLineChartView
def c2f(celsius):
    return ((celsius*9/5)+32)

        

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
class LineChartView(BaseLineChartView):
    type = ' '
    labels =[]
    max_list = []
    min_list = []
  
    def last_seven_days(self):
        self.type = self.kwargs.get('type')
        now = datetime.now()
        seven_days_ago = now - timedelta(days=7)
    
        if self.type == 'rh':
            datas = H.objects.order_by('record_time').filter(record_time__range=(seven_days_ago, now)).annotate(value=F('rh'))
        elif self.type == 'celsius':
            datas = Temperature.objects.order_by('record_time').filter(record_time__range=(seven_days_ago, now)).annotate(value=F('celsius'))    
        else:
            datas = Bp.objects.order_by('record_time').filter(record_time__range=(seven_days_ago, now)).annotate(value=F('p'))
            
        for data in datas:
            weekday = datetime.weekday(data.record_time)
            if days[weekday] not in self.labels:
                self.labels.append(days[weekday])
    
        self.max_list = [-100 for i in range(len(self.labels))]
        self.min_list = [99999999 for i in range(len(self.labels))]
        for data in datas:
             weekday = datetime.weekday(data.record_time)
             idx = self.labels.index(days[weekday])
             self.set_minmax(idx, data.value)
      
    def get_providers(self):
        return ['Max','Min']
    
    def get_labels(self):
        return self.labels
    
    def get_data(self):
        self.last_seven_days() 
        return [self.max_list, self.min_list]
        
    
    def set_minmax(self, index, item):
        if self.type == 'temp':
            item = c2f(item)
        if item > self.max_list[index]:
            self.max_list[index] = item
        if item < self.min_list[index]:
            self.min_list[index] = item
                 
    
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
    some_time_ago = now - timedelta(days=1)
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


   