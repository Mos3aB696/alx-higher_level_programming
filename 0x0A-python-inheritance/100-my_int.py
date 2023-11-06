#!/usr/bin/python3
"""Create Class That Inhertance From int"""


class MyInt(int):
    def __eq__(self, other):
        """Function That Swap Equal To Not Equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Function That Swap Not Equal To Equal"""
        return super().__eq__(other)
