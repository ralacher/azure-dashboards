import requests
import jinja2
import json
import os

urls = ['armLink', 'documentationLink', 'githubLink']

'''
Writes a .md file to widgets/
'''
def write_widget(file_name, rendered_template):
    with open('widgets/{}.md'.format(file_name), 'w') as file_object:
        file_object.write(rendered_template)

'''
Reads a .json file from widgets/json/
'''
def read_widget(file_name):
    with open('widgets/json/{}'.format(file_name)) as file_object:
        return json.load(file_object)

'''
Checks the HTTP status code for the URLs
'''
def test_urls(json_data):
    for url in urls:
        response = requests.get(json_data[url]).status_code
        if response != 200:
            return (url, response)
    return True

'''
Arbitrary checks
'''
def test_data(json_data):
    if len(json_data['description']) > 150:
        print('Description length cannot be greater than 150 characters')
        return False
    return True

if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('widgets/templates')
    environment = jinja2.Environment(loader=loader)
    template = environment.get_template('widget.md')

    for widget in os.listdir('widgets/json'):
        widget_name = widget.replace('.json', '')
        json_data = read_widget(widget)
        
        is_valid = test_urls(json_data)
        if is_valid is not True:
            print('{} returned a {} status code'.format(is_valid[0], is_valid[1]))
            continue

        rendered_template = template.render(json_data)
        write_widget(widget_name, rendered_template)
