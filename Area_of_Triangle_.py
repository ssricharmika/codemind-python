import math
def triangle_area_heron(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

a,b,c=map(int,input().split())
print('%0.2f' % triangle_area_heron(a,b,c))