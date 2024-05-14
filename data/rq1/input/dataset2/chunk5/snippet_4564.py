#Source: https://stackoverflow.com/questions/57717370/typeerror-int-object-is-not-callable-issue
class reflex_vacuum():

  global count


  def count(pos, l, r):
    global count
    global p 
    global left
    global right
    p = pos
    left = l 
    right = r 


    count = 0 

    def clean(pos, l, r):
      global p 
      global left
      global right

      if pos == 'left':
        if l == 1:
          l=0
        pos = 'right'

      else:
        if r == 1:
          r=0
        pos = 'left'
      p = pos
      left = l 
      right = r  

    while left==1 or right==1:
      clean(p, left, right)
      count=count+1 
    print (count)

  def scale(sum):
    global count
    s = 10 - (count/sum)
    print ('The score is ' + str(s) + ' out of 10.')


  print('This program checks the efficiency of the vacuum depending on the vacuum position and dirt placement. The scale is 10 points. each move deducts a point. If move was made with dirt on both sides (thus move was necessary) then the move count is divided by two. \n')    
  print('Starting left with no dirt')
  count('left', 0, 0)
  scale(2)

  print('\nStarting right with no dirt')
  count('right', 0, 0)
  scale(1)

  print('\nStarting left with dirt left')
  count('left', 1, 0)
  scale(1)