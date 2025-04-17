from configapp.models import GroupStudent
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = ['title', 'course', 'teacher']