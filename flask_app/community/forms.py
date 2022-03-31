from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length

from flask_app.models import Post


class PostForm(FlaskForm):
    title = StringField(
        label="Title", validators=[DataRequired(message="Title is required")]
    )
    content = TextAreaField(
        label="Content",
        description="Write something, don't be shy :)",
        validators=[
            DataRequired(message="Content is required"),
            Length(min=10, max=2000),
        ],
    )

    def validate_title(self, title):
        posts = Post.query.filter_by(title=title.data).first()
        if posts is not None:
            raise ValidationError(
                "A post with this title already exists, please be more creative"
            )
