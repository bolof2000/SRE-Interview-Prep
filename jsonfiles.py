import json

def getJSON(filepath):
	with open(filepath,'r') as files:
		return json.loads(files)


readJson = getJSON('employee.json')
print(readJson.get("userId",""))