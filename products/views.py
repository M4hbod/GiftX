from django.shortcuts import render
from django.views import View

from products.models import GiftCard, BrandCategory


class GiftCardBrandProductsView(View):
    def get(self, request, brand_id=None):
        products = GiftCard.objects.filter(brand__id=brand_id)
        return render(request, "products/gift_card_category_detail.html", {"products": products})


class BrandCategoryListView(View):
    def get(self, request):
        categories = BrandCategory.objects.prefetch_related("brands").all()
        return render(request, "products/brand_category_list.html", {"categories": categories})
