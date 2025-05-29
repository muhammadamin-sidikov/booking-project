from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserCreateSerializer, EmailVerificationSerializer, VerifyCodeSerializer
from .utils import send_verification_code
from .models import User, EmailVerification

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method 'POST' not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UserCreateApi(APIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'response': 'Successfully registered a new user.',
                'email': user.email,
                'name': user.name
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                }
            })
        else:
            return Response({"detail": "Email yoki parol noto‘g‘ri"},
                            status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return Response({"message": f"Salom, {request.user.email}!"})

class SendEmailVerificationCodeAPIView(APIView):
    # def get(self, request):
    #     return Response("get requeset")

    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = send_verification_code(email)
        return Response({"detail": "Kod yuborildi."})

class VerifyEmailCode(APIView):
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        try:
            verification = EmailVerification.objects.get(email=email)
        except EmailVerification.DoesNotExist:
            return Response({'detail': 'Kod topilmadi'}, status=status.HTTP_400_BAD_REQUEST)

        if verification.is_expired():
            return Response({'detail': 'Kod muddati tugagan'}, status=status.HTTP_400_BAD_REQUEST)

        if verification.code != code:
            return Response({'detail': 'Kod noto‘g‘ri'}, status=status.HTTP_400_BAD_REQUEST)

        verification.delete()

        return Response({'detail': 'Email muvaffaqiyatli tasdiqlandi'}, status=status.HTTP_200_OK)
