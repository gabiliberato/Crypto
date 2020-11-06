#!/usr/bin/env python
# -*- coding: utf-8 -*-

abc = "abcdefghijklmnopqrstuvwxyz"
phrase = 'name' #word

def rt13(x):
   return "".join([abc[(abc.find(c) + 13) % 26] for c in x])

print(rt13(phrase)) #Coder
print(rt13(rt13(phrase))) #Decoder
