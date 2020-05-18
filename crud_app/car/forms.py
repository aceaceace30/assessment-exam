from django import forms
from .models import Car

class CarSearchForm(forms.Form):

	COLOR = list(Car.COLOR)
	COLOR.insert(0, ['', '----'])

	def __init__(self, *args, **kwargs):
		super(CarSearchForm, self).__init__(*args, **kwargs)
		for myField in self.fields:
			self.fields[myField].widget.attrs['class'] = 'form-control form-control-md'

	color = forms.ChoiceField(label='Select a color', choices=COLOR)

class CarForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(CarForm, self).__init__(*args, **kwargs)
		for myField in self.fields:
			self.fields[myField].widget.attrs['class'] = 'form-control form-control-md'

	car = forms.ModelChoiceField(queryset=Car.objects.all().order_by('-pk'))