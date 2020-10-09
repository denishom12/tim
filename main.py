from multiprocessing import Queue
from threading import Thread
from multiprocessing import Process
import threading
import time


class CarDriver:
    FuelClass: int
    Money: int

    def __init__(self, fuel,m):
        self.FuelClass = fuel
        self.Money = m

    def stay(self):
        print("Машина остановлена")

    def go(self):
        print("Машина едет")

    def turnOfTheEngine(self):
        print("Двигатель заглушен")

    def openFuel(self):
        print("Лючок бака открыт")

    def pay(self):
        print("Оплатить", self.Money)
        return self.Money


class RefuelingStation:
    CashBox: int
    FuelDispenser: int

    def __init__(self, cash, fuel):
        self.CashBox = cash
        self.FuelDispenser = fuel

    def dispenser(self, fuel, pistol, col):
        if RefuelingStation.FuelDispenser == 1:
            print("Автомобиль заправляется", fuel, pistol, col)


class GasStation(RefuelingStation):
    FuelClass = []
    FuelPistol = []
    Status: int

    def __init__(self, fclass, pistol, dispenser, status):
        self.FuelClass = fclass
        self.FuelPistol = pistol
        self.FuelDispenser = dispenser
        self.Status = status

    def checkst(self):
        if self.Status == 0:
            return 0
        if self.Status == 1:
            return 1


class Refuels:
    name: str


class RefuelsClass1(Refuels, RefuelingStation):
    def __init__(self, name):
        self.name = name

    def acceptPayment(self, cash):
        print("Оплата принята")
        RefuelingStation.CashBox =+ cash

    def releaseFuel(self, a):
        RefuelingStation.FuelDispenser = a


class RefuelsClass2(Refuels, GasStation):
    def __init__(self, name):
        self.name = name

    def insertFuelGun(self, pistol):
        print("Пистолет вставлен", pistol)

    def takeOutFuelGun(self, pistol):
        print("Пистолет извлечен", pistol)


def all1(a1, b1, g1, g2, g3):
    print("her")
    car_1 = CarDriver(a1, b1)
    refst_1 = RefuelingStation(500, 0)

    gas_1 = g1
    gas_2 = g2
    gas_3 = g3

    ref_1 = RefuelsClass1("Ivan")
    ref_2 = RefuelsClass2("Leon")
    flag = 0
    flag2 = 0
    flag3 = 0

    for i in range(2):
        if gas_1.FuelClass[i] == car_1.FuelClass:
            flag = 1
        elif gas_2.FuelClass[i] == car_1.FuelClass:
            flag2 = 1
        elif gas_3.FuelClass[i] == car_1.FuelClass:
            flag3 = 1
    if gas_1.Status == 0 and flag == 1:
        print("Тут свободно, 1 станция")
        car_1.stay()
        car_1.turnOfTheEngine()
        car_1.openFuel()
        gas_1.Status = 1
        print("ZANATOOOO")
        time.sleep(6)

        for i in range(2):
            if car_1.FuelClass == gas_1.FuelClass[i]:
                flag1 = i
                i = 5
        pistol = gas_1.FuelPistol[flag1]
        ref_2.insertFuelGun(pistol)
        m = car_1.pay()
        ref_1.acceptPayment(m)
        ref_1.releaseFuel(1)
        refst_1.dispenser(car_1.FuelClass, pistol, 1)
        ref_2.takeOutFuelGun(pistol)
        car_1.go()

    elif gas_2.Status == 0 and flag2 == 1:
        print("Тут свободно, 2 станция")
        car_1.stay()
        car_1.turnOfTheEngine()
        car_1.openFuel()
        gas_2.Status = 1
        time.sleep(6)

        for i in range(2):
            if car_1.FuelClass == gas_2.FuelClass[i]:
                flag1 = i
                i = 5
        pistol = gas_2.FuelPistol[flag1]
        ref_2.insertFuelGun(pistol)
        m = car_1.pay()
        ref_1.acceptPayment(m)
        ref_1.releaseFuel(1)
        refst_1.dispenser(car_1.FuelClass, pistol, 1)
        ref_2.takeOutFuelGun(pistol)
        car_1.go()

    elif gas_3.Status == 0 and flag3 == 1:
        print("Тут свободно, 3 станция")
        car_1.stay()
        car_1.turnOfTheEngine()
        car_1.openFuel()
        gas_3.Status = 1
        time.sleep(6)

        for i in range(2):
            if car_1.FuelClass == gas_3.FuelClass[i]:
              flag1 = i
              i = 5
        pistol = gas_3.FuelPistol[flag1]
        ref_2.insertFuelGun(pistol)
        m = car_1.pay()
        ref_1.acceptPayment(m)
        ref_1.releaseFuel(1)
        refst_1.dispenser(car_1.FuelClass, pistol, 1)
        ref_2.takeOutFuelGun(pistol)
        car_1.go()


def writer(a, b, g1, g2, g3, event_for_wait, event_for_set):
    event_for_wait.wait()  # wait for event
    event_for_wait.clear()
    print("WRITE")
    a = int(input("Класс топлива"))
    b = int(input("Сумма"))
    all1(a, b, g1, g2, g3)
    event_for_set.set()


g1 = GasStation([95, 00], [1, 2], 0, 0)
g2 = GasStation([92, 92], [1, 2], 0, 0)
g3 = GasStation([95, 00], [1, 2], 0, 0)


while 1:
    k1 = g1.checkst()
    k2 = g2.checkst()
    k3 = g3.checkst()

    if k1 == 0:
        g1.Status = 0
    else:
        g1.Status = 1

    if k2 == 0:
        g2.Status = 0
    else:
        g2.Status = 1

    if k3 == 0:
        g3.Status = 0
    else:
        g3.Status = 1

    a = 0
    b = 0
    e1 = threading.Event()
    e2 = threading.Event()
    e3 = threading.Event()

    t1 = threading.Thread(target=writer, args=(a, b, g1, g2, g3, e1, e2))
    t2 = threading.Thread(target=writer, args=(a, b, g1, g2, g3, e2, e3))
    t3 = threading.Thread(target=writer, args=(a, b, g1, g2, g3, e3, e1))

    t1.start()
    t2.start()
    t3.start()

    e1.set()

    t1.join()
    t2.join()
    t3.join()

    g1.Status = 0
    g2.Status = 0
    g3.Status = 0

