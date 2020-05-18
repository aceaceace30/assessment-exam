from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarSearchForm, CarForm
from django.http import HttpResponse

from django.template.loader import render_to_string

def move_cars(request, pk):

	if request.method == 'POST':
		from_car = Car.objects.get(pk=pk)
		selected_car_id = request.POST.get('car_id')
		to_car = Car.objects.get(order=selected_car_id)

		to_car.order = from_car.order
		from_car.order = selected_car_id

		from_car.save()
		to_car.save()

		data = render_to_string('car/ajax_cars.html', {'cars': Car.objects.all()})

		return HttpResponse(data)


def view_cars(request):

	if request.method == 'POST':
		form = CarSearchForm(request.POST)
		if form.is_valid():
			cars = Car.objects.filter(color=form.cleaned_data['color'])
	else:
		cars = Car.objects.all()
		form = CarSearchForm()
	
	car_select = CarForm()

	context = {'cars': cars,
			   'form': form,
			   'car_select': car_select,}
	
	return render(request, 'car/view_cars.html', context)
	
