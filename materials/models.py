from django.db import models


class Materials(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')

    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=100, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'