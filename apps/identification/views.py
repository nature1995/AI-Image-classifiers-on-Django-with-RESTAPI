from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils

from keras.applications import ResNet50
from keras.applications import MobileNet, MobileNetV2
from keras.applications import InceptionV3, InceptionResNetV2
from keras.applications import DenseNet121, DenseNet169, DenseNet201
from keras.applications import VGG19, VGG16, Xception
from keras.applications import NASNetMobile, NASNetLarge
from PIL import Image
import numpy as np
import io
import tensorflow as tf
import json
import ssl


#  Convert the image as a correct formation
def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


#  ResNet50
def predict(request):
    try:
        load_model()
        ssl._create_default_https_context = ssl._create_unverified_context
    except:
        pass
    finally:
        return render(request, 'predict.html')


def load_model():
    # # NASNetLarge Model 331x331
    # settings.SITE_MODEL = NASNetLarge(weights="imagenet")
    # # NASNetMobile Model 224x224
    # settings.SITE_MODEL = NASNetMobile(weights="imagenet")
    # # Xception Model 299x299
    # settings.SITE_MODEL = Xception(weights="imagenet")
    # # VGG19 Model 224x224
    # settings.SITE_MODEL = VGG19(weights="imagenet")
    # # VGG16 Model 224x224
    # settings.SITE_MODEL = VGG16(weights="imagenet")
    # # DenseNet201 Model 224x224
    # settings.SITE_MODEL = DenseNet201(weights="imagenet")
    # # DenseNet169 Model 224x224
    # settings.SITE_MODEL = DenseNet169(weights="imagenet")
    # # DenseNet121 Model 224x224
    # settings.SITE_MODEL = DenseNet121(weights="imagenet")
    # # InceptionV3 Model 299x299
    # settings.SITE_MODEL = InceptionV3(weights="imagenet")
    # # InceptionResNetV2 Model 299x299
    # settings.SITE_MODEL = InceptionResNetV2(weights="imagenet")
    # # MobileNet Model 224x224
    # settings.SITE_MODEL = MobileNet(weights="imagenet")
    # # MobileNetV2 Model 224x224
    # settings.SITE_MODEL = MobileNetV2(weights="imagenet")
    # # ResNet50 Model 224x224
    settings.SITE_MODEL = ResNet50(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))
            # image = prepare_image(image, target=(224, 224))/255
            # image = prepare_image(image, target=(299, 299))/255
            # image = prepare_image(image, target=(331, 331))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds, top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


# MobileNet
def predict_MobileNet(request):
    try:
        load_MobileNet_model()
    except:
        pass
    finally:
        return render(request, 'predict_MobileNet.html')


def load_MobileNet_model():
    # # MobileNet Model 224x224
    settings.SITE_MODEL = MobileNet(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_MobileNet_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


# InceptionResNetV2
def predict_InceptionResNetV2(request):
    try:
        load_InceptionResNetV2_model()
    except:
        pass
    finally:
        return render(request, 'predict_InceptionResNetV2.html')


def load_InceptionResNetV2_model():
    # # InceptionResNetV2 Model 299x299
    settings.SITE_MODEL = InceptionResNetV2(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_InceptionResNetV2_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(299, 299))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  MobileNetV2
def predict_MobileNetV2(request):
    try:
        load_MobileNetV2_model()
    except:
        pass
    finally:
        return render(request, 'predict_MobileNetV2.html')


def load_MobileNetV2_model():
    # MobileNetV2 Model 224x224
    settings.SITE_MODEL = MobileNetV2(weights="imagenet")
        # # ResNet50 Model 224x224
    # settings.SITE_MODEL = ResNet50(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_MobileNetV2_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  Xception
def predict_Xception(request):
    try:
        load_Xception_model()
    except:
        pass
    finally:
        return render(request, 'predict_Xception.html')


def load_Xception_model():
    # # Xception Model 299x299
    settings.SITE_MODEL = Xception(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_Xception_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(299, 299))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  VGG16
def predict_VGG16(request):
    try:
        load_VGG16_model()
    except:
        pass
    finally:
        return render(request, 'predict_VGG16.html')


def load_VGG16_model():
    # # VGG16 Model 224x224
    settings.SITE_MODEL = VGG16(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_VGG16_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  VGG19
def predict_VGG19(request):
    try:
        load_VGG19_model()
    except:
        pass
    finally:
        return render(request, 'predict_VGG19.html')


def load_VGG19_model():
    # # VGG19 Model 224x224
    settings.SITE_MODEL = VGG19(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_VGG19_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6
            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds, top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  DenseNet121
def predict_DenseNet121(request):
    try:
        load_DenseNet121_model()
    except:
        pass
    finally:
        return render(request, 'predict_DenseNet121.html')


def load_DenseNet121_model():
    # # DenseNet121 Model 224x224
    settings.SITE_MODEL = DenseNet121(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_DenseNet121_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds, top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  DenseNet169
def predict_DenseNet169(request):
    try:
        load_DenseNet169_model()
    except:
        pass
    finally:
        return render(request, 'predict_DenseNet169.html')


def load_DenseNet169_model():
    # # DenseNet169 Model 224x224
    settings.SITE_MODEL = DenseNet169(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_DenseNet169_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  DenseNet201
def predict_DenseNet201(request):
    try:
        load_DenseNet201_model()
    except:
        pass
    finally:
        return render(request, 'predict_DenseNet201.html')


def load_DenseNet201_model():
    # # DenseNet201 Model 224x224
    settings.SITE_MODEL = DenseNet201(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_DenseNet201_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  InceptionV3
def predict_InceptionV3(request):
    try:
        load_InceptionV3_model()
    except:
        pass
    finally:
        return render(request, 'predict_InceptionV3.html')


def load_InceptionV3_model():
    # # InceptionV3 Model 299x299
    settings.SITE_MODEL = InceptionV3(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_InceptionV3_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(299, 299))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  NASNetMobile
def predict_NASNetMobile(request):
    try:
        load_NASNetMobile_model()
    except:
        pass
    finally:
        return render(request, 'predict_NASNetMobile.html')


def load_NASNetMobile_model():

    # # NASNetMobile Model 224x224
    settings.SITE_MODEL = NASNetMobile(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_NASNetMobile_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(224, 224))/255

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')


#  NASNetLarge
def predict_NASNetLarge(request):
    try:
        load_NASNetLarge_model()
    except:
        pass
    finally:
        return render(request, 'predict_NASNetLarge.html')


def load_NASNetLarge_model():

    # # NASNetLarge Model 331x331
    settings.SITE_MODEL = NASNetLarge(weights="imagenet")
    settings.SITE_GRAPH = tf.get_default_graph()


@csrf_exempt
def predict_NASNetLarge_request(request):

    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':

        top = request.POST.get("top")

        if request.FILES.get("image"):
            # read the image in PIL format
            image = request.FILES["image"].read()
            image = Image.open(io.BytesIO(image))

            if top:
                top = int(top)
            else:
                top = 6

            # preprocess the image and prepare it for classification
            # choice a format which the model use
            image = prepare_image(image, target=(331, 331))/100

            # classify the input image and then initialize the list
            # of predictions to return to the client
            with settings.SITE_GRAPH.as_default():
                preds = settings.SITE_MODEL.predict(image)
            results = imagenet_utils.decode_predictions(preds,top=top)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return HttpResponse(json.dumps(data), content_type='application/json')
