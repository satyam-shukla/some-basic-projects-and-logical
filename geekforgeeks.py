#######################          strings        ################################

#############################       1           ################################
# a=input("enter the words for checking palindome:- ")
# if a==a[::-1]:
#     print("its a palindrome")
# else:
#     print("its not a palindrome")


#############################       2           ##############################
# n=input("enter words do u want to reverse:- ")
# s=""
# for i in n[::-1]:
#     s=s+i
#     print(s)
    
###########################         3           #############################

# n=input("enter:- ")
# s=""
# for i in range(len(n)):
#     if i!=2:
#         s=s+n[i]
# print(s)
# print(n.replace("k","").strip())
###############################################################################
# n=input("enter:- ")
# l=0
# for i in range(len(n)):
#     l=l+1
# print(l)
#################################################################################
# n=input("enter:- ")
# b=n.strip()
# l=0
# for i in range(len(b)):
#     l=l+1
# print(l)

########################################################################
# s=0
# for i in range(len(n)):
#     if i%2==0:
#         s=s+1
# print(s)
###################################################################
# n=input("enter")
# halfn=len(n)//2
# s=""
# for i in range(len(n)):
#     if i>=halfn:
#         s=s+n[i].upper()
#     else:
#         s=s+n[i]
# print(s)
#############################################################
# n=input()
# b=n.title()
# s=""
# for i in b:
#     s=s+b[:-1]+b[-1].upper()
#     print(s)
#     break

# ############################################################

# for i in n:
#     if i.isdigit() :
#         print(True)
#         break
#     if i.isalpha()  :
#         print(True)
#         break
#     else:
#         print(False)
#         break
    
################################################################
# b=set("aeiou")
# s=set()
# for i in n:
#     if i in b:
#         s.add(i)   
#     else:
#         pass
# if len(s)==len(b):
#     print("accepted")
# else:
#     print("not accepted")
###########################################################
# n=input("enter:- ") 
# b=input("enter:- ")
# c=0
# c1=0
# for i in range(len(n)):
#     if n[i] in b:
#         c+=1
#     c1+=1
# print(c)

# n=input("enter:- ")
# for i in n:
#     c=n.count(i)
#     print(i,c) 
###########################################################
# x=0
# n=input("enter:- ")
# s=set("aeiou")
# for i in n:
#     if i in s:
#         x=x+1
# print(x)
#################################################
# n=input("enter:- ")
# b=""
# for i in n:
#     if i not in b:
#         b=b+i
# print(b)
################################################
# n=input("enter:- ")

# for i in range(len(n)):
#     if i%2==1:
#         print(n[i],i)

#################################################
# c=0
# n=input("enter:- ")
# for i in n:
#     c=n.count(i)
#     b=dict(zip(i,str(c)))
#     print(b)
##################################################
# n=input("enter:- ")
# a="@%&$"
# for i in range(len(n)):
#     if n[i] in a:
#         print(True)
#         break
#     if len(n)==i+1:
#         print(False)


############################################################


# a=input()
# b=len(a)
# d=""
# for i in a:
#     c=a.count(i)
#     if b>c:
#         b=c
#         d=i
# print(d,b)

###########################################################
# n=input("enter:- ")
# k=4
# l=[]
# for i in n.split(" "):
#     if len(i)>k:
#         # l=l+i
#         # print(l,end=" ")
#         l.append(i)
# print(l)

########################################################
# n=input("enter:- ")
# b=""
# for i in range(len(n)):
#     b+=n.replace(n[0],"")
#     print(b)
#     break
# ######################################################
# n=input("enter:- ")
# x=[]
# for i in n.split(" "):
#     x.append(i)
# print(x)
# b="-".join(x)
# print(b)
    
#########################################################
# n=input("enter:- ")
# b=set("01")
# s=set(n)

# if s==b or s=={"0"} or s == {"1"}:
#     print(True)
# else:
#     print(False)
        
        
######################################################
# import abc


# n=input("enter:- ")
# b=list(n)
# print(b)
# for i in range(len(n.split(n))):
#     print(i)

