from django.urls import path
from . import views


urlpatterns = [
    path('list', views.car_list_view, name='car_list'),
    path('<int:pk>', views.car_detail_view, name='car_detail'),
    path('showroom', views.ShowroomwView.as_view(), name='showroomw_view'),
    path('showroom/<int:pk>', views.ShowroomDetailView.as_view(), name='showroomw_detail_view'),
    path('review', views.ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
] 