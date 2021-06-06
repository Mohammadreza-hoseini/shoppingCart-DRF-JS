from django.db import models




class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.title
