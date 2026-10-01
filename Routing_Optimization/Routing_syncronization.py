# Setting a Depot
import pandas as pd
from ortools.constraint_solver import pywrapcp

# 1. Load your data first!
# Replace 'path_to_your_file.csv' with the actual file path
amravati_waste_dataset = pd.read_csv('amravati_waste_dataset.csv')

# 2. Create the routing index manager
# We use len(amravati_waste_dataset) to get the number of rows/locations
manager = pywrapcp.RoutingIndexManager(len(amravati_waste_dataset), 1, 0)

# 3. Create Routing Model
routing = pywrapcp.RoutingModel(manager)