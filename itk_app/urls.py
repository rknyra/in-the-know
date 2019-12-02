from django.conf.urls import url
from . import  views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('my-profile/',views.myProfile,name='my_profile'),
    path('update-profile/',views.updateProfile,name='update_profile'),
    path('share-notice/',views.shareNotice,name='share_notice'),
    path('notices/',views.viewNotices,name='view_notices'),
    path('add-business/',views.addBusiness,name='add_business'),
    path('businesses/',views.business,name='view_businesses'),
    path('search-businesses/',views.searchBusiness,name='search_businesses'),
    path('health-centers/<int:neighborhood_id>',views.healthCenters,name='health_centers'),
    path('police-stations/<int:neighborhood_id>',views.policeStations,name='police_stations'),
    path('neighborhoods/',views.neighborhood,name='view_neighborhoods'),
    path('add-neighborhood/',views.addNeighborhood,name='add_neighborhood'),


]
