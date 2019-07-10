from django.shortcuts import render, HttpResponse

html_base = """
<h1>MI web personal</h1>
<ul>
    <li><a href="/"> Portada </a></li>
    <li><a href="/about"> acerca de </a></li>
</ul>    
"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")