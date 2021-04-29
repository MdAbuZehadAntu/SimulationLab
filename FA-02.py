A,B,C=50,25,20
t=0
kf,kb=0.035,0.02
while True:
    a,b,c=A,B,C
    t+=0.3
    A=A+(kb*c-2*kf*a*b)*0.3
    B=B+(kb*c-1.6*kf*a*b)*0.3
    C=C+(3*kf*a*b-1.8*kb*c)*0.3
    print(f"At time {round(t,1)} : ")
    print(f"C1 : {A}")
    print(f"C2 : {B}")
    print(f"C3 : {C}")
    if abs(A-a)<0.1 and abs(B-b)<0.1 and abs(C-c)<0.1:
        break

