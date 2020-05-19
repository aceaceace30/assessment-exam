from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarSearchForm, CarForm
from django.http import HttpResponse, JsonResponse

from django.template.loader import render_to_string

def move_cars(request, pk):

	if request.method == 'POST':

		form = CarForm(request.POST)

		if form.is_valid():
			car_to_be_moved = Car.objects.get(pk=pk) #order - 793
			position = form.cleaned_data['position'] # before(-1) or after(+1) the selected car
			car_selected = Car.objects.get(pk=form.cleaned_data['car'].pk) #order - 786

			if position == 'before':
				order_value = car_selected.order - 1
			else:
				order_value = car_selected.order + 1

			# select all the cars needed to update by order make sure to remove the selected
			if car_to_be_moved.order > car_selected.order:
				cars_to_update = Car.objects.filter(order__gte=order_value, order__lt=car_to_be_moved.order).exclude(pk=car_to_be_moved.pk).order_by('order')
			else:
				cars_to_update = Car.objects.filter(order__gt=car_to_be_moved.order, order__lte=order_value).exclude(pk=car_to_be_moved.pk).order_by('-order')

			for update in cars_to_update:
				if car_to_be_moved.order > car_selected.order:
					update.order=update.order+1
				else:
					update.order=update.order-1
				update.save()

			# update the value of the car to be moved
			car_to_be_moved.order = order_value
			car_to_be_moved.save()

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
	
