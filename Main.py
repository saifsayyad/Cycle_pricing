import argparse
import os
import json
import jsonschema

from glob import glob
from queue import Queue
from threading import Thread, Lock
from time import time

from cycle.Cycle import Cycle

from Config import VALIDATION_SCHEMA, logger, PARTS_PATH

print_lock = Lock()


class PricingWorker(Thread):

    def __init__(self, queue, x):
        Thread.__init__(self)
        self.queue = queue
        self.thread_id = x

    def run(self):
        while True:
            configuration, task_id = self.queue.get()
            cycle = Cycle(configuration)
            print_lock.acquire()
            logger.info(f'Printing: {task_id}')
            cycle.print_bill()
            print_lock.release()
            self.queue.task_done()


def valid_json(input_data):
    try:
        jsonschema.validate(input_data, VALIDATION_SCHEMA)
        return True
    except jsonschema.ValidationError as _e:
        logger.error(f'Please verify input file! {str(_e)}')
        return False


def display_parts():
    components = dict()
    path_sep = '/' if os.name == 'posix' else '\\'
    for part in glob(PARTS_PATH + f'{path_sep}**{path_sep}*.ini', recursive=True):
        if part.split(path_sep)[-2] in components:
            components[(part.split(path_sep)[-2])].append(part.split(path_sep)[-1].replace('.ini', ''))
        else:
            components[(part.split(path_sep)[-2])] = [part.split(path_sep)[-1].replace('.ini', '')]
    logger.info('Available Parts list -')
    for component, parts in components.items():
        logger.info(f'\t{component}:')
        for part in parts:
            logger.info(f'\t\t{part}')
    logger.info("---------------------------------------------------------")


def main(args):
    queue = Queue()
    ts = time()
    config_file_path = args.configfile
    show_parts = args.availableparts

    if not show_parts and config_file_path is None:
        parser.error("--configfile or --availableparts is required")

    if show_parts:
        display_parts()

    if config_file_path is not None:
        if not os.path.exists(config_file_path):
            logger.error(f'Provided file doesn\'t exists! - {config_file_path}')
            exit(1)
        else:
            with open(config_file_path, 'r') as fp:
                configs = json.load(fp)
                if not valid_json(configs):
                    exit(1)

        for x in range(10):
            worker = PricingWorker(queue, f'Thread-{x}')
            worker.daemon = True
            worker.start()
        bill_no = 0
        for config in configs:
            bill_no += 1
            queue.put((config, f'Bill-{bill_no}'))
        queue.join()
        logger.info('Took %s', time() - ts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--configfile", help="JSON file path for Cycle Config")
    parser.add_argument("--availableparts", help="Lists all available Parts.", action='store_true')
    args = parser.parse_args()
    main(args=args)
