import os
import logging
import json

VALIDATION_SCHEMA = json.load(open("Input_schema.json", 'r'))

PARTS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cycle', 'Components', 'Parts_pricing')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('Cycle_Pricing')