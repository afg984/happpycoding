from django_fsu import url
from . import views


urlpatterns = [
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
]
