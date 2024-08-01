import csv

# with open("Files\\makingcsv.csv","w",newline="") as csvfile:
#     wrtngfile = csv.writer(csvfile,delimiter=",",quotechar="|",quoting = csv.)

# with open('persona;.csv','r') as file:
# 	reader = csv.reader(file,quoting=csv.Quote_ALL,skipinitialspace=True)
# 	for row in reader:
# 		print(row)

# 	reader = csv.DictReader(file)
# 	for row in reader:
# 		print(dict(row))

# import csv
# with open("persons.csv",'w',newline='') as csvfile:
# 	filewriter = csv.writer(csvfile, delimiter=',')
# 	filewriter.writerrow(['Name','Age','Profession'])
# 	filewriter.writerrow(['Derek','23','Docter'])
# 	filewriter.writerrow(['Ni Pinping','68','Secratory'])
# 	filewriter.writerrow(['Chadra','21','Sweeper'])

# with open('persons1.csv', 'w', newline='') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['Name', 'age','Profession'])
#     filewriter.writerow(['Derek','23', 'Doctor'])
#     filewriter.writerow(['Steve', '22','Engineer'])
#     filewriter.writerow(['Paul', '32', 'Manager'])
# row_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(row_list)

# with open('players.csv','w',newline='') as file:
# 	fieldnames = ['player_name','fide_rating']
# 	writer = csv.DictWriter(file,fieldnames=fieldnames)
# 	writer.writeheader()
# 	writer.writerow({'player_name':'Magnus Carlsen','fide_rating':2870})
# 	writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating':2822})
# 	writer.writerow({'player_name':'Ding Liren','fide_rating:2801':2801})