from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

# Create your views here.
def book_list(request):
    books= Book.objects.all().order_by('title')
    paginator = Paginator(books, 5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'books/book_list.html', {'page_obj': page_obj})