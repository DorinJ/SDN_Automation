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

        bad_name_indexes = []

        # mark bad names
        i = 0
        for cluster in self.clusters:
            try:
                cluster_name = str(cluster.name).split("-")
                if len(cluster_name) == 2:
                    pattern = r'[A-Z]'
                    if re.match(pattern, cluster_name[0]) and len(cluster_name[0]) == 3 and self.name[:3].upper() == cluster_name[0].upper():
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
                bad_name_indexes.append(i)
            i = i + 1

        # delete clusters indicated by bad_name_indexes list
        while len(bad_name_indexes) > 0:
            del self.clusters[bad_name_indexes[0]]
            del bad_name_indexes[0]
            i = 0
            for x in bad_name_indexes:
                bad_name_indexes[i] = x - 1
                i = i + 1
