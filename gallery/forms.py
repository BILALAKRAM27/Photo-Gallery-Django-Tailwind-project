from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Photo, Comment

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class PhotoForm(forms.ModelForm):
    image_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        required=True
    )

    class Meta:
        model = Photo
        fields = ['title', 'description', 'public']

    def save(self, commit=True):
        instance = super(PhotoForm, self).save(commit=False)
        image_files = self.cleaned_data.get('image_file')

        if image_files:
            # Handle multiple images (upload each image)
            for image in image_files:
                # Create a new Photo object for each uploaded image
                new_photo = Photo(
                    user=self.instance.user,
                    title=self.cleaned_data['title'] or image.name,
                    description=self.cleaned_data['description'] or "No description",
                    public=self.cleaned_data.get('public', False)
                )
                # Save the image as binary data
                new_photo.set_image(image.read())
                new_photo.save()

        return instance


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add your comment...'}))

    class Meta:
        model = Comment
        fields = ['body']  # Only the comment body field is needed.

    def save(self, photo, user, commit=True):
        # Associate the comment with the specific photo and the current user
        comment = super().save(commit=False)
        comment.image_comment = photo  # Correct association
        comment.user = user  # Correct association
        if commit:
            comment.save()
        return comment
