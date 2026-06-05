import csv
import io
import json
from abc import ABC, abstractmethod
from typing import Any

import requests
import yaml


class Component(ABC):
    """
    Общий интерфейс компонента.
    Все конкретные компоненты и декораторы должны реализовывать operation().
    """

    @abstractmethod
    def operation(self) -> Any:
        pass


class ConcreteComponent(Component):
    """
    Конкретный компонент получает исходные данные с сайта ЦБ РФ
    и возвращает их в виде словаря Python.
    """

    def operation(self) -> dict:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()


class Decorator(Component):
    """
    Базовый декоратор хранит ссылку на объект Component
    и делегирует ему выполнение operation().
    """

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> Any:
        return self._component.operation()


class JsonDecorator(Decorator):
    """
    Декоратор преобразует данные в JSON-строку.
    """

    def operation(self) -> str:
        data = super().operation()
        return json.dumps(data, ensure_ascii=False, indent=4)


class YamlDecorator(Decorator):
    """
    Декоратор преобразует данные в YAML-строку.
    """

    def operation(self) -> str:
        data = super().operation()
        return yaml.safe_dump(data, allow_unicode=True, sort_keys=False)


class CsvDecorator(Decorator):
    """
    Декоратор преобразует данные о валютах в CSV-строку.
    """

    def operation(self) -> str:
        data = super().operation()

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(["Code", "Name", "Nominal", "Value", "Previous"])

        for code, valute in data.get("Valute", {}).items():
            writer.writerow([
                code,
                valute.get("Name", ""),
                valute.get("Nominal", ""),
                valute.get("Value", ""),
                valute.get("Previous", "")
            ])

        return output.getvalue()


def client_code(component: Component) -> None:
    """
    Клиентский код работает с любым объектом через общий интерфейс Component.
    """

    print(component.operation())


if __name__ == "__main__":
    source = ConcreteComponent()

    print("===== JSON =====")
    client_code(JsonDecorator(source))

    print("\n===== YAML =====")
    client_code(YamlDecorator(source))

    print("\n===== CSV =====")
    client_code(CsvDecorator(source))
