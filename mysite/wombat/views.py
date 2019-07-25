from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import os, sys

# Create your views here.
@csrf_exempt
def assignment1(request):
	return JsonResponse({"test":"working"})