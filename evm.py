bjp=0;cong=0;sp=0;aap=0;bsp=0
while True:
    print("*****WELCOME TO THE EVM*****")
    print("Press 1 to vote for BJP\nPress 2 to vote for Congress\nPress 3 to for Samajwadi party\nPress 4 to vote for Aam aadmi party\npress 5 to vote for BSP\n")
    vote=int(input("Enter your vote :: "))
    if vote==1:
        bjp=bjp+1
        num=int(input("Do you want to continue -\nPress 1 to continue \nPress 2 to exit\n"))
        if  num==1:
            continue
        elif num==2:
            break
    elif vote==2:
        cong=cong+1
        num=int(input("Do you want to continue -\nPress 1 to continue \nPress 2 to exit\n"))
        if  num==1:
            continue
        elif num==2:
            break
    elif vote==3:
        sp=sp+1
        num=int(input("Do you want to continue -\nPress 1 to continue \nPress 2 to exit\n"))
        if  num==1:
            continue
        elif num==2:
            break
    elif vote==4:
        aap=aap+1
        num=int(input("Do you want to continue -\nPress 1 to continue \nPress 2 to exit\n"))
        if  num==1:
            continue
        elif num==2:
            break
    elif vote==5:
        bsp=bsp+1
        num=int(input("Do you want to continue -\nPress 1 to continue \nPress 2 to exit\n "))
        if  num==1:
            continue
        elif num==2:
            break
    else:
        print("wrong input. Please enter valid option")
        num=int(input("Do you want to continue -\nPress 1 to continue \nPress 2 to exit\n"))
        if  num==1:
            continue
        elif num==2:
            break

print("Total number of votes of BJP is ::",bjp)
print("Total number of votes of Congress is ::",cong)
print("Total number of votes of samajwadi party is ::",sp)
print("Total number of votes of aam admi party  is ::",aap)
print("Total number of votes of BSP is ::",bsp)

if bjp>cong and bjp>sp and bjp>aap and bjp>bsp:
    print("\n             *****bjp is winner*****")
elif cong>bjp and cong>sp and cong>aap and cong>bsp:
    print("\n             *****congress is winner*****")
elif sp>bjp and sp>cong and sp>aap and sp>bsp:
    print("\n             *****samajwadi party is winner*****")
elif aap>bjp and aap>cong and aap>sp and aap>bsp:
    print("\n             *****aam admi party is winner*****")
elif bsp>bjp and bsp>cong and bsp>sp and bsp>aap:
    print("\n             *****bsp is winner*****")
    

