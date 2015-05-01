from django.shortcuts import get_object_or_404, render_to_response
from stonegarant.models import *
from django.template import RequestContext


def replies_view(request):
    all_replies = Reply.objects.all().order_by('-id')
    service_page_data = get_object_or_404(ServicePage, id=77)
    return render_to_response('reply.html', {
        'replies': all_replies,
        'service_page': service_page_data
    }, context_instance=RequestContext(request))