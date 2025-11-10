from django.urls import path
from webapp import views

urlpatterns =[
    path('Home_Page/',views.home_page,name="Home_Page"),
    path('About_Page/', views.about_page, name="About_Page"),
    path('Contact_Page/', views.contact_page, name="Contact_Page"),
    path('All_Perfumes/', views.all_perfumes_page, name="All_Perfumes"),
    path('Filtered_Perfumes/<perfume_category>/',views.filtered_perfume_page,name="Filtered_Perfumes"),
    path('Single_Perfume/<int:pfume_id>',views.single_perfume, name="Single_Perfume"),
    path('Sign_Up/', views.sign_up, name="Sign_Up"),
    path('Save_User/',views.save_user, name="Save_User"),
    path('Login_Page/', views.sign_in, name="Login_Page"),
    path('Login/', views.user_sign_in, name="Login"),
    path('Logout/', views.user_logout, name="Logout"),

]