from datetime import datetime

import pytest

from example import photo_div, render_person
from person import Person
from photo import Photo


@pytest.fixture(scope="module")
def photo():
    return Photo("Test", "Seoul", datetime(2022, 1, 2, 10, 30, 54))


@pytest.fixture(scope="module")
def person(photo):
    return Person("Minwoo Jeong", photo)


def test_photo_div(photo):
    assert photo_div(photo) == "\n".join(
        [
            "<div>",
            "<p>Title: Test</p>",
            "<p>Date: 2022-01-02 10:30:54</p>",
            "<p>Location: Seoul</p>",
            "</div>",
        ]
    )


def test_render_person(person):
    assert render_person(person) == "\n".join(
        [
            "<p>Minwoo Jeong</p>",
            "<p>(Rendered HTML of the photo 'Test')</p>",
            "<p>Title: Test</p>",
            "<p>Date: 2022-01-02 10:30:54</p>",
            "<p>Location: Seoul</p>",
        ]
    )
