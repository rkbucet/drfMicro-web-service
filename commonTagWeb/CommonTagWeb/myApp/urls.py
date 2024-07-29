from django.urls import path


from .views import (CreateCommon, ListCommon, UpdateCommon, DetailsCommon, DeleteCommon)

urlpatterns = [
    path('create/', CreateCommon.as_view(), name='create'),
    path('list/', ListCommon.as_view(), name='list'),
    path('update/', UpdateCommon.as_view(), name='update'),
    path('details/', DetailsCommon.as_view(), name='details'),
    path('delete/', DeleteCommon.as_view(), name='delete')
]