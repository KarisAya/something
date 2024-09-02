persons = {}
info = []


class Person:
    def __init__(self, sex, name, rank) -> None:
        self.sex: int = sex
        """男0女1"""
        self.name: str = name
        self.rank: int = rank

    def rule(self, func):
        self.rule = func
        global persons
        persons[self.name] = self

    def __repr__(self) -> str:
        return self.name


@Person(1, "妈妈", 0).rule
def _(other: Person) -> bool:
    info.append(f"妈妈 把 {other.name} 榨死了")
    return other.sex == 0


@Person(0, "爸爸", 1).rule
def _(other: Person) -> bool:
    info.append(f"爸爸 把 妹妹 超市了")
    return other.name == "妹妹"


@Person(0, "哥哥", 2).rule
def _(other: Person) -> bool:
    info.append(f"哥哥 把 妹妹 超市了")
    return other.name == "妹妹"


@Person(1, "妹妹", 3).rule
def _(other: Person) -> bool:
    info.append(f"妹妹 把 {other.name} 榨死了")
    return other.name == "哥哥"


@Person(0, "路人", 4).rule
def _(other: Person) -> bool:
    info.append(f"路人 把 {other.name} 橄榄了（悲）")
    return other.name == "哥哥"


type StatusKey = tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], str]


class Status:
    left: tuple[str, ...]
    ship: tuple[str, ...]
    right: tuple[str, ...]
    position: str
    next_status: list["Status"]
    dead: bool = False
    done: bool = False
    last_key: StatusKey | None

    def __init__(
        self,
        key: StatusKey,
        last_key: StatusKey | None = None,
    ) -> None:
        self.key = key
        self.left, self.ship, self.right, self.position = key
        self.next_status = []
        self.last_key = last_key
        self.dead = False

    def check(self):
        for status in self.next_status:
            if status.dead:
                return False
            if status.next_status:
                if all(next_status.dead for next_status in status.next_status):
                    status.dead = True
                    return False
                return status.check()
            return True

    def __repr__(self) -> str:
        return f"{self.left}{self.ship}{self.right} {self.position}"


class Manager:
    current_status: Status
    status_history: dict[StatusKey, Status] = {}
    left: list[Person] = []
    ship: list[Person] = []
    right: list[Person] = []

    position: str

    def __init__(self) -> None:
        self.left = list(persons.values())
        self.position = "left"
        self.record()

    @property
    def status_key(self) -> StatusKey:
        self.left.sort(key=lambda p: p.rank)
        self.ship.sort(key=lambda p: p.rank)
        self.right.sort(key=lambda p: p.rank)

        return tuple(p.name for p in self.left), tuple(p.name for p in self.ship), tuple(p.name for p in self.right), self.position

    def record(self):
        key = self.status_key
        if key in self.status_history:
            self.current_status = self.status_history[key]
        else:
            status = Status(key)
            try:
                self.current_status.next_status.append(status)
                status.last_key = self.current_status.key
            except Exception as e:
                print(e)
            self.status_history[key] = self.current_status = status

    @staticmethod
    def rule(a: Person, b: Person):
        return a.rule(b) or b.rule(a)

    def rule_check(self):
        if len(self.left) == 2 and self.rule(*self.left):
            return False
        if len(self.ship) == 2 and self.rule(*self.ship):
            return False
        if len(self.right) == 2 and self.rule(*self.right):
            return False
        return True

    def back_status(self):
        for status in self.status_history.values():
            if status.done:
                continue
            if status.check():
                self.left = [persons[name] for name in status.left]
                self.ship = [persons[name] for name in status.ship]
                self.right = [persons[name] for name in status.right]
                self.position = status.position
                self.current_status = status
                if self.position == "left":
                    self.right.extend(self.ship)
                    self.position = "right"
                else:
                    self.left.extend(self.ship)
                    self.position = "left"
                self.ship.clear()
                print("Back To", self.current_status)
                return
        raise Exception("No solution")

    def action(self):
        info.clear()
        if self.position == "left":
            self.position = "right"
            side = self.right
        else:
            self.position = "left"
            side = self.left
        if len(self.ship) == 1 and self.ship[0].name == "妹妹":
            info.append("妹妹 划船累死了")
            side.extend(self.ship)
            self.current_status.dead = True
            return

        if (
            (len(self.ship) == 2 and self.rule(*self.ship))
            or (len(self.left) == 2 and self.rule(*self.left))
            or (len(self.right) == 2 and self.rule(*self.right))
        ):
            side.extend(self.ship)
            self.current_status.dead = True
            return

        side.extend(self.ship)
        if len(side) == 2 and self.rule(*side):
            self.current_status.dead = True
            return

    def show(self):
        print(self.current_status.key)


manager = Manager()


class Done(Exception): ...


while True:
    try:
        if manager.position == "left":
            side = manager.left
        else:
            side = manager.right

        len_side = len(side)

        for i in range(len_side):
            manager.ship = [side[i]]
            side.pop(i)
            status_key = manager.status_key
            side.insert(i, manager.ship[0])
            if status_key in manager.status_history:
                continue
            manager.current_status.next_status.append(Status(status_key, last_key=manager.current_status.key))

        if len_side > 1:

            for i in range(len_side):
                ship = [side[i], None]
                side.pop(i)
                for j in range(i, len_side - 1):
                    ship[1] = side[j]
                    side.pop(j)
                    manager.ship = ship
                    status_key = manager.status_key
                    side.insert(j, ship[1])
                    if status_key in manager.status_history:
                        continue
                    manager.current_status.next_status.append(Status(status_key, last_key=manager.current_status.key))
                side.insert(i, ship[0])

        for i in range(len_side):
            manager.ship = [side[i]]
            side.pop(i)
            status_key = manager.status_key
            if status_key in manager.status_history:
                side.insert(i, manager.ship[0])
                continue
            manager.record()
            raise Done
        else:
            if len_side > 1:
                for i in range(len_side):
                    ship = [side[i], None]
                    side.pop(i)
                    for j in range(i, len_side - 1):
                        ship[1] = side[j]
                        side.pop(j)
                        manager.ship = ship
                        status_key = manager.status_key
                        if status_key in manager.status_history:
                            side.insert(j, ship[1])
                            continue
                        manager.record()
                        raise Done
                    side.insert(i, ship[0])
            manager.current_status.done = True
            manager.back_status()
            if manager.position == "left":
                manager.right.extend(manager.ship)
            else:
                manager.left.extend(manager.ship)
            manager.ship.clear()

            continue

    except Done:
        manager.action()
        manager.show()
        if manager.current_status.dead:
            print(f"Dead！{info[-1]}")
            manager.back_status()

            continue
        if not manager.left:
            status = manager.current_status
            print("Done！")
            while status.last_key != None:
                print(status)
                status = manager.status_history[status.last_key]

            raise Done("WIN")
