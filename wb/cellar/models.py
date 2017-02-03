from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from bjcp.models import SubCategory
from django.contrib.auth.models import User


class Brewery(models.Model):
    """
    Where the magic happens
    """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'breweries'


class Beer(models.Model):
    """
    The platonic recipe
    """
    name = models.CharField(max_length=255)
    style = models.ForeignKey(SubCategory)
    description = models.TextField(blank=True)
    brewery = models.ForeignKey(Brewery)

    def __unicode__(self):
        return "{0} ({1})".format(self.name, self.style.name)


class Brew(models.Model):
    """
    The actual brewed variant
    """
    PLANNED, PRIMARY, SECONDARY, BOTTLED, KEGGED = range(5)
    STATUS_OPTIONS = (
        (PLANNED, 'planned'),
        (PRIMARY, 'primary'),
        (SECONDARY, 'secondary'),
        (BOTTLED, 'bottled'),
        (KEGGED, 'kegged')
    )
    EMPTY, VERY_LOW, LOW, HIGH = range(4)
    STOCK_OPTIONS = (
        (EMPTY, 'empty'),
        (VERY_LOW, 'very low'),
        (LOW, 'low'),
        (HIGH, 'high')
    )
    beer = models.ForeignKey(Beer)
    batch = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    status = models.PositiveSmallIntegerField(choices=STATUS_OPTIONS, default=PRIMARY)
    stock = models.PositiveSmallIntegerField(choices=STOCK_OPTIONS, default=HIGH)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return "{0} #{1}".format(self.beer, self.batch)
