from django.shortcuts import render

# Create your views here.


def rules(request):

    template = 'pages/rules.html'
    context = {}

    return render(request, template, context)


def about(request):

    template = 'pages/about.html'
    context = {}

    return render(request, template, context)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_token_exception_page(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def server_error_page(request, *args, **argv):
    return render(request, 'pages/500.html', status=500)
