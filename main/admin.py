from django.contrib import admin
from .models import (Contact, Comment, Company, Product, Taklif, Buyurtma, Mainpart)


admin.site.register(Taklif)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Buyurtma)
admin.site.register(Mainpart)

