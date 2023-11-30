import pyautogui
import time, random
from PIL import Image
pyautogui.FAILSAFE = True

# Find n click like btn
# delay
# find n click yt-like btn -> scroll if not found
# find n click yt-like btn -> scroll if not found
# delay
# ctrl + w -> close window
# delay
# find  n click conf btn

def delay():

    time.sleep(random.randrange(1,4))

def find_click(img: str, alt_img = None, recall=True, scroll: bool = False, click = True, confidence=0.999):

    print(f"FIND N CLICK: {img}")
    try:
        
        img_pos = pyautogui.locateCenterOnScreen(f"imgs/{img}", grayscale=True, confidence=confidence)
        print(f"{img} FOUND")
        if click:
            pyautogui.click(img_pos)
        else:
            pyautogui.moveTo(img_pos)
        return True
        #m_img.close()
    except Exception as e:
        #print("IMG NO FOUND")
        #print(e)
        if alt_img:
            delay()
            ret = find_click(img=alt_img,  recall=False, confidence=confidence + .15,click=False)
            if ret:
                return
        if (scroll):
            #print("SCROLLING")
            pyautogui.scroll(-1,)
            delay()
        if recall:
            find_click(img=img, recall=recall, scroll=scroll, click=click, confidence=confidence, alt_img=alt_img)

def main():
    
    find_click(img="like-btn.png")
    delay()
    find_click("yt-like-btn.png", alt_img="yt-liked-btn.png", scroll=True, click=True, confidence=.7)
    #delay()
    #print("LIKING")
    #pyautogui.hotkey("shift", "+")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "w")
    find_click("conf-btn.png")
    delay()

if __name__ == "__main__":
    print("ENGINE START")
    for i in range(100):
        print(f"TAKE [{i + 1}]")
        main()
    #find_click("yt-like-btn.png", scroll=True, click=False, confidence=.7)