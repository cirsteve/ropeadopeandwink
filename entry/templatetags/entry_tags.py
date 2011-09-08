from django import template

from entry.models import Category, Entry

register = template.Library()

#class CategoryList(Node):

@register.inclusion_tag('temp_tags/categories_list.html')
def cat_list():
    cats = Category.objects.all()
    return {'cats': cats}
    
@register.inclusion_tag('temp_tags/recent_posts.html')
def recent_posts():
    posts = Entry.objects.all().order_by('-date')
    return {'recent_posts': posts}