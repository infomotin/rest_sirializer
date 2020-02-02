from abc import ABC
from datetime import datetime
# timesince are a functions
from django.utils.timesince import timesince

from rest_framework import serializers
from news.models import Article, Journalist


# # Create a serializer that like a models as Django create a database table
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=50)
#     title = serializers.CharField(max_length=120)
#     descriptions = serializers.CharField(max_length=200)
#     body = serializers.CharField()
#     location = serializers.CharField(max_length=200)
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField(default=True)
#     create_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#
#     # ArticleSerializer class are Inherited with rest frameworks serializers bass class
#
#     # that is functions overwrite
#     def create(self, validated_data):
#         # article Model are create that get from json format
#         return Article.objects.create(**validated_data)  # arguments are like **kwargs (key with value)
#         # if class properties are satisfied with key data as like insert sql commend then object are insert into
#         # database
#
#     # instance are Article objects
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.descriptions = validated_data.get('descriptions', instance.descriptions)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         if data["title"] == data["descriptions"]:
#             raise serializers.ValidationError(" Title and descriptions are not Same ")
#         return data
# now another serializer adding to our serializer file for Journalist

# class JournalistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Journalist
#         fields = "__all__"


# Create Model serializer class
class ArticleSerializer(serializers.ModelSerializer):
    # new method declaring at first
    # its works as new fields as like model fields but not effect on database table
    # its temporary work with function
    # working as like javascript current data work
    time_since_publication = serializers.SerializerMethodField()

    # this variable are contain Foreignkey value with this value
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__" # for all fields in Article Model
        # fields = ("title","body") # selected fields

    # now create a method for serializer method field tins functions has naming conventions That are depend on
    # SerializerMethodField (get + var_name(SerializerMethodField()))
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    # implement a functions that are verified field data
    # its a bass class function that over lade forms this class
    # functions parameter name is your won just its is class instance
    def validate(self, data):
        # model field name
        if data["title"] == data["descriptions"]:
            raise serializers.ValidationError("Can Not Same title and descriptions")
        return data

    # if return this functions than insert data into database fields

    # set conditions on a Specific fields with functions
    # has naming conventions validated + fields name as like validated + title
    # thi paramitter are class properties of objects instance
    def validated_title(self, value):
        if len(value) < 45:
            raise serializers.ValidationError(" Your Title are smaller then 45 Creator ")
        return value
    # if return this functions than insert data into database fields


class JournalistSerializer(serializers.ModelSerializer):
    # Hyper Link views Serializer declearing
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, validators="class-apilist")

    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"
