from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
    	verbose_name='tag'
    	verbose_name_plural='tags'
    	ordering=['name']

    def _str_(self):
    	return self.name
class PublicBookManager(models.Manager):
    def get_queryset(self):
        qs=super(PublicBookManager, self).get_queryset()
        return qs.filter(is_public=True)	


class Bookmark(models.Model):
	url=models.URLField('url', max_length=255)
	title=models.CharField('description', max_length=20)
	description=models.TextField('description', blank=True)
	is_public=models.BooleanField('public', default=True)
	date_created=models.DateTimeField('date created')
	date_updated=models.DateTimeField('date updated')
	owner=models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
	tags=models.ManyToManyField(Tag, blank=True)

	class Meta:
		verbose_name='bookmark'
		verbose_name_plural='bookmarks'
		ordering=['-date_created']

	def _str_(self):
	    return '%s (%s)' % (self.title, self.url)

	def save(sef, *args, **kwargs):
	    if not self.id:
	    	self.date_created=now()
	    self.date_updated=now()
	    super(Bookmark, self).save(*args, **kwargs)	
