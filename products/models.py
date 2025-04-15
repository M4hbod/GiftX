from django.db import models


class GiftCardGroup(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GiftCardCountry(GiftCardGroup):
    country_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gift Card Country"
        verbose_name_plural = "Gift Card Countries"


class BrandCategory(models.Model):
    name = models.CharField(max_length=225, unique=True)
    icon = models.ImageField(upload_to="brand_categories/", null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=225, unique=True)
    category = models.ForeignKey(BrandCategory, on_delete=models.CASCADE, related_name="brands")
    image = models.ImageField(upload_to="brands/")

    def __str__(self):
        return self.name


class GiftCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    country = models.ForeignKey(GiftCardCountry, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return self.brand.image.url

    def get_title(self):
        title = self.title + " - " + self.category.title
        if self.country:
            title += " (" + self.country.title + ")"
        return title


class GiftCardCode(models.Model):
    gift_card = models.ForeignKey(GiftCard, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code
