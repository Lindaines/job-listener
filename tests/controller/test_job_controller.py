import pytest

from controller.job_controller import JobController


def test_handler_raise_exception():
    package = {}
    with pytest.raises(Exception):
        JobController().handle_package(package)
