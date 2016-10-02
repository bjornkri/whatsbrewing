from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from bjcp.models import Category, Stat


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open('bjcp/data/styleguide-2015.xml')
        soup = BeautifulSoup(f, 'xml')
        beers = soup.find('class', type="beer")
        for category in beers.findAll('category'):
            note_order = 0
            print category['id'], category.find('name').text
            cat = Category.objects.create(
                name=category.find('name').text,
                code=category['id'])
            for note in category.findAll('notes'):
                cat.note_set.create(order=note_order, text=note.text)
                note_order += 1
            for style in category.findAll('subcategory'):
                print "- ", style['id'], style.find('name').text
                subcat = cat.subcategory_set.create(
                    code = style['id'],
                    name = style.find('name').text
                )
                for attr in ['aroma', 'appearance', 'flavor', 'mouthfeel', 'impression', 'comments', 'history',
                             'ingredients', 'comparison', 'examples', 'varieties', 'entryinstructions']:
                    if getattr(style, attr):
                        setattr(subcat, attr, getattr(style, attr).text)
                for stat in ['ibu', 'og', 'fg', 'srm', 'abv']:
                    if getattr(style, stat):
                        if not getattr(style, stat)['flexible'] == 'true':
                            setattr(subcat, stat, Stat.objects.create(
                                low=getattr(style, stat).low.text.replace('.', ''),
                                high=getattr(style, stat).high.text.replace('.', '')))
                subcat.save()