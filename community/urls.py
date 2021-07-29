from community.views import community_page
from django.urls import path


urlpatterns = [
    path('community_page',community_page,name='community_page' ),
]