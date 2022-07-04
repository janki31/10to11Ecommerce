from django.db import models

# Create your models here.
class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=100,default="")
    product_desc=models.TextField()
    product_price=models.IntegerField(default=0)
    pub_date=models.DateField()
    product_image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return str(self.pid)+"."+self.product_name

class Contact(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    emailid=models.EmailField(max_length=150,default="")
    mobileno=models.IntegerField(default=0)
    feedback=models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    oid=models.AutoField(primary_key=True)
    items=models.TextField()
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50,default="")
    email=models.EmailField(max_length=100,default="")
    address=models.TextField()
    mobileno=models.IntegerField(default=0)
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    zipcode=models.IntegerField(default="")
    totalprice=models.IntegerField(default=0)

    def __str__(self):
        return str(self.oid)+"."+self.firstname



