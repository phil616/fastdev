from tortoise import Model, fields

class BasicTimeStampMixin(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_by = fields.CharField(max_length=100, null=True, default=None)
    updated_by = fields.CharField(max_length=100, null=True, default=None)

    class Meta:
        abstract = True