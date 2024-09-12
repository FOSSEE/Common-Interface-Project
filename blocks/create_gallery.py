import os
import django
from django.test import RequestFactory
import json

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocks.settings')

# Initialize Django
django.setup()

from saveAPI.views import GalleryView


def escape_quotes(value):
    if value is None:
        return ''
    # Escape backslashes, single quotes, and double quotes
    return value.replace('\\', '\\\\').replace("'", "\\'")


def format_js_object(data):
    # This function will format each data item into the required JavaScript object structure
    formatted = f"""{{
    save_id: '{escape_quotes(data["save_id"])}',
    data_dump: '{escape_quotes(data["data_dump"])}',
    name: '{escape_quotes(data["name"])}',
    description: '{escape_quotes(data["description"])}',
    media: '{escape_quotes(data["media"])}',
    shared: {str(data["shared"]).lower()}
}}"""
    return formatted


if __name__ == "__main__":
    # Create a request object
    factory = RequestFactory()
    request = factory.get('/gallery')

    # Instantiate the view
    galleryView = GalleryView.as_view()

    # Call the view with the request object
    response = galleryView(request)

    # Render the response if it's not already rendered
    if not response.is_rendered:
        response.render()

    # Check if the response status code is 200 OK
    if response.status_code == 200:
        data = json.loads(response.content)
        print('// Sample schematics in gallery section are stored below as array of JS objects.')
        print()
        print('const GallerySchSample = [')

        formatted_objects = [format_js_object(item) for item in data]
        print(','.join(formatted_objects))

        print(']')
        print()
        print('export default GallerySchSample')
    else:
        print(f"Error: {response.status_code}")
