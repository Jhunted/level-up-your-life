from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class User(AbstractUser):
  pass
  score = models.IntegerField(default=0)
  level = models.CharField(max_length=100, default='Newbie')

class Journal(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=2500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'journal_id': self.id})

class Post(models.Model):
  name = models.CharField(max_length=250)
  date = models.DateField(default=date.today)
  content = models.TextField(max_length=2500)
  journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
  tasks = models.ManyToManyField(Task)
  likes = models.ManyToManyField(User)

class Task(models.Model):
  title = models.CharField(max_length=100)
  progress = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
