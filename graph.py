from itertools import combinations

def IterCombine(n, a):
 return list(combinations(range(n), a))

def C(m, a):
 rst = 1
 for i in range(m, m-a, -1):
  rst *= i
 for i in range(1, a+1):
  rst /= i
 return rst

def Weight(K):
 r = 0
 edgeK=[]
 Bcolor = False
 Wcolor = False
 for i in range(3):
  for j in range(i+1,4):
   edgeK.append(edge[K[i]][K[j]])
 for e in edgeK:
  if e == 1:
   r = r+1
  elif e == 2:
   Bcolor = True
   if Wcolor == True:
    return 0
  else:
   Wcolor = True
   if Bcolor == True:
    return 0
 if Bcolor and Wcolor:
  return 0
 elif Bcolor == False and Wcolor == False:
  return 2 ** (1-C(a,2))
 else:
  return 0.5 ** r





if __name__ == '__main__':
	n=10
	a=4
	Klist=IterCombine(n, a)
	edge=[] #0 no edge; 1 no color; 2 black; 3 white
	for i in range(n):
	 for j in range(n):
	  if j == 0:
	   data = []
	  if i == j:
	   data.append(0) 
	  else:
	   data.append(1)
	 edge.append(data)

	W0=C(n,a)*(2**(1-C(a,2)))
	print W0
	#coloring
	for i in range(1,n):
	 for j in range(0,i):
	  # print i,j
	  edge[i][j] = 2
	  edge[j][i] = 2
	  Wi = 0
	  for Ka in Klist:
	   Wi = Wi + Weight(Ka)
	  if Wi > W0:
	   edge[i][j] = 3
	   edge[j][i] = 3
	   Wi = 2*W0 - Wi
	  W0 = Wi
	  print W0
	count = 0
	print '===================== answer ======================='
	for i in range(n):
	 print edge[i]
	print '================== answer  over ===================='
	for k in Klist:
	 white_flag = False
	 black_flag = False
	 #list(combinations(range(n), a))
	 edges = list(combinations(k, 2))
	 for e in edges:
	  if edge[e[0]][e[1]] == 2:
	   white_flag = True
	  else:
	   black_flag = True
	 if white_flag and black_flag:
	  continue
	 else:
	  count += 1
	print count