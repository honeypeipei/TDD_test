from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from django.test import TestCase
from lists.models import Item,List
from django.core.exceptions import ValidationError

# Create your tests here.
class ListAndItemModelTest(TestCase):

	def test_default_text(self):
		item = Item()
		self.assertEqual(item.text, '')

    #双重保险，确认外键关联是否正常
	def test_item_is_ralated_to_list(self):
		list_ = List.objects.create()
		item = Item()
		item.list = list_
		item.save()
		self.assertIn(item, list_.item_set.all())


	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item(list = list_, text = '')
		with self.assertRaises(ValidationError):
			item.save()
			item.full_clean()




class ListModelTest(TestCase):

	def test_get_absolute_url(self):
		list_ = List.objects.create()
		self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

	def test_duplicate_items_are_invalid(self):
		list_ = List.objects.create()
		Item.objects.create(list = list_, text = 'bla')
		with self.assertRaises(ValidationError):
			item = Item(list = list_, text = 'bla')
			item.full_clean()
			# item.save()

	def test_list_ordering(self):
		list1 = List.objects.create()
		item1 = Item.objects.create(list = list1, text = 'i1')
		item2 = Item.objects.create(list = list1, text = 'item2')
		item3 = Item.objects.create(list = list1, text = '3')
		self.assertEqual(
			list(Item.objects.all()),
			[item1, item2, item3]
		)

	def test_string_representation(self):
		item = Item(text = 'some text')
		self.assertEqual(str(item), 'some text')

