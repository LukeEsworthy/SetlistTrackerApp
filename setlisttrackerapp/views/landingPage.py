from django.shortcuts import render


def landing_page(request):
    if request.method == 'GET':
        template = 'landingPage.html'
        context = {}

        return render(request, template, context)
