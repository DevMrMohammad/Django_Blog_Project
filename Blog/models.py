from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# object for author articles ---------------------------.----------------------.

# cascade

# set null

# protect

# set default

# ------------------------------------------------------.----------------------.



class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)



    def  __str__(self):
        return self.title


class Article(models.Model):

    CHOICES = (
        ('a', 'python'),
        ('b', 'django'),
    )
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    category = models.ManyToManyField(Category)
    # help_text = enter a text for help write at more fild 
    # UNIQE = because not replay title or mode data 
    # CHOICES = because select betwin two option for fild
    title = models.CharField(max_length=70, help_text="ENTER A VALID TITLE", choices=CHOICES)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # add timezone for view time write 
    pub_date = models.DateField(default=timezone.now())



    def __str__(self):
        return f"{self.title} - {self.body[:30]}"