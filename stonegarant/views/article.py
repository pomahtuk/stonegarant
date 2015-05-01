from django.shortcuts import get_object_or_404, render_to_response
from stonegarant.models import *
from django.template import RequestContext


def articles_view(request):
    all_articles = StaticPage.objects.filter(show_in_list=True)
    service_page_data = get_object_or_404(ServicePage, id=80)
    return render_to_response('article.html', {
        'articles': all_articles,
        'service_page': service_page_data
    }, context_instance=RequestContext(request))