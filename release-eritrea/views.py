from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'error404.html', status=404)