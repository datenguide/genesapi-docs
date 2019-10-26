from flask import Flask, render_template, request

from util import get_dimension, get_measure, get_measures


app = Flask(__name__)


REGION_LEVELS = ('Deutschland', 'Bundesländer', 'Reg.-Bezirke / Regionen', 'Kreise', 'Gemeinden')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/measures')
def render_measures():
    measures, search = get_measures(request.args.get('q') or '')
    return render_template('measures.html', measures=measures, search=search, level_labels=REGION_LEVELS)


@app.route('/<statistic>/<measure>')
def render_measure(statistic, measure):
    data = get_measure(statistic, measure)
    data['level_labels'] = REGION_LEVELS
    return render_template('measure.html', **data)


@app.route('/<statistic>/<measure>/<dimension>')
def render_dimension(statistic, measure, dimension):
    data = get_dimension(statistic, measure, dimension)
    data['level_labels'] = REGION_LEVELS
    return render_template('dimension.html', **data)
