from django.shortcuts import render
from rest_framework import status, generics, mixins
from django.db import transaction
from .models import Tag_vls
from rest_framework.permissions import IsAuthenticated
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class ListCommonAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Tag_vls.objects.all().order_by('id')
    serializer_class = TagSerializer

    def post(self, request):
        common_serializer = TagSerializer(data=request.data)
        query = request.query_params.get("q")
        if query:
            self.queryset = self.queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = TagSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CreateCommonAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Tag_vls.objects.all().order_by('id')
    serializer_class = TagSerializer

    # permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        tag_serializer = TagSerializer(self, data=request.data)
        if tag_serializer.is_valid():
            post_data = request.data
            try:
                common = Tag_vls()  # common is the object of  Tag_vls table
                # Inserting the data into  Tag_vls table through object
                common.parent_id = post_data.get('parent_id')
                common.tag = post_data.get('tag')
                common.alternate_name = post_data.get('alternate_name')
                common.tag_type = post_data.get('tag_type')
                common.tag_status = post_data.get('tag_status')
                common.description = post_data.get('description')
                common.image_path = post_data.get('image_path')
                common.user_generated_indicator = post_data.get('user_generated_indicator')
                common.added_to_topics_indicator = post_data.get('added_to_topics_indicator')
                common.popular_indicator = post_data.get('popular_indicator')
                common.creating_user = post_data.get('creating_user')
                common.save()
                # return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
                return Response({"status": status.HTTP_201_CREATED, "message": "Tag created successfully"})
            except Exception as err:
                return Response({'status': status.HTTP_417_EXPECTATION_FAILED, 'message': str(err)})
        return Response(tag_serializer.errors, status=status.HTTP_201_CREATED)


# this class show the details views .in this class define 3 function (GET,PUT,DELETE)
class DetailsCommonAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = TagSerializer

    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        pass

    def get_object(self, tag_id):
        obj = Tag_vls.objects.filter(id=tag_id).first()
        if obj is None:
            raise APIException({"code": status.HTTP_200_OK, "message": " Record Does Not Exist"})
        else:
            return obj

    # used  pk to show the particular record.
    def post(self, request, *args, **kwargs):
        pk = request.data.get('tag_id')
        obj = self.get_object(pk)
        serializer = TagSerializer(obj)
        return Response(serializer.data)


class UpdateCommonAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = TagSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Tag_vls.objects.all().order_by('id')

    def get_object(self, tag_id):
        obj = Tag_vls.objects.filter(id=tag_id).first()
        if obj is None:
            raise APIException({"code": status.HTTP_200_OK, "message": " Record  Does Not Exist"})
        else:
            return obj

    # update the particular record  through pk
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        tag_id = request.data.get('tag_id')
        obj = self.get_object(tag_id)
        serializer = TagSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=200)
            return Response({"code": 200, "message": " Updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommonAPIView(mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = TagSerializer

    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        pass

    def get_object(self, tag_id):
        obj = Tag_vls.objects.filter(id=tag_id).first()
        if obj is None:
            raise APIException({"code": status.HTTP_200_OK, "message": " Record  Does Not Exist"})
        else:
            return obj

    # delete the particular Record of common_tag through pk
    @transaction.atomic
    def post(self, request):
        tag_id = request.data.get('tag_id')
        obj = self.get_object(tag_id)
        obj.delete()
        return Response({"status": status.HTTP_204_NO_CONTENT, "message": " Record deleted successfully"})
