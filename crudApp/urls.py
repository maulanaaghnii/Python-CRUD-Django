from django.urls import path
from .import views
urlpatterns = [
    path('', views.addStudent, name="add_student"),
    path('update/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.deleteStudent, name="delete_student"),
]

# from django.contrib import admin
# from django.urls import path
# from django.urls import include  # new
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('crudApp.urls')),  # new
# ]