import ipaddress


class NetworkCollection:
    def __init__(self, ipv4_network: ipaddress.IPv4Network, raw_entry_list: list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.raw_entry_list = raw_entry_list

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        ipv4_network = ipaddress.ip_network(self.ipv4_network)
        raw_entry_list = self.raw_entry_list

        bad_ip_entry = []

        # mark bad entries and keep only network's IPv4 addresses
        index = 0
        for entry in raw_entry_list:
            try:
                ip = ipaddress.ip_address(entry["address"])
                if not (ip in ipv4_network):
                    raise Exception
            except Exception as e:
                bad_ip_entry.append(index)
            index = index + 1

        # delete bad entries
        while len(bad_ip_entry) > 0:
            del raw_entry_list[bad_ip_entry[0]]
            del bad_ip_entry[0]
            i = 0
            for x in bad_ip_entry:
                bad_ip_entry[i] = x - 1
                i = i + 1

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
