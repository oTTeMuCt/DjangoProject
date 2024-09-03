from django.urls import path
from .views import review_list, delete_review, confirm_delete

urlpatterns = [
    path('reviews/', review_list, name='review_list'),
    path('reviews/delete/<int:review_id>/', confirm_delete, name='confirm_delete'),
    path('reviews/delete/<int:review_id>/confirm/', delete_review, name='delete_review'),
]
