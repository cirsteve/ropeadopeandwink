from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tagging.fields import TagField
import tagging
from treebeard.mp_tree import MP_Node

# Create your models here.
class Category(MP_Node):
	name = models.CharField(max_length=30, unique=True)
	slug = models.SlugField(editable=False)
	description = models.TextField(blank=True)
	
	node_order_by = ['name']
	
	def __unicode__(self):
		return '%s' % self.name
		
	def save(self,*args,**kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Category, self).save(*args,**kwargs)
	
	def get_absolute_url(self):
		return '/blog/category/%s' % self.slug

class Entry(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(editable=False)
	date = models.DateTimeField(auto_now=True)
	modified = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	body = models.TextField()
	category = models.ForeignKey(Category)
	tag = TagField()
	image = models.ImageField(upload_to='entry_img/', blank=True)
	link = models.URLField(blank=True)
	
	def __unicode__(self):
		return '%s' % self.title
	
	def save(self,*args,**kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Entry, self).save(*args,**kwargs)
	
	def get_absolute_url(self):
		return '/blog/%s' % self.slug
	
tagging.register(Entry)