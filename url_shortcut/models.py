from django.db import models
import random, string
# Create your models here.


class MiniURL(models.Model):
    default_url = models.URLField(verbose_name='Enter the URL', max_length=150, unique=True)
    url_code = models.CharField(max_length=6, unique=True)
    create_at = models.DateField(auto_now_add=True)
    identifier_create = models.CharField(verbose_name='Identifier', max_length=50, blank=True, null=True)
    access_number = models.IntegerField(default=0)

    def __str__(self):
        return "[{0}] {1}".format(self.url_code, self.default_url)#self.default_url

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(6)
            
        super(MiniURL, self).save(*args, **kwargs)

    def generate(self, nb_caracteres):
        chars = string.ascii_letters + string.digits
        random_char = [random.choice(chars) for _ in range(nb_caracteres)]

        self.url_code = ''.join(random_char)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"

