from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

    search_fields = (
        'name',
    )

    ordering = (
        'name',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'status',
        'created_date',
        'updated_date',
    )

    list_display_links = (
        'title',
    )

    list_filter = (
        'status',
        'category',
        'author',
        'created_date',
    )

    search_fields = (
        'title',
        'content',
        'author__username',
    )

    filter_horizontal = (
        'category',
    )

    ordering = (
        '-created_date',
    )

    readonly_fields = (
        'created_date',
        'updated_date',
    )

    date_hierarchy = 'created_date'

    fieldsets = (
        (
            'Post Information',
            {
                'fields': (
                    'title',
                    'content',
                    'image',
                )
            }
        ),

        (
            'Publishing',
            {
                'fields': (
                    'author',
                    'category',
                    'status',
                )
            }
        ),

        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'updated_date',
                )
            }
        ),
    )