# colors.py
# rows in level of rarity. level 1 are store bought, 2-4 are mutations, 5 is inbreeding

class Color():
    levelonecolorsdict = {101:"C46210",102:"A57164",103:"FFFF99",104:"F1DDCF",105:"A9A9A9",106:"BA8759"}
    leveltwocolorsdict = {201:"FFBF00",202:"00BFFF",203:"44D7A8",204:"F4BBFF",205:"A52A2A"}
    levelthreecolorsdict = {301:"004225",302:"062A78",303:"560319"}
    levelfourcolorsdict = {401:"000000"}
    levelfivecolorsdict = {501:"964B00",502:"F5F5F5",503:"DCDCDC"}

    @staticmethod
    def getColor(key):
        return Color.levelonecolorsdict[key]

    @staticmethod
    def getColorDict():
        return Color.levelonecolorsdict
