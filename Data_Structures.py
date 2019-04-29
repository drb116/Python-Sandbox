

def list_play(my_list):
    print(my_list[3].upper())
    print(my_list[1][2])
    print("dog" in my_list)
    print(4 in my_list)
    print(my_list[2:4])

    list2 = [0,1,2,3,4]
    print(list2)
    list2[1] = 10
    print(list2)
    list2[2:4] = [20,30]
    print(list2)
    list2[-1:-1] = [50] #adds to the end, even if you don't know the pos
    list2[2:2] = [11,14,18] #Adds at that pos
    list2[1:1] = [5] #Must be a list item for this
    print(list2)
    list2[1:3] = []
    print(list2)
    del list2[1:3] #Does the same as above
    print(list2)

def makeGrid():
    board = [[1]*8]*8
    for i in range(8):
        for j in range(8):
            print (board[i][j], end = "  ")
        print ()


def dict_study():
    students = []
    while True:
        first_name = input("Enter student's first name: ")
        if first_name == "done":
            break
        last_name = input("Enter student's last name: ")
        grade = input("Enter student's grade: ")
        student = {
            "first_name":first_name,
            "last_name": last_name,
            "grade": int(grade)
        }

        alt_student = dict(first_name = first_name, last_name= last_name, grade=int(grade))
        del student["last_name"]
        print (student.keys())
        print (student.values())
        alt_student["school"] = "PRES"
        #Check to see if a key exists:
        if  "first_name" in alt_student:
            print ("Ok, I got " + first_name)
        students.append(alt_student)

    for student in students:
        if student.get("first_name") == "Ryan":
            student["grade"] +=1
        print(student["first_name"] + " is in grade " + str(student.get("grade")) + " at " + student["school"])

def tuple_study():
    #Faster than lists
    #Can be used as a key in a dictionary (think battleship?)
    #Protected data

    new_list = [1,2,3] #creates new list
    new_tup = (1,2,3, "Apple", "Pear") #Creates tuple
    print (type(new_tup))
    print (new_tup)

def set_study():
    people = {"David", "Heather", "Jackson", "Ryan"}
    persons = set(["David", "Heather", "Jackson", "Ryan"])
    print (type(people))
    print(persons)
    people.add("Tom")
    people.add("Tom")
    print(people.difference(persons))
    print(people.intersection(persons))
    everyone = people|persons #or people.union(persons)
    print(everyone)

if __name__ == '__main__':
    new_list = [0,[0,3,4],3,"dog",8] #Can be mixed types
    #list_play(new_list)
    #Need to look at tuples and dictionaries

    #makeGrid()
    tuple_study()
    set_study()
