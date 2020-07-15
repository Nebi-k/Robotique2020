#!/usr/bin/env python
import spytank
print("taper z pour avancer")
print("taper s pour reculer")
lettre = input(">> ")

if lettre == "z":
    spytank.avance(100)
elif lettre == "s":
    spytank.recule(100)