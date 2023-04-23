from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField('Категория', max_length=40)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Виды шоколада"""
    name = models.CharField('Продукт', max_length=160)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    url = models.SlugField(unique=True)
    description = models.TextField('Описание')
    price = models.IntegerField()
    available = models.BooleanField('В наличии', default=True)
    COLOR_CHOICES = (
        ('milk', 'Молочный шоколад'),
        ('dark', 'Темный шоколад'),
        ('Kakao', 'Какао'),
        ('forms', 'Формы для кондитеров'),
        ('ingredients', 'Ингредиенты'))
    color = models.CharField(max_length=25, choices=COLOR_CHOICES, default='молочный')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])