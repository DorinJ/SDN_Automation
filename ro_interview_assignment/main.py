import requests
import ipaddress
import json
import time
import datetime


from data_structures.datacenter import Datacenter
from data_structures.entry import Entry
from data_structures.network_collection import NetworkCollection
from data_structures.cluster import Cluster


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


def parse_mocky(data):

    def parse_entry(address: str, available: str, last_used: str):
        address = address
        available = bool(available)
        last_used = datetime.datetime.strptime(last_used, "%d/%m/%y %H:%M:%S")

        entry = Entry(address, available, last_used)

        return entry

    datacenters_data = []

    datacenters_location = list(data.keys())

    for datacenter in datacenters_location:
        datacenter_name = datacenter
        datacenter_clusters = data[datacenter_name]

        network_clusters = []

        for cluster in datacenter_clusters:
            cluster_name = cluster
            cluster_networks = datacenter_clusters[cluster]["networks"]
            cluster_security = datacenter_clusters[cluster]["security_level"]

            network_collections = []

            # append network collections
            for network in cluster_networks:
                network_address = network
                network_entries = cluster_networks[network_address]
                network_entries_ = []

                # append network entries
                for network_entry in network_entries:
                    address = network_entry["address"]
                    available = network_entry["available"]
                    last_used = network_entry["last_used"]

                    entry = parse_entry(address, available, last_used)
                    network_entries_.append(entry)

                network_collection = NetworkCollection(ipaddress.ip_network(network_address), network_entries_)
                network_collections.append(network_collection)

            cluster = Cluster(cluster_name, network_collections, cluster_security)
            network_clusters.append(cluster)

        datacenters_data.append(Datacenter(datacenter_name, network_clusters))

    return datacenters_data


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = parse_mocky(data)

    # remove invalid clusters from datacenters
    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()

    # remove invalid records from cluster's networks
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                network.remove_invalid_records()

    # sort records in cluster's networks
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                network.sort_records()


if __name__ == '__main__':
    main()
