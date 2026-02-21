from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.urls import reverse

# object for author articles ---------------------------.----------------------.

# cascade

# set null

# protect

# set default
# ithem for database = 
    # help_text = enter a text for help write at more fild 
    # UNIQE = because not replay title or mode data 
    # CHOICES = because select betwin two option for fild
    # CHOICES = (
    #     ('a', 'python'),
    #     ('b', 'django'),
    #     ('c', 'animals'),
    #     ('d', 'laptop'),
    # )
# ------------------------------------------------------.----------------------.



class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)



    def  __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # add timezone for view time write 
    pub_date = models.DateField(default=timezone.now())




    def get_absolute_url(self):
        return reverse("blog:article_deteil", kwargs={"title": self.title})
    



    def __str__(self):
        return f"{self.title} - {self.body[:30]}"