from django.db import models

# Create your models here.
class hi(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    contactno=models.BigIntegerField()
    class Meta:
        db_table="hello"
