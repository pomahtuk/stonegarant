from django.shortcuts import get_object_or_404, render_to_response
from stonegarant.models import *
from django.template import RequestContext


def memorial_view(request, memorial_slug):
    memorial_data = get_object_or_404(Memorial, slug=memorial_slug)
    # add 1 to popularity of this particular monument on view
    memorial_data.popularity += 1
    memorial_data.save()
    return render_to_response('product.html', {'memorial': memorial_data}, context_instance=RequestContext(request))
