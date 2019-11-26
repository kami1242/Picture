import numpy as np

class Star:
    def __init__(self, _m, _idnumber, _r, _v):
        """
        A constructor: m is mass, r is radius vector, v is velocity (vector), idnumber is id (int)
        mass unit: solar mass
        distance unit: a.u.
        time unit: year
        """
        self.m = _m
        self.idnumber = _idnumber
        self.r = _r
        self.v = _v

