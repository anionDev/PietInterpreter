from typing import Union
import numpy as np
from .imageFunctions import getPixel, boundsChecker, getCodel
from .colors import isBlack, isColor, isWhite, getPixelChange
from .movementFunctions import getNextPosition
from .tokens import BoBlackToken, ToWhiteToken, BaseLexerToken, getTokenType, ToColorToken
from .errors import UnknownColorError
from .dataStructures import Edge


def edgeToToken(image: np.ndarray, inputEdge: Edge) -> Union[BaseLexerToken, BaseException]:
    """
    This function creates a token based on the given edge
    :param image: input image
    :param inputEdge: an edge containing (coords, direction)
    :return: Either a newly created token, or an exception
    """
    if not boundsChecker(image, inputEdge.edge[0]):
        return IndexError("Edge position {} is not in image".format(inputEdge.edge[0]))

    nextPosition = getNextPosition(inputEdge.edge[0], inputEdge.edge[1].pointers[0])
    if not boundsChecker(image, nextPosition):
        return BoBlackToken("edge")

    pixel = getPixel(image, nextPosition)

    if isBlack(pixel):
        return BoBlackToken("toBlack")

    if isWhite(pixel):
        return ToWhiteToken()

    if not isColor(pixel):
        return BoBlackToken("Unknown color")

    colorChange = getPixelChange(getPixel(image, inputEdge.edge[0]), getPixel(image, nextPosition))
    if isinstance(colorChange, BaseException):
        # Modify existing error message with location
        newText = "{} at position {}".format(colorChange.args[0], nextPosition)
        return UnknownColorError(newText)

    tokenType = getTokenType(colorChange['hueChange'], colorChange['lightChange'])
    return ToColorToken(tokenType, len(getCodel(image, inputEdge.edge[0]).codel))
