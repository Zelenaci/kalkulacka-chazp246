#!/usr/bin/env python3
# Soubor:  kalkulacka.py
# Datum:   28.03.2022 08:31
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################
import math

zasobnik = []


def operace(token):
    if token.upper() == "Q":
        exit()
    if token.upper() == "PI":
        zasobnik.append(math.pi)
    if token == "+":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a + b)
    if token == "-":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a - b)
    if token == "*":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a * b)
    if token == "**":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a ** b)
    if token == "sin":
        a = zasobnik.pop()
        zasobnik.append(math.sin(a))
    if token == "cos":
        a = zasobnik.pop()
        zasobnik.append(math.cos(a))


dva_operandy = {}
dva_operandy["+"] = lambda a, b: a + b
dva_operandy["-"] = lambda a, b: a - b
dva_operandy["*"] = lambda a, b: a * b
dva_operandy["/"] = lambda a, b: a / b
dva_operandy["//"] = lambda a, b: a // b
dva_operandy["**"] = lambda a, b: a ** b

jeden_operand = {}
jeden_operand["sin"] = math.sin
jeden_operand["cos"] = math.cos
jeden_operand["tg"] = math.tan
jeden_operand["tan"] = math.tan


def operace(token):
    if token.upper() == "Q":
        exit()
    if token.upper() == "PI":
        zasobnik.append(math.pi)
    if token.upper() == "SW":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(b)
        zasobnik.append(a)
    if token in dva_operandy.keys():
        if len(zasobnik) >= 2:
            b = zasobnik.pop()
            a = zasobnik.pop()
            zasobnik.append(dva_operandy[token](a, b))
        else:
            print("Nemám dost operandů!!!")
    if token in jeden_operand.keys():
        if len(zasobnik) >= 1:
            a = zasobnik.pop()
            zasobnik.append(jeden_operand[token](a))
        else:
            print("Nemám dost operandů!!!")


def zpracuj(radek):
    tokeny = radek.split()
    for token in tokeny:
        try:
            zasobnik.append(float(token))
        except ValueError:
            operace(token)


# čtu vstup
while True:
    radek = input(zasobnik.__repr__() + ">>> ")
    zpracuj(radek)
