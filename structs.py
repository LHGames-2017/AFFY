import math

class ActionTypes():
    DefaultAction, MoveAction, AttackAction, CollectAction, UpgradeAction, StealAction, PurchaseAction = range(7)


class UpgradeType():
    CarryingCapacity, AttackPower, Defence, MaximumHealth, CollectingSpeed = range(5)


class TileType():
    Tile, Wall, House, Lava, Resource, Shop = range(6)


class TileContent():
    Empty, Resource, House, Player, Wall, Lava, Shop = range(7)


class Point(object):

    # Constructor
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    # Overloaded operators
    def __add__(self, point):
        return Point(self.X + point.X, self.Y + point.Y)

    def __sub__(self, point):
        return Point(self.X - point.X, self.Y - point.Y)

    def __str__(self):
        return "{{{0}, {1}}}".format(self.X, self.Y)

    def __hash__(self):
        return hash((self.X, self.Y))

    def __eq__(self, other):
        return (self.X, self.Y) == (other.X, other.Y)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    # Distance between two Points
    def MahanttanDistance(self, p2):
        delta_x = abs(self.X - p2.X)
        delta_y = abs(self.Y - p2.Y)
        return delta_x + delta_y

    def EulerDistance(self, p2):
        delta_x = abs(self.X - p2.X)
        delta_y = abs(self.Y - p2.Y)
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))


class GameInfo(object):

    def __init__(self):
        self.HouseLocation = None
        self.Map  = None
        self.Players = dict()
        self.Shop = list()
        self.Resources = list()
        self.Lava = list()
        self.Wall = list()
        self.Empties = list()

        # nearest
        self.nearestResource = None
        self.nearestPlayer = None

    def addResource(self, point):
        if point not in self.Resources:
            self.Resources.append(point)

    def addShop(self, point):
        if point not in self.Shop:
            self.Shop.append(point)

    def addWall(self, point):
        if point not in self.Wall:
            self.Wall.append(point)

    def clean(self):
        self.Lava = list()
        self.Players = dict()
        self.Empties = list()


    def addLava(self, point):
        self.Lava.append(point)

    def addEmpty(self, point):
        self.Empties.append(point)

    def addPlayer(self, position, playerInfo):
        self.Players[position] = playerInfo

    def findNearestResource(self, position):
        dist = 40
        for point in self.Resources:
            if position.MahanttanDistance(point) < dist:
                self.nearestResource = point
                dist = position.MahanttanDistance(point)
        return self.nearestResource

    def findNearestPlayer(self, position):
        dist = 40
        for (point, playerInfo) in self.Players:
            if position.MahanttanDistance(point) < dist:
                self.nearestPlayer = (point, playerInfo)
                dist = position.MahanttanDistance(point)

        return self.nearestPlayer


class Tile(object):

    def __init__(self, content=None, x=0, y=0):
        self.Content = content
        self.X = x
        self.Y = y


class Player(object):

    def __init__(self):
        self.Health = 0
        self.MaxHealth = 0
        self.Position = 0
        self.Defense = 0
        self.AttackPower = 0
        self.Score = 0
        self.CarriedRessources = 0
        self.CarryingCapacity = 0

    def Update(self, health, maxHealth, position, score, defense, attackPower, carriedRessources,
                 carryingCapacity=1000):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position
        self.Defense = defense
        self.AttackPower = attackPower
        self.Score = score
        self.CarriedRessources = carriedRessources
        self.CarryingCapacity = carryingCapacity


class PlayerInfo(object):

    def __init__(self, health, maxHealth, position, attackPower, defense, carriedRessources):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position
        self.Defense = defense
        self.AttackPower = attackPower
        self.CarriedRessources = carriedRessources

class ActionContent(object):

    def __init__(self, action_name, content):
        self.ActionName = action_name
        self.Content = str(content)
