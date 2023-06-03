from re import L
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from app_polo.models import Order, Product
from .forms import OrderForm

# Create your views here.
def index(req: HttpRequest):
    return render(req, "index.html", {})


@login_required
def profile(req:HttpRequest):
    ctx = {
        "title": "Fiók",
    }
    return render(req, "registration/profile.html", ctx)

@login_required
def logout_view(req:HttpRequest):
    logout(req)
    return redirect(index)

@login_required
def orders(req:HttpRequest):
    ord = Order.objects.filter(user=req.user.polouser)

    ctx = {
        "title": "Rendelések",
        "orders": ord,
    }
    return render(req, "orders.html", ctx)

@login_required
def order(req:HttpRequest):
    query = (req.GET or req.POST)

    p = None
    if "product" in query:
        p: Product | None = Product.objects.get(id=query.get("product"))

    id = None
    instance = None
    if "id" in query:
        id = query.get("id")
        instance = get_object_or_404(Order, id=id)

    if query.get("delete"):
        instance.delete()
        return redirect(orders)


    if req.method == "POST":
        form = OrderForm(p, req.POST, instance=instance)
        if form.is_valid():
            print(form.cleaned_data)
            ord = form.save(commit=False)
            ord.id = id
            ord.user = req.user.polouser
            print(ord)
            ord.save()
            return redirect(orders)
        else:
            print("INVALID FORM!!")

    else:
        form = OrderForm(p, instance=instance)

    return render(req, "order.html", { "form": form, "id": id })
