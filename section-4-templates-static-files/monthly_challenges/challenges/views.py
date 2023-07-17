from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

  response_data = f"<ul>{list_items}</ul>"
  
  return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
    return HttpResponseNotFound("Invalid month")

  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
      "text": challenge_text,
      "month_name": month.capitalize()
    })
  except:
    return HttpResponseNotFound("<h1>This month is not supported</h1>")

  return HttpResponse(response_data)