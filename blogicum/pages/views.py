from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AboutPage(TemplateView):
    """About page view"""

    template_name = 'pages/about.html'


class RulesPage(TemplateView):
    """Rules page view"""

    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_token_exception_page(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def server_error_page(request, *args, **argv):
    return render(request, 'pages/500.html', status=500)
