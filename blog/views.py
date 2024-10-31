from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Maxsulot, Kirim, Chiqim
from blog.serializer import MaxsulotSerializer, KirimSerializer, ChiqimSerializer


class MaxsulotListAPI(APIView):
    def get(self,request):
        maxsulotlar = Maxsulot.objects.all()
        serializer = MaxsulotSerializer(maxsulotlar, many=True).data
        return Response(serializer)

    def post(self, request):
        data = request.data
        serializer = MaxsulotSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            malumot = {
                "status":"Okk",
                "xabar": "malumot saqlandi"
            }
            return Response(malumot)
        else:
            malumot = {
                "status":"Fail",
                "xaabar":"saqlashda xatolik bo'ldi"

            }
        return Response(malumot)

class MaxsulotDetail(APIView):

    def maxsulot_olish(self, pk):
        try:
            return Maxsulot.objects.get(id=pk)
        except Maxsulot.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        maxsulot = self.maxsulot_olish(pk)
        serializer = MaxsulotSerializer(maxsulot).data

        return Response(serializer)

    def put(self, request, pk):
        maxsulot = self.maxsulot_olish(pk)
        serializer = MaxsulotSerializer(maxsulot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        maxsulot = self.maxsulot_olish(pk)
        maxsulot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KirimListAPI(APIView):
    def get(self,request):
        kirim = Kirim.objects.all()
        serializer = KirimSerializer(kirim, many=True).data
        return Response(serializer)


    def post(self, request):
        data = request.data
        serializer = KirimSerializer(data=data)
        if serializer.is_valid():

            kirim = serializer.save()
            maxsulot = kirim.maxsulot
            maxsulotSoni =int(request.data["maxsulotSoni"])
            umumiySoni = int(maxsulot.umumiySoni)
            yigindi = int(maxsulotSoni + umumiySoni)
            maxsulot.umumiySoni = yigindi
            maxsulot.save()

            malumot = {
                    "status":"Okk",
                    "xabar": "malumot saqlandi"
                }
            return Response(malumot)
        else:
            malumot = {
                "status":"Fail",
                "xaabar":"saqlashda xatolik bo'ldi"

            }
        return Response(malumot)

class ChiqimListAPI(APIView):

    def get(self, request):
        maxsulotlar = Chiqim.objects.all()
        serializer = ChiqimSerializer(maxsulotlar, many=True).data
        return Response(serializer)

    def post(self, request):
        data = request.data
        serializer = ChiqimSerializer(data=data)
        if serializer.is_valid():

            chiqim = Chiqim
            umumiy_narxi = int(chiqim.maxsulot.sotish_narxi)
            qolishi = int(umumiy_narxi - umumiy_narxi)
            chiqim.maxsulot.sotish_narxi = qolishi
            chiqim.save()

            malumot = {
                    "status":"Okk",
                    "xabar": "malumot saqlandi"
                }
            return Response(malumot)
        else:
            malumot = {
                "status":"Fail",
                "xaabar":"saqlashda xatolik bo'ldi"

            }
        return Response(malumot)
