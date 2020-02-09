from utils.endpoints import *
import requests as r
import json


def make_url(endpoint):
    url = host + endpoint
    return url


def get(endpoint, headers=None, params=None, data=None):
    request = r.get(url=make_url(endpoint),
                    headers=headers,
                    params=params,
                    json=data)
    return request


def post(endpoint, headers=None, params=None, data=None):
    request = r.post(url=make_url(endpoint),
                     headers=headers,
                     params=params,
                     json=data)
    return request


def put(endpoint, headers=None, params=None, data=None):
    request = r.put(url=make_url(endpoint),
                    headers=headers,
                    params=params,
                    json=data)
    return request


def patch(endpoint, headers=None, params=None, data=None):
    request = r.patch(url=make_url(endpoint),
                      headers=headers,
                      params=params,
                      json=data)
    return request


def delete(endpoint, headers=None, params=None, data=None):
    request = r.delete(url=make_url(endpoint),
                       headers=headers,
                       params=params,
                       json=data)
    return request


def transform_json(content):
    try:
        result = '\n    ' + json.dumps(content, indent=4).replace('None', 'null').replace("\n", "\n    ")
    except BaseException:
        result = 'Not serializable'
    return result
