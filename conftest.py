from main import BooksCollector
import pytest

@pytest.fixture
def create_obj_class():
    collector = BooksCollector()
    return collector