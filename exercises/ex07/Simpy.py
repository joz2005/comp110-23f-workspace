"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730655251"


class Simpy:

    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, list_call: list[float]):
        self.values = list_call

    def __str__(self) -> str:
        return f"Simpy({self.values})"
    
    def fill(self, fill_values: float, max_fills: int) -> None:

        new_list: list[float] = []

        for index in range(max_fills):
            new_list.append(fill_values)

        self.values = new_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        
        new_list: list[float] = [start]

        assert step != 0

        for x in range(int((stop - start) / step - 1)):
            new_list.append(new_list[-1] + step)

        self.values = new_list

    def sum(self) -> float:
        return sum(self.values)
    
    def __add__(self, addition: Simpy | float) -> Simpy:

        new_list: list[float] = []

        if type(addition) == float:
            print(new_list)
            for x in range(len(self.values)):
                new_list.append(self.values[x] + addition)
        else:
            for x in range(len(self.values)):
                new_list.append(self.values[x] + addition.values[x])

        return new_list

    def __pow__(self, exponent: Simpy | float) -> Simpy:
        new_list: list[float] = []

        if type(exponent) == float:
            for x in range(len(self.values)):
                new_list.append(self.values[x] ** exponent)
        else:
            for x in range(len(self.values)):
                new_list.append(self.values[x] ** exponent.values[x])

        return new_list
    
    def __eq__(self, equals: Simpy | float) -> list[bool]:

        bool_list: list[bool] = []

        if type(equals) == float:
            for x in range(len(self.values)):
                if self.values[x] != equals:
                    bool_list.append(False)
                else:
                    bool_list.append(True)
        else:
            for x in range(len(equals.values)):
                if equals.values[x] != self.values[x]:
                    bool_list.append(False)
                else:
                    bool_list.append(True)

        return bool_list

    def __gt__(self, greater_than: Simpy | float) -> list[bool]: 
        bool_list: list[bool] = []

        if type(greater_than) == float:
            for x in range(len(self.values)):
                if self.values[x] <= greater_than:
                    bool_list.append(False)
                else:
                    bool_list.append(True)
        else:
            for x in range(len(self.values)):
                if self.values[x] <= greater_than.values[x]:
                    bool_list.append(False)
                else:
                    bool_list.append(True)

        return bool_list
    
    def __getitem__(self, rhs: int | list[float]) -> float | Simpy:

        if type(rhs) == int:
            return self.values[rhs]
        else: 
            return Simpy([self.values[index] for index in range(len(self.values)) if rhs[index]])

ones = Simpy([1., 1., 1., 1., 1.])
print(ones.values)
print(ones)

twos = Simpy([])
twos.fill(2.0, 3)
print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0])") 
twos.fill(2.0, 5)
print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0, 2.0, 2.0])")

mixed = Simpy([])
mixed.fill(3.0, 3)
print("Actual: ", mixed, " - Expected: Simpy([3.0, 3.0, 3.0])")
mixed.fill(2.0, 2)
print("Actual: ", mixed, " - Expected: Simpy([2.0, 2.0])")

positive = Simpy([])
positive.arange(1.0, 5.0)
print("Actual: ", positive, " - Expected: Simpy([1.0, 2.0, 3.0, 4.0])")

fractional = Simpy([])
fractional.arange(0.0, 1.0, 0.25)
print("Actual: ", fractional, " - Expected: Simpy([0.0, 0.25, 0.5, 0.75])")

negative = Simpy([])
negative.arange(-1.0, -5.0, -1.0)
print("Actual: ", negative, " - Expected: Simpy([-1.0, -2.0, -3.0, -4.0])")

ones = Simpy([1.0, 1.0, 1.0])
print("Actual: ", ones.sum(), " - Expected: 3.0")

one_to_nine = Simpy([])
one_to_nine.arange(1.0, 10.0)
print("Actual: ", one_to_nine.sum(), " - Expected: 45.0")

a = Simpy([1.0, 1.0, 1.0])
b = Simpy([2.0, 3.0, 4.0])
c = a + b
print("Actual: ", c, " - Expected: Simpy([3.0, 4.0, 5.0])")
print("Actual: ", a + a, " - Expected: Simpy([2.0, 2.0, 2.0])")
print("Actual: ", b + b, " - Expected: Simpy([4.0, 6.0, 8.0])")


a = Simpy([1.0, 2.0, 3.0])
b = a + 10.0
print("Actual: ", b, " - Expected: Simpy([11.0, 12.0, 13.0])")
print("Actual: ", a + 1.0, " - Expected: Simpy([2.0, 3.0, 4.0])")

a = Simpy([2.0, 2.0, 2.0])
b = Simpy([1.0, 2.0, 3.0])
c = a ** b
print("Actual: ", c, " - Expected: Simpy([2.0, 4.0, 8.0])")
print("Actual: ", a ** a, " - Expected: Simpy([4.0, 4.0, 4.0])")
print("Actual: ", b ** b, " - Expected: Simpy([1.0, 4.0, 27.0])")

a = Simpy([1.0, 2.0, 3.0])
b = a ** 2.0
print("Actual: ", b, " - Expected: Simpy([1.0, 4.0, 9.0])")
print("Actual: ", a ** 3.0, " - Expected: Simpy([1.0, 8.0, 27.0])")

simpy_instance: Simpy = Simpy([])
simpy_instance.fill(2, 16)

exponential_simpy: Simpy = Simpy([])
exponential_simpy.arange(0, 16)

simpy_instance = simpy_instance ** exponential_simpy

print(simpy_instance)

a = Simpy([1.0, 2.0, 3.0, 4.0])
b = Simpy([1.0, 2.0, 1.0, 4.0])
c = a == b
print("Actual: ", c, " - Expected: [True, True, False, True]")
print("Actual: ", a == a, " - Expected: [True, True, True, True]")

a = Simpy([1.0, 2.0, 1.0, 4.0])
b = a == 1.0
print("Actual: ", b, " - Expected: [True, False, True, False]")
print("Actual: ", a == 2.0, " - Expected: [False, True, False, False]")

a = Simpy([1.0, 2.0, 3.0, 4.0])
b = Simpy([2.0, 1.0, 1.0, 5.0])
c = a > b
print("Actual: ", c, " - Expected: [False, True, True, False]")
print("Actual: ", b > a, " - Expected: [True, False, False, True]")

a = Simpy([1.0, 2.0, 3.0, 4.0])
b = a > 2.0
print("Actual: ", b, " - Expected: [False, False, True, True]")
print("Actual: ", a > 3.0, " - Expected: [False, False, False, True]")

a = Simpy([10.0, 20.0, 30.0])
print("Actual: ", a[0], " - Expected: 10.0")
print("Actual: ", a[1], " - Expected: 20.0")
print("Actual: ", a[2], " - Expected: 30.0")

a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
b = a[a > 2.0]
print("Actual: ", b, " - Expected: Simpy([3.0, 4.0])")
print(a + 1.0 == 2.0)
print("Actual: ", a[a + 1.0 == 2.0], " - Expected: Simpy([1.0, 1.0])")