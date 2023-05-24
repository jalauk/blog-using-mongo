from marshmallow import fields,validate,Schema

class registerSchema(Schema):
    name = fields.Str(required=True,validate=validate.Length(min=2,max=64))
    email = fields.Email(required=True,validate=validate.Length(min=6,max=128))
    password = fields.Str(required=True,validate=validate.Length(min=8,max=32))
    username = fields.Str(required=True,validate=validate.Length(min=3,max=64))
    is_author = fields.Bool(required=True)

    class Meta:
        fields = ("name","email","password","username","is_author")

register_schema = registerSchema()
    