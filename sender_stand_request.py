import configuration
import requests
import data


# запрос для создания заказа
def post_an_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_AN_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# запрос для получения заказа по трек номеру
def get_order_by_track(track_number):
    params = {
        't': track_number
    }
    return requests.get(configuration.URL_SERVICE + configuration.GET_AN_ORDER_BY_ITS_NUMBER_PATH, params=params)