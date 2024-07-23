from model.Basic import BasicTimeStampMixin
from tortoise import fields

class OAuthorizationCodes(BasicTimeStampMixin):
    id = fields.IntField(pk=True)
    code = fields.CharField(max_length=256, unique=True)
    expire_at = fields.DatetimeField()
    mode = fields.CharField(max_length=16)
    user_id = fields.IntField()
    