from django.db import models
from django.contrib.auth.models import User


# object for author articles ---------------------------.----------------------.

# cascade

# set null

# protect

# set default

# ------------------------------------------------------.----------------------.



class Article(models.Model):
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    # help_text = enter a text for help write at more fild 
    # UNIQE = because not replay title or mode data 
    title = models.CharField(max_length=70, help_text="ENTER A VALID TITLE")
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    def __str__(self):
        return f"{self.title} - {self.body[:30]}"