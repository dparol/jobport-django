from rest_framework import serializers
from .models import uploadresume,candidateApplied


class resumeserializer(serializers.ModelSerializer):
    class Meta:
        model = uploadresume
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = candidateApplied
        fields = '__all__'

        
























































































































































































































































































































