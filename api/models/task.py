from django.db import models
from .user import User

class Task(models.Model):
    id=models.AutoField(primary_key=True)
    owner=models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    descripton=models.CharField(max_length=1000)
    due_date=models.DateField()