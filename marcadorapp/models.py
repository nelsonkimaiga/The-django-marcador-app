from django.db import models

# Create your models here.
class Macardor(models.Model):
	id=models.AutoField(primary_key=True)
	url=models.models.URLField(max_length=20)
	title=models.CharField(max_length=20)
	description=models.TextField(max_length=20)
	is_public=models.BooleanField(max_length=20)
	date_created=models.DateTimeField(max_length=20)
	date_updated=models.DateTimeField(max_length=20)
	owner=models.ForeignKey(max_length=20)
	tags=models.ManyToManyField(max_length=20)

class Tag(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20)
