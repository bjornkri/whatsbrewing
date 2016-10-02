from rest_framework import serializers

from .models import Category, SubCategory, Stat, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('text', )


class StatCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = ('low', 'high')


class InlineSubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('code', 'name', 'url')
        extra_kwargs = {
            'url': {'lookup_field': 'code'}
        }


class MinimalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('code', 'name', 'url')


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('category', 'code', 'name', 'url',
                  'aroma', 'appearance', 'flavor', 'mouthfeel', 'impression', 'comments',
                  'history', 'ingredients', 'comparison', 'examples', 'varieties', 'entryinstructions',
                  'ibu', 'og', 'fg', 'srm', 'abv', 'tags')
        extra_kwargs = {
            'url': {'lookup_field': 'code'}
        }

    category = MinimalCategorySerializer()
    ibu = StatCategorySerializer()
    og = StatCategorySerializer()
    fg = StatCategorySerializer()
    srm = StatCategorySerializer()
    abv = StatCategorySerializer()


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('code', 'name', 'notes', 'url', 'styles')

    styles = InlineSubCatSerializer(many=True, source='subcategory_set')
    notes = NoteSerializer(many=True, source='note_set')
