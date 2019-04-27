# In this code, it takes two pictures (Klopp and Radwan) as known images for the model then add new unknown image that we don't know whether it's like the first or the second or a new one.
import face_recognition, json
from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def index():

    klopp_image = face_recognition.load_image_file("known_people/klopp.jpg")
    radwan_image = face_recognition.load_image_file("known_people/radwan.jpg")
    unknown_image = face_recognition.load_image_file("klopp2013.jpg")

    try:
        klopp_face_encoding = face_recognition.face_encodings(klopp_image)[0]
        radwan_face_encoding = face_recognition.face_encodings(radwan_image)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    known_faces = [klopp_face_encoding,radwan_face_encoding]

    results = face_recognition.compare_faces(known_faces,unknown_face_encoding)
    i = 0
    returned = []
    for r in results:
        returned.append([i,str(r)])
        i+=1
    
    y = jsonify(returned)
    print(y)
    return y
if __name__ == "__main__":
    app.run(debug=True)