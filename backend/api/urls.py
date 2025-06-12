from django.urls import path
from.import views

urlpatterns = [
    #path('',views.ProductListView.as_view(),name="List_view"),
    path('',views.ListCreateApiView.as_view(),name="create_list"),
    path('udr/<int:pk>/',views.RetriveDestroyUpdateApiview.as_view()),
    #path("product/<int:pk>/",views.ProductDetailView.as_view(),name="home"),
    
    #path("product/create/",views.CreateApiView.as_view(),name="home"),

]
