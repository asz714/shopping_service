import logging
import os

logger = logging.getLogger(__name__)

log_file = 'events.log'

path = os.path.join(os.path.dirname(__file__), log_file)

handler = logging.FileHandler(path)

format = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

handler.setFormatter(format)

logger.addHandler(handler)



