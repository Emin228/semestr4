import requests


class  ConcreteComponent():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    r = requests.get(url)
    data = r.json()

    def x(cls):
        return cls.data

    def operation(self) -> str:
        return "ConcreteComponent"
    
x = ConcreteComponent().x()
print(x)

