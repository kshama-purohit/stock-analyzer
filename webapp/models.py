from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length = 10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()       
    close = models.FloatField()
    date = models.DateField()
    volume = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.date}'
    
class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    feedback = models.TextField(max_length = 500)

    def __str__(self):
        return f'{self.name}'
    