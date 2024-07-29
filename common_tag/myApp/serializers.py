

from rest_framework import serializers
from .models import Tag_vls


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        # """ call the  Tenant_msp models or table """
        model = Tag_vls
        # call all the  fields of Tenant_msp  table with ForeignKey fields
        fields = ['parent_id',
                  'tag',
                  'alternate_name',
                  'tag_type',
                  'tag_status',
                  'description',
                  'image_path',
                  'user_generated_indicator',
                  'added_to_topics_indicator',
                  'popular_indicator'
        ]