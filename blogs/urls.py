from django.urls import path,include
from rest_framework.routers import DefaultRouter

from blogs import views

router = DefaultRouter()
router1= DefaultRouter()
router.register(r'product', views.BlogAPIViewpr)
router1.register(r'category', views.BlogAPIViewca)

urlpatterns = [
    #path('v2/<int:pk>/', views.BlogRetrieveAPIView.as_view()),
    #path('v2/', views.BlogAPIView.as_view()),
    path('', include(router.urls)),
    path('', include(router1.urls))
]
