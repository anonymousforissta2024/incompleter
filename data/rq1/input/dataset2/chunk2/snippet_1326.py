#Source: https://stackoverflow.com/questions/67249213/why-is-ipython-returning-nameerror-while-decorating-interact
@interact
def show_crank(angle = slider(0,2*pi,pi/20,pi/10,label='angle')):
    center = (0,0)
    endpnt = (cos(angle),sin(angle))
    pltcnt = point(center, size = 50)
    pltend = point(endpnt, size = 50)
    crank = line([center,endpnt])
    (pltcnt + crank + pltend).show(xmin=-1,xmax=1,ymin=-1,ymax=1)