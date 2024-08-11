"""
#
# Part: Python Comment
#
"""
#---------------------

# this is a comment 
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (t)
#---------------------
"""
 v = s/t
 v = ความเร็ว (m/s)
 s = ระยะทาง (m)
 t = เวลา (t)
"""
#---------------------

print("Hello World")

#-------------------------------------
"""
#
# Part: Python Variables
#
"""
#------------------------*************
x = 50 #Integer
y = "Hey Brus"  #String"5"`เป็นstring`
b = 10

print(x-b,y)
#----------------------*************
x=str(3)
y=int(5)
z=float(7)
print(type(x),type(y),type(z))
#----------------------**************
"""
#
# Part: Variables Names
#
"""
#------------------------------------
myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
MY_VAR="John"
my_var2="John"
#**************ทำให้อยู่ในกลุ่มกัน***********
#----------------------------------------
#******************ทำไม่ได้*********
#2my_var="John"
#my-var="john"
#my var="john"
# Camel Case
myVariablName="John"
#Pascal Case
MyVariablName="John"
#Snake Case
my_variabl_name="John"
#----------------------------------------
"""
#
# Part: Python String
#
"""
#---------------------------------------
x="Hey Brus"
print(x)
#****************ทำแบบนี้จะทำให้เกิดเพระที่ซอนไว************
y="""
1Hey Brus
2Hey Brus
3Hey Brus
"""
print(y)
#*****************************************************
#*************เป็นการระบุกตำแน*************************
x="Hey Brus"
print(x[2])
print(len(x))
print("Hey" in x) #***แชกว่ามีไม**********
print("555555" not in x)#*****แชกว่าไม่มีใช้********
print(x.upper())#***********`ทำเป็นตัวใหย์ทั้งหมด*******
print(x.lower())#**********ทำเป็นตัวเล็กทั้งหมด*********


print(x.replace("Brus","Sis"))
print(x.split(" "))


a="Apple"
b="Company"
print(a +""+ b)


price=20
word=f"Price:{price:.2f}"
print(word)
#**************************************************
