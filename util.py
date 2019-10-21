from schema import SCHEMA


def get_attributes(q):
    q = q.lower().strip()
    if q:
        res = []
        for k, info in SCHEMA.attributes.items():
            name = info.get('name', '').lower()
            desc = info.get('description', '').lower()
            if q in k.lower():
                if k not in res:
                    res.append((k, info, len(k) - len(q)))
            if q in name:
                if k not in res:
                    res.append((k, info, len(name) - len(q)))
            if q in desc:
                if k not in res:
                    res.append((k, info, len(desc) - len(q)))
        return [(k, info) for k, info, _ in sorted(res, key=lambda x: x[2])], True
    return sorted(SCHEMA.attributes.items(), key=lambda x: x[0]), False


def get_attribute(name):
    return SCHEMA.attributes.get(name)
