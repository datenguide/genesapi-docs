from flask import Flask, render_template, request

from util import get_attribute, get_attributes


app = Flask(__name__)


REGION_LEVELS = ('Deutschland', 'Bundesländer', 'Reg.-Bezirke / Regionen', 'Kreise', 'Gemeinden')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/attribute')
def render_attributes():
    attributes, search = get_attributes(request.args.get('q') or '')
    return render_template('attributes.html', attributes=attributes, search=search, level_labels=REGION_LEVELS)


@app.route('/<attribute>')
def render_attribute(attribute):
    data = get_attribute(attribute)
    if data:
        data['attribute'] = attribute
        data['level_labels'] = REGION_LEVELS
        return render_template('attribute.html', **data)


@app.route('/<attribute>/<argument>')
def render_argument(attribute, argument):
    attr = get_attribute(attribute)
    if attr:
        data = attr.get('dimensions', {}).get(argument)
        if data:
            data['attribute'] = attr
            data['level_labels'] = REGION_LEVELS
            return render_template('argument.html', **data)
