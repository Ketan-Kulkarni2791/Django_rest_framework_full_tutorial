from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('showroom', views.ShowroomViewSet, basename='showroom')

urlpatterns = [
    path('list', views.car_list_view, name='car_list'),
    path('<int:pk>', views.car_detail_view, name='car_detail'),
    # path('showroom', views.ShowroomwView.as_view(), name='showroomw_view'),
    # path('showroom/<int:pk>', views.ShowroomDetailView.as_view(), name='showroomw_detail_view'),
    path('showroom/', include(router.urls)),
    path('review', views.ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
] 