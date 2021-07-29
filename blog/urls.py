from django.urls import path
from .views import view_blog,add_blog,blog_detailed_view,edit_blog,my_blog,comment_section,reply_section

urlpatterns = [
    path('view_blog', view_blog, name='view_blog'),
    path('comment_section/<slug:slug>', comment_section, name='comment_section'),
    path('reply_section/<int:pk>/<slug:slug>', reply_section, name='reply_section'),
    path('my_blog', my_blog, name='my_blog'),
    path('add_blog', add_blog, name='add_blog'),
    path('edit_blog/<slug:slug>', edit_blog, name='edit_blog'),
    path('blog_detailed_view/<slug:slug>', blog_detailed_view, name='blog_detailed_view'),
]