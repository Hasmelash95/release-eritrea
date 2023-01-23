from django.shortcuts import render


def handler400(request, exception):
    """
    Renders the custom error 400 page.
    """
    return render(request, 'error/error400.html', status=400)


def handler403(request, exception):
    """
    Renders the custom error 403 page.
    """
    return render(request, 'error/error403.html', status=403)


def handler404(request, exception):
    """
    Renders the custom error 404 page.
    """
    return render(request, 'error/error404.html', status=404)


def handler405(request, exception):
    """
    Renders the custom error 405 page.
    """
    return render(request, 'error/error405.html', status=405)


def handler500(request):
    """
    Renders the custom error 500 page.
    """
    return render(request, 'error/error500.html', status=500)
