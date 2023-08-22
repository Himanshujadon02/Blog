from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contactustb(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=90)
    email=models.CharField(max_length=50)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class Popular_blogs(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True) 
    content=RichTextField()
    image = models.ImageField(upload_to = "myapp2/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


class Regular_blogs(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to = "myapp2/images",default="")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title