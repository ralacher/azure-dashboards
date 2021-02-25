import requests
import jinja2
import json
import os

URLS = ['armLink', 'documentationLink', 'githubLink']
WORKDIR='widgets/'

'''
Writes a .md file to markdown/
'''
def write_widget(file_name, rendered_template):
    with open(os.path.join(WORKDIR, f'markdown/{file_name}.md'), 'w') as file_object:
        file_object.write(rendered_template)

'''
Reads a .json file from data/
'''
def read_widget(file_name):
    with open(os.path.join(WORKDIR, f'data/{file_name}'), 'r') as file_object:
        return json.load(file_object)

'''
Checks the HTTP status code for the URLs
'''
def test_urls(json_data):
    for url in URLS:
        response = requests.get(json_data[url]).status_code
        if response != 200:
            return (url, response)
    return True

'''
Delete existing markdown files prior to building new ones
'''
def clean():
    files = os.listdir(os.path.join(WORKDIR, 'markdown'))
    for file_name in files:
        if file_name.endswith('.md'):
            os.remove(os.path.join(WORKDIR, f'markdown/{file_name}'))

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
    loader = jinja2.FileSystemLoader(os.path.join(WORKDIR, 'templates'))
    environment = jinja2.Environment(loader=loader)

    # jinja2 template setup
    widget_template = environment.get_template('widget.md')
    dashboard_widget = environment.get_template('widget.json')

    # ARM template
    arm_template_data = None
    with open(os.path.join(WORKDIR, 'templates/deployDashboard.json'), 'r') as file_object:
        arm_template_data = json.load(file_object)
        clean()

        x_pos = 3
        y_pos = 0
        for index, widget in enumerate(os.listdir(os.path.join(WORKDIR, 'data')), 1):
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
            rendered_arm = json.loads(
                    dashboard_widget.render(
                        json_data, index=index, x=x_pos, y=y_pos, widgetName='{}.md'.format(widget_name)))

            # Increment x and y position to place the next widgets
            y_pos += 3
            if index % 3 == 0:
                x_pos += 4
                y_pos = 0
            arm_template_data['resources'][0]['properties']['lenses']['0']['parts'][index] = rendered_arm

    with open('arm-templates/deployDashboard.json', 'w') as file_object:
        json.dump(arm_template_data, file_object, indent=4)
