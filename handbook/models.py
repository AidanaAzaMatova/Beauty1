from django.conf import settings
from django.db import models
from django.utils import timezone

COMPANY_TYPES_CHOICES=(
    ("Internet Shop","Қолға арналған лак"),
    ("SuperMarket","Макияж щеткасы"),
    ("Shopping center","Көзге арналған тень"),
    ("Furniture Shop","Бетке арналған опадалап"),
    ("IT Company","Көзге арналған тушь"),
    ("Educational Center","Ерін памадасы")
)
COMPANY_RATE_CHOICES=(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5")
)


# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=40,blank=True)
    company_about=models.TextField(blank=True)
    company_phone=models.CharField(max_length=30,blank=True)
    comapny_category=models.CharField(max_length=40,choices=COMPANY_TYPES_CHOICES,blank=True)
    company_email=models.EmailField(blank=True)
    company_logo=models.ImageField(blank=True,upload_to='logos/',null=True)
    published_date=models.DateTimeField(blank=True, null=True)

    def get_media_url(self):
        return self.company_logo.url.replace('media/','')
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.company_name

class Rate(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    rate=models.CharField(max_length=20,choices=COMPANY_RATE_CHOICES)
    

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.company)+":"+self.rate