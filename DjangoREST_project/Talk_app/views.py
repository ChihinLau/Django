from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from Talk_app.models import talkModel
from Talk_app.serializers import TalkSerializer
from django.views.decorators.csrf import csrf_exempt
import datetime
"""
#ID, Name, Speaker, Venue, Duration
talk1 = talkModel.objects.create(Name="talk1", Speaker="Tom", Venue="Venue1", Duration=datetime.timedelta(hours=1))
talk2 = talkModel.objects.create(Name="talk2", Speaker="John", Venue="Venue2", Duration=datetime.timedelta(hours=5))
talk1.save()
talk2.save()
"""

@csrf_exempt
#@Employee(['GET', 'POST'])

def talk_list(request):
	if request.method == "GET":
		talks=talkModel.objects.all()
		serializer = TalkSerializer(talks, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = TalkSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def talk_detail(request, pk):

    try:
        new_talk = talkModel.objects.get(pk=pk)
    except talkModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TalkSerializer(new_talk)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TalkSerializer(new_talk, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        new_talk.delete()
        return HttpResponse(status=204)
