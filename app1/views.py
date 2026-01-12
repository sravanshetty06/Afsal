from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render

def index(request):
    """
    Renders the MR.Tech__077 CCTV landing page
    """
    return render(request, "app1/index.html")
