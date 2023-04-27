from django.db import models
from django.urls import reverse

class Product(models.Model):
    """Виды шоколада"""
    MILK = 'milk chocolate'
    DARK = 'dark chocolate'
    KAKAO = 'kakao'
    INGREDIENTS = 'ingredients'

    CHOICE_GROUP = {
        (MILK, 'milk chocolate'),
        (DARK, 'dark chocolate'),
        (KAKAO, 'kakao'),
        (INGREDIENTS, 'ingredients'),
    }

    name = models.CharField('Продукт', max_length=160)
    group = models.CharField(max_length=30, choices=CHOICE_GROUP, default='milk chocolate')
    description = models.TextField('Описание')
    price = models.IntegerField()
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    url = models.SlugField(unique=True)
    available = models.BooleanField('В наличии', default=True)

    def __str__(self):
        return self.name

def get_absolute_url(self):
    return reverse("product_detail", kwargs={'slug': self.url})