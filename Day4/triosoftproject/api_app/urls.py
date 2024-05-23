

from django.urls import include, path
from api_app.views import TrioCompanyViewSet,MatrixSoftViewSet
from rest_framework import routers


#creating omne Router for
router=routers.DefaultRouter()
# Routers provide an easy way of automatically determining the URL conf.
#               (r'main url',        viewset  )
router.register(r'triocompany',TrioCompanyViewSet)
router.register(r'matrixsoft',MatrixSoftViewSet)

urlpatterns = [
    # is blank becauze it will take url directly 
    # from router register main url
   
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
   path('', include(router.urls))
]


