"""

Unit tests - Tests suite

"""


import ipaddress

import pytest

import datetime
import json
import os


from ro_interview_assignment.utils.utils import parse_mocky
from ro_interview_assignment.data_structures.entry import Entry
from ro_interview_assignment.data_structures.datacenter import Datacenter
from ro_interview_assignment.data_structures.network_collection import NetworkCollection
from ro_interview_assignment.data_structures.cluster import Cluster


# @pytest.fixture(scope="session")
def fixture__file_read():
    path = os.path.realpath(__package__)
    json_file = "response.json"
    json_file_path = r"{}\{}".format(path, json_file)

    json_file_content = ""

    with open(json_file_path, encoding="utf-8") as f:
        json_file_content = f.read()

    return json_file_content


def test__module__entry():
    """

    Tests for Entry class

    """

    address = "192.168.2.1"
    available = False
    timestamp = datetime.datetime.now()

    entry = Entry(address, available, timestamp)

    assert isinstance(address, str) is isinstance(entry.address, str)
    assert isinstance(available, bool) is isinstance(entry.available, bool)
    assert isinstance(timestamp, datetime.datetime) is isinstance(entry.last_used, datetime.datetime)


def test__module__network_collection():
    """

    Tests for NetworkCollection class

    - This test assumes that the remove_invalid_records method is validated by assuming that the results from
    network_collections were manually validated against response.json file;
    see ro_interview_assignment/tests/docs/datacenter_collection.png

    - This test assumes that the sort_records method is validated by assuming that the results from
    network_collections were manually validated against response.json file; Entry objects are ordered correctly in
    NetworkCollection.entry, ascending by Entry.address;
    see ro_interview_assignment/tests/docs/datacenter_collection.png

    """

    def fixture_closure(data: dict):
        """

        A closure used as a "fixture".

        :param data: payload
        :return: list of NetworkCollection

        """

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

        return datacenters

    # ------------------------------------------------------------------------------------------------------------------

    # Scenario 1: the response payload has no data

    data_mix = {}

    datacenters = fixture_closure(data_mix)

    assert len(datacenters) == 0

    # ------------------------------------------------------------------------------------------------------------------

    # Scenario 2: the response has mix data

    json_file_content = fixture__file_read()

    data_mix = json.loads(json_file_content)

    datacenters = fixture_closure(data_mix)

    assert len(datacenters) == 2
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                assert isinstance(network, NetworkCollection) is True
                assert isinstance(network.ipv4_network, ipaddress.IPv4Network) is True
                for entry in network.entries:
                    assert isinstance(entry, Entry) is True

    # ------------------------------------------------------------------------------------------------------------------


def test__module__cluster():
    """

    Tests for Cluster class

    """

    name = "BER-1"

    address = "192.168.2.1"
    available = False
    timestamp = datetime.datetime.now()
    entry = Entry(address, available, timestamp)
    ipv4_network = ipaddress.ip_network("192.168.0.0/24")
    network_collection = NetworkCollection(ipv4_network, entry)

    security_level = 1

    cluster = Cluster(name, network_collection, security_level)

    assert isinstance(name, str) is isinstance(cluster.name, str)
    assert isinstance(network_collection, NetworkCollection) is isinstance(cluster.networks, NetworkCollection)
    assert isinstance(security_level, int) is isinstance(cluster.security_level, int)


def test__module__datacenter():
    """

    Tests for Datacenter class

    - This test assumes that the remove_invalid_clusters method is validated by assuming that the results from
    valid_datacenters were manually validated against response.json file;
    see ro_interview_assignment/tests/docs/valid_datacenters.png

    """

    def fixture_closure(data: dict):
        """

        A closure used as a "fixture".

        :param data: payload
        :return: valid datacenters

        """

        datacenters = parse_mocky(data)

        # remove invalid clusters from datacenters
        for datacenter in datacenters:
            datacenter.remove_invalid_clusters()

        return datacenters

    json_file_content = fixture__file_read()

    data_mix = json.loads(json_file_content)

    valid_datacenters = fixture_closure(data_mix)

    assert len(valid_datacenters) == 2
    for datacenter in valid_datacenters:
        assert isinstance(datacenter, Datacenter) is True
        assert isinstance(datacenter.name, str) is True
        for cluster in datacenter.clusters:
            assert isinstance(cluster, Cluster) is True


test__module__entry()

test__module__network_collection()

test__module__cluster()

test__module__datacenter()
