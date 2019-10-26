import requests

# download schema on app startup
res = requests.get('https://data.genesapi.org/regionalstatistik/schema.json')
data = res.json()

# flatten measures
measures = sorted(((key, {**measure, **{'statistic': statistic}})
                   for statistic in data.values()
                   for key, measure in statistic['measures'].items()),
                  key=lambda x: x[1]['title_de'])


class SCHEMA:
    measures = measures
    statistics = data
