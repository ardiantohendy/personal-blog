from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'