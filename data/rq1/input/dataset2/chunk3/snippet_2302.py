#Source: https://stackoverflow.com/questions/59004021/typeerror-float-object-is-not-callable-issue
from ROOT import TFile, TDirectory, TTree, TH1F, TCanvas
import math
import numpy as np

myfile = TFile("/home/hilary/root/compile/Research/angle_smearing.root")
hist = file.Get("Zenith_Angles")
hgm = TH1F('Fvsx', 'Smearing_Test_1',100,0,90)

for i in range(1, 100,1):
    for y in range (1, 100, 1):
        u = hist.GetBinCenter(i)
        N = hist.GetBinContent(i)
        o = 1
        x = hist.GetBinCenter(y)
        F = (N/(o*math.sqrt(2*math.pi))*math.e((-(x-u)**2)/(2*(o**2)))) 
        hgm.Fill(F)

c1 = TCanvas()
hgm.Draw()
c1.SaveAs("/home/hilary/Desktop/Out_going_muons_etc/smearing_test_1.png")