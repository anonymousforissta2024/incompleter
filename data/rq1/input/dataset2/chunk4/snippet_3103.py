#Source: https://stackoverflow.com/questions/63684600/typeerror-float-argument-must-be-a-string-or-a-number-not-tuple-valueerror
def integrand_x1(x, Kte_1, Ktc_1, Kae_1, Kac_1, Kre_1, Krc_1, Wdz):
    r = 0.0002
    f = 2/360*10**(-5)
    S = r + f*sin(x) - sqrt(r**2 - (f**2)*(cos(x))**2)
    
    dFa_1 = (Kac_1*S + Kae_1)*Wdz
    dFr_1 = (Krc_1*S + Kre_1)*Wdz
    dFt_1 = (Ktc_1*S + Kte_1)*Wdz
    
    return (cos(30*pi/180)*dFa_1 + sin(30*pi/180)*cos(5.4*pi/180)*dFr_1 - sin(30*pi/180)*sin(5.4*pi/180)*dFt_1)/((cos(30*pi/180))**2 + (sin(30*pi/180))**2*cos(2*5.4*pi/180))
def integrand_x2(x, Kte_2, Ktc_2, Kae_2, Kac_2, Kre_2, Krc_2, Wdz):
    r = 0.0002
    f = 2/360*10**(-5)
    S = r + f*sin(x) - sqrt(r**2 - (f**2)*(cos(x))**2)    

    dFa_2 = (Kac_2*S + Kae_2)*Wdz
    dFr_2 = (Krc_2*S + Kre_2)*Wdz
    dFt_2 = (Ktc_2*S + Kte_2)*Wdz
    
    return (cos(30*pi/180)*dFa_2 + sin(30*pi/180)*cos(5.4*pi/180)*dFr_2 - sin(30*pi/180)*sin(5.4*pi/180)*dFt_2)/((cos(30*pi/180))**2 + (sin(30*pi/180))**2*cos(2*5.4*pi/180))
Kte_1 = df.iloc[i,4]
Kte_2 = df.iloc[i,5]
Kre_1 = df.iloc[i,6]
Kre_2 = df.iloc[i,7]
Kae_1 = df.iloc[i,8]
Kae_2 = df.iloc[i,9]

Ktc_1 = df.iloc[i,11]
Ktc_2 = df.iloc[i,12]
Krc_1 = df.iloc[i,13]
Krc_2 = df.iloc[i,14]
Kac_1 = df.iloc[i,15]
Kac_2 = df.iloc[i,16]

t = (df.iloc[i,0])
Wdz = t/sin(31.19*pi/180)

df['Fx_1'] = 0
df['Fy_1'] = 0
df['Fz_1'] = 0
df['Fx_2'] = 0
df['Fy_2'] = 0
df['Fz_2'] = 0
for i in range(0,1999,1):
    df.Fx_1.iloc[i] = quad(integrand_x1, 95*pi/180, 0, args=(Kte_1, Ktc_1, Kae_1, Kac_1, Kre_1, Krc_1, Wdz)) + quad(integrand_x1, 0, 15*pi/180, args=(Kte_1, Ktc_1, Kae_1, Kac_1, Kre_1, Krc_1, Wdz))