from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'
    

def lista_libros(request):
    # Obtén todos los libros
    all_books = Book.objects.all()
    # Filtra los libros con valoración mayor a 1500
    high_rated_books = Book.objects.filter(valoracion__gt=1500)

    context = {
        'all_books': all_books,
        'high_rated_books': high_rated_books
    }
    return render(request, 'lista_libros.html', context)



# https://docs.djangoproject.com/en/5.1/topics/forms/
def crear_libro(request):
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST)
        if form.is_valid(): # si el formulario es valido
            form.save() # guarda los datos en la base de datos
            return redirect('lista_libros')
    else: # si el metodo es GET
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})

