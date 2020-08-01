from cycle.Components.Frame import FrameFactory
from cycle.Components.Handle import HandleFactory
from cycle.Components.Seat import SeatFactory
from cycle.Components.Wheel import WheelFactory
from cycle.Components.Chain import ChainFactory
from datetime import datetime
from Config import logger


class Cycle(object):
    def __init__(self, config):
        self.bill_date = datetime.strptime(config['bill_date'], '%d.%m.%Y')
        frame_factory = FrameFactory(self.bill_date)
        handle_and_brake_factory = HandleFactory(self.bill_date)
        seat_factory = SeatFactory(self.bill_date)
        wheels_factory = WheelFactory(self.bill_date)
        chain_factory = ChainFactory(self.bill_date)

        self.frame = frame_factory.get_frame(config['frame'])
        self.handle = handle_and_brake_factory.get_handle(config['handle'])
        self.seat = seat_factory.get_seat(config['seat'])
        self.wheels = wheels_factory.get_wheel(config['wheel'])
        self.chain = chain_factory.get_chain(config['chain'])

    def print_bill(self):
        total = self.frame.get_price() + self.handle.get_price() + self.seat.get_price() \
                + self.wheels.get_price() + self.chain.get_price()
        logger.info("---------------------------------------------------------")
        logger.info(f'Date: {(25-len("Date: "))*" "}{self.bill_date}')
        logger.info(f'Frame {type(self.frame).__name__}:{(25-len("Frame: "+type(self.frame).__name__))*" "}{self.frame.get_price()}')
        logger.info(f'Handle {type(self.handle).__name__}:{(25-len("Handle: "+type(self.handle).__name__))*" "}{self.handle.get_price()}')
        logger.info(f'Seating {type(self.seat).__name__}:{(25-len("Seating: "+type(self.seat).__name__))*" "}{self.seat.get_price()}')
        logger.info(f'Wheels {type(self.wheels).__name__}:{(25-len("Wheels: "+type(self.wheels).__name__))*" "}{self.wheels.get_price()}')
        logger.info(f'Chain {type(self.chain).__name__}:{(25-len("Chain: "+type(self.chain).__name__))*" "}{self.chain.get_price()}')
        logger.info(f'Total:{(25-len("Total: "))*" "} {total}')
        logger.info("---------------------------------------------------------")
