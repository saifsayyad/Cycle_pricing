from cycle.Cycle import Cycle
import pytest

test_data = [
    (
        {
            "bill_date": "22.02.2005",
            "frame": "Steel",
            "handle": "Steel",
            "seat": "RacingSeat",
            "wheel": "Tubeless",
            "chain": "SixGears"
        },
        {
            "frame": 100,
            "handle": 80,
            "seat": 89,
            "wheel": 185,
            "chain": 700
        }
    ),
    (
        {
            "bill_date": "22.02.2020",
            "frame": "CarbonFiber",
            "handle": "Steel",
            "seat": "RacingSeat",
            "wheel": "Tubeless",
            "chain": "SixGears"
        },
        {
            "frame": 820,
            "handle": 100,
            "seat": 110,
            "wheel": 200,
            "chain": 650
        }
    )
]


@pytest.mark.parametrize("in_config, expected", test_data)
def test_components_price(in_config, expected):
    """
        This test case verifies the that the parts price are Time sensitive, by providing different
        dates in the configuration and getting the same values as expected.

        asserts: Value of each component
        asserts: Total value

    :param in_config: Input configuration
    :param expected: Expected price for each component
    :return: None
    """
    cycle = Cycle(in_config)
    assert cycle.frame.get_price() == expected['frame']
    assert cycle.chain.get_price() == expected['chain']
    assert cycle.handle.get_price() == expected['handle']
    assert cycle.seat.get_price() == expected['seat']
    assert cycle.wheels.get_price() == expected['wheel']

    total = cycle.frame.get_price() + cycle.chain.get_price() + cycle.handle.get_price() \
            + cycle.seat.get_price() + cycle.wheels.get_price()

    expected_total = expected['frame'] + expected['chain'] + expected['handle'] + \
                     expected['seat'] + expected['wheel']
    assert total == expected_total
