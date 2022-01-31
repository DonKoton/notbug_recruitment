from django.urls import reverse_lazy

from cars.models import Car, Parts
from cars.forms import PartsList, CarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


class CarsList(ListView):
    model = Car
    template_name = 'cars/cars_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = Parts.objects.filter(car_id=self.kwargs['pk'])
        return context


class StoreCarView(CreateView):
    model = Car
    template_name = 'cars/store_car.html'
    form_class = CarForm


class AddPartView(CreateView):
    model = Parts
    template_name = 'cars/add_part.html'
    form_class = PartsList

    def form_valid(self, form):
        form.instance.car = Car.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(AddPartView, self).form_valid(form)


class UpdateCarView(UpdateView):
    model = Car
    template_name = 'cars/update.html'
    form_class = CarForm


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('cars:cars_list')
