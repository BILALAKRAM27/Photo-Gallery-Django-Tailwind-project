from django.contrib import admin
from django.utils.html import format_html
from .models import Photo, Comment, Like

# Photo Admin Configuration
class PhotoAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'user', 'description', 'uploaded_at', 'public', 'image_preview')
    # Make fields editable in the list view
    list_editable = ('description', 'public')
    # Search functionality
    search_fields = ('title', 'description', 'user__username')
    # Filters
    list_filter = ('public', 'uploaded_at')
    # Ordering
    ordering = ('-uploaded_at',)

    # Custom method to display the image as a preview in the admin panel
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="data:image/jpeg;base64,{}" width="100" height="100" />', 
                obj.image_data  # The property that returns the base64 encoded image
            )
        return "No Image"

    image_preview.short_description = 'Image Preview'  # Custom label in the admin interface

# Comment Admin Configuration
class CommentAdmin(admin.ModelAdmin):
    list_display = ('image_comment', 'user', 'body', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('body', 'user__username')
    ordering = ('-created',)
    actions = ['make_active', 'make_inactive']

    # Custom admin actions
    def make_active(self, request, queryset):
        queryset.update(active=True)
    make_active.short_description = "Mark selected comments as active"

    def make_inactive(self, request, queryset):
        queryset.update(active=False)
    make_inactive.short_description = "Mark selected comments as inactive"

# Like Admin Configuration
class LikeAdmin(admin.ModelAdmin):
    list_display = ('photo', 'user', 'created')
    list_filter = ('created',)
    search_fields = ('user__username', 'photo__title')
    ordering = ('-created',)

# Registering the models with the admin site
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
