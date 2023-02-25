import data
import sender_stand_request


def test_get_order_track():
    response_with_order = sender_stand_request.post_an_order(data.order_body)
    order_track = response_with_order.json()['track']
    response_with_order = sender_stand_request.get_order_by_track(order_track)

    assert response_with_order.status_code == 200
