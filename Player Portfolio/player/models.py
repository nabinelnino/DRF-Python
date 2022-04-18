from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    height = models.IntegerField()
    DOB = models.DateField()
    age = models.IntegerField()
    country = CountryField()
    spouse_name = models.CharField(max_length=50,null=True,blank=True)
    #MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    #medal = models.CharField(blank=True,choices=MedalType.choices, max_length=20)
    PLAYER_CATEGORY=[
        ('Age_Group','Age_Group'),
        ('Junior','Junior'),
        ('Senior', 'Senior'),
        ('Captain','Captain')
    ]
    player_category= models.CharField(max_length=10, choices=PLAYER_CATEGORY,default='Junior')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(User,max_length=20)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.country