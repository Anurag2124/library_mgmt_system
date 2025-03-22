from .models import AdminUser, Book
from rest_framework import serializers

class AdminSignupSerializer(serializers.ModelSerializer):
  """
  Serializer for AdminUser signup
  """

  password = serializers.CharField(write_only=True, min_length=6)

  class Meta:
    model = AdminUser
    fields = ['id','username','email','password']

  def create(self, validated_data):
    """Creates a new admin."""
    return AdminUser.objects.create_superuser(**validated_data)


class BookSerializer(serializers.ModelSerializer):
  """
  Serializer for Book model.
  """

  class Meta:
    model = Book
    fields = '__all__'
