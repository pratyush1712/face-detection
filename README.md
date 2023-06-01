# Cornell Detection
A Flask+React based application that utilizes Haar Cascade model to detect faces and eyes in images received from the webcam

## Technologies Used
- React for the frontend
- Flask for the backend (on run, flask application renders the index.html file in the React Build Folder)
- Heroku for deployement

## Steps to run on a local server
- ```git clone https://github.com/pratyush1712/face-detection.git```
- ```cd face-detection/backend```
- ```gunicorn --bind localhost:3000 app:app```

### <a href="https://cornell-detection.herokuapp.com/" target="_blank">Located Here</a>
