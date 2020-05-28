from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List
from django.core.exceptions import ValidationError
from lists.forms import ExistingListItemForm, ItemForm

# Create your views here.
def home_page(request):
	return render(request, 'home.html', { 'form' : ItemForm() })

def view_list(request, list_id):
	list_ = List.objects.get(id = list_id)
	form = ExistingListItemForm(for_list = list_)
	#handle two types of request
	if request.method == 'POST':
		form = ExistingListItemForm(for_list = list_, data = request.POST)
		if form.is_valid():
			form.save()
			# print(form.save())
			# Item.objects.create(text = request.POST['text'], list = list_)
			return redirect(list_)
	return render(request, 'list.html', {'list':list_, "form": form})

def new_list(request):
	form = ItemForm(data = request.POST)
	if form.is_valid():
		list_ = List.objects.create()
		form.save(for_list = list_)
		# Item.objects.create(text = request.POST['text'], list = list_)
		return redirect(list_)
	else:
		return render(request, 'home.html', {"form":form})
	# try:
	# 	item.full_clean()
	# 	item.save()
	# except ValidationError:
	# 	list_.delete()
	# 	error = "You can't have an empty list item"
	# 	return render(request, 'home.html',{"error":error})
	# # return redirect(f'/lists/{list_.id}/')
	# # Using get_absolute_url for Redirects
	# # return redirect('view_list', list_.id)
	# #在视图中使用get_absolute_url函数，把重定向的目标对象传给redirect函数，redirect函数自动调用get_absolute_url函数
	# return redirect(list_)

#delete the add_item view
# def add_item(request, list_id):
# 	#视图保存新建的待办事项mkae it save our new list item
# 	list_ = List.objects.get(id = list_id)
# 	Item.objects.create(text = request.POST['item_text'], list = list_)
# 	return redirect(f'/lists/{list_.id}/')  
