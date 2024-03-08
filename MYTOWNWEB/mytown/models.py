from django.db import models


class AddReport(models.Model):
    title = models.CharField(max_length=500)
    email = models.EmailField()

    CITY_CHOICES = [
        ('BEER', 'Beer Sheva'),
        ('ASD', 'Ashdod'),
        ('ASHQ', 'Ashkelon'),
        ('NEOT', 'Netivot'),
        ('OFK', 'Ofakim'),
        ('SDR', 'Sderot'),
        ('KRM', 'Kiryat Malachi'),
        ('KSP', 'Kiryat Gat'),
        ('NPM', 'Netiv HaAsara'),
        ('REH','Rehovot'),  
        ('OME', 'Omer'),
        ('MET', 'Metar'),  
        ('RAH', 'Rahat'),  
        ('LAk', 'Lakiya'),  
        ('HURA', 'Hura'),  
        ('HOL', 'Holon'),
        ('KSI','Ksifa'),
        ('DEM','Dimona'),
         ('ARAD', 'Arad'),  
    ]

   

    city = models.CharField(max_length=5, choices=CITY_CHOICES)
    description=models.CharField(max_length=1000)
    location=models.CharField(max_length=500)
    picture = models.ImageField(upload_to='report_pictures/', null=True, blank=True)
 
    class Meta:
        db_table = 'addreport'
    def __str__(self):
        return self.title


class Workerlogin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'workerlogin'
    def __str__(self):
        return self.username

