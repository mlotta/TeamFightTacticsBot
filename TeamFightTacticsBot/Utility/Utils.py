# Python downloaded libraries
import time
import pytesseract as get_text
import pyautogui as auto_gui
import pyscreenshot as image_grab
from PIL import Image
from PIL import ImageOps
import cv2 as cv
import numpy
# Objects
from TeamFightTacticsBot.Structures.Point import Point
from TeamFightTacticsBot.Structures.Player import Player

# Constants
from TeamFightTacticsBot.Utility.Champions import Champions
from TeamFightTacticsBot.Utility.Constants import PERCENTAGE_VARIANCE_ALLOWED
from TeamFightTacticsBot.Utility.Constants import PERCENTAGE_ACCURACY
from TeamFightTacticsBot.Utility.Constants import USER_32
# Global Variable imports
import TeamFightTacticsBot.Utility.Constants as Constants


def scan_shop():
    screen = Image.open("Test1.png")
    shop_slots = []
    shop_slots.append(screen.crop((479, 927, 674, 1073)))
    shop_slots.append(screen.crop((680, 927, 875, 1073)))
    shop_slots.append(screen.crop((881, 927, 1076, 1073)))
    shop_slots.append(screen.crop((1083, 927, 1278, 1073)))
    shop_slots.append(screen.crop((1284, 927, 1479, 1073)))
    return shop_slots


def shop_to_champion():
    champion_slots = []
    shop_slots = scan_shop()
    for slot in shop_slots:
        value = image_to_champion(slot)
        champion_slots.append(value)
    return champion_slots


def image_to_champion(champion_image):
    # Loop through CHARACTER_IMAGE_LIST until accuracy reaches > 90%
    champion_image_pixels = champion_image.load()
    cost = get_cost(champion_image_pixels[170, 140])
    index_start = search_by_cost(cost)
    is_found = False
    while (not is_found) and (index_start <= len(Constants.CHARACTER_IMAGE_LIST)):
        is_found = compare_images_strictly(champion_image, Constants.CHARACTER_IMAGE_LIST[index_start], .9)
        if is_found:
            break
        index_start += 1

    return get_champion_from_list_index(index_start)


def get_cost(pixel):
    if pixel == Constants.COST_CARD_BORDER_COLOR[0]:
        return 1
    if pixel == Constants.COST_CARD_BORDER_COLOR[1]:
        return 2
    if pixel == Constants.COST_CARD_BORDER_COLOR[2]:
        return 3
    if pixel == Constants.COST_CARD_BORDER_COLOR[3]:
        return 4
    if pixel == Constants.COST_CARD_BORDER_COLOR[4]:
        return 5


def search_by_cost(cost):
    if cost is 1:
        return 0
    elif cost is 2:
        return 12
    elif cost is 3:
        return 24
    elif cost is 4:
        return 36
    elif cost is 5:
        return 45
    return 0


def get_champion_from_list_index(index):
    list_of_champion_enums = []
    for champ in Champions:
        list_of_champion_enums.append(champ)

    return list_of_champion_enums[index].value


def get_gold(screen):
    gold_image = screen.crop((868, 880, 910, 913))
    gold = int_from_image(gold_image)
    return gold


def check_place(screen):
    place = screen.load()
    if place[1770, 226] == (145, 109, 49):
        return 1
    elif place[1770, 300] == (145, 109, 49):
        return 2
    elif place[1770, 372] == (145, 109, 49):
        return 3
    elif place[1770, 445] == (145, 109, 49):
        return 4
    elif place[1770, 518] == (145, 109, 49):
        return 5
    elif place[1770, 591] == (145, 109, 49):
        return 6
    elif place[1770, 664] == (145, 109, 49):
        return 7
    elif place[1770, 737] == (145, 109, 49):
        return 8
    else:
        return 8


