from django.contrib import admin
from entry.models import Entry, Category
from treebeard.admin import TreeAdmin

class CategoryAdmin(TreeAdmin):
	pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry)
