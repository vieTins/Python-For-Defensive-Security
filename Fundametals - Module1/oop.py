from abc import ABC, abstractmethod
class Downloader(ABC): 
    @abstractmethod
    def fetch(self, url:str)-> bytes:
        pass

class HTTPDownloader(Downloader):
    def fetch(self, url):
        return b"HTTP response"

from typing import Protocol
class Runable(Protocol):
    def run(self)->None:
        pass
class Job:
    def run(self):
        print("Job is running")
class Task:
    def run(self):
        print("Task is running")
def start(task: Runable):
    task.run()

job = Job()
task = Task()
start(job)
start(task)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return abs(self.x) + abs(self.y)

    from dataclasses import dataclass
    @dataclass(frozen=True, slots=True)
    class User:
        id:int
        name:str
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    print(user1)
    print(user1 == user2)
