from django.shortcuts import redirect, render
from .models import Car, Part
from .forms import MaintenanceForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# CBV(Class Based View) functions

class CarCreate(CreateView):
    model = Car
    fields = ['year', 'make', 'model', 'comment']

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

# Create your views here.
def add_maintenance(request, car_id):
    form = MaintenanceForm(request.POST)

    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.car_id = car_id
        new_maintenance.save()
    return redirect('detail', car_id=car_id)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    parts_car_doesnt_have = Part.objects.exclude(id__in = car.parts.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', { 
        'car': car,
        'maintenance_form': maintenance_form, 
        'parts': parts_car_doesnt_have
        })

def assoc_part(request, car_id, part_id):
    Car.objects.get(id=car_id).parts.add(part_id)
    return redirect('detail', car_id=car_id)

class PartList(ListView):
    model = Part

class PartDetail(DetailView):
    model = Part

class PartCreate(CreateView):
    model = Part
    fields = '__all__'

class PartUpdate(UpdateView):
    model = Part
    fields = ['name', 'type']

class PartDelete(DeleteView):
    model = Part
    success_url = '/parts/'
