>>> print(type(1234))
<class 'int'>
>>> print(type(143.3234))
<class 'float'>
>>> print('"안녕"이라고 말했다.'))
  File "<stdin>", line 1
    print('"안녕"이라고 말했다.'))
                         ^
SyntaxError: unmatched ')'
>>> print(type('"안녕"이라고 말했다.')) 
<class 'str'>
>>> print("안녕\n안녕")                 
안녕
안녕
>>> print("안녕\t안녕")
안녕    안녕
>>> print("안녕\t\안녕") 
안녕    \안녕
>>> print("안녕\t\\안녕") 
안녕    \안녕
>>> print("안녕\t\\\안녕") 
안녕    \\안녕
>>> print(r"안녕\t\\\안녕") 
안녕\t\\\안녕
>>> print("구름\t3\t강서구") 
구름    3       강서구
>>> print("""동해물과 백두산이 마르고 닳도록
... 하느님이 보우하사 우리나라 만세
... 무궁화 삼천리 화려강산 대한사람
... 대한으로 길이 보전하세""")
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
>>> print("""\\\동해물과 백두산이 마르고 닳도록 
... 하느님이 보우하사 우리나라 만세
... 무궁화 삼천리 화려강산 대한사람 
... 대한으로 길이 보전하세""")
\\동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
>>> print("aaa"+"bbb")                         
aaabbb
>>> print("aaa"+1)     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print("aaa"+str(2)) 
aaa2
>>> print("11"+2)       
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(int("11")+2)  
13
>>> print("aaa" * 5)
aaaaaaaaaaaaaaa
>>> print(5*"aaa")   
aaaaaaaaaaaaaaa
>>> print("안녕하세요"[0])
안
>>> print("안녕하세요"[-1]) 
요
>>> print("안녕하세요"[-2]) 
세
>>> print("안녕하세요"[1:4]) 
녕하세
>>> print("안녕하세요"[0:3]) 
안녕하
>>> print("안녕하세요"[:3])  
안녕하
>>> print("안녕하세요"[0:])  
안녕하세요
>>> print(len("안녕하세요."))
6
>>> print(5/7)
0.7142857142857143
>>> print(14/7) 
2.0
>>> print(14//7) 
2
>>> print(10//7) 
1
>>> print(10%7)  
3
>>> print(10**3)  
1000
>>> print(2**3)  
8
>>> print(2**6) 
64
>>> print(1.212**2)  
1.468944
>>> string="문자열"
>>> number="1234"
>>> string + number 
'문자열1234'
>>> number=1234     
>>> string + number 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> string + str(number)
'문자열1234'
>>> print("안녕"+"하세요" *3)
안녕하세요하세요하세요
>>> pi=3.14159265
>>> pi + 2
5.14159265
>>> pi - 2
1.1415926500000002
>>> pi *2 
6.2831853
>>> pi / 2
1.570796325
>>> pi %2
1.1415926500000002
>>> pi * pi
9.869604378534024
>>> a = 10   
>>> a+=1
>>> a
11
>>> a**=2
>>> a
121
>>> a =10
>>> a /=2
>>> a
5.0
>>> str = "안녕"
>>> str += "!"
>>> 
>>> int("안녕")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '안녕'
>>>