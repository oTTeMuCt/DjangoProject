from django.urls import path
from .views import review_list, delete_review, confirm_delete, update_review

urlpatterns = [
    path('reviews/', review_list, name='review_list'),
    path('reviews/delete/<int:review_id>/confirm/', confirm_delete, name='confirm_delete'),
    path('reviews/delete/<int:review_id>/', delete_review, name='delete_review'),
    path('reviews/update/<int:review_id>/', update_review, name='update_review'),
]
