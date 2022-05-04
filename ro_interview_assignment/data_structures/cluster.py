from ro_interview_assignment.data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name: str, networks: NetworkCollection, security_level: int):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.networks -> list(NetworkCollection)
        self.security_level -> int
        """

        self.name = name
        self.networks = networks
        self.security_level = security_level
