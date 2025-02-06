from django.db import models
import datetime

class Books(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  year = models.IntegerField()
  publisher = models.CharField(max_length=100)
  owner = models.CharField(max_length=100)
  is_avaliable = models.BooleanField()
  avaliable_at = models.DateTimeField(default=datetime.datetime.now)
  def __str__(self):
    return self.title

class BookLendings(models.Model):
  book = models.ForeignKey(Books, on_delete=models.CASCADE)
  borrower = models.CharField(max_length=100)
  date = models.DateTimeField(default=datetime.datetime.now)

  def __str__(self):
    return self.borrower