from django.db import models
from django.db.models import SlugField


class Finder(models.Model):
    slug = SlugField(max_length=30, unique=True, db_index=True)
    title=models.CharField('Name', max_length=50, default='Name')
    anons = models.CharField('Anons', max_length=250, default='Anons')
    fill_text=models.TextField('Game_FILL')
    url = models.URLField('URL', blank=True, max_length=100)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="game"
        verbose_name_plural = "games"
