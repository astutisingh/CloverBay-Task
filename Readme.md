# Clover Bay Technologies Task

## Problem
Create an API which should accept the following JSON as input (request parameter)
```
{
"input1": "Clark Kent",
"input2": "Bruce Wayne",
"input3": "Diana Prince"
}
```

The response should be a plain string : stating:
`" ecnirP anaiD, Bruce Wayne, tneK kralC "`

( There are odd number of input, hence the middle one will not be reversed. If there are even then the 2 entries in middle will not be reversed.
If there is 1 json element, then do NOT reverse it's value. If there are 2 then reverse both values)

---

## Solution
I have solved this problem using FASTAPI in Python and used uvicorn for server.

### Install Requirements
`pip install -r requirements.txt`

### Run server
`uvicorn main:app --reload`

### Usage
In any Browser open `http://localhost:8000/docs`

### Testing API in Postman
- URL: `http://localhost:8000/data`
- Data Format:
  ```
  {
    "inputs":{
    
    }
  }
  ```
