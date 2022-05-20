from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=250,unique=True)
    created_at = models.DateTimeField()


    def __str__(self):
        return self.brand_name

class Model(models.Model):
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    model_name = models.CharField(max_length = 250)
    price = models.IntegerField()
    launch_date = models.DateTimeField()

    def __str__(self):
        return self.model_name
