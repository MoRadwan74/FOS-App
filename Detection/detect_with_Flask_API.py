import face_recognition
from flask import Flask, jsonify, request
app = Flask(__name__)

'''def split(word): 
    return [char for char in word]
'''
@app.route('/filter', methods=['POST'])
def clone():
        
        path = request.args.get('key1')
        '''r = split(path)
        for c in r:
                if c == '\\':
                        z = '\\'
                        c = c + z

        f = ''.join(r)'''
        
        image = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(image)
        return jsonify(len(face_locations))

        
if __name__ == '__main__':
    app.run()
