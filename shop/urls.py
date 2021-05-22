from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('mahsol/', views.mahsol_list,name='mahsol'),
    path('mahsol/<slug:brand_slug>/', views.pro_list,name='prolist'),
    path('about/',views.About_us, name='aboutus'),
    path('contact/',views.contact_us, name='contactus'),
    path('search_result/',views.searchb_us, name='searchb'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]
