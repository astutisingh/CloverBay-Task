# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel


# Initialize the app
app = FastAPI()


# GET operation at route '/'
@app.get('/')
async def index():
    return {"greeting": "server is running!"}


# data model
class Data(BaseModel):
    inputs:dict


# add a new record using POST method
@app.post('/data')
async def post_data(data: Data):
    # convert to dictionary
    new_data = data.dict()

    # Count number of elements
    count = len(new_data["inputs"])
    print("count: ", count)

    # Extract values from dictionary
    values = new_data["inputs"].values()

    # Response
    if count == 1:  # do not reverse
        values = ", ".join(values)  # convert list to string
        print(values)
        return values

    elif count == 2:  # reverse both values
        values = [i[::-1] for i in values]  # reverse characters of individual elements
        values = values[::-1]   # reverse list order
        values = ", ".join(values)  # convert list to string
        print(values)
        return values

    elif count % 2 == 0: # reverse only middle 2 elements
        itr = 0
        result = []
        for i in values:
            if itr == (count//2) or itr == (count//2)-1:    # to exclude middle two elements
                result.append(i)
            else:
                result.append(i[::-1])  # reverse characters of individual elements
            itr += 1

        result = result[::-1]   # reverse list order
        result = ", ".join(result)  # convert list to string
        print(result)
        return result

    else:  # reverse only middle element
        itr = 0
        result = []
        for i in values:
            if itr == (count//2):   # to exclude middle element
                result.append(i)
            else:
                result.append(i[::-1])  # reverse characters of individual elements
            itr += 1

        result = result[::-1]   # reverse list order
        result = ", ".join(result)  # convert list to string
        print(result)
        return result
