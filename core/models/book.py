from django.db import models 


class Book(models.Model):
    title=models.CharField(max_length=200,blank=False)
    years=models.TimeField()
    price=models.IntegerField()

    def __str__(self):
        return self.title

    