from schema import SCHEMA


def get_measures(q):
    q = q.lower().strip()
    if q:
        res = []
        for k, info in SCHEMA.measures:
            name = info.get('title_de', '').lower()
            desc = info.get('definition_de', '').lower()
            if q in k.lower():
                if k not in res:
                    res.append((k, info, len(k) - len(q)))
            if q in name:
                if k not in res:
                    res.append((k, info, len(name) - len(q)))
            if q in desc:
                if k not in res:
                    res.append((k, info, len(desc) - len(q)))
            if q in ''.join(d.get('definition_de', '') for d in info['dimensions'].values()).lower():
                if k not in res:
                    res.append((k, info, 0))
            if q in ''.join(info['dimensions'].keys()).lower():
                if k not in res:
                    res.append((k, info, 0))
        return [(k, info) for k, info, _ in sorted(res, key=lambda x: x[2])], True
    return SCHEMA.measures, False


def get_measure(statistic, measure):
    statistic = SCHEMA.statistics[statistic]
    return {'statistic': {'title_de': statistic['title_de'], 'key': statistic['name']},
            'measure': {**{'key': measure}, **statistic['measures'][measure]}}


def get_dimension(statistic, measure_key, dimension_key):
    statistic = SCHEMA.statistics[statistic]
    measure = statistic['measures'][measure_key]
    dimension = measure['dimensions'][dimension_key]
    return {'statistic': {'title_de': statistic['title_de'], 'key': statistic['name']},
            'measure': {**{'key': measure_key}, **measure},
            'dimension': {**{'key': dimension_key}, **dimension}}
