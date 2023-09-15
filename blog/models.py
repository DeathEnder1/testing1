from django.db import models

# Create your models here.
class Blog(models.Model):
    Userid= models.BigIntegerField()
    Title=models.CharField(max_length=30)
    Content= models.TextField()
    Image=models.URLField(max_length=4000)
    
    class Meta:
        db_table="Blog"