from flask import Flask, Response
from flask.helpers import send_from_directory
import cv2
from PIL import Image
from numpy import asarray
import os
import json

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
camera = cv2.VideoCapture(-0, cv2.CAP_DSHOW)
app.config["CORS_HEADERS"] = "Content-Type"

# -----------------constants------------------------------
faceDetector = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
eyesDetector = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")


# -----------------routes---------------------------------
@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/video")
def video():
    return Response(getImages(), mimetype="multipart/x-mixed-replace; boundary=frame")


# -----------------helper functions-----------------------
def getImages():
    while True:
        try:
            success, frame = camera.read()
            if not success:
                yield errorImage()
            faces = faceDetector.detectMultiScale(frame, 1.1, 7)
            drawRectanglesFaces(frame, faces)
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
        except:
            yield errorImage()


def errorImage():
    img = Image.open("notFound.jpg")
    img = asarray(img)
    ret, buffer = cv2.imencode(".jpg", img)
    frame = buffer.tobytes()
    return b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"


def drawRectanglesFaces(frame, faces):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 140), 2)
        roiGray = gray[y : y + h, x : x + w]
        roiColor = frame[y : y + h, x : x + w]
        eyes = eyesDetector.detectMultiScale(roiGray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex + ew, ey + eh), (0, 0, 140), 2)


def build_response(statusCode, key, val):
    return {
        "statusCode": statusCode,
        "headers": {"Access-Control-Allow-Origin": "*", "Content-Type": "text/plain"},
        key: json.dumps(val),
    }


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=2022)
    # app.run(debug=True, host="localhost", port=2001)
