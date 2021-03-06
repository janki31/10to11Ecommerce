from django.db import models

# Create your models here.
class Blogpost(models.Model):
    bid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    desc=models.TextField()
    head0=models.CharField(max_length=200,default="")
    chead0=models.TextField()
    head1 = models.CharField(max_length=200, default="")
    chead1 = models.TextField()
    head2 = models.CharField(max_length=200, default="")
    chead2 = models.TextField()
    pub_date=models.DateField()
    blog_image=models.ImageField(upload_to='blog/images',default="")

    def __str__(self):
        return self.title
