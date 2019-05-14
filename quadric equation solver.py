import math
print 'Quadric Equation solver'

print 'please enter your quadric equation'
print 'a='

a=int(raw_input())
print 'b='
b=int(raw_input())
print 'c='
c=int(raw_input())

print 'Processing'

sqrt = math.sqrt(b*b -4*a*c)
equation1 = -b + sqrt
equation2 = -b - sqrt
x=0
ky=x*x+b*x+c
print 'cut points with x line'
print 'x1=' + str(equation1/2*a)
print 'x1=' + str(equation2/2*a)
x=-b/2*a
print 'kodkod = '+  str(x) +','+ str(ky)
if a>0:
    print 'thum aliya = x>' + str(x)
else:
    print 'thum aliya = x<' + str(x)
