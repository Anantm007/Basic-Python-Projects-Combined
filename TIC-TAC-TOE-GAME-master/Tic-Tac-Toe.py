def draw(board):
    from IPython.display import clear_output
    clear_output()
    
    print('  ' + '  |  ' '   | ')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('  ' + '  |  ' '   | ')
    print('-------------------')
    print('  ' + '  |  ' '   | ')
    print(' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('  ' + '  |  ' '   | ')
    print('-------------------')
    print('  ' + '  |  ' '   | ')
    print(' ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('  ' + '  |  ' '   | ')
   
    
def place_marker(board,position,marker):
    
    if position>9 or position<0:
              
        print('Invalid choice, Please enter a valid number!')
        return False
    
    if board[position]=='X' or board[position]=='O':
        
        print('Invalid choice, Please enter a valid number!')
        return False
                
    board[position]=marker
    return True
            

def is_full(board):
    
    if board[1]!='1' and board[2]!='2' and board[3]!='3' and board[4]!='4' and board[5]!='5' and board[6]!='6'and board[7]!='7' and board[8]!='8' and board[9]!='9':
        
        return True
    
    return False
    
    
def won(board,marker):
    
    if board[1]==board[2] and board[2]==board[3] and board[3]==marker:
        return True
    
    if board[4]==board[5] and board[5]==board[6] and board[6]==marker:
        return True
    
    if board[7]==board[8] and board[8]==board[9] and board[9]==marker:
        return True
    
    if board[1]==board[4] and board[4]==board[7] and board[7]==marker:
        return True
    
    if board[2]==board[5] and board[5]==board[8] and board[8]==marker:
        return True
    
    if board[3]==board[6] and board[6]==board[9] and board[9]==marker:
        return True
    
    if board[1]==board[5] and board[5]==board[9] and board[9]==marker:
        return True
    
    if board[3]==board[5] and board[5]==board[7] and board[7]==marker:
        return True
    
def play(): 
    
    from IPython.display import clear_output
    clear_output()
    
    print('WELCOME TO THE TIC-TAC-TOE TWO PLAYER GAME\n\n')

    board=['0','1','2','3','4','5','6','7','8','9']
    player=1
    marker=''

    c1=input('Player 1 choose your character  (X or O)    -    ')

    if c1=='X':
        c2='O'
    elif c1=='O':
        c2='X'

    else:
        print('You made an invallid choice')
        play()

    print('\n\nPLAYER 1 CHOSE    -    {}'.format(c1))
    print('\nPLAYER 2 HAS      -    {}'.format(c2))

    import time

    time.sleep(3)

    draw(board)

    player=1
    marker=c1

    k=0

    while 1:
        
        
        full=False
        available=False
        
        while available==False:
            position=int(input('Player {} enter your number '.format(player)))
            available=place_marker(board,position,marker)
        
        draw(board)
    
        if(won(board,marker)):
            print('\n\nPLAYER {} WINS.... CONGRATULATIONS!!!!'.format(player))
            break
        
        if(is_full(board)):
            print('MATCH DRAWN!!!')
            break
            
        

        if player==1:
                player=2
                marker=c2
        else:
                player=1
                marker=c1




play()