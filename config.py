from arctic import Arctic
from main import monitor_pair
from threading import Thread
import yaml

# Arctic START
store = Arctic('mongodb://ledbest_arctic:4rcT1c@kerzane.ddns.net/arctic')

# Threading Method
def exchthreads(exch, pairs):
    monitor_pair(pairs, exch, store)

# Open .yml file and append to dictionary exch_pairs
with open('data.yml', 'r') as stream:
    try:
        exch_pairs = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Iterate through each key(exchange), i.e. bitfinex etc
# and create thread for each exchange
for key, value in exch_pairs.items():
    t = Thread(target=exchthreads, args=(key, value,))
    t.start()
