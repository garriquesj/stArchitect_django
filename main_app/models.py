from django.db import models
import time


# Create your models here.
class Architect(models.Model):
        name = models.CharField(max_length=100)
        image = models.CharField(max_length=250)
        firm = models.CharField(max_length=100)
        nationality = models.CharField(max_length=100)
        award = models.TextField(max_length=500)
        bio = models.TextField(max_length=500)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ['name']


class Building(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE, related_name="buildings")

    def __str__(self):
        return self.name
    
    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.length))
