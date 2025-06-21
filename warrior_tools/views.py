from django.shortcuts import render


def handler404(request, exception):
    """
    Custom 404 error handler.

    Renders the 404 error page when a requested resource is not found.

    Args:
        request: The HttpRequest object.
        exception: The exception that triggered this handler.

    Returns:
        HttpResponse with status code 404 and rendered 404 template.
    """
    return render(request, "errors/404.html", status=404)
