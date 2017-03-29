from django.shortcuts import get_object_or_404, render
from stonegarant.models import *
from django.template import RequestContext


def ready_works_view(request):
    works = ReadyWork.objects.all().order_by('-pub_date')
    service_page_data = get_object_or_404(ServicePage, id=76)
    return render(request, 'ready_work.html', {
        'works': works,
        'service_page': service_page_data
    })
