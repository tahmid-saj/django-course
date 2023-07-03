from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#   return HttpResponse("Eat veggies")

# def feburary(request):
#   return HttpResponse("Walk for at least 20 mins per day")

# def march(request):
#   return HttpResponse("Learn Django for at least 20 min per day")

# def april(request):
#   return HttpResponse("Code")

def monthly_challenge_by_number(request, month):
  return HttpResponse(month)

def monthly_challenge(request, month):
  challenge_text = None

  if month == "january":
    challenge_text = "Eat veggies"
  elif month == "february":
    challenge_text = "Walk for at least 20 mins per day"
  elif month == "march":
    challenge_text = "Learn Django for at least 20 min per day"
  else:
    return HttpResponseNotFound("This month is not supported")

  return HttpResponse(challenge_text)