from django.urls import path
import accounts.views as views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('submissions', views.view_all_submissions, name="View"),
    path('submissions/new', views.create_submission, name="Create"),
    path('submissions/<int:sub_id>/edit', views.edit_submission, name="Edit"),
    path('submissions/<int:sub_id>/delete', views.delete_submission, name="Delete"),
    path('submissions/<int:sub_id>', views.view_submission, name="ViewSub"),
]