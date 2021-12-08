from province import Province, sample_province_data


def test_province_short_fall():
    asia = Province(sample_province_data())
    assert asia.short_fall == 5
