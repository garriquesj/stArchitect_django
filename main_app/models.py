from django.db import models

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