from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import Http404, JsonResponse
from stonegarant.models import *
from django.template import RequestContext
from stonegarant.forms import OrderCreateForm, OrderUpdateForm
from django.http import JsonResponse


def order_create_view(request):
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order_instance = order_form.save()
        else:
            print('form invalid', order_form.errors)
            raise Http404

        return JsonResponse({'order_number': order_instance.order_number})

    else:
        print('not POST')
        raise Http404


def order_email_test(request):
    order_data = Order.objects.all()[:1].get()
    order_data.send_email()
    # order_data = get_object_or_404(Order, order_number='af4e4121')
    return render_to_response('email/html/new_order.html', {'order': order_data}, context_instance=RequestContext(request))


# this has to respond on GET if order created already
def order_confirm_view(request, order_number):
    order_data = get_object_or_404(Order, order_number=order_number)
    return render_to_response('order_confirm.html', {'order': order_data}, context_instance=RequestContext(request))


# POST - update order and return confirmation page
# GET - just render confirmation page
def order_details_view(request, order_number):
    order_data = get_object_or_404(Order, order_number=order_number)
    # check if we have a post request and data is not set yet
    if order_data.status != 'D':
        if request.method == 'POST':
            order_form = OrderUpdateForm(request.POST or None, instance=order_data)
            if order_form.is_valid():
                order_data = order_form.save()
                order_data.status = 'D'
                order_data.save()
    return render_to_response('order_details.html', {'order': order_data}, context_instance=RequestContext(request))
