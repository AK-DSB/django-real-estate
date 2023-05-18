from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    full_name = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    # reviews = serializers.SerializerMethodField()
    reviews = RatingSerializer(source='agent_review', many=True)

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'full_name', 'email',
                  'id', 'phone_number', 'profile_photo', 'about_me', 'license',
                  'gender', 'country', 'city', 'is_buyer', 'is_seller', 'is_agent',
                  'rating', 'num_reviews', 'reviews', 'top_agent']

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f'{first_name} {last_name}'

    # def get_reviews(self, obj):
    #     reviews = obj.agent_review.all()
    #     serializer = RatingSerializer(reviews, many=True)
    #     return serializer.data


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_photo', 'about_me', 'license', 'gender',
                  'country', 'city', 'is_buyer', 'is_seller', 'is_agent', 'top_agent']
