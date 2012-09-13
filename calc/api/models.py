from django.db import models

# Create your models here.

class KidPlaylist(models.Model):
	kid_name = models.CharField(max_length=200,null=True,blank=True)
	kid_login_name = models.CharField(max_length=200)
	creation_date = models.DateField(auto_now=True)
	
class Header(models.Model):
    title = models.CharField(max_length = 255)
    created_by = models.CharField(max_length = 255)

class Criteria(models.Model):
   details =   models.CharField(max_length = 255)
   head = models.ForeignKey(Header)
