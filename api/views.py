from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from .models import Users
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/user-list/',
		'Detail View':'/user-detail/<str:pk>/',
		'Create':'/user-create/',
		'Update':'/user-update/<str:pk>/',
		'Delete':'/user-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def userList(request):
	users = Users.objects.all().order_by('-id')
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
	users = Users.objects.get(id=pk)
	serializer = UserSerializer(users, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
	user = Users.objects.get(id=pk)
	serializer = UserSerializer(instance=user, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	user = Users.objects.get(id=pk)
	user.delete()

	return Response('Item succsesfully delete!')



