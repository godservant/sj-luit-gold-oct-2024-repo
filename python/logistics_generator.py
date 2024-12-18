import time
import requests

LAMBDA_FUNCTION_URL = ''
NUMBER_OF_REQUESTS = 1000
TIME_DELAY = 5 # seconds

for i in range(1, NUMBER_OF_REQUESTS):
    print("step: ", i)
    time.sleep(TIME_DELAY)
    r = requests.get(LAMBDA_FUNCTION_URL)
    print(r)
    print(r.content)





