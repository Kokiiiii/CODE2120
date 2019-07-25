from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.
@csrf_exempt
def assignment1(request):
	jsob = {"startNumber": 0, "length": 10, "multiNumber": 2, "maximum": 50000} #defaults
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			#######################
			#Custom Function Below#
			#######################
			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			multiNumber = int(jsob["multiNumber"])
			maximum = int(jsob["maximum"])
			loop = range(length)


			numarray = []

			baseno = startNumber


			for l in loop:
				if baseno < maximum:
					numarray.append(baseno)
					baseno = baseno*multiNumber
					

			return JsonResponse({"assignment1":numarray})

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})		
	else:
		return JsonResponse(jsob)		