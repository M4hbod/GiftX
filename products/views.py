from django.shortcuts import render
from django.views import View

from products.models import GiftCard, BrandCategory


class GiftCardCategoryView(View):
    def get(self, request, category_id=None):
        products = GiftCard.objects.filter(category__id=category_id)
        return render(request, "products/gift_card_category_detail.html", {"products": products})


class BrandCategoryListView(View):
    def get(self, request):
        categories = BrandCategory.objects.prefetch_related("brands").all()
        return render(request, "products/brand_category_list.html", {"categories": categories})
