"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views
from basic_app.views import get_data,thankyou
from basic_app.views import HomeView, get_data2, ChartData

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^homeview/',homeview.as_view(),name='homeview'),
    #url(r'^special/',views.special,name='special'),
    url(r'^admin/', admin.site.urls),
    url(r'^base/', views.thankyou,name='thankyou'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^data/',views.data,name='dat'),


    



    # url(r'^data2/', HomeView.as_view(), name='home'),
    # url(r'^api/data/$', get_data2, name='api-data'),
    # url(r'^api/chart/data/$', ChartData.as_view()),
    #url(r'^chartdata/',chartdata.as_view()),
    #url(r'^basic_app/',include('basic_app.urls')),
    #url(r'^logout/$', views.user_logout, name='logout'),
    ]

