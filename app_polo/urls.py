from django.urls import path, include

from . import views

urlpatterns = [
    path("accounts/profile/", views.profile),
    path("accounts/logout/", views.logout_view),
    path("accounts/", include("django.contrib.auth.urls")),
    path("orders/", views.orders),
    path("order/", views.order),
    path("", views.index, name="index")
]
