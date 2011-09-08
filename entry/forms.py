from django.forms import ModelForm
from treebeard.forms import MoveNodeForm
from entry.models import Category

class CategoryForm(MoveNodeForm):
	class Meta:
		model = Category
		fields = ('name', 'description')