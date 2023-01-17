from rest_framework import serializers
from blogs import models

class Productserializers(serializers.ModelSerializer):

    class Meta:  #uslovnost
        model = models.Product
        fields = ('id','name','price','description','quantity','is_active')


class Categoryserializers(serializers.ModelSerializer):
    class Meta:  # uslovnost
        model = models.Category
        fields = ('id', 'name1')
