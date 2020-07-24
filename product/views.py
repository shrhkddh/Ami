import json

from django.views import View
from django.http import (
        JsonResponse, 
        HttpResponse
)

from .models import (
        ProductColor,
        ProductImage,
        Color,
        Product
)

class ListView(View):
    def get(self, request):
        product_list = ProductColor.objects.prefetch_related("color").prefetch_related("product")
        try:
            product_info= [{
                "product_id"      : item.product.id,
                "product_color_id": item.color.id,
                "product_name"    : item.product.name,
                "product_price"   : int(item.product.price),
                "product_color"   : item.color.name,
                "button_colors"   : [colors.color.name for colors in ProductColor.objects.filter(
                                     product_id = item.product.id)],
                "button_image"    : item.color.button_color,
                "button_images"   : [button.color.button_color for button in ProductColor.objects.filter(
                                     product_id = item.product.id)],
                "product_images" : [image.image_url for image in item.productimage_set.all()]
                } for item in product_list]

            return JsonResponse({"product_data" : product_info}, status = 200)

        except KeyError:
            return HttpResponse("KeyError", status = 400)

        except:
            return HttpResponse("not match product", status = 400)

class DetailView(View):
    def get(self, request, req_product_id, req_color_id):
        try:
            if not ProductColor.objects.filter(color_id = req_color_id, product = req_product_id).exists():
                return HttpResponse(status = 404)

            product_detail   = ProductColor.objects.prefetch_related(
                               "color").filter(color_id = req_color_id).prefetch_related(
                               "product").filter(product_id = req_product_id)

            for item in product_detail:
                product_info = {
                        "sub_sub_category" : item.product.type_name.name,
                        "product_name"     : item.product.name,
                        "product_price"    : int(item.product.price),
                        "product_guide"    : [guide for guide in item.product.guide.split(',')],
                        "product_color"    : item.color.name,
                        "product_color_id" : item.color.id,
                        "product_size"     : [size for size in item.product.product_size.size.split(',')],
                        "button_colors"    : [colors.color.name for colors in ProductColor.objects.filter(
                                              product_id = item.product.id)],
                        "button_images"    : [button.color.button_color for button in ProductColor.objects.filter(
                                              product_id = item.product.id)],
                        "product_images"   : [image.image_url for image in ProductImage.objects.filter(
                                              product_color = ProductColor.objects.get(
                                              color = Color.objects.get(id = item.color.id),
                                              product = Product.objects.get(id = item.product.id)))]
                        }

            return JsonResponse({"product_data" : product_info}, status = 200)

        except KeyError:
            return HttpResponse("KeyError", status = 400)

