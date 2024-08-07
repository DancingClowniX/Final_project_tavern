from django.db import models

# Create your models here.
class Table(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название',blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='reserved/image', blank=True,null=True,)