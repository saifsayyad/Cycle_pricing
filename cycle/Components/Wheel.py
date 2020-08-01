from configparser import ConfigParser
import os
from datetime import datetime
from abc import ABCMeta, abstractmethod
from Config import PARTS_PATH, logger

FILE_NAME = __name__.split('.')[-1]
CONFIG_PATH = os.path.join(PARTS_PATH, FILE_NAME)


class WheelFactory:
    def __init__(self, bill_date):
        self.bill_date = bill_date

    def get_wheel(self, config):
        return globals()[config](self.bill_date)


class Wheel(metaclass=ABCMeta):
    config = ConfigParser()

    @abstractmethod
    def get_price(self):
        """":returns Current price of frame"""

    def _get_price_from_config(cls, bill_date):
        for date_range in cls.config.sections():
            start_d, end_d = date_range.split('-')
            try:
                start_d = datetime.strptime(start_d, "%d.%m.%Y")
                if end_d != 'latest':
                    end_d = datetime.strptime(end_d, "%d.%m.%Y")
                else:
                    end_d = datetime.now()
            except ValueError as _e:
                print("Date Format wrong in Steel.ini file, Use 'DD.MM.YYYY'")
            if start_d <= bill_date <= end_d:
                return int(cls.config[date_range]['Price'])


class OffRoad(Wheel):
    def __init__(self, bill_date):
        self.config.read(os.path.join(CONFIG_PATH, f'{type(self).__name__}.ini'))
        self.price = self._get_price_from_config(bill_date)

    def get_price(self):
        return self.price


class Racing(Wheel):
    def __init__(self, bill_date):
        self.config.read(os.path.join(CONFIG_PATH, f'{type(self).__name__}.ini'))
        self.price = self._get_price_from_config(bill_date)

    def get_price(self):
        return self.price


class Tubeless(Wheel):
    def __init__(self, bill_date):
        self.config.read(os.path.join(CONFIG_PATH, f'{type(self).__name__}.ini'))
        self.price = self._get_price_from_config(bill_date)

    def get_price(self):
        return self.price
