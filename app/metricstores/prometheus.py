import requests
import logging


class PrometheusMetricStore(object):
    def __init__(self, config):
        self.config = config

    def get_metric_value(self, metric_query):
        prometheus_url = self.config['url']
        prometheus_query_url = "{}/api/v1/query".format(prometheus_url)
        response = requests.get(prometheus_query_url, params=dict(query=metric_query))
        response_json = response.json()
        if len(response_json['data']['result']) != 0:
            return float(response['data']['result'][0]['value'][1])
        else:
            return None


