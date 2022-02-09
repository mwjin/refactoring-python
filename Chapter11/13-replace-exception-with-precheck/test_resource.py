import pytest

from resource_pool import Resource, ResourcePool


@pytest.fixture
def resource_pool():
    yield ResourcePool()
    Resource.reset()


def test_add_resouce(resource_pool):
    for _ in range(3):
        resource_pool.add()

    for i in range(2, -1, -1):
        assert resource_pool.get().id == i


def test_get_resource_without_add(resource_pool):
    for i in range(3):
        assert resource_pool.get().id == i
