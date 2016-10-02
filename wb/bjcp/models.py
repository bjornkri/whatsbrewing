from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    code = models.CharField(max_length=31)
    name = models.CharField(max_length=255)


class Note(models.Model):
    order = models.PositiveIntegerField(default=0)
    text = models.TextField()
    category = models.ForeignKey(Category)


class Stat(models.Model):
    low = models.PositiveIntegerField()
    high = models.PositiveIntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=255)


class SubCategory(models.Model):
    code = models.CharField(max_length=31)
    name = models.CharField(max_length=255)
    aroma = models.TextField(blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    mouthfeel = models.TextField(blank=True, null=True)
    impression = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    comparison = models.TextField(blank=True, null=True)
    examples = models.TextField(blank=True, null=True)
    varieties = models.TextField(blank=True, null=True)
    entry_instructions = models.TextField(blank=True, null=True)
    ibu = models.ForeignKey(Stat, blank=True, null=True, related_name='ibu_subcategory')
    og = models.ForeignKey(Stat, blank=True, null=True, related_name='og_subcategory')
    fg = models.ForeignKey(Stat, blank=True, null=True, related_name='fg_subcategory')
    srm = models.ForeignKey(Stat, blank=True, null=True, related_name='srm_subcategory')
    abv = models.ForeignKey(Stat, blank=True, null=True, related_name='abv_subcategory')
    tags = models.ManyToManyField(Tag)
