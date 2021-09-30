from django.db import models
from .validators import audio_only
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Beat(models.Model):

    songName = models.CharField(max_length=20,blank=False)

    songImage = models.ImageField(upload_to='images/%Y/%m/%d/',null=True,blank=False)

    audioFile = models.FileField(upload_to='audio/%Y/%m/%d/'
    ,null=True
    ,blank=False
    ,validators=[audio_only])

    choices = [
        ("PLAYBACK",'Playback'),
        ("BEAT",'Beat'),
    ]


    mediaType = models.CharField(
        max_length=15,
        choices=choices,
        default="so",
    )

    todownload = models.BooleanField(default=False)
    author = models.CharField(max_length=20,default="AnonGuy")
    postTime = models.DateTimeField(auto_created=True,blank=True)
    


class Contact(models.Model):
    first_name = models.CharField(max_length=30,blank=False,null=False)
    last_name = models.CharField(max_length=30,blank=False,null=False)

    email = models.EmailField(max_length=35)

    phone = PhoneNumberField(blank=True)

    message = models.TextField(max_length=200,blank=False,null=False)



class ArijitAddress(models.Model):
    address = models.TextField(max_length=200,blank=False,null=False)
    phone = PhoneNumberField(blank=False)
    email = models.EmailField(max_length=35,blank=False,null=False)
    

