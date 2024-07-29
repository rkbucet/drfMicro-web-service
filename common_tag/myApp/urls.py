from django.urls import path


from .views import (CreateCommonAPIView, ListCommonAPIView, UpdateCommonAPIView, DetailsCommonAPIView, DeleteCommonAPIView)

urlpatterns = [
    path('create/', CreateCommonAPIView.as_view(), name='create'),
    path('list/', ListCommonAPIView.as_view(), name='list'),
    path('update/', UpdateCommonAPIView.as_view(), name='update'),
    path('details/', DetailsCommonAPIView.as_view(), name='details'),
    path('delete/', DeleteCommonAPIView.as_view(), name='delete'),
]