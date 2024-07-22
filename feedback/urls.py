from django.urls import path, re_path

import feedback.views as feedback

urlpatterns = [

    path('', feedback.feedback),
    path('edit_feedback/<int:feedback_id>/', feedback.editFeedback, name='editFeedback'),
    path('delete_feedback/<int:feedback_id>/', feedback.deleteFeedback, name='deleteFeedback'),

]