import ipaddress


from ro_interview_assignment.data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network: ipaddress.IPv4Network, entries: Entry):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.entries = entries

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        ipv4_network = ipaddress.ip_network(self.ipv4_network)
        entries = self.entries

        bad_ip_entry = []

        # mark bad entries and keep only network's IPv4 addresses
        index = 0
        for entry in entries:
            try:
                ip = ipaddress.ip_address(entry.address)
                if not (ip in ipv4_network):
                    raise Exception
            except Exception as e:
                bad_ip_entry.append(index)
            index = index + 1

        # delete bad entries
        while len(bad_ip_entry) > 0:
            del self.entries[bad_ip_entry[0]]
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

        # self.entries = sorted(self.entries)

        # -------------------------------------------------------------------------------------------------------------

        # To be discussed..
        # This method needs to be improved..
        # Working here to avoid circular imports..

        ips = []

        for entry in self.entries:
            ips.append(entry.address)

        ips = sorted(ips, key=lambda ip: [int(ip) for ip in ip.split(".")])

        sorted_entries = {}

        for entry in self.entries:
            ip = entry.address
            index = ips.index(ip)
            sorted_entries[index] = entry

        self.entries = \
            [sorted_entries[key] if key in sorted_entries.keys() else 0 for key in range(len(sorted_entries))]

        # -------------------------------------------------------------------------------------------------------------
