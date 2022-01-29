import os
import time

import requests

if url := os.environ.get("PINGER"):
    if url.endswith("/"):
        url = url[:-1]
    while True:
        time.sleep(int(os.environ.get("PINGER_INTERVAL", 900)))
        requests.get("%s/api/v1/ping" % (url))
