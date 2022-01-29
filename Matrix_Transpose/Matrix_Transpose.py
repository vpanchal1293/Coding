m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

'''
Take 0'th elemet of all sublist make as m_t 0th sublist
Take 1'th elemet of all sublist make as m_t 1th sublist
Take 2'th elemet of all sublist make as m_t 2th sublist
...
Take N'th elemet of all sublist make as m_t Nth sublist

'''
m_t = []

for i in range(len(m[0])):
    temp = []
    for sub_list in m:
        temp.append(sub_list[i])
    m_t.append(temp)

print(m_t)

'''
m_t_c = [ [0th element of all sublist]
          [1th element of all sublist]
          [2th element of all sublist]
          ...
          [Nth element of all sublist]
        ]
'''

m_t_c = [[sublist[coloumn] for sublist in m] for coloumn in range(len(m[0]))]
print(m_t_c)
