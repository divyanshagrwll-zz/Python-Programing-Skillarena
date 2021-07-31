st = ''; ls =[]
while True:
    st = input()
    if st == 'End' or st == 'end':
        break
    ls.append(st)
nls = [ls.copy()]

while len(nls)!=len(ls):
    for q in nls:
        if len(q)>1:
            print('Splitting',q)
            temp = []
            for j in range(len(q)//2):
                temp.append(q[j])
                q.remove(q[j])
            nls.append(temp)
            print('into',q,'or',temp)
else:
    print('Final Result:')
    print(nls)