from django.shortcuts import render

# Create your views here.
def project_app(request):
    return render(request, 'index.html', {})
