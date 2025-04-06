from rest_framework import serializers
from descargas.models import Descarga

class DescargasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descarga
        fields = "__all__"
