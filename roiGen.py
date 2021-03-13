


roi =[
    [(239, 80), (667, 115), 'string', 'p1/username'],
    [(904, 80), (1006, 113), 'int', 'p1/score'],
    [(1041, 79), (1112, 112), 'int', 'p1/kills'],
    [(1141, 79), (1215, 114), 'int', 'p1/assists'],
    [(1235, 78), (1317, 113), 'int', 'p1/deaths'],
    [(1335, 79), (1419, 115), 'int', 'p1/ping'],
    
    [(240, 124), (672, 154), 'string', 'p2/username']
]


addToY = 44

for i in range(5):
    tuple1 = list((roi[i][0][0], roi[i][0][1] + addToY))
    tuple2 = list((roi[i][1][0], roi[i][1][1] + addToY))

    newType = roi[i][2]
    
    newPlayerAttrib = roi[i][3].split('/')[0].split('p')[0] + str(int(roi[i][3].split('/')[0].split('p')[1])) + roi[i][3].split('/')[1]
    
    newlist = list()
    list.append(tuple1,tuple2,newType, newPlayerAttrib)

    print(newlist)