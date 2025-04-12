from django.shortcuts import render
from django.http import JsonResponse
import json
import google.generativeai as genai

genai.configure(api_key="AIzaSyCz0zBOuiOAv6iBkjGNse05NROnuKAtLRY")
def chat(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text




def home(request):
	return render(request,'home.html',{})

def mutual(request):
	return render(request,'mutual.html',{})

def mutualfund(request,symbol):
	return render(request,'mutualfund.html',{'symbol':symbol})


def stock(request,symbol):
	return render(request,'stock.html',{'symbol':symbol.upper()})

def crypto(request):
	return render(request,'crypto.html',{})

def exchange(request):
	return render(request,'exchange.html',{})

def get_response(request):
	if request.method=='POST':
		data = json.loads(request.body)
		try:
			return JsonResponse({'message':chat(data['message'])})
		except:
			return JsonResponse({'message':'NOT WORKING'})

	return JsonResponse({"message":"Wrong Protocol"})

	
