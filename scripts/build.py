import requests
import jinja2
import json
import os

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

if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('widgets/templates')
    environment = jinja2.Environment(loader=loader)
    template = environment.get_template('widget.md')

    for widget in os.listdir('widgets/json'):
        widget_name = widget.replace('.json', '')
        json_data = read_widget(widget)
        rendered_template = template.render(json_data)
        write_widget(widget_name, rendered_template)
