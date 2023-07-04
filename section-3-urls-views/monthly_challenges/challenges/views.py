from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
  "january": "Eat veggies",
  "february": "Walk for at least 20 mins per day",
  "march": "Learn Django for at least 20 min per day",
  "april": "code",
  "may": "Eat veggies",
  "june": "Walk for at least 20 mins per day",
  "july": "Learn Django for at least 20 min per day",
  "august": "code",
  "september": "Eat veggies",
  "october": "Walk for at least 20 mins per day",
  "november": "Learn Django for at least 20 min per day",
  "december": "code"
}

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
  months = list(monthly_challenges.keys())

  if month > len(months):
    return HttpResponseNotFound("Invalid month")

  redirect_month = months[month - 1]

  return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
  except:
    return HttpResponseNotFound("This month is not suppoerted")

  return HttpResponse(challenge_text)