#!/usr/bin/env python3

from robot import *

Vorwärts(10)
Links(90)
Vorwärts(10)
Rückwärts(10)
Rechts(90)
Rückwärts(10)

Strecke, Winkel = Hypotenuse(10, 10)
Links(Winkel)
Vorwärts(Strecke)
Rechts(180)
Vorwärts(Strecke)
Rechts(180)
Rechts(Winkel)

