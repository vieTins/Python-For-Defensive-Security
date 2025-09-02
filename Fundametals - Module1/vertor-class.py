from dataclasses import dataclass

@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __iter__(self):
        yield self.x
        yield self.y

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1)
print(v1 + v2)
print(v1 - v2)
print(abs(v1))

x, y = v1
print(x, y)


s = {v1, v2}
print(s)
