from django.db import models

# Create your models here.
class Item(models.Model):
	"""docstring for Item"""
	text = models.TextField(default='')
	list = models.TextField(default = '')
class List(models.Model):
	text = models.TextField(default='')

