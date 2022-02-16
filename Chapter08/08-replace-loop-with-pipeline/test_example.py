import pytest

from example import acquire_data


@pytest.fixture
def csv():
    return "\n".join(
        [
            "office, country, telephone",
            "Chicago, USA, +1 312 373 1000",
            "Beijing, China, +86 4008 900 505",
            "Bangalore, India, +91 80 4064 9570",
            "Porto Alegre, Brazil, +55 51 3079 3550",
            "Chennai, India, +91 44 660 44766",
        ]
    )


def test_acquire_data(csv):
    assert acquire_data(csv) == [
        {"city": "Bangalore", "phone": "+91 80 4064 9570"},
        {"city": "Chennai", "phone": "+91 44 660 44766"},
    ]
