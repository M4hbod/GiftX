from django.shortcuts import render
from django.views import View

from products.models import Brand


class HomeView(View):
    def get(self, request):
        gift_card_brands = Brand.objects.all()
        return render(request, "core/index.html", {"gift_card_brands": gift_card_brands})
