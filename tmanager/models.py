from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Task(models.Model):
    PRIORITIES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )

    name = models.CharField(max_length=70)
    description = models.TextField()
    date_of_creation = models.DateField()
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.description}"

    def get_absolute_url(self):
        return reverse('task', args={self.pk})
