from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty

from .models import Maxsulot, Kirim, Chiqim


class MaxsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maxsulot
        fields = ("__all__")

    def validate(self, data):

        nomi = data.get("nomi",None)

        if Maxsulot.objects.filter(nomi__exact=nomi):

            raise ValidationError ({
              "status": False,
                "xabar": "qoshildi"
            })
        return data

class KirimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kirim
        fields = ("maxsulot", "maxsulotSoni", "xodim", "kirim_narxi")

class ChiqimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chiqim
        fields = ("maxsulot", "maxsulotSoni", "sotish_narxi", "xodim")