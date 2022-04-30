from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    cat_image = models.ImageField(
        upload_to='photos/categories', null=True, blank=True)

    def get_urls(self):
        return reverse('products-by-category', args=[self.slug])

    def __str__(self):
        return self.category_name
