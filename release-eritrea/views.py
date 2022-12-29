from django.shortcuts import render


def handler400(request, exception):
    return render(request, 'error/error400.html', status=400)


def handler403(request, exception):
    return render(request, 'error/error403.html', status=403)


def handler404(request, exception):
    return render(request, 'error/error404.html', status=404)


def handler500(request):
    return render(request, 'error/error500.html', status=500)