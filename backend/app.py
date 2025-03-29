from flask import Flask, request, send_file  #import Flask modules for web app idfk 
from PIL import Image  # For image handling (built- in)
import io  #handling byte streams

app = Flask(__name__)

#----------------------------------------------------

def upscale_image(image_stream, scale=2):
    #default x2
    #imagestream - uploading image file

    #opening image using Pillow
    image = Image.open(image_stream).convert("RGB")
    
    #math
    new_width = image.width * scale
    new_height = image.height * scale
    upscaled_image = image.resize((new_width, new_height), Image.BICUBIC) 
    
    #saves the image into a byte stream 
    byte_io = io.BytesIO()
    upscaled_image.save(byte_io, 'PNG')  #saves image as PNG into byte stream
    byte_io.seek(0) #resets stream positon
    return byte_io

#----------------------------------------------------

@app.route('/app', methods=['POST'])
def upscale():
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400 
     #if there is no image given - gives error
    
    file = request.files['file']
    upscaled_image_stream = upscale_image(file.stream) 
     #if image is given and it upscales it
    
    #returns image as png
    return send_file(upscaled_image_stream, mimetype='image/png', as_attachment=True, download_name='upscaled.png')

#----------------------------------------------------
    #runs program
if __name__ == '__main__':

    app.run(debug=True)  #starts the flask app



