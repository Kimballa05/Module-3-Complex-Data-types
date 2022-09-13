#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""BMI 6018 Fall 2022 

Instructions: For this assignment, please return all answers as variables in your
.py file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled one_c. While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
 .b Add 3 to the 5th indexed element
 .c Coerce all elements in the list to floats using list comprehension
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j



Problem 2: Dictionary woes

2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}



Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?
 

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list
 
 
Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

#Start your assignment here
print("Assignment 3")
print("Problem 1")


#Created a list variable containing int values 0 to 9
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Inserting int 3 into the 5th index, or index[5]. Printing the one_a variable should show the result
one_b = one_a.insert(5, 3)

#Making all elements in the list into a float. A new variable is created containing the list of float elements
one_c = [float(x) for x in one_a]

#Creating a variable containing the list that has been coerced into a set
one_d = set(one_c)

#Adding int 10 into the set. Printing the one_d variable should show the result
one_e = one_d.add(10)

#Pop or removed an item from the set. Printing the one_d variable should show the result
one_f = one_d.pop()

#Using the len function to count the number of items in the set. Printing the one_g variable will give the count
one_g = len(one_d)

#Created a boolean variable that, if printed, returns True if # of items in the set and list are the same and False if not
one_h = len(one_d) == len(one_a)

#Created a list variable containing the set coerced into a list and the list form 1.a
one_i = list(one_d) + one_a

#Created a variable containing the list from 1.i coerced into a set
one_j = set(one_i)

#Created a variable containing the number of elements in the set created in 1.j
one_k = len(one_j)



# In[10]:


""""2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again
"""

print("Assignment 3")
print("Problem 2")

#Combines the 3 given dictionaries into one nested dictionary known as two_a
two_a = {
    "two_patient_dictionary_kinoko" : {
    "name" : "Kinoko",
    "year" : 2021
    },
    "two_patient_dictionary_dango" : {
    "name" : "Dango",
    "year" : 2019
    },
    "two_patient_dictionary_mochi" : {
    "name" : "Mochi",
    "year" : 2020
    }
}
print(two_a)

#Created a variable that contains the retrieved name
two_b = two_a["two_patient_dictionary_dango"]["name"]
print(two_b)

#two_c: Not a variable as directed by the question, but the code updates the value of Mochi's year
two_a["two_patient_dictionary_mochi"]["year"] = 2018
print(two_a)

#Created a new dictionary where the patient names are the keys and the year as the values (Mochi's value is now 2019)
two_d = {
    "Kinoko" : 2021,
    "Dango" : 2019,
    "Mochi" : 2019
    }
print(two_d)

#Variable contains the keys from two_d in a list type
two_e = list(two_d.keys())
print(two_e)

#Variable contains the values from two_d in a list type
two_f = list(two_d.values())
print(two_f)

#Variable contains the two previous lists combined into a dictionary again
two_g = dict(zip(two_e, two_f))
print(two_g)



# In[11]:


"""Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?
"""
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

print("Assignment 3")
print("Problem 3")

#Created a boolean variable that returns True if set E is a subset of set A and false if otherwise 
three_a = three_setE.issubset(three_setA)
print(three_a)

#Created a set variable that returns True if set E is a strict subset of set A and false if otherwise
three_b = three_setE < three_setA
print(three_b)

#Created a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print(three_c)

#Created a set that is the union of sets C, D, and E
three_d = three_setC.union(three_setD, three_setE)
print(three_d)

#Adding (or attempting to) int 9 to the previous set. Printing three_d should show result
three_e = three_d.add(9)
print(three_d)

#Comparing the set to the list created in one_a. Returns a boolean value
three_f = three_d == set(one_a)
print(three_f)

#Updating the set variable three_d with list (converted to a set) one_a so that they both 
#will have the same values and thus comparison would be True
three_d.update(set(one_a))
#Created boolean variable showing if the updated set and list one_a (converted to a set) are comparable
three_g = three_d == set(one_a)
print(three_g)


# In[12]:


"""
Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list
 
 
Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

three_setA = {1,2,3,4,5}

print("Assignment 3")
print("Problem 4")

#Assigned a variable with int 8
four_a = 8

#Created an empty list
four_b = []

#Added data type of four_a to the list. Printing the four_b list will show the result
four_c = four_b.append(type(four_a))
print(four_b)

#Added float value 0.39 to the list. Printing the four_b list will show the update
four_d = four_b.append(0.39)
print(four_b)

#Appended the type of 0.39 to the list. Printing four_b list will show the update
four_e = four_b.append(type(0.39))
print(four_b)

#Exponentiated 0.39 to the -10, rounded it to no decimal places, then appended the value to list four_b
four_f = four_b.append(int(0.39 ** -10))
print(four_b)

#Appended the type of 0.39 ^-10 (rounded) to the list. Printing four_b list will show the update
four_g = four_b.append(type(int(0.39 ** -10)))
print(four_b)

print("Problem 5")

#Created a dictionary from the list in Problem 4. The keys are the index of the list and the values are items in the list 
five_a = {
    "0" : type(four_a),
    "1" : 0.39,
    "2" : type(0.39),
    "3" : int(0.39 ** -10),
    "4" : type(int(0.39 ** -10))
    }
print(five_a)

#Added int 300 coerced into a string (variable five_b) into the list
five_b = str(300)
four_b.append(five_b)
print(four_b)

#Appended the type of int 300 coerced into a string into the list
five_c = four_b.append(type(five_b))
print(four_b)

#Sliced the string "300" (variable five_b) up to the 2nd element
five_d = five_b[0:2]
print(five_d)

#Appended the data type of the sliced string into the list
five_e = four_b.append(type(five_d))
print(four_b)

#Using list comprehension, converted string "30" (variable five_d) into a list of integers
five_f = [int(x) for x in five_d]
print(five_f)

#Appended the type of list five_f into our older list (four_b)
five_g = four_b.append(type(five_f))
print(four_b)

#Appended the type of set three_setA from Problem 3 into our older list (four_b)
five_h = four_b.append(type(three_setA))
print(four_b)


# In[ ]:




