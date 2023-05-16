from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    # rater = serializers.SerializerMethodField()
    # agent = serializers.SerializerMethodField()
    rater = serializers.StringRelatedField(source='rater.username')
    agent = serializers.StringRelatedField(source='agent.user.username')

    class Meta:
        model = Rating
        exclude = ['updated_at', 'pkid']

    # def get_rater(self, obj):
    #     return obj.rater.username

    # def get_agent(self, obj):
    #     return obj.agent.user.username
