from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(null=True)
    double_number = models.IntegerField(null=True)


class ForeignModel(models.Model):
    name = models.CharField(max_length=100)
    my = models.ForeignKey(MyModel)


class NullableForeignModel(models.Model):
    name = models.CharField(max_length=100)
    my = models.ForeignKey(MyModel, null=True, blank=True)


class NonNullableForeignModel(models.Model):
    name = models.CharField(max_length=100)
    my = models.ForeignKey(MyModel)
