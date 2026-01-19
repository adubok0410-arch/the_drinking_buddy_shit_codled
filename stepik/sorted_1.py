def list_sorted(my_list):

    correct = True
    last_number = 0
    
    while correct:

        correct = False
        
        for i in range(len(my_list) - 1 - last_number):
        
            if my_list[i + 1] < my_list[i]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                last_number += 1
                correct = True
                
    return my_list

a = [int(i) for i in input().split()]
print(*(list_sorted(a)))