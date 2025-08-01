from django.urls import path
from . import views

# todo esto es la estructura de nuestras diferentes pages todo quedo dentro de esta base
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('problem/<str:pk>/', views.problem, name="problem"),
    path('solution/<str:pk>/', views.solution, name="solution"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-solution/<str:pk>/', views.createSolution, name="create-solution"),
    path('update_solution/<str:pk>/', views.updateSolution, name="update-solution"),
    path('delete_solution/<str:pk>/', views.deleteSolution, name="delete-solution"),
    path('delete_message/<str:pk>/', views.deleteMessage, name="delete-message"),
]