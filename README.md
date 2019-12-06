# AI Image classifiers on Django server with REST API

<div align="center">
    <a href=""><img src="https://i.loli.net/2019/03/19/5c8ff77663c65.png" width="200" hegiht="200"/></a>
</div>
<br>

[![python3.5](https://img.shields.io/badge/python-3.5-blue.svg)]()
[![python3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)]()
[![python3.6](https://img.shields.io/badge/python-3.7-orange.svg)]()
[![django3.0.0](https://img.shields.io/badge/django-3.0.0-brightgreen.svg)]()
[![Build Status](https://travis-ci.com/nature1995/AI-Image-classifiers-on-Django-with-RESTAPI.svg?branch=master)](https://travis-ci.com/nature1995/AI-Image-classifiers-on-Django-with-RESTAPI)


## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Features](#features)
- [Architecture](#architecture)
- [Usage](#usage)
- [Results](#results)
- [Issue](#issue)
- [Others](#others)
- [License](#license)

## Introduction  
A Keras deep learning image classifiers on Django server with REST API. It can help you quickly deploy and apply ML models.

## Description 
Machine Learning (ML) models are typically trained and test on benchmark data sets. However, such data sets may not represent the data in real applications. These ML models should be updated after tested on real data sets. Deployment of the models after each update may be time consuming. Therefore, automated deployment is needed to save time and effort. In this proposal, we describe our solution to integrate trained ML models into any application of interest. We use Django web-based platform to build REST API for model deployment. Jenkins is used for continuous integration and automated deployment of ML models into Django servers.

## Features
- [x] Add Account management funtion
- [x] Add Login & Signup
- [x] Add Django Rest Framework
- [x] Optimize front-end interface, adapt to mobile and PC interface
- [x] Design front-end and back-end interactive interfaces
- [x] Add feature: Face comparison
- [x] Add feature: Bank card identification
- [x] Add feature: Gesture identification
- [x] Add feature: Image classify using following model：
  - [x] ResNet50
  - [x] Xception  
  - [x] MobileNet, MobileNetV2  
  - [x] InceptionV3, InceptionResNetV2
  - [x] DenseNet121, DenseNet169, DenseNet201
  - [x] VGG16, VGG19
  - [x] NASNetMobile, NASNetLarge
- [x] Run each part of functions seperately in local and cloud server
- [x] Run all the functions in local server and cloud server
- [x] Design and using machine learning CI/CD Tools such as Git, Jenkins, Nginx, uwgsi for deployment.

## Architicture

<div align="center">
<img src="https://s2.ax1x.com/2019/05/01/EJBx0S.png" width="600" height="300" alt="Result01.png" title="Result01.png" />
</div>

## Usage
I assume you already have your own local virtual environment.  
```
git clone https://github.com/nature1995/image-classify-django-server.git
```
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000
```
Access the web page though this link: http://127.0.0.1:8000/

Name         				| Description
--------------------------- | -----------------------
Face comparison  			| Extract and analyze facial features in pictures
Bank card identification  	| Identify the field information above the bank card
Gesture identification  	| Detect and return the meaning of the gesture in the picture.
Image classify 				| Detects objects in the image, returns the detected object name, and the corresponding confidence.		

### Docker
You can use `dockerfile` to build this project easily.
```sh
# Follow any instruction to install the docker-ce, docker for OS X or PC in your device
docker build -t ai_image_classifiers .
docker run -it --rm -p 8000:8000 --name ai_image_classifiers_app ai_image_classifiers:latest
```

## Result

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

## Compatibility
Support to Django>=2.1.5 or Django==3.0.0 and Python 3.5, 3.6, 3.7.

## Issue
If you have questions or issues, please feel free to tell us.
## Contribution
Welcome to make pull request. If you have a related project/component/tool, add it with a pull request to add it!

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

## Contributors

[@nature1995](http://ranxiaolang.com)  

[@sergulaydore](https://sergulaydore.com)  

## License

[MIT](LICENSE) ©