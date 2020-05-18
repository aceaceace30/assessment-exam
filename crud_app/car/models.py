from django.db import models

class Car(models.Model):

	COLOR = (
		('red', 'Red'),
		('blue', 'Blue')
		)

	order = models.IntegerField()
	color = models.CharField(choices=COLOR, max_length=15)

	class Meta:
		ordering = ['-order']

	def __str__(self):
		return '%s | %s' % (str(self.pk), self.color)