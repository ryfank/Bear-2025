
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from PIL import Image
import io

# Function to upscale the image
def upscale_image(image_path, scale=2):
    image = Image.open(image_path)  # Open the uploaded image
    width, height = image.size
    new_width = width * scale
    new_height = height * scale
    upscaled_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return upscaled_image

# View for handling image upload and upscaling
def upload_and_upscale(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        
        # Save uploaded file to the filesystem
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        # Upscale the image
        upscaled_image = upscale_image(fs.url(filename), scale=2)

        # Save the upscaled image
        response_image = io.BytesIO()
        upscaled_image.save(response_image, format='PNG')
        response_image.seek(0)
        
        # Return the upscaled image as an HTTP response
        return HttpResponse(response_image, content_type='image/png')
    
    return render(request, 'upload.html')  # Return an upload form template


from django.shortcuts import render

# Create the view to render the index page
def index(request):
    return render(request, 'index.html')

