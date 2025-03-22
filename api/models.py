from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AdminUser(AbstractUser):
  """
  Custom AdminUser model using email for authentication.
  """
  email= models.EmailField(unique=True)
  username= models.CharField(max_length=150)

  USERNAME_FIELD= 'email'
  REQUIRED_FIELDS= ['username']

  def __str__(self):
    return self.email
  
  
class Book(models.Model):
  """
  Model representing a book.
  """

  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  published_date = models.DateField()

  def __str__(self):
    return self.title