def get_player_healths(screen, place):
    healths = []
    # if you are in 1st
    if place is 1:
        healths.append(int_from_image(screen.crop((1785, 215, 1827, 240))))
        healths.append(int_from_image(screen.crop((1825, 303, 1850, 319))))
        healths.append(int_from_image(screen.crop((1825, 376, 1850, 392))))
        healths.append(int_from_image(screen.crop((1825, 448, 1850, 464))))
        healths.append(int_from_image(screen.crop((1825, 519, 1850, 537))))
        healths.append(int_from_image(screen.crop((1825, 591, 1850, 609))))
        healths.append(int_from_image(screen.crop((1825, 664, 1850, 682))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 2nd
    elif place is 2:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1785, 285, 1827, 310))))
        healths.append(int_from_image(screen.crop((1825, 373, 1850, 391))))
        healths.append(int_from_image(screen.crop((1825, 446, 1850, 464))))
        healths.append(int_from_image(screen.crop((1825, 519, 1850, 537))))
        healths.append(int_from_image(screen.crop((1825, 591, 1850, 609))))
        healths.append(int_from_image(screen.crop((1825, 664, 1850, 682))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 3rd
    elif place is 3:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1825, 278, 1850, 296))))
        healths.append(int_from_image(screen.crop((1785, 359, 1827, 384))))
        healths.append(int_from_image(screen.crop((1825, 446, 1850, 464))))
        healths.append(int_from_image(screen.crop((1825, 519, 1850, 537))))
        healths.append(int_from_image(screen.crop((1825, 591, 1850, 609))))
        healths.append(int_from_image(screen.crop((1825, 664, 1850, 682))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 4th
    elif place is 4:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1825, 278, 1850, 296))))
        healths.append(int_from_image(screen.crop((1825, 351, 1850, 369))))
        healths.append(int_from_image(screen.crop((1785, 432, 1827, 457))))
        healths.append(int_from_image(screen.crop((1825, 519, 1850, 537))))
        healths.append(int_from_image(screen.crop((1825, 591, 1850, 609))))
        healths.append(int_from_image(screen.crop((1825, 664, 1850, 682))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 5th
    elif place is 5:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1825, 278, 1850, 296))))
        healths.append(int_from_image(screen.crop((1825, 351, 1850, 369))))
        healths.append(int_from_image(screen.crop((1825, 424, 1850, 442))))
        healths.append(int_from_image(screen.crop((1785, 505, 1827, 530))))
        healths.append(int_from_image(screen.crop((1825, 591, 1850, 609))))
        healths.append(int_from_image(screen.crop((1825, 664, 1850, 682))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 6th
    elif place is 6:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1825, 278, 1850, 296))))
        healths.append(int_from_image(screen.crop((1825, 351, 1850, 369))))
        healths.append(int_from_image(screen.crop((1825, 424, 1850, 442))))
        healths.append(int_from_image(screen.crop((1825, 497, 1850, 515))))
        healths.append(int_from_image(screen.crop((1785, 578, 1827, 603))))
        healths.append(int_from_image(screen.crop((1825, 664, 1850, 682))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 7th
    elif place is 7:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1825, 278, 1850, 296))))
        healths.append(int_from_image(screen.crop((1825, 351, 1850, 369))))
        healths.append(int_from_image(screen.crop((1825, 424, 1850, 442))))
        healths.append(int_from_image(screen.crop((1825, 497, 1850, 515))))
        healths.append(int_from_image(screen.crop((1825, 570, 1850, 588))))
        healths.append(int_from_image(screen.crop((1785, 651, 1827, 676))))
        healths.append(int_from_image(screen.crop((1825, 737, 1850, 755))))
    # if you are in 8th
    elif place is 8:
        healths.append(int_from_image(screen.crop((1825, 205, 1850, 223))))
        healths.append(int_from_image(screen.crop((1825, 278, 1850, 296))))
        healths.append(int_from_image(screen.crop((1825, 351, 1850, 369))))
        healths.append(int_from_image(screen.crop((1825, 424, 1850, 442))))
        healths.append(int_from_image(screen.crop((1825, 497, 1850, 515))))
        healths.append(int_from_image(screen.crop((1825, 570, 1850, 588))))
        healths.append(int_from_image(screen.crop((1825, 643, 1850, 661))))
        healths.append(int_from_image(screen.crop((1785, 724, 1827, 749))))

    return healths


def get_player_names(screen, place):
    players = []
    # if you are in 1st
    if place is 1:
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 303, 1815, 319))))
        players.append(string_from_image(screen.crop((1712, 376, 1815, 392))))
        players.append(string_from_image(screen.crop((1712, 448, 1815, 464))))
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 2nd
    elif place is 2:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 373, 1815, 391))))
        players.append(string_from_image(screen.crop((1712, 446, 1815, 464))))
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 3rd
    elif place is 3:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 446, 1815, 464))))
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 4th
    elif place is 4:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 519, 1815, 537))))
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 5th
    elif place is 5:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 591, 1815, 609))))
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 6th
    elif place is 6:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append(string_from_image(screen.crop((1712, 497, 1815, 515))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 664, 1815, 682))))
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 7th
    elif place is 7:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append(string_from_image(screen.crop((1712, 497, 1815, 515))))
        players.append(string_from_image(screen.crop((1712, 570, 1815, 588))))
        players.append("Me")
        players.append(string_from_image(screen.crop((1712, 737, 1815, 755))))
    # if you are in 8th
    elif place is 8:
        players.append(string_from_image(screen.crop((1712, 205, 1815, 223))))
        players.append(string_from_image(screen.crop((1712, 278, 1815, 296))))
        players.append(string_from_image(screen.crop((1712, 351, 1815, 369))))
        players.append(string_from_image(screen.crop((1712, 424, 1815, 442))))
        players.append(string_from_image(screen.crop((1712, 497, 1815, 515))))
        players.append(string_from_image(screen.crop((1712, 570, 1815, 588))))
        players.append(string_from_image(screen.crop((1712, 643, 1815, 661))))
        players.append("Me")

    return players


