

def list_play(my_list):
    print(my_list[3].upper())
    print(my_list[1][2])
    print("dog" in my_list)
    print(4 in my_list)
    print(my_list[2:4])
    my_name = "jackson"
    print(my_name[2]) #One letter
    print(my_name[2:4]) #Includes 2, but not 4
    print(my_name[2:]) #From 2 on
    print(my_name[:4]) #Up to 4

    list2 = [0,1,2,3,4]
    print(list2)
    list2[1] = 10
    print(list2)
    list2[2:4] = [20,30]
    print(list2)
    list2[-1] = 50 #adds to the end, even if you don't know the pos
    list2[2:2] = [11,14,18] #Adds at that pos
    list2[1:1] = [5] #Must be a list item for this
    print(list2)
    list2[1:3] = []
    print(list2)
    del list2[1:3] #Does the same as above
    print(list2)




if __name__ == '__main__':
    new_list = [0,[0,3,4],3,"dog",8] #Can be mixed types
    list_play(new_list)
    #Need to look at tuples and dictionaries
