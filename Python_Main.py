# This File Contain Every thing of Python



                            #<------------------- Variable -------------------------->


 
""" Variable is a data container which is used store data"""

print("<------------------- Variable -------------------------->")

Name = "Bhuresh" #Here Name is variable which contain Bhuresh as value

print(Name) #Here Print is used to print the thing which is in () or ""

Age = 20
print(type(Age))#Here Type used to show the datatype of var



                            #<------------------- Comments -------------------------->



        #there are 2types os comment
        # this is single line comment
"""This is Multiline comment"""




                            #<------------------- Operaters -------------------------->



    
"""
    There are Four Types Of Operators
    1) Arithmetic Operator (* , + , - , / , % , **)
    2) Realtion / Comparison Operator (== , != , > , < , >= , <= )
    3) Assignment Operator (= , += , -= , *= , /= , %= , **=)
    4) Logical Operator (not , and , or )
"""
print("<------------------- Operaters -------------------------->")


#1) Arithmetic Operator (* , + , - , / , % , **)

print("<------------------- Arithmetic Operator (* , + , - , / , % , **) -------------------------->")
A=20
B=30
print("A+B=",A+B)#A+B=20+30=50
print("A-B=",A-B)#A-B=20-30=-10
print("A*B=",A*B)#A*B=20*30=600
print("A/B=",A/B)#A/B=20/30=0.666...
print("A%B=",A%B)#A%B=20%30=20
print("A**B=",A**B)#A^B=20^30=1073741824......

#2) Realtion / Comparison Operator (== , != , > , < , >= , <= )

print("<------------------- Realtion / Comparison Operator (== , != , > , < , >= , <= ) -------------------------->")
Realational_variable1=20
Realational_variable2=30

print(Realational_variable1   ==   Realational_variable2)#20=30 False
print(Realational_variable1   !=   Realational_variable2)#20!=30 True
print(Realational_variable1   >    Realational_variable2)#20>30 False
print(Realational_variable1   <    Realational_variable2)#20<30 True
print(Realational_variable1   >=   Realational_variable2)#20>=30 False
print(Realational_variable1   <=   Realational_variable2)#20<=30 True


#3) Assignment Operator (= , += , -= , *= , /= , %= , **=)

print("<-------------------  Assignment Operator (= , += , -= , *= , /= , %= , **= ) -------------------------->")
    #<----------- = ----------->
Assignment_Variable1 = 20 #Here = have two side right and left which mean right value assign to left
    #<----------- += ----------->
Assignment_Variable1 += 20 #Assignment_Variable1 + 20 = 20+20=40
print(Assignment_Variable1)

    #<----------- -= ----------->
Assignment_Variable1 -= 20 #Assignment_Variable1-20=40-20=20
print(Assignment_Variable1)

    #<----------- *= ----------->
Assignment_Variable1 *= 20 #Assignment_Variable1*20=20*20=400
print(Assignment_Variable1)

    #<----------- /= ----------->
Assignment_Variable1 /= 20 #Assignment_Variable1/20=400/20=20
print(Assignment_Variable1)

    #<----------- %= ----------->
Assignment_Variable1 %= 20 #Assignment_Variable1%20=20%20=0
print(Assignment_Variable1)

    #<----------- **= ----------->
Assignment_Variable1 **= 2 #Assignment_Variable1**2=0^2=0
print(Assignment_Variable1)

#4) Logical Operator (not , and , or )

print("<------------------- Logical Operator (not , and , or ) -------------------------->")
Logical_Operato1=True

    #<----------- Not ----------->
print(" Ans Of Not Operator ",not False) # Not use as !False in c it give the opossite ans

    #<----------- And ----------->
val1 = True
val2 = True
print("Ans Of And ",val1 and val2 )#Both value should be correct

    #<----------- Or ----------->

print("ans of OR ", val1 or val2)#anyone value should be correct 







                            #<------------------- Conversion -------------------------->



print("<------------------- Conversion -------------------------->")
"""
        There Are two types of Conversion 
        1) Type Conversion
        2) Casting
"""

#1) Type Conversion
print("<------------------- Type Conversion -------------------------->")
"""
        Type conversion Python auto convert fromone type to another
"""
a=2
b=3.5
sum=a+b
print(sum)
#here we know that a is int and b is float but sum is float so a will be change to float so 2=2.0


#2) Casting
print("<------------------- Casting -------------------------->")

S="2"#type of S is String
S2=3
S4=int(S)#this is clled Casting which change String to int

"""
     Note : Only Number in String can Be change to int float or double but word or sentance cant be convert to number
"""
print(S2+S4)





                                #<------------------- User Input-------------------------->





"""
        Syntax : input()
        for storing use input we can use var like : Name = input("Enter your Name")

        Note : In python user input value have only String data type so we have to use casting as above
"""

print("<------------------- User Input-------------------------->")

Name=input("Enter Your Name : ")
print("Data Type of your Input is : ",type(Name))

print("For casting------------------------>")
Age=int(input("Enter Your Age : "))
print("Your age is : ", Age)



                                #<----------------- String ------------------->
                            
                        
                    
"""
            String is a datatype which store sequence of characters 
            Syntax : var = "Your String" or 'Your String' 
            Note :- we can note give noraml next line in python so for next line we have to use \n as we had used in c
            """
str1="This is my string"
str2="this is my second string"

    #<=--------------------------------Concatenation------------------------------=>

print(str1+str2)#adittion of bot string in one string is called concatenation

    #<------------------------------Length-------------------------------->

print("Length Of String is ",len(str1))#length of string


    #<=-----------------------------Slicing------------------------------=>

"""
            Slicing is mean that access the word or prase which are in string 
            Syntax : str[starting_index:ending_index]

"""
print(str1[1:4])
print(str1[1:])#python auto choose end index as length of string
print(str1[:5])#python auto choos start of index as 0
print(str1[-8:-1])#in python string can be slice from reverse also


            #<=-----------------------String funvtions -------------------------------=>

Str = "i am Zenitsu Agtsuma"

    #1) Endswith ------------------------------------------->

"""
        This Function is used to find some word which are in end of string or not
        Syntax : var.endswith("words")
        """
print("The String Contain uma at end ? ans:", Str.endswith("uma"))

    #2) Capatalize ----------------------------------------->

"""
            This fns is used to capatalize the first letter of String
            Syntax : var.capatalize()
            """

Str = Str.capitalize()
print("new String after capatalize is : ",Str)

    #3)Replace -------------------------------------------->

"""
        This fns is used to replace the given word with new word in string
        Syntax : var.replace(old,new)
            """

print("replacing a with o in string : ",Str.replace("a","o"))

    #4) Find --------------------------------------------->

"""
        Find is used to find spesific character or word in the given String
        Syntax : var.find("Word")
"""

print("The given word is at ",Str.find("z") , "th index")


    #5) Count ----------------------------------------------->

"""
        Count is used to count the times it comming in given string
        Syntax : var.count("word")
"""

print("The given word is ",Str.count("a"), " times in the String")



                    #<-------------------------- Conditional Statments ------------------------------>

"""
        if elif and else
        i dotn haev any theory for it so lets check a programme
        """

Marks = int(input("enter Your Mark : "))
if(Marks >= 90):
    print("Your Grade is A")
elif(90>Marks and Marks >=80):
    print("Your Grade is B")
elif(80>Marks and Marks>=70):
    print("Your grade is C")
elif(Marks>70):
    print("Your Grade is D")
else:
    print("You failed")