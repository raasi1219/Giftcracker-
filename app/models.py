from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
    fname = models.CharField(max_length = 100)
    #mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    #lname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    is_registered = models.BooleanField(default = False)
@receiver(post_save, sender= User)
def create_user_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()   
  
class Subcategory(models.Model):
   #gid = models.CharField(max_length = 50)
    subcategory_type = models.CharField(max_length = 100)
    #qty= models.CharField(max_length = 100)
    color = models.CharField(max_length = 20)
    price = models.CharField(max_length = 100)
    weight = models.CharField(max_length = 100)
    imagepath = models.CharField(max_length = 100)
    size = models.CharField(max_length = 100)
    stock = models.CharField(max_length = 10)
    def __str__(self):
        return self.imagepath

class Occasion(models.Model):
   # occasion_id = models.CharField(max_length = 50)
    occasion_type = models.CharField(max_length = 40)
    def __str__(self):
    	return self.occasion_type

class Category(models.Model):
    # category_id = models.CharField(max_length = 50)
     category_type = models.CharField(max_length = 40)
     imagepath = models.CharField(max_length = 100)
     def __str__(self):
         return self.category_type

class C_S_Mapping(models.Model):
     s_c_id = models.ForeignKey(Subcategory,max_length=50)
     c_id = models.ForeignKey(Category,max_length=50)
     def __str__(self):
         return str(self.s_c_id)

class Orders(models.Model):
     c_s_id = models.ForeignKey(C_S_Mapping,max_length=50)
     quantity = models.CharField(max_length = 40)
     Adress = models.CharField(max_length = 40)
     Note = models.TextField()
     #datetime = models.DateTimeField(default=datetime.now)
     date = models.DateField()
     def __str__(self):
         return "{0}-{1}-{2}".format(self.c_s_id,self.quantity,self.Adress)

