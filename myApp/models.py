from django.db import models

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Name    

class Images(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Image = models.ImageField(upload_to='images')
    Added_date = models.DateTimeField()
    Location = models.CharField(max_length=2083)
    Cat = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.Title

