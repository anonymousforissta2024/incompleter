#Source: https://stackoverflow.com/questions/67764955/init-takes-1-positional-argument-but-2-were-given-type-error
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AvonleaForm
from .models import AvonleaClass
from django.contrib import messages
from django.views import View


#Operational

def home(request):
    return render(request, 'meter_readings/home.html' )


# Complexes

#AVONLEA
#
#
#

class AvonleaView( View):

    def get(self,request):
        created_nums= AvonleaClass.objects.all().values('unitNumber')

        Aprev = AvonleaClass.objects.all().order_by('-unitDateEntered')
        previousReading = Aprev[1].newReading
        # created_nums= AvonleaClass.objects.all()
        print(created_nums , previousReading)

        created_nums =[int(i['unitNumber']) for i in created_nums]
        print(created_nums , previousReading)

        form = AvonleaForm()
        return render(request,"meter_readings/avonlea.html",{'form':form , 'created_nums':created_nums , 'name':name, 'previousReading' : previousReading })

    def post(self,request):
        created_nums= AvonleaClass.objects.all().values_list('unitNumber')
        print(created_nums)
        form = AvonleaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unt-url' , name )
            messages.success(request , 'creates successfully ')
        else:
            return render(request, 'meter_readings/avonlea.html', {'form': form ,  created_nums:created_nums })

def currentavonleas(request):
    avonleas = AvonleaClass.objects.all()
    return render(request, 'meter_readings/currentavonleas.html', {'avonleas':avonleas})

def viewavonlea(request,  avonleas_pk):
    avonlea = get_object_or_404(AvonleaClass, pk=avonleas_pk)
    if request.method == 'GET':
        form = AvonleaForm(instance=avonlea)
        return render(request, 'meter_readings/viewavonleas.html', {'avonlea': avonlea, 'form':form})
    else:
        try:
            form =  AvonleaForm(request.POST, instance=avonlea)
            form.save()
            return redirect('Avonlea')
        except ValueError:
            return render(request, 'meter_readings/viewavonleas.html', {'avonlea': avonlea, 'form':form, 'error':'Bad info'})

def deleteavonlea(request, avonleas_pk):
    avonlea = get_object_or_404(AvonleaClass, pk=avonleas_pk)
    if request.method == 'POST':
        avonlea.delete()
        return redirect('Avonlea')

import csv
def Avonleacsv(request):
    data =AvonleaClass.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="saved_file.csv"'
    writer = csv.writer(response)
    writer.writerow(['Unit', 'Number of Units'
                     ])
    for avonleaclass in data:
        writer.writerow([
                        avonleaclass.unitNumber,
                        avonleaclass.newReading,
                         ])
    return response