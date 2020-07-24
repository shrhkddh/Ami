import json

from django.views import View
from django.http import (
    JsonResponse,
    HttpResponse
)

from .models import (
    Menu,
    Category
)

class CategoryView(View):
    def get(self, request):
        try:
            menus = Menu.objects.prefetch_related('menucategory_set__categorytype_set__type_name')
            for menu in menus:
                category_list = [{
                    'category_id' : types.type_name.id,
                    'category_name' : types.type_name.name
                } for category in menu.menucategory_set.all() 
                for types in category.categorytype_set.all()]
                return JsonResponse({'category_list' : category_list}, status=200)

        except Category.DoesNotExist:
            return HttpResponse(status=401)