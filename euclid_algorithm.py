def gcd(a,b): #유클리드 알고리즘
    print("gcd",(a,b))
    while b != 0:
        r = a%b
        a=b
        b=r
        print("gcd",(a,b))
    return a
print(gcd(120,78))

def find_max(A):
    max = A[0]
    for i in range(len(A)):
        if A[i]>max:
            max = A[i]
    return max

array = [20,30,12,93,45,19,89,55,24]
print(array, "max:",find_max(array))
      
books = [234,82,128,50,155]
total = 0
for x in books:
    total +=x
print("합계:",total)
print("평균",total/len(books))

x=0
while x<5:
    print("안녕하세요.")
    x += 1

for x in range(5):
    print("안녕하세요")

age = int(input('Age: '))
pay = "3000원"
if age >= 65 or age <5:
    pay = "무료"
print("입장료:", pay)

kor=int(input('국어점수: '))
eng=int(input('영어점수: '))
math=int(input('수학점수: '))
total=kor+eng+math
avr=total/3
print("총점:",total,end=" ")
print("평균:",avr)

a=10
b=20
c=a+b
print(c)

a=input("first numnber: ")
b=input("second number: ")
c=a+b
print(c)


