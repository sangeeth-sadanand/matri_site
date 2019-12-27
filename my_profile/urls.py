from django.urls import path, include
from . import views
#from matri_site.config import *
#data = load_config()
#print(data)

urlpatterns = [
    path('',views.show, name = 'profile_show'),
    path('edit/',views.edit, name = 'profile_edit'),
    path('upload-photo/',views.upload_photo, name = 'upload_profile'),
    path('search/', views.search, name = 'search_profile'),
    path('intersted-profiles/', views.interested_page, name = 'interested_profiles'),
    path('i-req/',views.interested_request,name='interested_request'),
    path('interested-me/',views.intereseted_in_me, name='interested_me' ),
    path('view-profile/<id>',views.view_profile_detail, name='view_profile'),
    path('proposal-request/',views.proposal_request,name='proposal_request'),
    path('proposal-for-me/',views.proposals_for_me, name='proposal_for_me'),
    path('proposed-profiles/',views.proposed_profiles, name='proposed_profiles'),
    path('we-are-getting-married/', views.we_are_getting_married, name='we_are_getting_married' ),
    path('edit-preference/',views.edit_preference, name='edit_preference'),
]
