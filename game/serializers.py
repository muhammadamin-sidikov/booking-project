from rest_framework import serializers
from .models import Game
from fields.models import Field

class MaydonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['nomi']

class GameListSerializer(serializers.ModelSerializer):
    maydon = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['qolgan_joy']

    def create(self, validated_data):
        maydon = validated_data['maydon']
        validated_data['qolgan_joy'] = maydon.joy_soni
        return super().create(validated_data)

    def get_maydon(self, obj):
        return obj.maydon.name

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['maydon', 'sana']


