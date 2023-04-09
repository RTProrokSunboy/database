from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Phone(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=60, null=False)
    image = models.URLField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(default=None)
    print(slug)

    def __str__(self):
        return f'{self.id}. {self.name}'

    # def get_absolut_url(self):
    #     return reversed ('phone', kwarqs = {'slag': self.slug})
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)


