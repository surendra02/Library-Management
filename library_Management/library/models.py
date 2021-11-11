from django.db import models
import datetime
# Create your models here.

class Books(models.Model):
    b_name=models.CharField(max_length=50)
    b_author = models.CharField(max_length=30)
    b_title=models.TextField(max_length=150)
    publish_date=models.DateField(default=datetime.date.today())
    b_image=models.ImageField(upload_to='book_images',max_length=150)

