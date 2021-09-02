from django.contrib import admin
from .models import Country, Item, ItemVariant, Review, Category

admin.site.register(ItemVariant)
admin.site.register(Country)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Item)

# Register your models here.
