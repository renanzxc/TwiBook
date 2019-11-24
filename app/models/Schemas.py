from marshmallow import fields, validates, ValidationError
from app.models.UserModel import User
from app.models.PostModel import Post
from app.models.LikePostModel import LikePost
from app.models.CommentModel import Comment

from app import ma

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        include_fk = True

class LikePostSchema(ma.ModelSchema):
    class Meta:
          model = LikePost
          include_fk = True

class CommentSchema(ma.ModelSchema):
    class Meta:
        model = Comment
        include_fk = True

    user = fields.Nested(UserSchema, only=["id","username","name"])

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
        include_fk = True

    user = fields.Nested(UserSchema, only=["id","username","name"])
    comment = fields.Nested(CommentSchema, many=True)
