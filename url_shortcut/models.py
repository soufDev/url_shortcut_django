from django.db import models

# Create your models here.


class MiniURL(models.Model):
    default_url = models.URLField(max_length=150, unique=True)
    url_code = models.CharField(max_length=15, unique=True)
    create_at = models.DateField(auto_now_add=True)
    identifier_create = models.CharField(max_length=50, blank=True)
    access_number = models.IntegerField(max_length=11, default=0)

    def __str__(self):
        return self.default_url



