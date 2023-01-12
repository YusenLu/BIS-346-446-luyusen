# Exercise5.20

def display_table(input_list):
    for i in range(len(input_list[1])):
        if i==0:
            print(f'{i:>7}',end='')
        else:
            print(f'{i:>5}',end='')
    print()
    
    for j in range(len(input_list)):
        print(f'{j:>2}',end='')
        for k in range(len(input_list[1])):
                print(f'{input_list[j][k]:>5}',end='')
        print()
            
values = [list(range(90, 100)), 
          list(range(100, 110)), 
          list(range(110, 120)), 
          list(range(120, 130)), 
          list(range(130, 140)), 
          list(range(140, 150)), 
          list(range(150, 160)), 
          list(range(160, 170)), 
          list(range(170, 180)), 
          list(range(180, 190)), 
          list(range(190, 200)),
          list(range(200, 210))]   

input_list=values
display_table(input_list) 
              
        
    

