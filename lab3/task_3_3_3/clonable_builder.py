from builder.string_builder import StringBuilder
from prototype.base import BasePrototype


class ClonableStringBuilder(StringBuilder, BasePrototype):
    def clone(self):
        return self.__class__().append_substring(self.result)
