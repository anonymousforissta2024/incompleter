#Source: https://stackoverflow.com/questions/57118363/why-is-this-for-loop-throwing-a-typeerror
class Image:

    def drawCircle(self, centerX, centerY, radius):
        sin45 = 0.70710678118                                               
        distance = radius/(2*sin45)
        for i in range(radius,distance,-1.0): ####This is the error line####
            j = math.sqrt(r*r - i*i)
            for k in range(-j, j, 1):
                self.writePixel(self.centerX - k, self.enterY + i)
                self.writePixel(self.centerX - k, self.enterY - i)
                self.writePixel(self.centerX + i, self.enterY + i)
                self.writePixel(self.centerX - i, self.enterY - i)

'''Testing the code'''
obj = Image()
obj.drawCircle(35.0, 35.0, 35.0)