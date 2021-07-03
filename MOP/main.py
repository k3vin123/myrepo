country_and_path = {'Greenland': ['USA'],
                    'USA': ['Sweden', 'Brazil', 'Greenland'],
                    'Sweden': ['USA', 'UK', 'China'],
                    'Brazil': ['USA', 'Spain', 'Argentina'],
                    'UK': ['Sweden', 'Italy'],
                    'Spain': ['Brazil', 'South_Africa'],
                    'Argentina': ['Brazil', 'Australia'],
                    'South_Africa': ['Spain', 'Italy', 'Madagascar'],
                    'Italy': ['UK', 'South_Africa', 'China', 'India'],
                    'China': ['Sweden', 'Italy', 'Russia'],
                    'India': ['Madagascar', 'Australia', 'Russia', 'Italy'],
                    'Madagascar': ['India', 'South_Africa'],
                    'Russia': ['China', 'India'],
                    'Australia': ['India', 'Argentina']}

a = "AR"
b = "AU"

class CountryNode:
    def __init__(self, name="Country", neighbors=None):
        self.name = name
        self.neighbors = neighbors if (neighbors) else list()

