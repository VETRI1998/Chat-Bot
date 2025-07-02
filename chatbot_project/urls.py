from django.contrib import admin
from django.urls import path, include  # include is required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),  # ✅ Add this line to route to your chat app
]
