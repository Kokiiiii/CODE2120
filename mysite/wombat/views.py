from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import os, sys

# Create your views here.
@csrf_exempt
def assignment1(request):
	jsob = {"startNumber": 0, "length": 10, "multiNumber": 2, "maximum": 50000} #defaults
	log = []
	if request.method == "POST":
		try:
			
			return JsonResponse({"assignment1":"numarray"})

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})		
	else:
		return JsonResponse(jsob)		