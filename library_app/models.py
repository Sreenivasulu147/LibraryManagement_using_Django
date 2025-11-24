from django.db import models
from datetime import date

# Create your models here.
class Book_info(models.Model):
    Book_id = models.IntegerField(primary_key=True)
    Book_name = models.CharField(max_length=69)
    Book_price = models.FloatField()
    Book_Author = models.CharField(max_length=69)
    Book_publish_year = models.DateField(default=date.today)
    Book_quantity = models.IntegerField()
    Book_stack = models.BooleanField(default=True)
    Book_image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    def __str__(self):
        return self.Book_name
