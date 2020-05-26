from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

#django提供了一个特殊的类ModelForm，用来生成模型的表单
class ItemForm(forms.models.ModelForm):

    #用特殊的属性Meta配置表单
	class Meta:
		model = Item
		fields = ('text',)
		#ModelForm字段也可使用widget参数定制
		widgets = {
		    'text': forms.fields.TextInput(attrs = {
		    	'placeholder' : 'Enter a to-do item',
		    	'class' : 'form-control input-lg',
			}),
		}
		error_messages = {
		'text' : {'required': EMPTY_ITEM_ERROR}
		}

	# item_text = forms.CharField(
	# 	widget = forms.fields.TextInput(attrs = {
	# 		'placeholder' : 'Enter a to-do item',
	# 		'class' : 'form-control input-lg',
	# 		}),
	# )

