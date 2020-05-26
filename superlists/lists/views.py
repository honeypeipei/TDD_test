from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm

# Create your views here.
def home_page(request):
	return render(request, 'home.html', { 'form' : ItemForm() })

def view_list(request, list_id):
	list_ = List.objects.get(id = list_id)
	error = None

	#handle two types of request
	if request.method == 'POST':
		try:
			item = Item(text = request.POST['text'], list = list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"

	return render(request, 'list.html', {'list':list_, 'error': error})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text = request.POST['text'], list = list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html',{"error":error})
	# return redirect(f'/lists/{list_.id}/')
	# Using get_absolute_url for Redirects
	# return redirect('view_list', list_.id)
	#在视图中使用get_absolute_url函数，把重定向的目标对象传给redirect函数，redirect函数自动调用get_absolute_url函数
	return redirect(list_)

#delete the add_item view
# def add_item(request, list_id):
# 	#视图保存新建的待办事项mkae it save our new list item
# 	list_ = List.objects.get(id = list_id)
# 	Item.objects.create(text = request.POST['item_text'], list = list_)
# 	return redirect(f'/lists/{list_.id}/')  
