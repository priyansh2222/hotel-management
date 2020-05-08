

from django.db import models

# Create your models here.
class slide(models.Model):
    name=models.CharField(max_length=300)
    image=models.ImageField(upload_to='pics',default='')
    def  __str__(self):
        return self.name



class room(models.Model):
    room_no=models.CharField(max_length=200)
    room_type=models.CharField(max_length=200)
    room_price=models.IntegerField()
    
    status=models.CharField(max_length=6)
    def __str__(self):
        return self.room_type + ' ' + self.room_no + ' is '+ self.status

class booking(models.Model):
    
    name=models.CharField(max_length=100)
    
    destination=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    roomtype=models.CharField(max_length=100)
    adharID=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    roomtype=models.CharField(max_length=100)
    mobileno=models.IntegerField()
    members=models.IntegerField()
    cid=models.DateField()
    cot=models.DateField()
    room_no=models.CharField(max_length=100)
    def __str__(self):
        return self.username +' has booked rooms  '+ self.room_no