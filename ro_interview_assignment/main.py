from ro_interview_assignment.utils.utils import parse_mocky
from ro_interview_assignment.utils.utils import get_data


def main():
    """
    Main entry to our program.
    """

    url = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"

    data = get_data(url)

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
