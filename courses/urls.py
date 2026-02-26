# from django.urls import path
# from . import views

# urlpatterns = [
#     path('courses/', views.course_list),
#     path('courses/<int:pk>/', views.course_detail),
#     path('courses/create/', views.create_course),
#     path('courses/<int:pk>/update/', views.update_course),
#     path('courses/<int:pk>/delete/', views.delete_course),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:pk>/update/', views.update_course, name='update_course'),
    path('courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
]