from stockfish import Stockfish
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time

def get_key(val):
    for key, value in x_coords.items():
         if val == value:
             return key
def get_key1(val):
    for key, value in y_coords.items():
         if val == value:
             return key
options=Options()
options.add_argument('start-maximized')
stockfish=Stockfish(r"C:\Users\DANDELIA\Downloads\stockfish-11-win\stockfish-11-win\Windows\stockfish_20011801_x64.exe")
driver=webdriver.Chrome(chrome_options=options,executable_path='C:\Program Files (x86)\chromedriver.exe')
driver.get('https://lichess.org/login')  #The following steps are for starting the game
link=driver.find_element_by_xpath('//*[@id="form3-username"]')
link.click()
link.send_keys('Holmes1109')
link=driver.find_element_by_xpath('//*[@id="form3-password"]')
link.click()
link.send_keys('Holmes@1109')
link=driver.find_element_by_xpath('//*[@id="main-wrap"]/main/form/div[1]/button')
link.click()
time.sleep(2)
actions=ActionChains(driver)
actions.move_by_offset(1300,460).click().perform()

time.sleep(5)
link=driver.find_element_by_xpath('//*[@id="modal-wrap"]/div/form/div[5]/button[1]')
link.click()
time.sleep(5)
stockfish.set_fen_position('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1') # Setting the starting position of chess board
#71.2 px
#440 x
#35 y
#Making dictionary for mapping x and y coordinates with screen pixels
x_coords=dict()
y_coords=dict()
#for i in range(8):
    #x_coords[str(chr(97+i))]=int(970-(i*71.2))
    #y_coords[str(i+1)]=int(40+(i*71.2))
#print(x_coords)
#print(y_coords)
i=0

#print(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[1]').location)
#print(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[2]').location)
for i in range(1,9):
    y_coords[str(i)]=int(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/coords[1]/coord['+str(i)+']').location['y'])-1+40
    x_coords[str(chr(96+i))]=int(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/coords[2]/coord['+str(i)+']').location['x'])+1+40
print(x_coords)
print(y_coords)
link=driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-resize')
link.click()
#//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/piece[1]
while True:

    moves=[]
    time.sleep(5)
    #links=driver.find_elements_by_xpath('//*[@id="main-wrap"]/main/div[1]/rm6/l4x/u8t')
    #print(len(link))
    #for link in links:
        #if len(str(link.text))==2:
            #moves.append(str(link.text))
        #elif len(str(link.text))==3:
            #moves.append(str(link.text[1:]))
        #elif len(str(link.text))==5:
            #moves.append(str(link.text[2:4]))
        #elif (len(str(link.text)))==4:
            #moves.append(str(link.text[2:]))
    xcoord2=get_key(int(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[1]').location['x'])+40)
    ycoord2 = get_key1(int(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[1]').location['y']) + 40)
    xcoord1=get_key(int(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[2]').location['x']+40))
    ycoord1 = get_key1(int(driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[2]').location['y'] + 40))
    moves.append(str(xcoord1)+str(ycoord1)+str(xcoord2)+str(ycoord2))
    if i%2==0: #if i is even then it is white's turn and it will skip that part
        i+=1
        continue
    print(moves)
    stockfish.set_position(moves)
    stockfish.get_fen_position()
    print()
    next_move = str(stockfish.get_best_move())
    print(next_move)
    print(driver.title)
    #spliting next move and mapping it with pixels from the above dictionaries
    xcoord1=int(x_coords[next_move[0]])
    ycoord1=int(y_coords[next_move[1]])
    xcoord2=int(x_coords[next_move[2]])
    ycoord2=int(y_coords[next_move[3]])
    print(xcoord1,ycoord1,xcoord2,ycoord2)
    time.sleep(5)
    #element=driver.find_element_by_xpath('/html/body')
    actions=ActionChains(driver)
    actions.move_by_offset(int(xcoord1),int(ycoord1)).click().perform()
    actions.move_by_offset(int(xcoord2),int(ycoord2)).click().perform()
    #time.sleep(2)
    #actions_1=ActionChains(driver)
    #actions_1.move_by_offset((xcoord2,ycoord2)).click().perform()
    #actions.drag_and_drop((xcoord1,ycoord1),(xcoord2,ycoord2)).perform()
    i+=1
