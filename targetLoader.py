import pyautogui as kbm
from python_imagesearch.imagesearch import imagesearch


def find_img(img):
    # locates an image and returns the position. Returns -1, -1 otherwise
    return imagesearch(img)


def click_button(pos):
    # clicks the button at the given position and returns true for clicking the
    # image. If the position is -1, the image wasn't clicked and returns false
    if -1 not in pos:
        kbm.click(pos)
        return True

    else:
        return False


def alt_tab():
    kbm.keyDown('alt')
    kbm.press('tab')
    pos = find_img('preview.jpg')
    result = click_button(pos)
    kbm.keyUp('alt')
    return result


def open_manager():
    pass


read_settings():
    pass
