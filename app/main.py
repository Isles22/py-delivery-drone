from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        super().__init__(weight)
        self.name = name
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] = self.coords[1] + step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] = self.coords[1] - step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] = self.coords[0] + step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] = self.coords[0] - step

    def get_info(self) -> str:
        return (f"Robot: {self.name}, Weight: {self.weight}")


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if self.coords == [0, 0] or \
            self.coords is None else coords

    def go_up(self, go: int = 1) -> None:
        self.coords[2] = self.coords[2] + go

    def go_down(self, go: int = 1) -> None:
        self.coords[2] = self.coords[2] - go


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None) and (
                cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
