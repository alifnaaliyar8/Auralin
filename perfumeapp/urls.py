from django.urls import path
from perfumeapp import views

urlpatterns = [
    path('Index_Page/',views.index_page,name="Index_Page"),

    path('Add_Fragrance_Note_Categories/',views.add_category,name="Add_Fragrance_Note_Categories"),
    path('Save_Add_Fragrance_Data/',views.save_add_category, name="Save_Add_Fragrance_Data"),
    path('Display_Add_Category_Data/',views.display_add_category,name="Display_Add_Category_Data"),
    path('Edit_Add_Category_Data/<int:fcategory_id>/',views.edit_add_category,name="Edit_Add_Category_Data"),
    path('Update_Add_Category_Data/<int:F_id>/',views.update_add_category,name="Update_Add_Category_Data"),
    path('Delete_Add_Category_Data/<int:fragrance_id>/',views.delete_add_category,name="Delete_Add_Category_Data"),

    path('Add_Perfumes/', views.add_perfumes, name="Add_Perfumes"),
    path('Save_Add_Perfumes/',views.save_add_perfumes, name="Save_Add_Perfumes"),
    path('Display_Add_Perfumes/', views.display_add_perfumes, name="Display_Add_Perfumes"),
    path('Edit_Add_Perfumes/<int:perfume_id>/', views.edit_add_perfumes, name="Edit_Add_Perfumes"),
    path('Update_Add_Perfumes/<int:P_id>/', views.update_add_perfumes, name="Update_Add_Perfumes"),
    path('Delete_Add_Perfumes/<int:pfume_id>/', views.delete_add_perfumes, name="Delete_Add_Perfumes"),

    path('Admin_Login_Page/',views.admin_login,name="Admin_Login_Page"),
    path('Admin_Login_Check/',views.admin_login_check, name="Admin_Login_Check"),
    path('Admin_Logout/',views.admin_logout,name="Admin_Logout")

]
 