import markdown2
from jinja2 import Environment, PackageLoader
from cuddlefish import apiparser
from cuddlefish import apiparser

def div(hunks):
    environment = Environment(loader=PackageLoader('cuddlefish', 'templates'))
    environment.filters['markdown'] = markdown2.markdown

    entities = []
    for h in hunks:
        if h[0] == 'api-json':
            h[1]['json_type'] = "api"
        else:
            print h
        entities.append(h[1])

    module = {'name': 'request', 'entities': entities}

    template = environment.get_template('module_div.html')
    return template.render(module = module)

def html(name, div_text):
    environment = Environment(loader=PackageLoader('cuddlefish', 'templates'))
    template = environment.get_template('module_doc.html')
    return template.render(name = name, div_text = div_text)

