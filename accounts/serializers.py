from rest_framework import serializers
from accounts.models import User

"""
    User registration serializer
"""
class UserRegistrationSerializer(serializers.ModelSerializer):

    mobile = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        exclude = ['user_id', 'date_joined', 'last_login', 'is_superuser',
                   'is_active', 'groups', 'user_permissions']
        extra_kwargs = {'password': {'write_only': True}}
