from django.shortcuts import render
from django.views import View

from gift_cards.models import GiftCardCategory


class HomeView(View):
    def get(self, request):
        gift_card_categories = GiftCardCategory.objects.all()
        return render(request, "core/index.html", {"gift_card_categories": gift_card_categories})
