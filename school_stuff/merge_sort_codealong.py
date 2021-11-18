import random
start_list = list(range(20))
random.shuffle(start_list)

l1 = start_list[0:5]
l2 = start_list[5:10]
l3 = start_list[10:15]
l4 = start_list[15:20]
l1.sort()
l2.sort()
l3.sort()
l4.sort()



def merge(in_l1, in_l2):
  out_l = []
  while len(in_l1) > 0 or len(in_l2) > 0:
    if len(in_l1) > 0 and len(in_l2)  > 0:
      if  in_l1[0] < in_l2[0]:
        out_l.append(in_l1.pop(0))
      else:
        out_l.append(in_l2.pop(0))
    else:
      out_l.extend(in_l1)
      out_l.extend(in_l2)
      in_l1, in_l2 = [],[]

  return out_l


out_l1 = merge(l1, l2)
out_l2 = merge(l3,l4)
print(merge(out_l1,out_l2))