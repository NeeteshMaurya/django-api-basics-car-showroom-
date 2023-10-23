from django.db import models

class ShowroomList(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    website = models.URLField(max_length=100)

    def __str__(self) :
        return self.name
 
class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100,blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True)
# many to one relationship with Showroom model.
    showroom = models.ForeignKey(ShowroomList,on_delete=models.CASCADE,related_name="Showroom",null=True)

    def __str__(self) :
        return self.name