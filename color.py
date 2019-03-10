from SMARS_Library3 import SMARSColor
import logging

# for n in range(0, 255):
#     print('N = ' + str(n+1)  + '\033[' + str(n+1) + 'm')
    # print(c.RESET + c.CLEAR_SCREEN)

logging.basicConfig(level=logging.CRITICAL)
logging.propagate = False

C = SMARSColor()
print(C.CLEAR_SCREEN)
print(C.BG_BLUE + C.YELLOW + "Hello World" + C.CLEAR_LINE_FROM_CURSOR)
C.cursor_right(11)
C.cursor_down(3)
print("now here")
# print(C.BG_BLACK + C.RESET + C.CLEAR_LINE)
# print(C.BG_BLUE + "Hello World" + C.CLEAR_LINE)
# C.cursor_left('11')
# print(C.RESET + C.BG_BLACK + C.CLEAR_LINE)

C.set_position(2, 2)
print(C.BG_RED + C.BRIGHTWHITE + "This is position 2, 2")
C.set_position(10, 10)
print(C.BG_BLUE + C.BRIGHTWHITE + "This is position 10, 10" + C.CLEAR_LINE_FROM_CURSOR)
print(C.RESET + C.BG_BLACK + C.CLEAR_SCREEN_FROM_CURSOR)