import requests

# download schema on app startup
res = requests.get('https://data.genesapi.org/regionalstatistik/schema.json')
data = res.json()

# for local developement
# import json  # noqa
# data = json.load(open('./schema.json'))

# flatten attributes (FIXME update this whole app to the new schema layout)
attributes = [attribute for statistic in data.values() for attribute in statistic['attributes'].values()]


class SCHEMA:
    attributes = {a['name']: a for a in attributes}
    statistics = data
