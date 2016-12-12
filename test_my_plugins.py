from datetime import datetime, timedelta
from my_plugins import convert_to_dict



def test_ctd_func_converts_correctly():
    starting = "qty 3 sku 'abc' average_unit_price 40"
    ending = "'qty': 3, 'sku': 'abc', 'average_unit_price': 40"
    assert convert_to_dict(starting) == ending

