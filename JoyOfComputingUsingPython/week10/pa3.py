n = int(input())
station_dict = {}
for i in range(n):
  train = input()
  compts = int(input())
  compt_dict = {}
  for j in range(compts):
    l = input().split(',')
    compt_dict[l[0]] = int(l[1])
  station_dict[train] = compt_dict