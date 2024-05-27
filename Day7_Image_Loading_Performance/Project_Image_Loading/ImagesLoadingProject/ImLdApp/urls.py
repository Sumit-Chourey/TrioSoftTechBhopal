
from django.urls import path


from ImLdApp.views import ImageFun2, ImageFun3
urlpatterns = [
    path('image2/',ImageFun2),
    path('image3/', ImageFun3, name='image_fun3')
]
