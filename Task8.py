MyNumb = 12346789
Answer = False
for i in str(MyNumb):
    if i == '5':
        Answer = True
        break

if Answer == 1:print ('YES')
else:print('NO')