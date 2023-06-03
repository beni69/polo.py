from django import forms

from app_polo.models import Color, Order, Size

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "size", "color", "amount"]
        labels = {
            "product": "Termék",
            "size": "Méret",
            "color": "Szín",
            "amount": "Darabszám",
        }

    def __init__(self, product, *args ,**kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        # reuse product value if editing an instance
        if "instance" in kwargs and kwargs.get("instance"):
            product = kwargs.get("instance").product

        if product is None:
            self.fields["color"].queryset = Color.objects.none()
            self.fields["size"].queryset = Size.objects.none()
        else:
            self.fields["color"].queryset = product.colors.all()
            self.fields["size"].queryset = product.sizes.all()
