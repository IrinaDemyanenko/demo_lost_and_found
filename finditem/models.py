from django.db import models
from django.utils import timezone



class Category(models.Model):
    """Категории пропавших вещей."""

    code = models.CharField('Код категории', max_length=50, unique=True)
    name = models.CharField('Название категории', max_length=200)

    def __str__(self):
        return f'Категория {self.name}'


class Station(models.Model):
    """Станция метро."""

    name = models.CharField('Название станции', max_length=200, unique=True)

    def __str__(self):
        return f'Станция {self.name}'


class FoundItem(models.Model):
    """Потерянная вещь."""

    STATUS_CHOICES = [
    ('До востребования', 'До востребования'),
    ('Выдан', 'Выдан'),
    ('Утилизирован', 'Утилизирован'),
]

    description = models.TextField('Описание вещи', max_length=500)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория'
        )
    station = models.ForeignKey(
        Station, on_delete=models.CASCADE, verbose_name='Станция'
        )
    found_date = models.DateField('Дата находки', default=timezone.now)  # auto_now_add=True запретит переопределение
    image_url = models.CharField('Фото (url)', max_length=500, blank=True, null=True)
    status = models.CharField('Статус', max_length=100, choices=STATUS_CHOICES, default='До востребования')

    def __str__(self):
        words = self.description.split()
        short_desc = ' '.join(words[:3])  # берём первые 3 слова
        if len(words) > 3:
            short_desc += '...'
        return f'{short_desc} — {self.category} ({self.station}, {self.found_date})'
