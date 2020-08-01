import json
from cycle.Cycle import Cycle
from cycle.Components import Chain, Frame, Handle, Wheel, Seat
import os
import subprocess
import pytest

FOR_VALIDATION = ['Cycle.py                    28 INFO     ---------------------------------------------------------',
                  'Cycle.py                    29 INFO     Date:                    2005-02-22 00:00:00',
                  'Cycle.py                    30 INFO     Frame Steel:             100',
                  'Cycle.py                    31 INFO     Handle Steel:            80',
                  'Cycle.py                    32 INFO     Seating RacingSeat:      89',
                  'Cycle.py                    33 INFO     Wheels Tubeless:         185',
                  'Cycle.py                    34 INFO     Chain SixGears:          700',
                  'Cycle.py                    35 INFO     Total:                   1154',
                  'Cycle.py                    36 INFO     ---------------------------------------------------------',
                  '']


def test_cycle_valid_out(caplog):
    """
        This test case verifies the basic requirement, When its called with correct json file.

        asserts: Is all the components and parts are initialised according to the config
        asserts: Output text format.
    """
    test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_valid_data.json'))
    valid_config = json.load(open(test_file_path, 'r'))

    for conf in valid_config:
        cycle = Cycle(conf)
        cycle.print_bill()

        #  Assert proper components
        assert isinstance(cycle.chain, Chain.Chain)
        assert isinstance(cycle.wheels, Wheel.Wheel)
        assert isinstance(cycle.frame, Frame.Frame)
        assert isinstance(cycle.seat, Seat.Seat)
        assert isinstance(cycle.handle, Handle.Handle)

        #  Assert valid parts as per configuration
        assert isinstance(cycle.chain, Chain.SixGears)
        assert not isinstance(cycle.chain, Chain.TwoGears)
        assert isinstance(cycle.handle, Handle.Steel)
        assert not isinstance(cycle.handle, Handle.Aluminium)
        assert isinstance(cycle.seat, Seat.RacingSeat)
        assert not isinstance(cycle.seat, Seat.ComfortSeat)
        assert isinstance(cycle.frame, Frame.Steel)
        assert not isinstance(cycle.frame, Frame.CarbonFiber)
        assert isinstance(cycle.wheels, Wheel.Tubeless)
        assert not isinstance(cycle.wheels, Wheel.OffRoad)

    captured = caplog.text.split('\n')
    for ind, valid_line in enumerate(FOR_VALIDATION):
        assert valid_line == captured[ind]


def test_cycle_invalid_out():
    """
        This test case verifies that, if a JSON file with wrong schema is passed as an argument it
        raises an error.

        asserts: if the correct key is caught in error.

    :return:
    """
    test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_invalid_data.json'))
    with pytest.raises(subprocess.CalledProcessError) as e:
        subprocess.check_output(["python", "Main.py", "--configfile", test_file_path])
        assert "ERROR - Please verify input file! 'frame' is a required property" in str(e)
