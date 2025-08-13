from django.db import models

class Autor(models.Model):
    name=models.CharField(max_length=300,blank=False)
    live=models.BooleanField()

    def __str__(self):
        return self.name