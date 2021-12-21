import example2
from customer_data import get_raw_data_of_customers


def test_compare_usage():
    result = example2.compare_usage("1995", "2016", "1")
    assert result["laterAmount"] == 50
    assert result["change"] == -20


def test_set_amount():
    example2.set_amount("1995", "2016", "2", 60)
    assert get_raw_data_of_customers()["1995"]["usages"]["2016"]["2"] == 60
