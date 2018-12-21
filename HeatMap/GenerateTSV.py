count = [[0]*24 for i in range(7)]
for row in train_df.iterrows():
    day = row[1]['weekday']
    hour = row[1]['hour']
    count[day][hour] = count[day][hour] + 1
fl = open('data.tsv','w')
fl.write('day\thour\tvalue\n')
for i in range(len(count)):
    for j in range(len(count[0])):
        fl.write(str(i+1)+'\t'+str(j+1)+'\t'+str(np.log(count[i][j]))+'\n')

fl = open('data.tsv','w')
fl.write('day\thour\tvalue\n')
for i in range(len(count)):
    for j in range(len(count[0])):
        fl.write(str(i+1)+'\t'+str(j+1)+'\t'+str(count[i][j])+'\n')