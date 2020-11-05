#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from string import lowercase as lc 

file = open(sys.argv[1], 'r').read().lower() #ARQUIVE
key = int(sys.argv[2]) #KEY
mode = sys.argv[3]

result = ''

for lt in file:
	if lt in lc:
		idx = lc.find(lt)
		if mode == 'enc':
			idx = (idx + key) % 26 # Aritmética modular - caso valores sobrem voltar ao inicio do alfabeto e contar novamente
		elif mode == 'dec':
			idx == (idx - key) % 26
		result+= lc[idx]
	else:
		result += lt


print result,



