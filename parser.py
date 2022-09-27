import json
from datetime import datetime

# Output Variables
today = datetime.today().strftime('%d/%m-%Y')
numberOfWorkspaces = 0
numberOfAPIs = 0
numberOfAPIsWithConnections = 0
numberOfConnections = 0
numberOfUniqueOwners = 0
uniqueOwners = []
uniqueAsyncOwners = []
numberOfOpenAPIs = 0
numberOfGraphQLs = 0
numberOfAsyncAPIs = 0

# Raw
f = open('amma-data.json')
data = json.load(f)

# Insight
for workspace in data:
    numberOfWorkspaces+=1
    for api in workspace["apis"]:
        connections = len(api["connections"])
        if connections > 0:
            numberOfConnections+=connections
            numberOfAPIsWithConnections+=1
        for spec in api["specifications"]:
            print("API", api["name"], spec["type"] )
            numberOfAPIs+=1
            if spec["type"] == "OpenAPI":
                numberOfOpenAPIs+=1
            if spec["type"] == "GraphQL":
                numberOfGraphQLs+=1
            if spec["type"] == "AsyncAPI":
                numberOfAsyncAPIs+=1
                for owner in workspace["owners"]:
                    owner = owner.lower()
                    if not owner in uniqueAsyncOwners:
                        uniqueAsyncOwners.append(owner)
    for owner in workspace["owners"]:
        owner = owner.lower()
        if not owner in uniqueOwners:
            uniqueOwners.append(owner)

# Finalize
f.close()

# Output
print("Number of APIs", numberOfAPIs)

