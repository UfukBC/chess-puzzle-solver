import pyautogui
import time
import keyboard
import cv2
import numpy
import winsound



class Piece:
   Empty = 0 
   Pawn = 1
   Rook = 2
   Knight = 3
   Bishop = 4
   Queen = 5
   King = 6

   White = 8
   Black = 16

templateWWKI =cv2.imread('Images/wwki.png',0)
templateWBKI =cv2.imread('Images/wbki.png',0)
templateBWKI =cv2.imread('Images/bwki.png',0)
templateBBKI =cv2.imread('Images/bbki.png',0)

templateWWQ =cv2.imread('Images/wwq.png',0)
templateWBQ =cv2.imread('Images/wbq.png',0)
templateBWQ =cv2.imread('Images/bwq.png',0)
templateBBQ =cv2.imread('Images/bbq.png',0)

templateWWB =cv2.imread('Images/wwb.png',0)
templateWBB =cv2.imread('Images/wbb.png',0)
templateBWB =cv2.imread('Images/bwb.png',0)
templateBBB =cv2.imread('Images/bbb.png',0)

templateWWK =cv2.imread('Images/wwk.png',0)
templateWBK =cv2.imread('Images/wbk.png',0)
templateBWK =cv2.imread('Images/bwk.png',0)
templateBBK =cv2.imread('Images/bbk.png',0)

templateWWR =cv2.imread('Images/wwr.png',0)
templateWBR =cv2.imread('Images/wbr.png',0)
templateBWR =cv2.imread('Images/bwr.png',0)
templateBBR =cv2.imread('Images/bbr.png',0)

templateWWP =cv2.imread('Images/wwp.png',0)
templateWBP =cv2.imread('Images/wbp.png',0)
templateBWP =cv2.imread('Images/bwp.png',0)
templateBBP =cv2.imread('Images/bbp.png',0)

WhiteLongCastle = False
WhiteShortCastle = False
BlackLongCastle = False
BlackShortCastle = False

i=0
Board =numpy.zeros(64)
Control = True
time.sleep(2)  # Wait before checking for the image

def CompareImgsB(templateDef,picGrayDef,pieceDef):#Black squares image compare
    global i
    result = cv2.matchTemplate(picGrayDef, templateDef, cv2.TM_CCOEFF_NORMED) #How similar are the images 
    threshold = 0.8
    loc = numpy.where(result >= threshold) #are the images matching more than threshold value
    if len(loc[0]) > 0:
        Board[i]=pieceDef
   
    

def CompareImgsW(templateDef,picGrayDef,pieceDef):#White squares image compare 
    global i
    result = cv2.matchTemplate(picGrayDef, templateDef, cv2.TM_CCOEFF_NORMED) #How similar are the images 
    threshold = 0.8
    loc = numpy.where(result >= threshold) #are the images matching more than threshold value
    if len(loc[0]) > 0:
        Board[i]=pieceDef
       

    
   
def TakeSs(xPos,yPos):
    pic=pyautogui.screenshot(region=(xPos,yPos,111,111))
    pic=numpy.array(pic)
    picGray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY) #Convert bgr to grayscale
    return picGray

while Control==True:
    if keyboard.is_pressed('k'):
        Control = False

    try:
     
     for y in range (135,1023,111):
        for x in range (373,1261,111):
         ss=TakeSs(x,y)
         if((x+y)%2==0): #Is the square white 
            CompareImgsW(templateWWR,ss,Piece.Rook | Piece.White)
            CompareImgsW(templateWBR,ss,Piece.Rook | Piece.Black)

            CompareImgsW(templateWWP,ss,Piece.Pawn | Piece.White)
            CompareImgsW(templateWBP,ss,Piece.Pawn | Piece.Black)

            CompareImgsW(templateWWK,ss,Piece.Knight | Piece.White)
            CompareImgsW(templateWBK,ss,Piece.Knight | Piece.Black)

            CompareImgsW(templateWWB,ss,Piece.Bishop | Piece.White)
            CompareImgsW(templateWBB,ss,Piece.Bishop | Piece.Black)

            CompareImgsW(templateWWQ,ss,Piece.Queen | Piece.White)
            CompareImgsW(templateWBQ,ss,Piece.Queen | Piece.Black)

            CompareImgsW(templateWWKI,ss,Piece.King | Piece.White)
            CompareImgsW(templateWBKI,ss,Piece.King | Piece.Black)
            
            i+=1
         else:
            CompareImgsB(templateBWR,ss,Piece.Rook | Piece.White)
            CompareImgsW(templateBBR,ss,Piece.Rook | Piece.Black)

            CompareImgsW(templateBWP,ss,Piece.Pawn | Piece.White)
            CompareImgsW(templateBBP,ss,Piece.Pawn | Piece.Black)

            CompareImgsW(templateBWK,ss,Piece.Knight | Piece.White)
            CompareImgsW(templateBBK,ss,Piece.Knight | Piece.Black)

            CompareImgsW(templateBWB,ss,Piece.Bishop | Piece.White)
            CompareImgsW(templateBBB,ss,Piece.Bishop | Piece.Black)

            CompareImgsW(templateBWQ,ss,Piece.Queen | Piece.White)
            CompareImgsW(templateBBQ,ss,Piece.Queen | Piece.Black)

            CompareImgsW(templateBWKI,ss,Piece.King | Piece.White)
            CompareImgsW(templateBBKI,ss,Piece.King | Piece.Black)
            i+=1


        Control=False  

    except:
        print('I cant see')
        time.sleep(1)   


if(Board[5]==22 and Board[8]==18):
    BlackShortCastle=True
if(Board[5]==22 and Board[1]==18):
    BlackShortCastle=True

if(Board[60]==14 and Board[56]==10):
    BlackShortCastle=True
if(Board[60]==14 and Board[63]==10):
    BlackShortCastle=True


print(Board[63])
winsound.Beep(2500,100)

# for Items in Board:
#            print(Items)
