from django.db import models
from django.utils.translation import ugettext_lazy as _


class Make(models.Model):
    class Meta:
        verbose_name = _("Марка")
        verbose_name_plural = _("Марки коли")

    car_make = models.CharField(max_length=45, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.car_make


class Car(models.Model):
    class Meta:
        verbose_name = _("Кола")
        verbose_name_plural = _("Коли")

    car_make_id = models.ForeignKey(Make, on_delete=models.DO_NOTHING)
    car_model = models.CharField(max_length=45)
    horsepower = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.car_model
