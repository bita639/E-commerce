from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='name')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='slug')

    #class meta???????
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='category')
    name = models.CharField(max_length=200, db_index=True, verbose_name='name')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='slug')
    image = models.ImageField(upload_to="products", default='ProductImage/blank.png', blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        ordering = ["-created_at"]

        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])