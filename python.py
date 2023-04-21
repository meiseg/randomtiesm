import csv

def menu_created()->int:
    
     print("World CUP SOCCER ANALYSIS PROGRAM")
     print("--------------------------------------------------------------")
     print("(1) Print Group Play Game Summary")
     print("(2) Report Teams(s) having maximum value for requested statistic")
     print("(3) ReportTeams(s) having minimum value for requested statistic")
     print("(4) Report Teams(s) having value greater than average for requested statistic")
     print("(5) Report Teams(s) having value less than average for requested statistic")
     print("(9) End program")
     print("--------------------------------------------------------------")
     return int(input("\nEnter a number to choose a command:\n")) 
stat_rec = ""
def requested_statistic()->int:
    located_stat = 0
    global stat_rec 
    stat_rec= str(input("Enter statistics name to report:\n"))
    for i in lines[0]:
        if i == stat_rec:
            located_stat = lines[0].index(i)
    return located_stat




input_rec = str(input("Enter filename to process:\n"))
with open(input_rec,'r') as f:
    datas= csv.reader(f,delimiter=',')
    lines = []
    for row in datas:
        lines.append(row)
option = menu_created()

while(option != 9):
    if option == 1:
        print(f"\t{lines[0][0]}\t{lines[0][1]}\t\t{lines[0][2]}\t{lines[0][3]}\tteam1\t\tteam2\t\tscore")
        for iter0 in range(1,len(lines)):
            if lines[iter0][0] == lines[iter0-1][0]:
                print("\t%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s-%s" %(lines[iter0][0],lines[iter0][1],lines[iter0][2],lines[iter0][3],lines[iter0-1][4],lines[iter0][4],lines[iter0-1][5],lines[iter0][5]))
       
            
            
        
    elif option == 2:
        located_stat = requested_statistic()
        max = 0
        my_list = []
        for iter1 in lines:
            item1 = iter1[located_stat]
            if item1.isdigit() and int(item1) > max:
                max =int(item1)
        
        for iter1 in lines:
            if str(max) in iter1[located_stat]:
                index = (lines.index(iter1),iter1.index(str(max)))
                my_list.append(index)

        print("Reporting teams having game(s) with highest number of %s (%d):\n" %(stat_rec,max))
        for i in range(len(my_list)):
            print(lines[my_list[i][0]][4])
        print("\n")
   
   
   
    elif option == 3:
        located_stat = requested_statistic()
        min = 10000
        my_list = []
        for iter2 in lines:
            item2 = iter2[located_stat]
            if(item2.isdigit() and int(item2) < min):
                    min =int(item2)
        
        for iter1 in lines:
            if str(min) in iter1[located_stat]:
                index = (lines.index(iter1),iter1.index(str(min)))
                my_list.append(index)

       
        print("Reporting teams having game(s) with lowest number of %s (%d):\n" %(stat_rec,min))
        for i in range(len(my_list)):
            print(lines[my_list[i][0]][4])
        print("\n")
    
    
    elif option == 4:
        located_stat = requested_statistic()
        ave = 0
        my_list = []
        for iter3 in lines:
            item3 = iter3[located_stat]
            if item3.isdigit():
                ave += int(item3)
        ave = ave/(len(lines)-1)
        
        for iter3 in lines:
            if iter3[located_stat].isdigit() and ave < int(iter3[located_stat]):
                index = (lines.index(iter3),iter3.index(iter3[located_stat]))
                my_list.append(index)
            
        
        print("Reporting teams having games with greater than average of %s (%.1f):\n" %(stat_rec,ave))
        for i in range(len(my_list)):
            print(lines[my_list[i][0]][4])
        print("\n")
            
    elif option ==5:
        located_stat = requested_statistic()
        ave =0
        my_list = []
        for iter4 in lines:
            item4 = iter4[located_stat]
            if item4.isdigit():
                ave += int(item4)
        ave = ave/(len(lines)-1)
        for iter4 in lines:
            if iter4[located_stat].isdigit() and ave > int(iter4[located_stat]):
                index = (lines.index(iter4),iter4.index(iter4[located_stat]))
                my_list.append(index)
            
        
        print("Reporting teams having games with less than average of %s (%.1f):\n" %(stat_rec,ave))
        for i in range(len(my_list)):
            print(lines[my_list[i][0]][4])    
        print("\n")       
      
    
    else:
        print("invalid selection")
        
    option = menu_created()
        
       
        
        
