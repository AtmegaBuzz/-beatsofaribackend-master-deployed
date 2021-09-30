from django.urls import path
from home import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[ 
    path("api/getbeats",views.BeatsApiView.as_view(),name="getbeats"),
    path("api/getbeats/beats",views.BeatsOnlyApiView.as_view(),name="beatsonly"),
    path("api/getbeats/playback",views.PlaybackOnlyApiView.as_view(),name="playbackonly"),
    path("contact/",views.contact,name="contact"),
] 


handler404 = "home.views.error_page_404"