from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fruta
from .serializers import FrutaSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Listar': '/listar/',
        'Crear': '/crear/',
        'Editar': '/editar/<str:pk>/',
        'Eliminar': '/eliminar/<str:pk>/',
        }
    return Response(api_urls)

@api_view(['POST'])
def crear_fruta(request):
    fruta = FrutaSerializer(data=request.data)
  
    # validating for already existing data
    if Fruta.objects.filter(**request.data).exists():
        raise fruta.ValidationError('This data already exists')
  
    if fruta.is_valid():
        fruta.save()
        return Response(fruta.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def listar_frutas(request):
    # checking for the parameters from the URL
    if request.query_params:
        fruta = Fruta.objects.filter(**request.query_param.dict())
    else:
        fruta = Fruta.objects.all()
  
    # if there is something in items else raise error
    if fruta:
        serializer = FrutaSerializer(fruta, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
def actualizar_fruta(request, pk):
    fruta = Fruta.objects.get(id=pk)
    serializer = FrutaSerializer(instance=fruta, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def eliminar_fruta(request, pk):
    fruta = Fruta.objects.get(pk=pk)
    if fruta:
        fruta.delete()
        return Response('Fruta borrada satisfactoriamente')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

