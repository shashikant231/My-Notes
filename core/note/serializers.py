from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("name",)

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = "__all__"