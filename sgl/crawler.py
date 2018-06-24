from sgl import sites


def get_houses(payload):
    '''
    house = {
        'name': <str>,
        'url': <str>,
        'price': <str>,
        'area': <str>,
        'kind': <str>,
        'update_time': <datetime>,
        'images': [
            <str>,
            <str>,
            ...
        ],
        'lat': <decimal>,
        'lng': <decimal>,
    }
    '''
    houses = sites.sgl.get(payload)
    return houses
