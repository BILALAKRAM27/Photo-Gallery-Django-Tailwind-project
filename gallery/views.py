from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, PhotoForm,CommentForm
from .models import Photo,Comment,Like
from django.http import JsonResponse

def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'welcome.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def private_gallery(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'private_gallery.html', {'photos': photos})

@login_required
def public_gallery(request):
    photos = Photo.objects.filter(public=True)

    if request.method == 'POST':
        photo_id = request.POST.get('photo_id')
        body = request.POST.get('body')

        if photo_id and body:
            photo = get_object_or_404(Photo, id=photo_id)
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(photo=photo, user=request.user)

                # Optionally, return the new comment as JSON or re-render with updated comments
                return JsonResponse({
                    'comment_user': comment.user.username,
                    'comment_body': comment.body,
                    'comment_created': comment.created.strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                return JsonResponse({'error': 'Invalid form submission'}, status=400)

    return render(request, 'public_gallery.html', {'photos': photos})


@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # Process each uploaded file
            files = request.FILES.getlist('image_file')
            for file in files:
                photo = Photo(
                    user=request.user,
                    title=form.cleaned_data['title'] or file.name,
                    description=form.cleaned_data['description'] or "",
                    public=form.cleaned_data['public'] or False
                )
                photo.set_image(file.read())  
                photo.save()
            return redirect('private_gallery')  
    else:
        form = PhotoForm()

    return render(request, 'upload_photo.html', {'form': form})

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if photo.user == request.user:
        photo.delete()
    return redirect('private_gallery')

def logout_view(request):
    logout(request)
    return redirect('base')

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Photo, Comment

@login_required
def comment(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    
    if request.method == 'POST':
        body = request.POST.get('body')  # Get the comment body from the form data
        if body:
            # Create and save the comment in the database
            comment = Comment(
                image_comment=photo,
                user=request.user,  # The user who is posting the comment
                body=body,
            )
            comment.save()

            # Return the newly created comment as JSON to update the frontend
            return JsonResponse({
                'comment_user': comment.user.username,
                'comment_body': comment.body,
                'comment_created': comment.created.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return JsonResponse({'error': 'Comment cannot be empty'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    
    # Check if the user already liked the photo
    existing_like = Like.objects.filter(photo=photo, user=request.user).first()
    
    if existing_like:
        # If the user already liked the photo, remove the like
        existing_like.delete()
        liked = False
    else:
        # If the user hasn't liked the photo, create a new like
        Like.objects.create(photo=photo, user=request.user)
        liked = True
    
    # Return the updated like status and the total count of likes
    return JsonResponse({
        'liked': liked,
        'like_count': photo.likes.count(),
    })
