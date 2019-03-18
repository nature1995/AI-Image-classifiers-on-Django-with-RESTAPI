# Image classify Django server with REST API

<div align="center">
    <a href=""><img src="https://i.loli.net/2019/03/19/5c8ff77663c65.png" width="200" hegiht="200"/></a>
</div>
<br>

[![python3.5](https://img.shields.io/badge/python-3.5-blue.svg)]()
[![python3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)]()
[![django2.1.5](https://img.shields.io/badge/django-2.1.5-orange.svg)]()
[![Build Status](https://travis-ci.com/nature1995/Django-AI-IOT.svg?token=ihxd9jwdJ367UvYy3j9G&branch=master)](https://travis-ci.com/nature1995/Django-AI-IOT)

## Introduction  
A Keras deep learning image classify Django server with REST API.

## Purposals  
This project provides image processing and recognition capabilities in the field of artificial intelligence by building web services. Those features can be conveniently and quickly used on mobile phones, computers, and tablets. Provide a good user experience and a beautiful interface。

## Features
- [x] Create Django web server in local
- [x] Add Account management funtion
- [x] Add Login & Signup
- [x] Buy and set cloud server (Alibaba Cloud), then install environment
- [x] Add Django Rest Framework
- [x] Run my Django web in cloud server
- [x] Optimize front-end interface, adapt to mobile and PC interface
- [x] Design front-end and back-end interactive interfaces
- [x] Add feature: Face comparison
- [x] Add feature: Bank card identification
- [x] Add feature: Gesture identification
- [x] Add feature: image classify using following model：
  - [x] ResNet50
  - [x] Xception  
  - [x] MobileNet, MobileNetV2  
  - [x] InceptionV3, InceptionResNetV2
  - [x] DenseNet121, DenseNet169, DenseNet201
  - [x] VGG16, VGG19
  - [x] NASNetMobile, NASNetLarge
- [x] Run each part of functions seperately in local server 
- [x] Run all the functions in local server
- [x] Run each part of functions seperately in my own cloud server 
- [x] Run all the functions in my own cloud server

## Requirements
```
pip3 install -r requirements.txt
```

## Usage
I assume you already have your own local virtual environment.  
```
git clone https://github.com/nature1995/image-classify-django-server.git
```
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Access the web page though this link: http://127.0.0.1:8000/

## Web API

Name         		| Input Size| API address
---------    		| ----------| ----------------------------------------------------
ResNet50     		| 224x224   | http://127.0.0.1:8000/predict/api/
Xception     		| 299x299   | http://127.0.0.1:8000/predict_Xception/api/
MobileNet     		| 224x224   | http://127.0.0.1:8000/predict_MobileNet/api/
MobileNetV2     	| 224x224   | http://127.0.0.1:8000/predict_MobileNetV2/api/
InceptionV3     	| 299x299   | http://127.0.0.1:8000/predict_InceptionV3/api/
InceptionResNetV2   | 224x224   | http://127.0.0.1:8000/predict_InceptionResNetV2/api/
DenseNet121     	| 224x224   | http://127.0.0.1:8000/predict_DenseNet121/api/
DenseNet169     	| 224x224   | http://127.0.0.1:8000/predict_DenseNet169/api/
DenseNet201     	| 224x224	| http://127.0.0.1:8000/predict_DenseNet201/api/
VGG16     			| 224x224   | http://127.0.0.1:8000/predict_VGG16/api/
VGG19     			| 224x224   | http://127.0.0.1:8000/predict_VGG19/api/
NASNetLarge     	| 331x331   | http://127.0.0.1:8000/predict_NASNetLarge/api/
NASNetMobile     	| 224x224   | http://127.0.0.1:8000/predict_NASNetMobile/api/

#### Input
Parameter | Type                           | Description
--------- | ------------------------------ | -----------------------------------------------------------------------------------
image     | file                           | Image file that you want to classify.
top       | text<br>(optional, default=6) | Return top-k categories of the results. Must me string in integer format.

Note: You can not send a very large size image.

#### Result
Parameter    | Type                | Description
------------ | ------------------- | --------------------------------------------
success      | bool                | Whether classification was sucessfuly or not 
predictions  | label, float        | pair of label and it's probability

#### Accuracy for individual models
Model	  			|   Accuracy	|	Top-6 Accuracy
------------------  | ------------  | --------------------
Xception			|	0.780		|		0.955	
VGG16				|	0.722		|		0.914	
VGG19				|	0.723		|		0.910	
ResNet50			|	0.748		|		0.931	
ResNet101			|	0.785		|		0.939	
ResNet152			|	0.776		|		0.941	
ResNet50V2			|	0.770		|		0.920	
ResNet101V2			|	0.783		|		0.938	
ResNet152V2			|	0.791		|		0.952	
ResNeXt50			|	0.787		|		0.948	
ResNeXt101			|	0.798		|		0.953	
InceptionV3			|	0.789		|		0.948	
InceptionResNetV2	|	0.813		|		0.963	
MobileNet			|	0.714		|		0.904	
MobileNetV2			|	0.723		|		0.912	
DenseNet121			|	0.761		|		0.934	
DenseNet169			|	0.772		|		0.952	
DenseNet201			|	0.783		|		0.945	
NASNetMobile		|	0.752		|		0.920	
NASNetLarge			|	0.837		|		0.959	


#### Example

Using [Postman](https://www.getpostman.com/downloads/) to test the API:  
POST http://127.0.0.1:8000/predict_VGG19/api/

**Result**
```
{
    "success": true,
    "predictions": [
        {
            "label": "red_fox",
            "probability": 0.8969062566757202
        },
        {
            "label": "kit_fox",
            "probability": 0.08841043710708618
        },
        {
            "label": "grey_fox",
            "probability": 0.012036639265716076
        },
        {
            "label": "Arctic_fox",
            "probability": 0.0022438077721744776
        },
        {
            "label": "coyote",
            "probability": 0.0002566342300269753
        },
        {
            "label": "white_wolf",
            "probability": 0.00005685776341124438
        }
    ]
}
```

## Preview
https://ranxiaolang.com

## Compatibility
The codes are tested using Travis-CI platform with django 2.1.5 and Python 3.5, 3.6

## Others

**Admin Account**
``` 
python manage.py createsuperuser

username: ranxiaolang
email: YOUR EMAIL  
password: ranxiaolang  
```
Access the web page though this link: http://127.0.0.1:8000/admin 

**Django Restframework**

Access the web page though this link: http://127.0.0.1:8000/iot/

## Author

* **Ziran Gong** - [Web Page](http://ranxiaolang.com)

## License
This software is licensed under the GNU General Public License v3.0 License. For more information, read the file [LICENSE](https://github.com/nature1995/image-classify-django-server/blob/master/LICENSE).
