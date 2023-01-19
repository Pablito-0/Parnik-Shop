from django.db import models
from django.urls import reverse


class Product(models.Model):
    """
    Основной класс для товаров, сюда будут скидываться все товары.
    """
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    article = models.PositiveIntegerField(verbose_name="Артикул", blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография",blank=True)
    description = models.TextField(verbose_name="Описание",blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    available = models.BooleanField(default=True, verbose_name='Есть в наличии', editable=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    quantity = models.PositiveIntegerField(verbose_name="Количество на складе")

    #  метод чтоб переопределить параметр.Чтоб он отображался текстом а не обьектом
    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['title', 'time_create', 'cost']
        index_together = (('id', 'slug'),)


class Category(models.Model):
    """
    Модель основных категорий для наших товаров,
    """
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', args={'category_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

