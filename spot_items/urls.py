from django.urls import path
from . import views
# spot_items urls
    # cri url
     # confirmationsuccess url
        # report url
            # found item url
                # detail pf item
                    # update url
app_name = 'spot_items'

urlpatterns = [
    path('', views.home, name='home'),
    path('cri/', views.cri, name='cri'),
    path('confirmationsuccess/', views.confirmationsuccessview, name='confirmationsuccessview'),
    path('report/', views.reportlostitems, name='reportlostitem'),
    path('found/<int:ItemID>/', views.markfounditem, name='found'),
    path('detail/<int:pk>/', views.itemdetails.as_view(), name='detail'),
    path('update/<int:ItemID>/', views.updatelostitem, name='update_lostitem'),
]
