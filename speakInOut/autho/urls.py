from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views, views_dashboard

app_name = 'auth'

urlpatterns = [
	path('login/', views.login_view, name='index'),
	path('setup/', views.setup_view, name='setup'),
	path('register/', views.register_view, name='register'),
	path('logout/', views.logout_view, name='logout'),
	path('dashboard/', views_dashboard.dashboard_view, name='dashboard'),
	path('upload_manuscript/', views_dashboard.upload_manuscript, name='upload_manuscript'),
	path('analyze/', views_dashboard.show_analysis, name="analysis"),
	path('myvideos/', views_dashboard.myvideos, name="myvideos")
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)