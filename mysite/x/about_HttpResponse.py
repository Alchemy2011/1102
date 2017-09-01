from django.http import HttpResponse


def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def ua_diaplay_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)


def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


