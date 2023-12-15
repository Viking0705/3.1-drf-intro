# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement

from measurement.serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer

from rest_framework import status

# Создание датчиков и список датчиков
class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Добавление измерений
class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    
# Информация по конкретному датчику и обновление информации о датчике
class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sen = self.queryset.get(id=pk)
        print(sen)
        ser_data = SensorSerializer(sen, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

