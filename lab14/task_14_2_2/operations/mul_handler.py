from numbers import Number

from .base import BaseOperationHandler


class MulHandler(BaseOperationHandler):
    SUPPORTED_OPERATION = "*"

    def _handle(self, a: Number, b: Number):
        return a * b
