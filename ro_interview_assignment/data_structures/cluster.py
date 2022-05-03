from ro_interview_assignment.data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name: str, network_dict: NetworkCollection, security_level: int):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.network_dict -> list(NetworkCollection)
        self.security_level -> int
        """

        self.name = name
        self.network_dict = network_dict
        self.security_level = security_level
