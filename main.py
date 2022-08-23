# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel


# Initialize the app
app = FastAPI()

# GET operation at route '/'
@app.get('/')
async def index():
	return {"greeting" : "server is running!"}


# data model
class Data(BaseModel):
  inputs: dict

# add a new record
@app.post('/data')
async def post_data(data: Data):
	# convert to dictionary
	new_data = data.dict()
	

	# Printing response to console
	count = len(new_data["inputs"])
	print("count: ", count)
	values = new_data['inputs'].values()
	
	if count == 1: # do not reverse
		values = ", ".join(values)
		print(values)
		return values

	elif count == 2: #reverse both values
		values = [i[::-1] for i in values]
		values = values[::-1]
		values = ", ".join(values)
		print(values)
		return values

	elif count%2 == 0: # reverse only middle 2 elements
		itr = 0
		result = []
		for i in values:
			if itr == (count//2) or itr == (count//2)-1:
				result.append(i)
			else:
				result.append(i[::-1])
			itr+=1

		result = result[::-1]
		result = ", ".join(result)
		print(result)
		return result

	else: #reverse only middle element
		itr = 0
		result = []
		for i in values:
			if itr == (count//2):
				result.append(i)
			else:
				result.append(i[::-1])
			itr+=1

		result = result[::-1]
		result = ", ".join(result)
		print(result)
		return result