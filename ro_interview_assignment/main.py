import requests
import json
import time

from data_structures.datacenter import Datacenter


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.

    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    data = {}

    trial = 0

    while True:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception
            else:
                data = json.loads(response.text)
                return data
        except Exception as e:
            if trial + 1 > max_retries - 1:
                return data
            trial = trial + 1
            time.sleep(delay_between_retries)


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    pass  # the rest of your logic here


if __name__ == '__main__':
    main()
