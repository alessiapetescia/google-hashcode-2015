# -*- coding: utf-8 -*-

def create_pizza(input_file='input_7.txt'):
  with open(input_file,'r') as file:
    f = file.readlines()
    pizza = []
    params = f[0].split(' ')
    nr = int(params[0])
    nc = int(params[1])
    min_ham, min_area = int(params[2]), int(params[2])
    max_area = int(params[3])
    for i in range(1,len(f)):
      s = []
      s[:] = f[i].strip('\n') 
      s = [1 if x == 'H' else 0 for x in s]
      pizza.append(s)
  return(pizza,nr,nc,min_ham,min_area,max_area)

def indexes_cols(nc):
  c = []
  for x in range(0,nc-1):
    t= x+1
    for i in range(t,nc):
      c.append([x,i])
  return(c)

def indexes_rows(nr):
  r = []
  for x in range(0,nr-1):
    t= x+1
    for i in range(t,nr):
      r.append([x,i])
  return(r)

def combs(c,r,max_area,min_area):
  comb = []
  for x in c:
    for y in r:
      a = x[1]-x[0]
      b = y[1]-y[0]
      ab = a*b
      if (ab <= max_area and ab >= min_area):
        comb.append([x,y,ab])

  return(comb)

def compute_slices(comb,pizza,min_ham):
  slices=[]
  ham = 0
  for i in comb:
    ham = 0
    for d in range(i[1][0],i[1][1]):
      ham += sum(pizza[d][i[0][0]:i[0][1]])
    if  (ham >= min_ham):
      slices.append([i[0],i[1],i[2],ham])
  slices = sorted(slices, reverse = True, key=lambda x: x[2])

  return(slices)

def get_ultimate_slices(nr,nc,slices):
  pizza_copy = create_pizza()[0]
  ultimate_slices = []
  s = 0
  check = False
  g=0
  count = 0 
  max = nr*nc

  while (s<= max and  g < len(slices)):

    for i in slices:
      count = 0
      for r in range(i[1][0],i[1][1]):
        for c in range(i[0][0],i[0][1]):
          if pizza_copy[r][c] == -1:
            count +=1

      if count == 0:   
          for r in range(i[1][0],i[1][1]):
            for c in range(i[0][0],i[0][1]):
              pizza_copy[r][c] = -1
          s = s + i[2]
          ultimate_slices.append(i)
      g+=1

  return(ultimate_slices)

def get_scores(ultimate_slices):
  with open('scores.txt','w') as f:
    f.write(str(len(ultimate_slices))+'\n')
    for i in ultimate_slices:
      f.write(str(i[1][0])+' '+str(i[0][0])+' '+str(i[1][1]-1)+' '+str(i[0][1]-1)+'\n')



pizza,nr,nc,min_ham,min_area,max_area = create_pizza()
c, r = indexes_cols(nc), indexes_rows(nr)
comb = combs(c,r,max_area,min_area)
slices = compute_slices(comb,pizza,min_ham)
ultimate_slices = get_ultimate_slices(nr,nc,slices)

get_scores(ultimate_slices)



