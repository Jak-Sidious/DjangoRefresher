
from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review

class CourseSerializer(serializers.ModelSerializer): 
    ##HyperlinkedRelatedField works best with single or few reviews
    reviews = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews',
        )
        model = models.Course