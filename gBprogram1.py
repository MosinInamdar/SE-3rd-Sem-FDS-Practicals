'''
    Write a pythonprogram to store roll numbers of student in array who attended training program in 
    random order. Write function for searching whether particular student attended training program or not, 
    using Linear search and Sentinel search.
'''

l=[]
def get():
    n=int(input("Enter the number of students in the class : "))
    for i in range(n):
        k=int(input("Enter roll no. : "))
        l.append(k)

def dis():
    for i in l:
        print(i,end=" ")

def linear():
    cnt=0
    key=int(input("Enter Roll for searching whether perticular "
                    "student attended training program or not "))
    for i in range(int(len(l))):
        if(key==l[i]):
            print("student attended session at ",i+1," located")
            break
        else:
            cnt+=1
    if(cnt-1==i):
        print("Student did not attend the session")

def sentinel():
    item=int(input("Enter Roll for searching whether perticular "
                    "student attended training program or not "))
    last=l[i-1]
    l[i-1]=item
    i=0
    while(item!=l[i]):
        i+=1
    l[-1]=last
    if(i<len(l)-1 or item==l[-1]):
        print("Roll No,=. ius found at ",i+1," location")
    else:
        print("No. is not found ")


if __name__=='__main__':
    get()
    dis()

    print("1.Linear Search using for loop")
    print("2.Sentinel Search1")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        linear()
    elif(ch==2):
        sentinel()
    else:
        print("Wrong Input!!")
