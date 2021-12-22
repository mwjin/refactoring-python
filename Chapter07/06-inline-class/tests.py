from shipment import Shipment, TrackingInformation


def test_tracking_info():
    _shipment = Shipment(TrackingInformation("Apple", 1234))
    assert _shipment.tracking_info == "Apple: 1234"
    _shipment.tracking_number = 5678
    assert _shipment.tracking_info == "Apple: 5678"
    _shipment.tracking_information.shipping_company = "Samsung"
    assert _shipment.tracking_info == "Samsung: 5678"
