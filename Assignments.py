# ----------------------------------------------
# This is my first assignment in Python 
# I'm so excited to finish Elzero Python course
# I have finished first 10 videos today ^_^
# ----------------------------------------------


Name = "Ahmed Gaga\""
Age = "Seventeen\""
Address = "Egypt \\ Beheira\""

print("\"Name : " + Name + "\n" + "\n" + "\"Age : " + Age + "\n" + "\n" + "\"Address : " + Address)

Name0 = "Ahmed Gaga"
Age0 = "Seventeen"
Address0 = "\'Egypt \\ Beheira\'\""

print( "\n" "\"Hello, My name is " + Name0 + " And my age is " + Age0 + " Years old" + " And i live in " + Address0)




# ----------------------------------------------
# This is my secnd assignment in Python 
# I'm so excited to finish Elzero Python course
# I have finished videos in 3 days ^_^
# ----------------------------------------------

# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

a, b, c = "\'Ahmed\'", "\"17\"\"", "Egypt"

print("\"Hello " + a + "," + " How You Doing \\ \n\"\"\" Your Age Is " + b + " + \nAnd Your Country Is: " + c)

name = "Elzero"

print("First litter is: " + "\"" + name[1] + "\"" + "\n" + "Second litter is: " + "\"" + name[2] + "\"" + "\n" + "Last litter is: " + "\"" + name[-1] + "\"")

print(name[0:3] + "\n" + name[::2] + "\n" + name[4] + name[2] + name[0])

dd = "#@#@Elzero#@#@"

print(dd.strip("#@"))


k, l, m, n = "9", "78", "928", "1600"

print(k.zfill(4) + "\n" + l.zfill(4) + "\n" + m.zfill(4) + "\n" + n.zfill(4) + "\n")

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

name_three = "OSamA"
name_four = "osaMA"

print(name_three.swapcase() + "\n" + name_four.swapcase())

sent = "I Love Python And Although Love Elzero Web School"

print(sent.count("Love"))

print(name.index("z"))

# another way

print(name.find("z"))

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))

print(msg.replace("<3", "Love"))

# another way

print(msg.replace("<3", "Love", 2))

aa, bb, cc = "Ahmed", 17, "Egypt"

print(f"My Name Is: {aa}, And My Age Is: {bb}, And My Country Is: {cc}")


# ----------------------------------------------
# This is my third assignment in Python 
# I'm so excited to finish Elzero Python course
# I have finished videos in half houre ^_^
# ----------------------------------------------

numOne, numTwo, numThree = 24, 20.06, 1+6j
print(f"{numOne}\n{numTwo}\n{numThree}")

print(f"Imagenary Num Is: {numThree.imag}\nReal Num Is: {numThree.real}")

print("{:.10f}".format(float(numOne)))

print(f"{int(numTwo)}\n{type(int(numTwo))}")

# 100 ? 115 = -15
# 50 ? 30 = 1500
# 21 ? 4 = 1
# 110 ? 11 = 10
# 97 ? 20 = 4

print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 // 11)
print(97 // 20)

# ----------------------------------------------
# This is my 4th assignment in Python 
# I'm so excited to finish Elzero Python course
# I have finished videos in One houre ^_^
# ----------------------------------------------

myList = ["Ahmed", "Hossam","Ashraf", "Yousef", "Abdo"]
print(f"{myList[0]}\n{myList.pop(-5)}")
print(f"{myList[-1]}\n{myList.pop(3)}")

myList0 = ["Ahmed", "Hossam","Ashraf", "Yousef", "Abdo"]
print(f"{myList0[::2]}\n{myList0[1::2]}")

print(f"{myList0[1:4]}\n{myList0[3:5:1]}")

myList0[3:5] = "Elzero", "Elzero"
print(myList0)

myList0.insert(0, "Bassem")

# myList0.insert(-1, "Marwan")
# another way
myList0.append("Marwan")

print(myList0)

myList0.remove("Bassem")
myList0.remove("Ahmed")
print(myList0)
myList0.remove("Marwan")
print(myList0)

myList1 = ["Ahmed", "Hossam","Ashraf", "Yousef", "Abdo"]
mylist2 = ["Yasser", "Mohammed"]
mylist3 = ["Atef", "Rady"]

myList1.extend(mylist2)
myList1.extend(mylist3)
print(myList1)

myList1.sort()
print(myList1)

myList1.sort(reverse=True)
print(myList1)

print(len(myList1))

lang = ["Python", "C++", "Java"]
fWorks = ["Django", "Boot", "Fish"]

lang.append(fWorks)
print(lang)
print(f"{lang[3][0]}\n{lang[3][-1]}")

# ----------------------------------------------
# This is my 5th assignment in Python 
# I'm so excited to finish Elzero Python course
# I have finished videos in quarter houre ^_^
# ----------------------------------------------

myTuple = "\"Ahmed\"",

print(myTuple[0])
print(type(myTuple))

myTupleTwo = ("Osama", "Ashraf", "Yousef")
print(myTupleTwo)
print(type(myTupleTwo))
print(len(myTupleTwo))

myTupleThree = (1, 2, 3)
myTupleFour = ("A", "B", "C")
myTupleFive = myTupleThree + myTupleFour
print(myTupleFive)
print(len(myTupleFive))

myNewTuple = (1, 2, 3, 4)
a9, b9, _, c9 = myNewTuple
print(f"{a9}\n{b9}\n{c9}")