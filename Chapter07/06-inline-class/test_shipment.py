from shipment import Shipment


def test_tracking_info():
    _shipment = Shipment("Apple", 1234)
    assert _shipment.tracking_info == "Apple: 1234"
    _shipment.tracking_number = 5678
    assert _shipment.tracking_info == "Apple: 5678"
    _shipment.shipping_company = "Samsung"
    assert _shipment.tracking_info == "Samsung: 5678"
