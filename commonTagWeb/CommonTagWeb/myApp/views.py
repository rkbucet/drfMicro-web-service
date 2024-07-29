import json
from django.http import JsonResponse
from rest_framework import generics
import requests
from .serializers import (CreateCommonWebSerializer
, ListCommonWebSerializer, UpdateCommonWebSerializer, DetailCommonWebSerializer, DeleteCommonWebSerializer )

MODULE_URL = 'http://127.0.0.1:8000/'
# MODULE_URL = 'micro-collab-content/content/'
# FINAL_URL = BASE_URL + MODULE_URL

def headerValue(request):
    # print(request.headers)
    try:
        # authtoken = request.headers['authtoken']
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json",}
                   # "Authorization": authtoken}
        return headers
    except Exception:
        return {'code': 404, 'message': 'Your Token is not working'}
def post_webservice(request, url, data):
    try:
            headers = headerValue(request)
            #     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
            resp = requests.post(url, data=data, headers=headers)
            print(resp)
            return resp
    except Exception:
        return {'code': 404, 'message': 'Something went wrong. Please check your microservice.'}

# def put_webservice(request, url, data):
#     try:
#         headers = headerValue(request)
#         resp = requests.post(url, data=data, headers=headers)
#         return resp
#     except Exception:
#         return {'code': 404, 'message': 'Something went wrong. Please check your microservice.'}
# def delete_webservice(request, url, data):
#     try:
#         headers = headerValue(request)
#         resp = requests.post(url, json=data, headers=headers)
#         return resp
#     except Exception:
#         return {'code': 404, 'message': 'Something went wrong. Please check your microservice.'}

class ListCommon(generics.GenericAPIView):
    """ListTenant class define """
    serializer_class = ListCommonWebSerializer

    def post(self, request, *args, **kwargs):
        """This method: return json response"""
        post_data = request.data
        page = request.query_params.get('page')
        page_size = request.query_params.get('page_size')
        print(MODULE_URL + f'list/?page={page}&&page_size={page_size}')
        response = post_webservice(request, MODULE_URL + f'list/?page={page}&&page_size={page_size}', data=post_data)
        # print(response)
        data = response.json()
        return JsonResponse(data)


class CreateCommon(generics.GenericAPIView):
    """CreateTenant class define """
    serializer_class = CreateCommonWebSerializer

    def post(self, request, *args, **kwargs):
        """This method: return json response"""
        post_data = request.data
        print(MODULE_URL + 'create/')
        response = post_webservice(request, MODULE_URL + 'create/', data=post_data)
        # print(response.text)
        data = response.json()
        return JsonResponse(data)



class UpdateCommon(generics.GenericAPIView):
    """UpdateTenant class define """
    serializer_class = UpdateCommonWebSerializer

    def post(self, request, *args, **kwargs):
        """This method: return json response"""
        post_data = request.data
        response = post_webservice(request, MODULE_URL + 'update/', data=post_data)
        data = response.json()
        return JsonResponse(data)


class DetailsCommon(generics.GenericAPIView):
    """DetailsTenant class define """
    serializer_class = DetailCommonWebSerializer

    def post(self, request, *args, **kwargs):
        """This method: return json response"""
        post_data = request.data
        tag_id = request.data.get('tag_id')
        response = post_webservice(request, MODULE_URL + 'details/', data=post_data)
        data = response.json()
        return JsonResponse(data)


class DeleteCommon(generics.GenericAPIView):
    """DeleteTenant class define """
    serializer_class = DeleteCommonWebSerializer

    def post(self, request, *args, **kwargs):
        """This method: return json response"""
        post_data = request.data
        response = post_webservice(request, MODULE_URL + 'delete/', data=post_data)
        data = response.json()
        return JsonResponse(data)
