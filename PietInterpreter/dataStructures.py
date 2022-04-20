import copy
from .tokens import BaseLexerToken

class position():
    """
    A coords is a tuple of x and y coordinates
    """
    def __init__(self, newPosition: tuple[int, int]):
        self.coords = newPosition

    def __str__(self):
        return "{}".format(self.coords)

    def __repr__(self):
        return str(self)

    def __deepcopy__(self, memodict):
        return position(copy.deepcopy(self.coords))

    # Functions to allow this datatype to behave in sets
    def __hash__(self):
        return hash(self.coords)

    def __eq__(self, other):
        return other.coords == self.coords

    def __ne__(self, other):
        return not self == other


class Direction():
    """
    A direction is made up of a Direction Pointer (DP) at .pointers[0] and a Codel Chooser (CC) at .pointers[1].
    """
    def __init__(self, newPointers: tuple[int, int]):
        self.pointers = newPointers

    def __str__(self):
        return "{}".format(self.pointers)

    def __repr__(self):
        return "{}".format(self.pointers)

    def __deepcopy__(self, memodict):
        return Direction(copy.deepcopy(self.pointers))

    # Functions to allow this datatype to behave in sets
    def __eq__(self, other):
        return self.pointers == other.pointers

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.pointers)

class Codel():
    """
    A codel is a set of positions adjacent to each other and with the same color as each other
    """
    def __init__(self, newCodel: set[position]):
        self.codel = newCodel

    def __str__(self):
        return "{}".format(self.codel)

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return Codel(copy.copy(self.codel))

    # Functions to allow this datatype to behave in sets
    def __hash__(self):
        # Return a hash of a frozenset, because a normal set can't be hashed
        return hash(frozenset(self.codel))

    def __eq__(self, other):
        return other.codel == self.codel

    def __ne__(self, other):
        return not self == other

class Edge():
    """
    The edge contains a position and direction (DP and CC)
    """
    def __init__(self, newEdge: tuple[position, Direction]):
        self.edge = newEdge

    def __str__(self):
        return "{}".format(self.edge)

    def __repr__(self):
        return str(self)


class GraphNode():
    """
    The key to the token and coords is a direction
    """
    def __init__(self, newNode: dict[Direction, tuple[BaseLexerToken, position]]):
        self.graphNode = newNode

    def __str__(self):
        return "{}".format(self.graphNode)

    def __repr__(self):
        return str(self)


class Graph():
    """
    Each codel has a node of directions and tokens associated with those directions (and where the edge will start)
    """
    def __init__(self, newGraph: dict[Codel, GraphNode]):
        self.graph = newGraph

    def __str__(self):
        return "{}".format(self.graph)

    def __repr__(self):
        return str(self)

class ProgramState():
    """
    The program state contains the graph of the program, the position, direction and stack.
    """
    def __init__(self, newGraph:  Graph, newPosition: position, newDirection: Direction, dataStack: list[int] = None):
        if dataStack is None:
            dataStack = []

        self.graph = newGraph
        self.position = newPosition
        self.direction = newDirection
        self.dataStack = dataStack

    def __str__(self):
        return "Pos:{pos} / {pointers}. Stack: {stack}".format(pos=self.position, pointers=self.direction, stack=self.dataStack)

    def __repr__(self):
        return str(self)

    def __deepcopy__(self, memodict):
        # Don't copy the graph, because it is not intended to be edited, and it is a slow process
        return ProgramState(self.graph, copy.deepcopy(self.position), copy.deepcopy(self.direction), copy.deepcopy(self.dataStack))
