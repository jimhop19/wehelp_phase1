def find_index_of_car(seats, status, number):
# your code here
    available_seats = []
    result = 0
    
    for x in range(len(seats)):
        if status[x] == 1 and seats[x] >= number:
            available_seats.append(seats[x])
    
    if available_seats == []:
        print(-1)
    else:
        result = min(available_seats) 
        print(seats.index(result))
    

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2