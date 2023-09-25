from django.contrib import admin
from django.urls import path
from TODOapp import views

    
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home,name='home'), # type: ignore
    path('login/',views.login,name='login'), # type: ignore
    path('signup/',views.signup), # type: ignore
    path('addtodo/',views.add_todo), # type: ignore
    path('logout/',views.signout),
    path('delete-todo/<int:id>',views.delete_todo),
    path('change-status/<int:id>/<str:status>',views.change_status)
    
]