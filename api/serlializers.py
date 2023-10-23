from django.db.models import fields
from rest_framework import serializers
from .models import Carlist,ShowroomList
 


class CarListSerializer(serializers.ModelSerializer):
    # if we want to show a field but it does not exist in model,it is just use at some 
    # occassion so we do not want to save it in DB.we will just show it in api---
    # here we calculate discount price and show it in api response but we will not save it in DB.

    discounted_price = serializers.SerializerMethodField()


    # getting models fields directly, No need of writing big code-
    # Youtube- https://www.youtube.com/watch?v=9gxKJTBoFk8
    # he greatly explains how basics works then how Model Serializer works
    class Meta:
        model = Carlist
        fields = '__all__'
        # fields = ['id','name','description']    To show only 3 fields in api
        # exclude = ['name']                      To exclude one field 

    def get_discounted_price (self,object):     # def get_{your field name}
        discountprice = object.price-5000
        return discountprice

    def validate_price(self, value):
        if value <= 20000:
            raise serializers.ValidationError('Price must be greater than 20000')
        return value



class ShowroomSerializer(serializers.ModelSerializer):
    #<<<<-----use to show data with help of Foreign key------>>>>
    #Showroom= CarListSerializer(read_only=True,many=True)   #-----to show all fields in api------->>>>
    
    # it returns name field of cars in showroom because in car model we return name field
    # Showroom = serializers.StringRelatedField(many=True)

    Showroom = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    class Meta:
        model = ShowroomList
        fields = '__all__'