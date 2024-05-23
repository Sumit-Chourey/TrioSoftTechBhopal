





#Function(method) based view
from django.http import HttpResponse,JsonResponse
#(1) function based view 
def home_page(request):

    print("Home page requested..")
    return HttpResponse("This is home page...")

#after creating view , we have map into url so we goto the urls.py file

#(2) function based view
def first_page(request):
    print("first_ page reqyested.. ")
    return HttpResponse("This is first page... ")


#(2) function based view
def second_page(request):
    print("Second page requested...")
    return HttpResponse("This is second page....")

#(3) function based view
def third_page(request):
    print("Third page requested...")
    friends=['Hanuman','vikas','subham','trio']
    return JsonResponse(friends,safe=False)