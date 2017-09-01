from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import Http404
from django.template import Template, Context, loader
from django.shortcuts import render_to_response


# Create your views here.
def hello(request):
    return HttpResponse("Hello Python Django!")


def current_datetime(request):
    current_date = datetime.datetime.now()
    # now = datetime.datetime.now()
    # t = loader.get_template('hellodjango/current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    # return render_to_response('hellodjango/current_datetime.html',
    #                           {'current_date': now})
    return render_to_response('hellodjango/current_datetime.html',
                              locals())


def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    # assert False
    current_date = datetime.datetime.now()
    next_time = current_date + datetime.timedelta(hours=hour_offset)
    # return render_to_response('hellodjango/hours_ahead.html',
    #                           {'offset': offset, 'hours_ahead': dt})
    return render_to_response('hellodjango/hours_ahead.html', locals())


def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('hellodjango/meta.html', locals())
