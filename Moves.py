import Code
import subprocess
import pyperclip
from stockfish import Stockfish

stockfish = Stockfish(path="C:\stockfish\stockfish-windows-x86-64-avx2.exe")


def ConverToFen(BoardArray):
    color=input("Are you playing white or black w/b: ")
    previousDigit= 0
    fen= ''
    loopCounter = 0
    for pieces in BoardArray:
        
        

        if(loopCounter%8==0 and loopCounter!=0):
            if previousDigit > 0:
                fen += str(previousDigit)
            fen+="/"
            previousDigit=0


        match pieces:
            case 9:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="P"
                previousDigit=0
            case 10:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="R"
                previousDigit=0
            case 11:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="N"
                previousDigit=0
            case 12:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="B"
                previousDigit=0
            case 13:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="Q"
                previousDigit=0
            case 14:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="K"
                previousDigit=0
            case 17:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+='p'
                previousDigit=0
            case 18:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="r"
                previousDigit=0
            case 19:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="n"
                previousDigit=0
            case 20:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="b"
                previousDigit=0
            case 21:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="q"
                previousDigit=0
            case 22:
                if previousDigit > 0:
                    fen += str(previousDigit)
                fen+="k"
                previousDigit=0
            case _:
                previousDigit += 1

        if(loopCounter==63 and previousDigit>0):
            fen+=str(previousDigit)

        loopCounter+=1
    if(color=="b"):
        fen=fen[::-1]
    fen =  fen + ' '+color+' '
    if(Code.WhiteShortCastle==True):
        fen= fen + "K"
    if(Code.WhiteLongCastle==True):
        fen= fen + "Q"
    if(Code.BlackShortCastle==True):
        fen= fen + "k"
    if(Code.BlackLongCastle==True):
        fen= fen + "q"
    if(Code.BlackLongCastle==False and Code.BlackShortCastle==False and Code.WhiteLongCastle==False and Code.WhiteShortCastle==False):
        fen= fen + "-"
    fen= fen + " - 0 1"    
    return fen   
 

def get_best_line(moveAmount):
    stockfish.set_depth(20)
    stockfish.set_fen_position(fen)
    myLine = []
    otherLine = []
    for i in range(moveAmount):
        bestMove= stockfish.get_best_move()
        if not bestMove:
            break
        if i % 2==0:
            myLine.append(bestMove)
        else:
            otherLine.append(bestMove)

        stockfish.make_moves_from_current_position([bestMove])

    return myLine



fen = ConverToFen(Code.Board)

pyperclip.copy(fen)
print(fen)

bestLine=get_best_line(7)


print(bestLine)



#r1bq1rk1/p3bppp/1p1ppn2/6B1/2PN4/2NQ4/PP3PPP/4RRK1 b - - 0 1



#************************************************************************************************************************



# engine =subprocess.Popen(
#     stockfish, universal_newlines=True,
#     stdin=subprocess.PIPE, stdout=subprocess.PIPE
# )


        
# def stockfish_command(command):
#     engine.stdin.write(command + "\n")
#     engine.stdin.flush()
#     response = ""
#     while True:
#         text = engine.stdout.readline().strip()
#         if text == "readyok":
#             break
#         response += text + "\n"
#     return response

# def set_position(fen_string):
#     stockfish_command(f"position fen {fen_string}")

# def get_best_move():
#     engine.stdin.write("go depth 15\n")
#     engine.stdin.flush()
#     while True:
#         output = engine.stdout.readline().strip()
#         if output.startswith("bestmove"):
#             return output.split(" ")[1]
        

# set_position(fen)
# best_move = get_best_move()

# print(best_move)


