multiplier=3,5
below=1000
lcm=1
for i in multiplier:
    lcm*=i
first_sequence=[]
gap=[]

for i in range(lcm+1):
    for a in multiplier:
        if i%a==0:
            first_sequence.append(i)
            break

for i in range(len(first_sequence)-1):
    difference=first_sequence[i+1]-first_sequence[i]
    gap.append(difference)

step=((below-1)//lcm)-1
total_rectangle=int(step*(step+1)*0.5)

rec_area=(lcm*len(gap))*total_rectangle

triangle_area=(step+1)*sum(first_sequence)

remains=sum(range((step+1)*lcm,below))

result=rec_area+triangle_area+remains

print(result)
input()
