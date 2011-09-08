from django.conf.urls.defaults import *
from entry.views import EntryListView, EntryDetailView
from entry.views import CategoryListView, CategoryDetailView
from entry.views import EntryTagListView, EntryTagDetailView
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'tags/$', EntryTagListView.as_view(), name='entry_tag_list'),
	url(r'tags/(?P<pk>[-\d]+)/$', EntryTagDetailView.as_view(), name='entry_tag_detail'),
	url(r'category/$', CategoryListView.as_view(), name='entry_category_list'),
	url(r'category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='entry_category_detail'),
	url(r'(?P<slug>[-\w]+)/$', EntryDetailView.as_view(), name='entry_detail'),
	url(r'^$', EntryListView.as_view(), name='entry_list'),
)