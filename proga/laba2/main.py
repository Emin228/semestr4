import requests
import yaml
import csv
import io

from abc import ABC, abstractmethod
class Component(ABC):
    """
    Базовый интерфейс Компонента определяpip install PyYAMLет поведение,
    которое изменяется декораторами.
    """
    @abstractmethod
    def operation(self):
        pass



class  ConcreteComponent(Component):
    def operation(self) -> dict:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        r = requests.get(url)
        return r.json()
        
    

class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self):
        return self._component.operation()


class YamlDecorator(Decorator):
    def operation(self) -> str:
        data  = super().operation()
        return yaml.dump(data, allow_unicode=True)
    
class CsvDecorator(Decorator):
    def operation(self) -> str:
        data = super().operation()
        output = io.StringIO()
        writer = csv.writer(output)

        # заголовки
        writer.writerow(["Currency", "Value"])

        # данные (пример: Valute)
        for code, val in data["Valute"].items():
            writer.writerow([code, val["Value"]])

        return output.getvalue()


def client_code(component: Component) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с
    которыми работает.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")
    
simple = ConcreteComponent()
print("Client: I've got a simple component:")
client_code(simple)

print("\n")