##############################   ADVANCE STRING PROGRAMS     ###############################
# help_dict = {
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9',
# 	'zero' : '0'
# }
# test_str = input("enter:- ")
# print(test_str)
# res = ''.join(help_dict[ele] for ele in test_str.split())
# print(res)

################################################################################################
#################################       list       ###################################
#                                 ######### 1 #######
# n=[1,2,3,4,5,6]
# a=int(input("enter index to swap element:- "))
# b=int(input("enter index to swap element:- "))
# n[a],n[b]=n[b],n[a]
# print(n)

######################################################################################

# a=[1,2,3,4,5,6,7]
# b=int(input("enter:- "))
# for i in a:
#     if i == b:
#         print(True)
#         break
#     if len(a)== i+1:
#         print(False)

#####################################################################################
# lst=[1,2,3,45,6,7]
# for i in lst[::]:
#     lst.pop()
# print(lst)
    
##################################################
# for i in lst[:]:
#     lst.remove(i)
# print(lst)

################################################
# lst=[1,2,3,45,6,7]
# v=[]
# for i in lst[:]:
#     a=lst.pop()
#     v.append(a)
# print(v)
    
#####################################################
# a=[1,2,3,4,5,6,7,8]
# b=[]
# for i in a:
#     b.append(i)
# print(b)

###############################################
# a=[1,2,3,5,6,7,8,3,5,6,7,8,3,5,6,7,8,3,5,6,7,8,3,5,6,7,8,3,5,6,7,8]
# for i in a:
#     c=a.count(i)
#     print(i,c)


# Python program to convert a byte string to a list of integers  #
# n=input("enter:- ")
# b=[]
# for chr in n:
#     b.append(ord(chr))
# print(b)

##################################################################

# test_list = [5, 6, [], 3, [], [], 9]
# b=[]
# for i in test_list:
#     if i ==[]:
#         b.append(i)
# print(b)

##############################################################

# a=["name","id"]
# b=["satyam","99","shukla","1001"]
# n=len(b)
# r=[]
# for i in range(0,n,2):
#     r.append({a[0]: b[i], a[1] : b[i + 1]})
# print(r)

#############################################################
# a=[["a","b", 1, 2], ["c", "d", 3, 4], ["e", "f", 5, 6]]
# b=dict()
# for i in a:
#     b[tuple(i[:2])]=tuple(i[2:])
# print(b)

##############################################################
# a=[1,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
# b=set()
# for i in a:
#     if i not in b:
#         b.add(i)
# print(len(b))


##########################################################

# a=[1,2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
# l=[]
# for i in a:
#     if i not in l:
#         l.append(i)
# p=1
# for i in l:
#     p*=i
# print(p)

###########################################################

# l=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k=3
# b=[]
# for i in l:
#     x=l.count(i)
#     if x>k and i not in b:
#         b.append(i)
# print(b)

########################################################

# n=input("enter")
# halfn=len(n)//2
# s=""
# v=""
# for i in range(len(n)):
#     if i>=halfn:
#         s=s+n[i]
#     else:
#         v=v+n[i]
# print(s,v)

####################################################
# a=[1,3,4,5,6,13,7]
# a.sort()
# b=max(a[:-3])
# print(b)

# # ###############################################

# b=[]   
# maxx=[]
# minn=[]        
# a=[222,1,3,4,5,6,13,77]
# for i in range(len(a)):
# 	for j in range(len(a)-i-1):
# 		if a[j]>a[j+1]:
# 			x=a[j]
# 			a[j]=a[j+1]
# 			a[j+1]=x
# # print(a)
# for i in a[:3]:
#     minn.append(i)
# print(minn)
# for i in a[-3:]:
#     maxx.append(i)
# print(maxx)


# a=[15,15,15,10,20,16,14,2,5,11,22,8,9]
# b=[]
# # ccc=[]
# for i in a:
#     for j in a:
#         if (j or i not in a) and j+i==30:
#             c=[]
#             c.append(i)
#             c.append(j)
#             if c and c[-1::-1] not in b:
#                 b.append(c)
# print(b)
# for i in b:
#     if i not in  ccc:
#         ccc.append(i)
#         print(c)

################################################################################################

