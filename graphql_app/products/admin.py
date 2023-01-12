from django.contrib import admin
from .models import Client, Book, Category, Order, BookHasOrder, Delivery, Review

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(BookHasOrder)
admin.site.register(Delivery)
admin.site.register(Review)

