import csv
import pickle
import random
import math


def count():
    count = 0
    f = open("story.txt", "r")
    r = f.readlines()
    for line in r:
        if line.strip().endswith("A"):
            count += 1
    print("Number of lines ending with 'A':", count)
    f.close()
count()

def count1():
    count = 0
    f = open("story.txt", "r")
    r = f.read()
    d = r.split()
    for word in d:
        if word[-1] == "i" :
            count += 1
    print("Number of words ending with 'i':", count)
    f.close()
count1()

def count2():
    count = 0
    f = open("story.txt", "r")
    r = f.read()
    d = r.split()
    for word in d:
        if len(word) >= 3:
            count += 1
    print("Number of words with three or more letters:", count)
    f.close()
count2()

even = []
def push_even(N):
    for i in N:
        if i % 2 ==0:
            even.append(i)
    print(even)
push_even([1,2,3,4,5,6,7,8,9,10])

def pop_even():
    if even == []:
        print("Empty")
    else:
        print(even.pop())
pop_even()

def disp_even():
    if even == []:
        print("None")
    else:
        print(even)
disp_even()

BookStack = []
def push_book(BookStack, New_Book):
    BookStack.append(New_Book)
    print(BookStack)
push_book(BookStack, "Math")

def pop_book(BookStack):
    if BookStack == []:
        print("Underflow - No book to remove")
    else:
        print(BookStack.pop())
pop_book(BookStack)

def Accept():
    f = open("Result.csv", "a", newline='')
    wr = csv.writer(f)
    St_Id = input("Enter Student ID: ")
    St_Name = input("Enter Student Name: ")
    St_Game = input("Enter Student Game: ")
    Result = input("Enter Student Result: ")
    L = [St_Id, St_Name, St_Game, Result]
    wr.writerow(L)
    f.close()
Accept()

def wonCount():
    f = open("Result.csv", "r", newline='')
    r = csv.reader(f)
    count = 0
    for i in r:
        if i[3].strip().lower() == "won":
            count += 1
    print("Number of students who won:", count)
    f.close()
wonCount()

BigNums = []
def Push_Big(Nums):
    for i in Nums:
        if len(str(i)) >= 5:
            BigNums.append(i)
    print(BigNums)
Push_Big([213,10025,167,254923,14,1297653,31498,386,92765])

def Pop_Big():
    while BigNums:
        print(BigNums.pop())
    print("Stack Empty")
Pop_Big()
