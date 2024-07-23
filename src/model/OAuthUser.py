from tortoise import Model, fields
from model.Basic import BasicTimeStampMixin

class OAuthUser(BasicTimeStampMixin):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=510)
    email = fields.CharField(max_length=254, unique=True)
    is_active = fields.BooleanField(default=True)
    class Meta:
        table = "oauth_user"
        table_description = "OAuth User"
        ordering = ["-created_at"]
    


