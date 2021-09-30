from rest_framework.serializers import ModelSerializer
from .models import Beat


class GetBeatsSerializer(ModelSerializer):

    

    class Meta:
        model = Beat
        fields="__all__"