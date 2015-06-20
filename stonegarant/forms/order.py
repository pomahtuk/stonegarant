from django.forms import ModelForm
from stonegarant.models import Order

class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['memorial', 'stella', 'cvetnik', 'podstavka', 'polirovka']


class OrderUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user_email', 'user_phone', 'user_name', 'user_comment']
