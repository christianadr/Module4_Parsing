import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()
jobTitle = []
companyName = []
categories = []
cities = []

for title in root.iter("job_title"):
    jobTitle.append(title.text)

for company in root.iter("company_name"):
    companyName.append(company.text)

# iterating category tags
for category in root.iter("category"):
    categories.append(category.text)

# iterating city tags
for city in root.iter("city"):
    cities.append(city.text)


print(jobTitle)
print(companyName)
print(categories)
print(cities)