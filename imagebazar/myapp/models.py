from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_date = models.DateField()
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.title