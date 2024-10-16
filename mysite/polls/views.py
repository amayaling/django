from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from .tasks import send_query


def query(request):
    queries = request.GET.dict()
    print(queries) # goes to terminal; personal touch to see what code was doing 
    send_query.delay(queries)
    # this returns the key value pairs and not just the key 
    # return HttpResponse(queries) = returns the param and not the value 
    return JsonResponse(queries)

'''
IGNORE EVERYTHING BEOLOW 
'''
#     send_req.delay
#     "Hello from Celery!",
#     "This is an email sent using Celery and Django.",
#     "your@email.com",

#     )

#     return HttpResponse("Hello, world. You're at the polls index.")

# send_req.delay(
#     "Hello from Celery!",
#     "This is an email sent using Celery and Django.",
#     "your@email.com",

# )

# def register_user(request, form):
#     if form.is_valid():
#         user = form.save()
#         send_req.delay(
#             "Welcome to our site!",
#             "Thank you for registering.",
#             "your@email.com",
#         )


# # Create your views here.
