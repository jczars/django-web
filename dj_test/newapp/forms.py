from django.forms import ModelForm
from newapp.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto']