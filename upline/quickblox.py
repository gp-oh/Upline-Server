# -*- encoding: utf-8 -*-
# Link: http://quickblox.com/developers/Authentication_and_Authorization#Signature_generation
import json
import requests
import sha
import hmac

#========== YOUR DATA =======================
application_id = '25117'
authorization_key = '7eO2Mj-q9tDegSU'
authorization_secret = '3V3Ds8tcxfZTZp4'
# ===========================================

def get_timestamp_nonce():
    import random
    import time

    return str(time.time()), str(random.randint(1, 10000))

def create_signature_simple(timestamp, nonce):
    string_for_signature = 'application_id={id}&auth_key={auth_key}&nonce={nonce}&timestamp={timestamp}'.format(id=application_id,
                           auth_key=authorization_key, nonce=nonce, timestamp=timestamp)

    return hmac.new(authorization_secret, string_for_signature, sha).hexdigest()

def get_params_simple():
    timestamp, nonce = get_timestamp_nonce()
    return {'application_id': application_id,
            'auth_key': authorization_key,
            'timestamp': timestamp,
            'nonce': nonce,
            'signature': create_signature_simple(timestamp, nonce)}

def get_session_token():
    http_headers = {'Content-Type': 'application/json',
                   'QuickBlox-REST-API-Version': '0.1.0'}
    request_path = 'https://api.quickblox.com/session.json'
    json_data = json.dumps(get_params_simple())
    r = requests.post(request_path, data=json_data, headers = http_headers)
    return json.loads(r.text)

def create_user(member):
    token = get_session_token();
    print json.dumps({
                "user": {
                    "password": member.quickblox_password,
                    "login": member.user.username,
                    "email": member.user.email,
                    "external_user_id": member.id,
                    "full_name": member.name+' batata'
                }
            })
    try:
        r = requests.post(
            url="http://api.quickblox.com/users.json",
            headers = {
                "Content-Type":"application/json",
                "QuickBlox-REST-API-Version ":"0.1.0",
                "QB-Token":token['session']['token'],
            },
            data = json.dumps({
                "user": {
                    "password": member.quickblox_password,
                    "login": member.user.username,
                    "email": member.user.email,
                    "external_user_id": member.id,
                    "full_name": member.name
                }
            })
        )
        data = json.loads(r.text)
        member.quickblox_id = data['user']['id']
        return member
    except requests.exceptions.RequestException as e:
        return False