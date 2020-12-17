from math import sqrt
def get_new_point(A1,A2,A3,h):#A1,A2,A3 три точки. отрезки A2A1 и A3A2 сдвигаются на h, функция возвращает точку A2* нового многоугольника
    #Нормаль к отрезку A2A1
    normal1 = [0,0]
    normal1[0] = -(A2[1]-A1[1])/sqrt((A2[0]-A1[0])**2+(A2[1]-A1[1])**2)
    normal1[1] = (A2[0]-A1[0])/sqrt((A2[0]-A1[0])**2+(A2[1]-A1[1])**2)
    #Нормаль к отрезку A3A2
    normal2 = [0,0]
    normal2[0] = -(A3[1]-A2[1])/sqrt((A3[0]-A2[0])**2+(A3[1]-A2[1])**2)
    normal2[1] = (A3[0]-A2[0])/sqrt((A3[0]-A2[0])**2+(A3[1]-A2[1])**2)
    #Косинус между нормалями
    cos_a = normal1[0]*normal2[0]+normal1[1]*normal2[1]
    #нужен тангенс a/2
    tg_a_2 = sqrt((1-cos_a)/(1+cos_a))
        
    #Направляющий вектор отрезка A1A2
    napr_vector = [0,0]
    napr_vector[0] = (A2[0]-A1[0])/sqrt((A2[0]-A1[0])**2+(A2[1]-A1[1])**2)
    napr_vector[1] = (A2[1]-A1[1])/sqrt((A2[0]-A1[0])**2+(A2[1]-A1[1])**2)
        
    #Новая точка = исходная точка + h*normal1+napr_vector*tg_a_2*h
    #print(tg_a_2)
    P = [0,0]
    P[0] = A2[0]+h*normal1[0]+napr_vector[0]*tg_a_2*h
    P[1] = A2[1]+h*normal1[1]+napr_vector[1]*tg_a_2*h
    
    return P

def main():
    A = []
    B = []
    try:
        f = open("ppp.p","r")
    except IOError:
        print("Failed to open ppp.p file")
        return
    h = int(f.readline().split('\n')[0])
    for l in f:
        v = []
        line = l.split('\n')[0]
        v.append(float(line.split(' ')[0]))
        v.append(float(line.split(' ')[1]))
        A.append(v)
    f.close()
    for i in range(-1,len(A)-2):
        B.append(get_new_point(A[i],A[i+1],A[i+2],h))
    B.append(get_new_point(A[-2],A[-1],A[0],h))
    
    for i in range(len(B)):
        print(B[i])    

if __name__ == "__main__":
    main()
