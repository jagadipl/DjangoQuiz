from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text
