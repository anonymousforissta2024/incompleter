#Source: https://stackoverflow.com/questions/54841247/my-class-is-an-int-when-i-use-it-as-an-inheritance-attribute-error-what-is-th
class WithSrc(Raw):
    def __init__(he,src,dx=0,dy=0,ax=0,ay=0):
        print('Type Raw',type(Raw))
        Raw.__init__(dx,dy,ax,ay)
        he.changeTexture(src) #he.src = src