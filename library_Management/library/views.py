from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

# Create your views here.
def books(request):
    """This function is resposible to show all the book in home page for students after login """
    if request.user.is_authenticated:
        book_data=Books.objects.all()
        return render(request, "home.html",{'book_data':book_data})
    else:
        return HttpResponse("<center><h3><div style='color:red;margin-top:200px'>You'r invailed user!!!<br><a href='/login'>Login First</a></div>")