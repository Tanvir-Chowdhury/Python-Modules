import numpy as np
from pprint import pprint
from pprint import pformat
import logging

data = {
    "colts" : np.random.rand(10),
    "aurrents" : np.random.rand(20)
}

pprint(data)

logging.basicConfig(level=logging.DEBUG,format='%(levelname)-8s %(message)s',)
logging.debug('Logging pformatted data')

formatted = pformat(data)

for line in formatted.splitlines():
    logging.debug(line.rstrip())

pprint(formatted)
