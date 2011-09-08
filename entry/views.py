# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from tagging.models import Tag, TaggedItem


from entry.models import Entry, Category
from entry.forms import CategoryForm

class EntryListView(ListView):
	
	context_object_name = 'entry_list'
	queryset = Entry.objects.all()
	template_name = 'entry/entry_list.html'
		
class EntryDetailView(DetailView):
	context_object_name = 'entry'
	queryset = Entry.objects.all()
	template_name = 'entry/entry_detail.html'
	
	
class EntryCreateView(CreateView):
	model = Entry
	template_name = 'entry/entry_create.html'
	
class CategoryListView(ListView):
	
	context_object_name = 'category_list'
	queryset = Category.objects.all()
	template_name = 'entry/category_list.html'
	
class CategoryDetailView(DetailView):
	context_object_name = 'category'
	queryset = Category.objects.all()
	template_name = 'entry/category_detail.html'
	
class CategoryCreateView(CreateView):
	form_class = CategoryForm
	model = Category
	template_name = 'entry/category_create.html'
	
	
class EntryTagListView(ListView):
    context_object_name = 'tag_list'
#    queryset = Tag.objects.get_for_object(Topic)
    template_name = 'entry/tag_list.html'
   
    def get_queryset(self):
        return Tag.objects.usage_for_model(Entry, counts=True)
        
        
class EntryTagDetailView(DetailView):
    context_object_name = 'tag'
    model = Tag
    template_name = 'entry/tag_detail.html'
    queryset = Tag.objects.all()
  #  slug_field = 'name'
    
    def get_context_data(self, **kwargs):
        context = super(EntryTagDetailView, self).get_context_data(**kwargs)
        t = get_object_or_404(Tag, id=self.kwargs['pk'])
        context['tag_list'] = TaggedItem.objects.get_by_model(Entry, t)
        return context
