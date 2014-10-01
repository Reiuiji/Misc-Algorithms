import os
import sys
import argparse
import numpy as np
from numpy import genfromtxt

#input Parser
parser = argparse.ArgumentParser(description='Floyd\'s Algorithm Solver')
parser.add_argument("-i", "--input", dest='INPUT', help="Input File")

args = parser.parse_args()

if not args.INPUT:
	print("Need input file")
	sys.exit()
else:
	if not os.path.isfile(args.INPUT):
		print("Input File Does not Exist")
		sys.exit()

def floydmin(D,K):
	row = D.shape[0]
	col = D.shape[1]
	D1 = np.zeros([row,col],dtype='float64')
	for r in range(row):
		for c in range(col):
			D1[r][c] = minimum(D[r][c],D[r][K-1],D[K-1][c])
	return D1

def minimum(A,B,C): #A: first, B + C second
	if ((B == 'inf') or (C == 'inf')):
		D = 'inf'
	else:
		D = B + C
	if (D == 'inf'):
		D = A
	else:
		if not (A == 'inf'):
			if D > A:
				D = A
	#print(A,B,C,D)
	return D

def tprint(tbl,name):
	row = tbl.shape[0]
	col = tbl.shape[1]
	print(name)
	print("\t|1\t|2\t|3\t|4\t|5")
	print('{0}+'.format('+{0}'.format(str('-'*7))*6))
	for r in range(row):
		data = '{0}\t|'.format(r+1)
		for c in range(col):
			data = data + ('{0}\t|'.format(tbl[r][c]))
		print(data)

W = genfromtxt(args.INPUT, delimiter=' ')
tprint(W,"W Table")
D1 = floydmin(W,1)
tprint(D1,"D1 k=1 Table")
D2 = floydmin(W,2)
tprint(D2,"D2 k=2 Table")
D3 = floydmin(W,3)
tprint(D3,"D3 k=3 Table")
D4 = floydmin(W,4)
tprint(D4,"D4 k=4 Table")
D5 = floydmin(W,5)
tprint(D5,"D5 k=5 Table")
