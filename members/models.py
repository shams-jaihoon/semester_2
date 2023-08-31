from django.db import models

class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField(null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=50, null=True, blank=True )
  
  

  def __str__(self):
    return f"{self.title} {self.content} {self.pub_date}"




class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField(null=True, blank=True)
  description = models.TextField(null=True)

  def __str__(self):
    return f"{self.name} {self.price} {self.description}"

  


