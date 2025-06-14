from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    category = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
