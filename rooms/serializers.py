from rest_framework import serializers
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


# ModelSerializer를 사용하면 id, created_at, updated_at 필드는 자동으로 read_only로 지정됨
class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(serializers.ModelSerializer):
    # Serializer 관계 지정 필트 커스터마이징
    owner = TinyUserSerializer(
        read_only=True,
    )
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    # SerializerMethodField 정의 시 get_ 로 시작하는 method 정의
    def get_rating(self, room):
        return room.rating()


class RoomListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
        )

    def get_rating(self, room):
        return room.rating()
