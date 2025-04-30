from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('uplaod/', views.upload, name="upload"),
    path('allot/', views.allot, name="allot"),
    path('edit_section/<int:section_id>', views.edit_section, name="edit_section"),
    path('view_student/<int:paper_id>', views.view_student, name="view_student"),
    path('view_prof/<int:paper_id>', views.view_prof, name="view_prof"),
    path('upload/checked/<int:paper_id>', views.upload_checked, name = "upload_checked"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)