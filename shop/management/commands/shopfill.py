# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from shop import models
import os
from settings import MEDIA_ROOT
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        if options.get('verbosity'):
            self.stdout.write('Set shop item image borders\n')
        folder = 'borders_eta'
        path = os.path.join(MEDIA_ROOT, folder)
        listing = os.listdir(path)
        borders = []
        prefix = u'Рамка'
        for file in listing:
            file = file.split('.')
            name = "%s %s" % (prefix, file[0])
            try:
                border = models.Item_Image_Border.objects.get(name=name)
            except :
                border = models.Item_Image_Border(name=name)
            border.image = os.path.join(folder, '.'.join(file)).replace('\\', '/')
            border.save()
            borders.append(border)
            if options.get('verbosity') == 2: self.stdout.write(u'%s\n' % border)
        if options.get('verbosity'):
            self.stdout.write('Set shop item\n')
        folder_items_eta = 'items_eta'
        listing_items_eta = os.listdir(os.path.join(MEDIA_ROOT, folder_items_eta))
        folder_items_ad_eta = 'items_ad_eta'
        listing_items_ad = os.listdir(os.path.join(MEDIA_ROOT, folder_items_ad_eta))
        item_name = u'Товар %(name)s'
        img_name = u'Картинка %(name)s к товару %(item)s'
        for i in range(1, 60):
            name = item_name % {'name': i}
            try:
                item = models.Item.objects.get(name=name)
            except :
                item = models.Item(name=name)
            item.save()
            if options.get('verbosity') == 2:
                self.stdout.write(u'%s\n' % item)
            for image in models.Item_Image.objects.filter(item=item):
                image.delete()
                image = models.Item_Image(
                    item=item,
                    is_primary=True,
                    image=os.path.join(folder_items_eta, random.choice(listing_items_eta)).replace('\\', '/'),
                    border=random.choice(borders),
                    name=img_name % {'name': u'_основная_', 'item': item}
                )
                image.save()
                if options.get('verbosity') == 3:
                    self.stdout.write(u'    Add Image %s\n' % image)
            for ii in range(2, random.randrange(5, 12)):
                image = models.Item_Image(
                    item=item,
                    is_primary=False,
                    image=os.path.join(folder_items_ad_eta, random.choice(listing_items_ad)).replace('\\', '/'),
                    border=random.choice(borders),
                    name=img_name % {'name': ii, 'item': item}
                )
                image.save()
                if options.get('verbosity') == 3:
                    self.stdout.write(u'    Add Image %s\n' % image)
