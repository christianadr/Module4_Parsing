import json

with open('sample.json', 'r') as jsonFile:
    jsonData = json.load(jsonFile)
    certifications = jsonData['certifications']

    for certificate in certifications:
        # print(certificate['courses'])
        print(json.dumps(certificate['courses'], indent = 1))