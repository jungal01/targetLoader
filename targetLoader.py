import pyautogui as kbm
from python_imagesearch.imagesearch import imagesearch


def click_button(img, xMod=0, yMod=0):
    # attempts to locate the image and then clicks the button at the given
    # position. returns true for clicking the image, and false if the image
    # can't be found. Modifiers allow to click an image precisely
    x, y = imagesearch(img)
    if -1 not in (x, y):
        kbm.click(x+xMod, y+yMod)
        return True

    else:
        return False


def alt_tab():
    kbm.hotkey('alt', 'tab')


def open_manager():
    pass


def read_settings():
    pass


def main():
    check = click_button('start.jpg')
    if check:
        click_button('install.jpg')
    else:
        switch = click_button('PS5_logo.jpg')
        if switch:
            main()
        else:
            open_manager()
