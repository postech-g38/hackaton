import pytest

from src.services.service_base import BaseService, NotFoundExcepition


def test_base_service_query_result_then_return_result():
    # arrange
    _object = object()
    
    # act
    result = BaseService.query_result(_object)

    # assert
    assert result is _object


def test_base_service_query_result_then_raise_not_found_exception():
    # arrange
    _object = None

    # act
    with pytest.raises(NotFoundExcepition) as excpt:
        result = BaseService.query_result(_object)
    
    # assert
    # assert str(excpt.value) == 'Entity not found'