def string_from_image(image):
    new_image = cv.bilateralFilter(numpy.array(image), 9,  75, 75)
    new_image = cv.threshold(new_image, 127,  255, cv.THRESH_BINARY)[1]
    im = Image.fromarray(new_image)
    im = ImageOps.invert(im)
    # im.show()
    name = get_text.image_to_string(im, lang='eng',
                                    config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    # print(name)
    return name


def int_from_image(image):
    new_image = cv.bilateralFilter(numpy.array(image), 9,  75, 75)
    new_image = cv.threshold(new_image, 127,  255, cv.THRESH_BINARY)[1]
    im = Image.fromarray(new_image)
    im = ImageOps.invert(im)
    im = im.resize((int(2*im.size[0]), int(2*im.size[1])))
    # im.show()
    num = get_text.image_to_string(im, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return num


def get_into_game():
    play_button_location = find_play_button()

    if play_button_location is None:
        print("Could not find league client")
        return

    click_through_to_game(play_button_location)
    Constants.in_game = True


def click_through_to_game(point):
    # x, y is the locations of play button
    x = point.x
    y = point.y

    # This clicks on the play button
    click(x + 55, y + 10)

    # This clicks on the Team Fight Tactics part of game modes
    time.sleep(.5)
    click(x + 840, y + 250)

    # This clicks on the confirm for the game mode
    time.sleep(.5)
    click(x + 500, y + 666)

    # This clicks on the "Find Match" button once in a TFT lobby.
    time.sleep(3)
    click(x + 500, y + 666)

    # This checks if a queue is pops and then clicks on (Accept!/Decline)
    check_queue(point)


def check_queue(point):
    # get_screen()
    x = point.x
    y = point.y

    image = image_grab.grab(bbox=(x + 469, y + 234, x + 744, y + 424))
    image.save(get_analyzable_relative_path() + "queue_screenshot.png")
    queue_screenshot = Image.open(get_analyzable_relative_path() + "queue_screenshot.png")
    queue_check = Image.open(get_button_relative_path() + "queue_check.PNG")

    popped = False
    while not popped:
        popped = compare_images(queue_screenshot, queue_check)
        image = image_grab.grab(bbox=(x + 468, y + 234, x + 743, y + 424))
        image.save(get_analyzable_relative_path() + "queue_screenshot.png")
        queue_screenshot = Image.open(get_analyzable_relative_path() + "queue_screenshot.png")
        time.sleep(.5)

    # Accept queue
    # click(x + 600, y + 540)

    # Decline queue
    click(x + 600, y + 600)


def find_play_button():
    get_screen()
    screen_image = Image.open(get_analyzable_relative_path() + "screen.png")
    screen = screen_image.load()

    play_button_image = Image.open(get_button_relative_path() + "play_button.PNG")
    play_button_pixels = play_button_image.convert('RGB')
    play_button_pixels = play_button_pixels.load()

    for x in range(get_screensize()[0]):
        for y in range(get_screensize()[1]):
            if compare_pixels_strictly(screen[x, y], play_button_pixels[0, 0], 25):
                cropped_image = screen_image.crop((x, y, x + 154, y + 38))
                if compare_images(cropped_image, play_button_image):
                    return Point(x, y)

    return None


def compare_images(tested, master):
    return compare_pixels_strictly(tested, master, PERCENTAGE_ACCURACY)


def compare_images_strictly(tested, master, variance_allowed):
    search = tested.load()
    search_from = master.load()

    width, height = master.size
    pixels_wanted = (width * height) * variance_allowed
    pixels_accepted = 0

    for x in range(width):
        for y in range(height):
            if pixels_wanted < pixels_accepted:
                return True
            is_similar = compare_pixels(search[x, y], search_from[x, y])
            if is_similar:
                pixels_accepted += 1

    return False


def compare_pixels(tested, master):
    variance_allowed = (255 * PERCENTAGE_VARIANCE_ALLOWED) * 3

    return compare_pixels_strictly(tested, master, variance_allowed)


def compare_pixels_strictly(tested, master, variance_allowed):
    # Each input is a pixel with array values as such: [R, G, B, A]

    # Variance for red component
    variance = abs(master[0] - tested[0])
    # Variance for green component
    variance += abs(master[1] - tested[1])
    # Variance for blue component
    variance += abs(master[2] - tested[2])

    return variance < variance_allowed


def get_button_relative_path():
    return Constants.MAIN_FILE_LOCATION + "/Resources/Final/Buttons/"


def get_analyzable_relative_path():
    return Constants.MAIN_FILE_LOCATION + "/Resources/Analyzable/"


def get_screen():
    screenshot_name = get_analyzable_relative_path() + "screen.png"

    image = auto_gui.grab()
    image.save(screenshot_name)

    return Image.open(screenshot_name)


def get_screensize():
    return USER_32.GetSystemMetrics(0), USER_32.GetSystemMetrics(1)


def click(x, y):
    auto_gui.click(x, y)
    print("Clicked at (" + str(x) + ", " + str(y) + ")")
