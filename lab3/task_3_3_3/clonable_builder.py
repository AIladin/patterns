from builder.string_builder import StringBuilder
from prototype.base import BasePrototype


class ClonableStringBuilder(StringBuilder, BasePrototype):
    def clone(self):
        obj = self.__class__()
        obj.result = self.result
        return obj
