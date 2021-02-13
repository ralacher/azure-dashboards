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
Delete existing markdown files prior to building new ones
'''
def clean():
    files = os.listdir('widgets')
    for file in files:
        if file.endswith('.md'):
            os.remove('widgets/{}'.format(file))

'''
Arbitrary checks
'''
def test_data(json_data):
    if len(json_data['description']) > 150:
        print('Description length cannot be greater than 150 characters')
        return False
    return True

if __name__ == '__main__':

    # jinja2 setup
    loader = jinja2.FileSystemLoader('widgets/templates')
    environment = jinja2.Environment(loader=loader)

    # jinja2 template setup
    widget_template = environment.get_template('widget.md')
    dashboard_widget = environment.get_template('widget.json')

    # ARM template
    arm_template_data = None
    with open('widgets/templates/deployTemplate.json', 'r') as file_object:
        arm_template_data = json.load(file_object)
        clean()

        x_pos = 3
        y_pos = 0
        for index, widget in enumerate(os.listdir('widgets/json')):
            widget_name = widget.replace('.json', '')
            json_data = read_widget(widget)
            
            is_valid = test_urls(json_data)
            if is_valid is not True:
                print('{} returned a {} status code'.format(is_valid[0], is_valid[1]))
                continue

            # Render the markdown widget and write the file
            rendered_widget = widget_template.render(json_data)
            write_widget(widget_name, rendered_widget)

            # Render the ARM template
            arm_index = index + 1
            rendered_arm = json.loads(
                    dashboard_widget.render(
                        json_data, index=arm_index, x=x_pos, y=y_pos, widgetName='{}.md'.format(widget_name)))

            # Increment x and y position to place the next widgets
            y_pos += 3
            if arm_index % 3 == 0:
                x_pos += 4
                y_pos = 0
            arm_template_data['resources'][0]['properties']['lenses']['0']['parts'][arm_index] = rendered_arm

    with open('arm-templates/deployTemplate.json', 'w') as file_object:
        json.dump(arm_template_data, file_object)
