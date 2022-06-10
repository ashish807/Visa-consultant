"""visaAlliance2phase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sites.models import Site
from django.urls import include, path, re_path
from visaPage.sitemaps import (Static_Sitemap, Static_Sitemap2,
                               Static_Sitemap3, Static_Sitemap4)

from . import views

sitemaps = {
    'sitemap4': Static_Sitemap4(),
    'sitemap': Static_Sitemap(),
    'sitemap2': Static_Sitemap2(),
    'sitemap3': Static_Sitemap3(),
}



urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('basanta/visa_alliance/australia/@visa123/', admin.site.urls),
    path('', views.home, name='home'),
    path('visaPage/', include('visaPage.urls')),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^csu-nursing-campaign/$(?i)', views.LandingNursing.as_view(), name='nursing_campaign'),
    re_path(r'^acap-bachelor-socialwork-campaign/$(?i)', views.LandingSocialWork.as_view(), name='socialwork_campaign'),
    re_path(r'^acap-masters-socialwork-campaign/$(?i)', views.LandingMastersSocialWork.as_view(), name='master_socialwork_campaign'),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

