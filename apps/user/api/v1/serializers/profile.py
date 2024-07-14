from rest_framework import serializers

from apps.user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
