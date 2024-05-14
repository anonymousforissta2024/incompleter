#Source: https://stackoverflow.com/questions/64691365/name-error-in-one-program-whereas-syntax-error-in-another
my=input('Enter a character:')
list=[a,A,b,B,c,C,d,D,e,E,f,F,g,G,h,H,i,I,j,J,k,K,l,L,m,M,n,N,o,O,p,P,q,Q,r,R,s,S,t,T,u,U,v,V,w,W,x,X,y,Y,z,Z]
if my in list:
   if (my=='A' or my=='a' or my=='E' or my=='e' or my=='I'or my=='i'
        or my=='O' or my=='o' or my=='U' or my=='u'):
      print(my, "is a Vowel")
   else:
      print(my, "is a Consonant")
else:
    print ('HAHAHA')