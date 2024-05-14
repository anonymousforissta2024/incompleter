#Source: https://stackoverflow.com/questions/64863278/what-is-the-solution-to-this-type-error-list-indices-must-be-integers-or-slices
def run2(score,run):
  global appleX,appleY,snakeCoords
  startX=random.randint(20,cellWidth)
  startY=random.randint(20,cellHeight)
  apple=randomlocation()
  appleX=apple['x']*cell_s
  appleY=apple['y']*cell_s
  snakeCoords=[{"x":startX,"y":startY},
               {"x":startX-1,"y":startY},
               {"x":startX-2,"y":startY}]
  direction=RIGHT
  assert win_w % cell_s==0
  assert win_h % cell_s==0
  
  
  while run:
     
     if snakeCoords[head]['x']==19 or snakeCoords[head]['y']==19:
            gameover(window)
            pygame.time.wait(500)
            run=False
            terminate()
            sys.exit()
     if snakeCoords[head]['x']==win_w-20 or snakeCoords[head]['y']==win_h-20:
            gameover(window)
            pygame.time.wait(500)
            run=False                 
            terminate()
            sys.exit()
   
     for body in snakeCoords[1:]:
         if snakeCoords[head]['x']==body['x'] and snakeCoords[head]['y']==body['y']:
             gameover(window)
             pygame.time.wait(500)
             terminate()
             sys.exit()
             
 
     if direction==UP:
          move={'x':snakeCoords[head]['x']-1,'y':snakeCoords[head]['y']}
     if direction==DOWN:
          move={'x':snakeCoords[head]['x']+1,'y':snakeCoords[head]['y']}
     if direction==RIGHT:
          move={'x':snakeCoords[head]['x'],'y':snakeCoords[head]['y']+1}
     if direction==LEFT:
          move={'x':snakeCoords[head]['x'],'y':snakeCoords[head]['y']-1}
     snakeCoords.insert(0,move)
     
     
   
     if apple['x']==snakeCoords[head]['x'] and apple['y']==snakeCoords[head]['y']:
            apple=randomlocation()
            drawgame.drawapple(red)
            score+=1
            if appleX==snakeCoords[head]['x'] and direction==RIGHT:
                newhead=[{'x':startX-3,'y':startY}]
                snakeCoords+=newhead
            if appleX==snakeCoords[head]['x'] and direction==LEFT:
                newhead=[{'x':startX+3,'y':startY}]
                snakeCoords+=newhead
            if appleY==snakeCoords[head]['y'] and direction==UP:
                newhead=[{'x':startX,'y':startY+3}]
                snakeCoords+=newhead
            if appleY==snakeCoords[head]['y'] and direction==DOWN:
                newhead=[{'x':startX,'y':startY-3}]
                snakeCoords+=newhead
            pygame.display.update()
                        

     if score==10:
            gameover(window)
            pygame.time.wait(500)
            
            
   
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
           run=False
           terminate()
           sys.exit()
           
           
        
        if event.type==KEYDOWN:
             if event.key==K_RIGHT and direction!=LEFT:
                direction=RIGHT
             elif event.key==K_LEFT  and direction!=RIGHT:
                direction=LEFT
             elif event.key==K_UP and direction!=DOWN:
                direction=UP
             elif event.key==K_DOWN  and direction!=UP:
                direction=DOWN
             elif event.key==K_ESCAPE :
                terminate()
                sys.exit()
             else:
                print("Invalid Key Pressed")
                
    
if __name__=="__main__":
    main(run)