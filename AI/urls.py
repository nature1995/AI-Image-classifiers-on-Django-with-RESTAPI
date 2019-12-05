"""AI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from apps.qrcreate.views import generate_qrcode
from django.views.static import serve
from apps.face_comparison.views import *
from apps.bank_card.views import *
from apps.detect_object.views import *
from apps.gesture.views import *
from apps.identification.views import *
from apps.tenc_ai.views import *
import AI.views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', home, name='main'),
    path(r'accounts/', include('allauth.urls')),
    path(r'accounts/', include('myauth.urls')),
    # path(r'account/', include('account.urls')),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'media/favicon.ico')),
    url(r'^qr/(.+)$', generate_qrcode, name='qr'),
    url(r'^qr/', home, name='qrcode'),
    path(r'face-comparison/', face_compare, name='face_comparison'),
    path(r'face-comparison/face_compare_request/', face_compare_request, name='face_compare_request'),
    path(r'bank-card/', bank_card, name='bank_card'),
    path(r'bank-card/bank_card_request/', bank_card_request, name='bank_card_request'),
    path(r'gesture/', gesture, name='gesture'),
    path(r'gesture/gesture_request/', gesture_request, name='gesture_request'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path(r'', include('apps.identification.urls'), ),
    path('test', test),
    path('ajax', ajax),
    url(r'^tenc-ai/', tenc_ai, name='tenc_ai'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,) + static(settings.STATIC_URL,
                                                                            document_root=settings.STATIC_ROOT)
