import yaml
import sys
import os
from string import Template

here = os.path.dirname(os.path.abspath(__file__))

templates_folder = os.path.join(here, 'templates')
balena_yml_template = Template(open(os.path.join(templates_folder, 'balena.yml.template')).read())
readme_template = Template(open(os.path.join(templates_folder, 'README.md.template')).read())

template_data = {}
REPO_NAME = sys.argv[1]
VARIANT_NAME = REPO_NAME.split('_')[1]
template_data['VARIANT_NAME'] = VARIANT_NAME
# template_data['FLEET_NAME'] = f"hm_{VARIANT_NAME}_mainnet_openfleet"
template_data['REPO_NAME'] = REPO_NAME

print("template data: {template_data}")


balena_output = balena_yml_template.substitute(balena_yml_template)
readme_output = balena_yml_template.substitute(readme_template)

with open(os.path.join(here, 'balena.yml'), 'w') as f:
    f.write(balena_output)
    
with open(os.path.join(here, 'README.md'), 'w') as f:
    f.write(readme_output)


