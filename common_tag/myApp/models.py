from django.db import models

# Create your models here.
class Tag_vls(models.Model):
    parent_id = models.IntegerField(default=0)
    tag = models.CharField(max_length=255)
    alternate_name = models.CharField(max_length=255, null=True)
    tag_type = models.IntegerField(default=0)
    tag_status = models.IntegerField(default=1)
    description = models.TextField(max_length=1024, null=True)
    image_path = models.CharField(max_length=1024, null=True)
    user_generated_indicator = models.BooleanField(default=False)
    added_to_topics_indicator = models.BooleanField(default=False)
    popular_indicator = models.BooleanField(default=False)

    creating_user = models.IntegerField(null=True)

    def __str__(self):
        return self.tag

    class Meta:
        db_table = "common_tag"
        verbose_name_plural = "Tags"