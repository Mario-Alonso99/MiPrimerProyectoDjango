from django.shortcuts import render, HttpResponse

html_base ="""
<h1>Mi Web Personal</h1><h2>Portada</h2>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""


# Create your views here.
def home(request):
    return HttpResponse (html_base + """
            <h2>Portada</h2>
            <p>Esto es la Portada</p>
    """)

def about(request):
    return HttpResponse (html_base + """
            <h2>Acerca de</h2>
            <p>Me Llamo Mario y soy Desarrollador BackEnd.</p>
    """)

def portfolio(request):
    return HttpResponse (html_base + """
            <h2>Portafolio</h2>
            <p>Algunos de mis Trabajos</p>
    """)

def contact(request):
    return HttpResponse (html_base + """
            <h2>Contacto</h2>
            <p>Aquí dejo mi Email para preguntarme sobre cualquier duda: <a href="mario.blazter99@gmail.com">mario.blazter99@gmail.com</a></p>
    """)