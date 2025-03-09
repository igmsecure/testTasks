from rest_framework import serializers
from .models import Letter, Package


class LetterSerializer(serializers.ModelSerializer):
    letter_type_display = serializers.CharField(source="get_letter_type_display", read_only=True)

    class Meta:
        model = Letter
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    package_type_display = serializers.CharField(source="get_package_type_display", read_only=True)

    class Meta:
        model = Package
        fields = '__all__'
