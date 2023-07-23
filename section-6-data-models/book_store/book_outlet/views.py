from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.

def index(request):
  books = Book.objects.all()
  return render(request, "book_outlet/index.html", {
    "books": books
  })

def book_detail(request, slug):
  # try:
  #   book = Book.objects.get(pk=id)
  # except:
  #   raise Http404()

  book = get_object_or_404(Book, slug=slug)

  return render(request, "book_outlet/book_detail.html", {
    "title": book.title,
    "author": book.author,
    "rating": book.rating,
    "is_best_seller": book.is_best_selling
  })