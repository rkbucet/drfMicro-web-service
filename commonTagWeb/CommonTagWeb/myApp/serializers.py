from rest_framework import serializers


class CreateCommonWebSerializer(serializers.Serializer):
    """CreateCommonWebSerializer class define """
    parent_id = serializers.IntegerField()
    tag_type = serializers.IntegerField()
    tag_status = serializers.IntegerField()
    tag = serializers.CharField()
    alternate_name = serializers.CharField()
    description = serializers.CharField()
    image_path = serializers.CharField()
    user_generated_indicator = serializers.BooleanField()
    added_to_topics_indicator = serializers.BooleanField()
    popular_indicator = serializers.BooleanField()
    creating_user = serializers.IntegerField


class ListCommonWebSerializer(serializers.Serializer):
    """ListCommonWebSerializer class define """
    keyword = serializers.CharField()
    page = serializers.IntegerField()
    page_size = serializers.IntegerField()


class UpdateCommonWebSerializer(serializers.Serializer):
    """UpdateCommonWebSerializer class define """
    tenant_id = serializers.IntegerField()
    status = serializers.IntegerField()
    tenant_type = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    operating_market = serializers.CharField()
    url = serializers.CharField()
    logo_path = serializers.CharField()
    thumbnail_path = serializers.CharField()


class DetailCommonWebSerializer(serializers.Serializer):
    """DetailCommonWebSerializer class define """
    tag_id = serializers.IntegerField()
    tenant_id = serializers.IntegerField()
    status = serializers.IntegerField()
    tenant_type = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    operating_market = serializers.CharField()
    url = serializers.CharField()
    logo_path = serializers.CharField()
    thumbnail_path = serializers.CharField()


class DeleteCommonWebSerializer(serializers.Serializer):
    """DeleteCommonWebSerializer class define """
    tag_id = serializers.IntegerField()