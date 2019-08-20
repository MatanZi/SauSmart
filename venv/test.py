'''
This code demonstrates a simple HTTP endpoint that receives an Ubidots token
and a temperature value as URL parameters, then uses this data to make an
HTTP POST request to Ubidots API.

If you set the UbiFunction Method to GET, you can build a URL as explained below, and paste it into your web browser to
test the function. Example:

https://parse.ubidots.com/{your-function-URL}/?token={YOUR-TOKEN}&device=sample-function&temperature=45

Example by: Jose García, developer at @Ubidots
'''

import requests
import time

BASE_URL = "https://industrial.api.ubidots.com"

REQUESTS_FUNCTIONS = {"get": requests.get, "post": requests.post}


def main(args):
    '''
    Main function - runs every time the function is executed.
    "args" is a dictionary containing both the URL params and the HTTP body (for POST requests).
    '''
    token = args.get('token', None)
    device = args.get('device', None)

    if token is None or device is None:
        print("[ERROR] Please send your Ubidots Token and device label to update in your args")
        return {"status": "error"}

    del args['token']
    del args['device']

    # Log the payload to the console, for debugging purposes. You may access the function's logs using
    # the option in the above header.

    print("[INFO] Payload to send: {}".format(args))

    # Use the remaining parameters as payload
    req = update_device(device, args, token)

    # Prints the request result

    print("[INFO] Request result:")
    print(req.text)

    return {"status": "Ok", "result": req.json()}


def update_device(device, payload, token):
    """
    updates a variable with a single dot
    """

    url = "{}/api/v1.6/devices/{}".format(BASE_URL, device)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    req = create_request(url, headers, payload, attempts=5, request_type="post")

    return req


def create_request(url, headers, data, attempts, request_type):
    """
    Function to create a request to the server
    """

    request_func = REQUESTS_FUNCTIONS.get(request_type)

    kwargs = {"url": url, "headers": headers}

    if request_type == "post":
        kwargs["json"] = data

    try:
        req = request_func(**kwargs)
        print("[INFO] Request result: {}".format(req.text))
        status_code = req.status_code
        time.sleep(1)

        while status_code >= 400 and attempts < 5:
            req = request_func(**kwargs)
            print("[INFO] Request result: {}".format(req.text))
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        return req
    except Exception as e:
        print("[ERROR] There was an error with the request, details:")
        print(e)
        return None


if __name__ == '__main__':
        main(mqtt_client, ketchup)