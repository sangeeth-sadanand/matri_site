from django.forms import ModelForm
from my_profile.models import ProfilePhoto

class ProfilePhotoForms(ModelForm):

    class Meta:
        model = ProfilePhoto
        fields = "__all__"
