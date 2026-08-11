"""Test my_cicd."""

import my_cicd


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(my_cicd.__name__, str)
