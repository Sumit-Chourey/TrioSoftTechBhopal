




#Older code


from .models import ImageModel
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

@csrf_exempt
def ImageFun2(request ):
    if request.method == 'POST':
         image = request.FILES.get('image')
         description = request.POST.get('description')
           
           
         data = ImageModel.objects.create(image = image, description = description)
         data.save()
         return JsonResponse({"done":"done"})


@csrf_exempt
def ImageFun3(request):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))  # Get the page number from the request, default to 1 if not provided
        page_size = 10                                 # Number of items per page

        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size

        images = ImageModel.objects.all()[start_index:end_index].values()  # Query for images in the current page

        # Serialize the data
        serialized_images = list(images)

        return JsonResponse({"images": serialized_images})


