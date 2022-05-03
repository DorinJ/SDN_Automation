from ro_interview_assignment.data_structures.cluster import Cluster

import re


class Datacenter:
    def __init__(self, name: str, clusters: Cluster):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = clusters

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        bad_names = []

        # mark bad names
        for cluster in self.clusters:
            try:
                cluster_name = str(cluster).split("-")
                if len(cluster_name) == 2:
                    pattern = r'[A-Z]'
                    if re.match(pattern, cluster_name[0]) and len(cluster_name[0]) == 3:
                        pass
                    else:
                        raise Exception
                    pattern = r'[0-9]'
                    if re.match(pattern, cluster_name[1]) and 0 < int(cluster_name[1]) < 1000:
                        pass
                    else:
                        raise Exception
                else:
                    raise Exception
            except Exception as e:
                bad_names.append(cluster)

        # delete clusters indicated by bad_names list
        for key in bad_names:
            del self.clusters[key]
