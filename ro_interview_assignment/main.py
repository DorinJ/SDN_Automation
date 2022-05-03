import requests
import ipaddress
import json
import time


from data_structures.datacenter import Datacenter
from data_structures.entry import Entry
from data_structures.network_collection import NetworkCollection


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

    # remove invalid clusters from datacenters
    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()

    # create network collections
    network_collections = []
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            networks_from_cluster = datacenter.clusters[cluster]["networks"]
            for network in networks_from_cluster:
                entry_list = []
                for entry in networks_from_cluster[network]:
                    entry_list.append(Entry(entry["address"], entry["available"], entry["last_used"]))
                network_collections.append(NetworkCollection(network, entry_list))

    # remove invalid records from network_collections
    for network in network_collections:
        network.remove_invalid_records()

    # sort records from network_collections
    for network in network_collections:
        network.sort_records()


if __name__ == '__main__':
    main()
