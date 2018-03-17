from django.db import models

class Topic(models.Model):
	top_name = models.CharField(max_length=264, unique=True)

	def __str__(self):
		return self.top_name

class webpage(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(webpage, on_delete=models.PROTECT)
	date = models.DateField()

	def __str__(self):
		return str(self.date)

class TestUsers(models.Model):
	firstName = models.CharField(max_length=128)
	lastName = models.CharField(max_length=128)
	email = models.EmailField(max_length=128, unique=True)
