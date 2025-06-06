from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(null=True,blank=True)
    price=models.IntegerField()

    def __str__(self):
        return self.title

    