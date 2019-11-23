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
from django.urls import path
from .views import *


urlpatterns = [
    # path for each model separately
    path('predict/api/', predict_request, name='predict_request'),
    path('predict/', predict, name='predict'),
    #
    path('predict_MobileNet/api/', predict_MobileNet_request,
         name='predict_MobileNet_request'),
    path('predict_MobileNet/', predict_MobileNet, name='predict_MobileNet'),
    path('predict_InceptionResNetV2/api/', predict_InceptionResNetV2_request,
         name='predict_InceptionResNetV2_request'),
    path('predict_InceptionResNetV2/', predict_InceptionResNetV2, name='predict_InceptionResNetV2'),
    ##
    path('predict_MobileNetV2/api/', predict_MobileNetV2_request, name='predict_MobileNetV2_request'),
    path('predict_MobileNetV2/', predict_MobileNetV2, name='predict_MobileNetV2'),
    path('predict_Xception/api/', predict_Xception_request,
         name='predict_Xception_request'),
    path('predict_Xception/', predict_Xception, name='predict_Xception'),
    #
    path('predict_VGG16/api/', predict_VGG16_request,
         name='predict_VGG16_request'),
    path('predict_VGG16/', predict_VGG16, name='predict_VGG16'),
    ##
    path('predict_VGG19/api/', predict_VGG19_request,
         name='predict_VGG19_request'),
    path('predict_VGG19/', predict_VGG19, name='predict_VGG19'),

    path('predict_DenseNet121/api/', predict_DenseNet121_request,
         name='predict_DenseNet121_request'),
    path('predict_DenseNet121/', predict_DenseNet121, name='predict_DenseNet121'),
    path('predict_DenseNet169/api/', predict_DenseNet169_request,
         name='predict_DenseNet169_request'),
    path('predict_DenseNet169/', predict_DenseNet169, name='predict_DenseNet169'),
    path('predict_DenseNet201/api/', predict_DenseNet201_request,
         name='predict_DenseNet201_request'),
    path('predict_DenseNet201/', predict_DenseNet201, name='predict_DenseNet201'),

    path('predict_InceptionV3/api/', predict_InceptionV3_request,
         name='predict_InceptionV3_request'),
    path('predict_InceptionV3/', predict_InceptionV3, name='predict_InceptionV3'),
    path('predict_NASNetMobile/api/', predict_NASNetMobile_request,
         name='predict_NASNetMobile_request'),
    path('predict_NASNetMobile/', predict_NASNetMobile, name='predict_NASNetMobile'),
    path('predict_NASNetLarge/api/', predict_NASNetLarge_request,
         name='predict_NASNetLarge_request'),
    path('predict_NASNetLarge/', predict_NASNetLarge, name='predict_NASNetLarge'),
]