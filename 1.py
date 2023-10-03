#!/usr/bin/env python
# coding: utf-8

# # 1.a) Develop a program to read the student details like Name, USN, and Marks in three subjects. Display the student details, total marks and percentage with suitable messages

# In[7]:


stuName = input("Enter the name of the student : ")
stuUSN = input("Enter the USN of the student : ")
stuMarks1 = int(input("Enter marks in Subject 1 : "))
stuMarks2 = int(input("Enter marks in Subject 2 : "))
stuMarks3 = int(input("Enter marks in Subject 3 : "))


print("Student Details\n")
print("Name :", stuName)
print("USN :", stuUSN)
print("Marks 1 :", stuMarks1)
print("Marks 2 :", stuMarks2)
print("Marks 3 :", stuMarks3)
print("Total :", stuMarks1+stuMarks2+stuMarks3)
print("Percentage :", (stuMarks1+stuMarks2+stuMarks3)/3)


# # Develop a program to read the name and year of birth of a person. Display whether the person is a senior citizen or not.

# In[9]:


from datetime import date


Name = input("Enter the name of the person : ")
DOB = int(input("Enter year of birth : "))

currentYear = date.today().year
perAge = currentYear - DOB 

if (perAge > 60):
    print(Name, "aged", perAge, "years is a Senior Citizen.")
else:
    print(Name, "aged", perAge, "years is not a Senior Citizen.")

