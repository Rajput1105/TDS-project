import requests

url = "https://tds-project-8yyq483gz-rahul-s-projects-721ebf0e.vercel.app/api/"
files = {"file": open("./tests/q-compare-files.zip", "rb")}
data = {"question": "extract the data ?"}

response = requests.post(url,  data=data)

print(response.text)