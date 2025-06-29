from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.teacher} ({self.date})"
