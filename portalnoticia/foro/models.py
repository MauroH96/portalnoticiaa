from email.policy import default
from django.db import models

class Noticia(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    image=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="New"
        verbose_name_plural="News"

    def __str__(self):
        return "Titulo: "+self.title
    