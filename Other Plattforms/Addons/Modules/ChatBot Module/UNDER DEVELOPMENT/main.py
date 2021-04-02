# import the module
from prsaw import RandomStuff

# initiate the object
rs = RandomStuff()

# get a response from an endpoint
response =  rs.get_ai_response("How are you?")
print(response)

# close the object once done (recommended)
rs.close()