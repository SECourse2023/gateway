import requests
import json
import os
import warnings

publicKey = os.environ['DOLINK_PUBLIC_KEY']
privateKey = os.environ['DOLINK_PRIVATE_KEY']
do_url = 'http://39.104.200.8:18010'

def get_request(api_url):
    # Make the API call to receive the message
    response = requests.get(api_url)

    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the message from the response as a JSON object
        message = json.loads(response.content)
        return message

    else:
        print(f"Error: {response.status_code}")

def post_request(api_url, message):
    # Make the API call to receive the message
    response = requests.post(api_url, json=message)

    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the message from the response as a JSON object
        message = json.loads(response.content)
        return message

    else:
        print(f"Error: {response.status_code}")


def read_restful(api_url):
    return get_request(api_url)

def read_doip(api_url):
    result = get_request(api_url)
    assert result['operationId'] == '0.DOIP/Op.Search'
    return result['attributes']


def register_do(message=None):
    if message is None:
        warnings.warn('no message provided, using default message', UserWarning)
        message = dict(test_key='test_value')

    arg = dict(handleValues=message ,sm2KeyPair=dict(publicKey=publicKey, privateKey=privateKey))
    # Define the API endpoint URL
    api_url = do_url +\
            '/BDO?action=callBDO&shortId=GlobalRouter&operation=registerByHTTP&' +\
            f'arg={json.dumps(arg)}'

    message = get_request(api_url)
    assert message['status'] == 'Success'
    return message['result']

def resolve_do(doid):
    api_url = do_url +\
             '/BDO?action=callBDO&shortId=GlobalRouter&operation=resolveByHTTP&arg=' +\
             doid.replace('/', '%2F')

    message = get_request(api_url)
    assert message['status'] == 'Success'
    return message['result']

if __name__ == '__main__':
    register_id = register_do()
    print(f'register_id: {register_id}')
    resolve_result = resolve_do(register_id)
    print(f'resolve_result: {resolve_result}')