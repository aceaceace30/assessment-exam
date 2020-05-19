from car.models import Car
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):

	help = "Populate 100,000 rows of car"

	def handle(self, *args, **kwargs):
		for i in range(50):
			i += 1
			Car.objects.create(order=i, color=Car.COLOR[random.randint(0, (len(Car.COLOR)-1))][0])

			