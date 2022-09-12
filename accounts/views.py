from rest_framework import generics, permissions, status
from rest_framework.response import Response
from accounts.serializers import UserRegistrationSerializer
from accounts.models import User


class Registration(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            password = data['password']

            user = User(
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                mobile=data['mobile'],
                intro=data['intro'],
                is_active=False
            )

            if password is not None:
                user.set_password(password)

            user.save()

            if user:
                message = 'Account created successfully!'
                return Response({"message": message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
