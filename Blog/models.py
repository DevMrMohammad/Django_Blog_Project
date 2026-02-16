from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete =models.CASCADE, )
    # user and CADCADE = if delete user : all data for in user deleted 
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    def __str__(self):
        return f"{self.title} - {self.body[:30]}"