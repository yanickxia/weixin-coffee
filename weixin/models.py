from django.db import models


# Create your models here.

class AccessToken(models.Model):
    access_token = models.CharField(max_length=400)
    expires_time = models.DateTimeField()


class TextMessage(models.Model):
    to_user_name = models.CharField(max_length=100)
    from_user_name = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    msg_type = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    msg_id = models.CharField(max_length=20)


class UploadMedia(models.Model):
    type = models.CharField(max_length=10)
    media_id = models.CharField(max_length=100)
    created_at = models.DateTimeField()
