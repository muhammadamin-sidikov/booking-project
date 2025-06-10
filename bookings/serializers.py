from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from game.models import Game
from users.models import User
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, attrs):
        sana_obj = attrs.get("sana")
        soni = attrs.get("soni")

        if sana_obj.qolgan_joy == 0:
            raise serializers.ValidationError("Joy qolmadi.")
        elif sana_obj.qolgan_joy < soni:
            raise serializers.ValidationError("Mavjud joydan ko'proq bron qilyapsiz.")

        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class SanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['sana']


class BookingListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    sana = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = "__all__"

    @extend_schema_field(serializers.CharField())
    def get_user(self, obj):
        return obj.user.email

    def get_sana(self, obj) -> str:
        return f"{obj.sana.maydon} - {obj.sana.sana.strftime('%Y-%m-%d %H:%M')}"

