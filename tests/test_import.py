"""Test my-cicd."""

import my-cicd


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(my-cicd.__name__, str)
