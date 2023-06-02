# 1) ////////  Serializing Objects and Deserializing Objects //////// 
# from rest_framework import serializers

# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()


""" 
Serializing Objects

>>> from products.models import Comment
>>> from products.serializers import CommentSerializer
>>> from datetime import datetime  
>>> comment = Comment(email='elyor@gmail.com', content='foo bar')
>>> serializer = CommentSerializer(comment)
>>> serializer.data
{'email': 'elyor@gmail.com', 'content': 'foo bar', 'created': '2023-06-01T23:26:23.323816Z'}
>>> from rest_framework.renderers import JSONRenderer
>>> json = JSONRenderer().render(serializer.data)
>>> json
b'{"email":"elyor@gmail.com","content":"foo bar","created":"2023-06-01T22:23:13.474077Z"}'

Deserializing Objects

>>> import io
>>> from rest_framework.parsers import JSONParser
>>> stream = io.BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> serializer = CommentSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([('email', 'elyor@gmail.com'), ('content', 'foo bar'), ('created', datetime.datetime(2023, 6, 1, 22, 23, 13, 474077, tzinfo=zoneinfo.ZoneInfo(key='UTC')))])


"""

# 2) ///////// Saving instances  ////////
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance