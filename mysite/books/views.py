from django.shortcuts import render
from django.shortcuts import render_to_response
from . import models
from django.http import HttpResponse


# Create your views here.
def book_list(request):
    books = models.Book.objects.order_by('title')
    return render_to_response('books/book_list.html', {'books': books})


def search_form(request):
    return render_to_response('books/search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = models.Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html',
                                      {'books': books, 'query': q})
    return render_to_response('books/search_form.html',
                              {'errors': errors})


"""1
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return render_to_response('books/search.html', locals())
"""
