from .imageFunctions import getPixel, getCodel
from .colors import isBlack
from .tokens import ToColorToken
from .movementFunctions import getDP, getCC, getArrow
from .dataStructures import Direction

class InfoManager():
    def __init__(self, builder, generalInfoFrame, programStateInfoFrame):
        self.builder = builder
        self.generalInfo = generalInfoFrame
        self.programStateInfoFrame = programStateInfoFrame

    def updateInfo(self, image, graph, programState):
        self.updateGeneralinfo(image, graph, programState)
        self.updateProgramStateInfo(programState)

    def updateGeneralinfo(self, image, graph, programState):
        self.updateEdgesInfo(image, graph, programState)

    def updateProgramStateInfo(self, programState):
        self.updateStackInfo(programState.dataStack)
        self.updatePointersInfo(programState.position, programState.direction)


    def updateEdgesInfo(self, image, inputGraph, programState):
        edgesInfo = self.builder.get_object('codelEdgesMessage', self.generalInfo)

        if isBlack(getPixel(image, programState.position)):
            edgesInfo.configure(text = "Black pixels are no codel, and have no edges")

        codel = getCodel(image, programState.position)
        baseString = "Next step will be:\n"

        graphNode = inputGraph.graph[codel]

        edge = graphNode.graphNode[programState.direction]
        baseString += self.getEdgeDescription(edge, programState.direction)

        baseString += "\nCodel edges are as follows:\n"
        #Generate pointers
        edgePointers = list(map(lambda i: Direction((i%4, int(i/4))), iter(range(8))))
        for edgePointer in edgePointers:
            edge = graphNode.graphNode[edgePointer]
            baseString += self.getEdgeDescription(edge, edgePointer)
        edgesInfo.configure(text = baseString)

    def getEdgeDescription(self, edge, pointer):
        if isinstance(edge[0], ToColorToken) and edge[0].tokenType == "push":
            return "{}/{},{} -> {}({})\n".format(edge[1], getDP(pointer.pointers[0]), getCC(pointer.pointers[1]), edge[0].tokenType, edge[0].codelSize)
        else:
            return "{}/{},{} -> {}\n".format(edge[1], getDP(pointer.pointers[0]), getCC(pointer.pointers[1]), edge[0].tokenType)

    def updateStackInfo(self, stack):
        baseString = ""
        for item in reversed(stack):
            baseString += "{}\n".format(item)
        baseString.strip("\n")

        stackInfoMessage = self.builder.get_object("stackContents", self.programStateInfoFrame)
        stackInfoMessage.configure(text=baseString)

    def updatePointersInfo(self, position, direction):
        print("Update pointers: {} -> Arrow: {}".format(direction, getArrow(direction)))
        baseString = "Pos: ({},{})\n".format(position.coords[0], position.coords[1])
        baseString += "DP: {} ({},{})".format(getArrow(direction), getDP(direction.pointers[0]), getCC(direction.pointers[1]))

        pointersInfoMessage = self.builder.get_object("pointerMessage", self.programStateInfoFrame)
        pointersInfoMessage.configure(text=baseString)
