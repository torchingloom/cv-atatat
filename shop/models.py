# -*- coding: utf-8 -*-

import Image
from django.db import models
from shop import item_image_border_filename_generate, item_image_filename_generate

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name=u'название товара', help_text=u'Уникальное название товара. Будет фигурировать в ссылке на карточку товара.')
    info = models.TextField(null=True, verbose_name=u'информация')
    margin_left = models.IntegerField(default=0, verbose_name=u'отступ слева', help_text=u'Отступ слева от границы стеллажа или от другого товара. Может быть отрицательным.')
    is_exists = models.BooleanField(null=False, default=True, verbose_name=u'в наличии')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'товары'

class Item_Image_Border(models.Model):
    name = models.CharField(max_length=500, verbose_name=u'название рамки')
    image = models.ImageField(upload_to=item_image_border_filename_generate, verbose_name=u'картинка')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'рамка картинки товара'
        verbose_name_plural = u'рамки картинки товара'

class Item_Image(models.Model):
    item = models.ForeignKey(Item, null=False, on_delete=models.CASCADE)
    border = models.ForeignKey(Item_Image_Border, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500, verbose_name=u'название картинки')
    info = models.TextField(null=True, verbose_name=u'описание картинки')
    image = models.ImageField(upload_to=item_image_filename_generate, verbose_name=u'картинка')
    is_primary = models.BooleanField(default=False, verbose_name=u'основная')

    def __unicode__(self):
        return u'[%s] %s' % (self.item.name, self.name)

    class Meta:
        ordering = ['item', '-is_primary']
        verbose_name = u'картинка товара'
        verbose_name_plural = u'картинки товара'



