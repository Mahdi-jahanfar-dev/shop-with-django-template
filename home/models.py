from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)



    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        super(Category, self).save(*args, **kwargs)
        return self

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        super(Product, self).save(*args, **kwargs)
        return self



