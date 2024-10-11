from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from gm2m import GM2MField


class Owner(models.Model):
    class Meta:
        app_label = 'issue69'

    assets = GM2MField('Table', through='OwnerAsset', related_name='owners')

class OwnerAsset(models.Model):
    class Meta:
        app_label = 'issue69'

    # these are from legacy but I can't see how it's negatively affecting
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # owner_type = models.ForeignKey('OwnerType', on_delete=models.SET_NULL, null=True, blank=True)

    asset = GenericForeignKey('asset_type', 'asset_id')
    asset_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    asset_id = models.PositiveIntegerField()

class DeferredDataManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().defer('data')
class Table(models.Model):
    class Meta:
        app_label = 'issue69'

    data = models.CharField(null=True, blank=True, max_length=255)
    objects = DeferredDataManager()

