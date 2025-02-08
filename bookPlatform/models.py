from django.contrib.auth.models import User
from django.db import models
import datetime

class Books(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  year = models.IntegerField()
  publisher = models.CharField(max_length=100)
  owner = models.CharField(max_length=100)
  is_available = models.BooleanField(default=False)
  available_at = models.DateTimeField(default=None)
  is_listed = models.BooleanField(default=False)
  def __str__(self):
    return self.title

class BookLendings(models.Model):
  book = models.ForeignKey(Books, on_delete=models.CASCADE)
  lender = models.ForeignKey(User, on_delete=models.CASCADE)
  due_date = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(days=7))

  def __str__(self):
    return self.lender