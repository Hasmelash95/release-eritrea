from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'error404.html', status=404)


def handler500(request):
    return render(request, 'error/error500.html', status=500)