from ro_interview_assignment.data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name: str, cluster_dict: Cluster):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.cluster_dict = cluster_dict

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        pass
