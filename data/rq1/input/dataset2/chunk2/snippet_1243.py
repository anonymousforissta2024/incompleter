#Source: https://stackoverflow.com/questions/74549909/bentoml-localhost-server-returns-with-typeerror-runnermethod-object-is-not-ca
import json
from sys import argv

import numpy as np
import requests

SERVICE_URL = "http://localhost:3000/predict"

def make_request_to_bento_service(service_url: str, input_array: np.ndarray) -> str:
    serialized_input_data = json.dumps(input_array.tolist())
    response = requests.post(
        service_url,
        data=serialized_input_data,
        headers={"Content-Type": "application/json"}
        )
    return response.text

def main():
    # Read the data from argv as an np.ndarray
    input_data = np.array([float(x) for x in argv[1:]])
    print(input_data)
    prediction = make_request_to_bento_service(SERVICE_URL, input_data)
    print(prediction)

if __name__ == "__main__":
    main()