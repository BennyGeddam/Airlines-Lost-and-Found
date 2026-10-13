from django.urls import path
from . import views
from spot_items.views import markfounditem
# urls
    #feedbacks.
        #airport-staff-dashboard.
            #marking lost item mark-item-found/<int:ItemID>.
                # feedback-deletion/<int:feedbackId>/.

app_name = 'airport_staff'

urlpatterns = [
    path('submit-feedbacks/', views.submitfeedbacks, name='submit_feedbacks'),
    path('airport-staff-dashboard/', views.airportstaffdashboard, name='airport_staff_dashboard'),
    path('mark-item-found/<int:ItemID>/', markfounditem, name='mark_item_found'),
    path('feedback-deletion/<int:feedbackId>/', views.feedbackdeletion, name='feedback_deletion'),
]
