""" draw object using simplegui api """
# "draw" - generates widget for the President card game.
#
# I was trying to generate a playable version of the french canadian card game
# I am using  CodeSkulptor and SimpleGUI from An Introduction to Interactive Programming in Python
# Since it keeps the game has browser based therefore accessible to all devicess
# Please enjoy the game
#
# Programming - Samuel Paul (samuelspaul@gmail.com)
# Graphics    - Cards images from An Introduction to Interactive Programming in Python
#
# Current Version (v1.0 - 21 January 2024):
# File saved in : https://py3.codeskulptor.org/#user309_Qz4BBPIZtH_11.py
import random


try:
    folder = "https://dl.dropboxusercontent.com/scl/fi" #pylint: disable=invalid-name
    img_src = [ f"{folder}/ug7cyw615z3hb3grxyl5m/cards_jfitz.png?rlkey=oafwht2i4gbtxh4onrhpiqjt1&dl=0",
                f"{folder}/scl/fi/wvecry6r03wxncg3usuiu/cards_joker.png?rlkey=u6sliqta64fytbc576jtrfypo&dl=0",
                f"{folder}/jsqle71poqj6w3da5ovdi/cards_jfitz_selected.png?rlkey=elwgc0ch3sq34ftphtkrlru38&dl=0",
                f"{folder}/t23tgydsvr2qzzagkmclw/cards_joker_selected.png?rlkey=lmewxxx05kofsklrxj06i0i73&dl=0",
                f"{folder}/34t71zfqu7f2iegecgzw5/card_jfitz_back.png?rlkey=ap1m5l5nodi0pju7lgft4q23i&dl=0",

                f"{folder}/bnu6qeg5ronu6egku88k7/small_cards_jfitz.png?rlkey=cmrt2yzra4c945sp4tdoc5vp4&dl=0",
                f"{folder}/s883xcegdx6t75sv3g5kc/small_cards_joker.png?rlkey=njhazyuza99tfc2v5tiq5xxgo&dl=0",
                f"{folder}/b4zln2w1c5md9ymppzebh/small_cards_jfitz_selected.png?rlkey=gxa867awfsc97fq5ubcafayzz&dl=0",
                f"{folder}/p6ypy5vioqsaka342ma12/small_cards_joker_selected.png?rlkey=h5qyu35xacrqjmzcs4de74zp6&dl=0",
                f"{folder}/kpdwd0bss0coo796ctptl/small_card_jfitz_back.png?rlkey=eqgz4k8qkmtiohcv89cry3wve&dl=0",

            f"{folder}/ej5xs39tsoa44k0cf4hvb/big_cards_jfitz.png?rlkey=qjzd8csibekb89g5lwqzc1ygq&dl=0",
            f"{folder}/bje41q63dxri5xbrihnrh/big_cards_joker.png?rlkey=usxw4heqrnpst1dahjgyech3o&dl=0",
            f"{folder}/jklf0leioufbqbpidj9ft/big_cards_jfitz_selected.png?rlkey=35d7sipo93su3r90vhzjd9fbw&dl=0",
            f"{folder}/g1by65rm3v9mgygr311tk/big_cards_joker_selected.png?rlkey=h9x53hzwp32yxp1cd48f77u2b&dl=0",
            f"{folder}/xeobp120otuarszm58fie/big_card_jfitz_back.png?rlkey=qk77v3srt1k0pgnori06txmbt&dl=0",
            ]
    import simplegui # type: ignore
    from user309_Kd3jylJSQd_0 import Hand, Card, RANKS, SUITS, card_seq_increment
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    import os
    folder = os.path.dirname(os.path.abspath(__file__)) + "/../img/"
    img_src = [f"{folder}/cards_jfitz.png", f"{folder}/cards_joker.png", f"{folder}/cards_jfitz_selected.png", f"{folder}/cards_joker_selected.png",
               f"{folder}/card_jfitz_back.png", f"{folder}/small_cards_jfitz.png", f"{folder}/small_cards_joker.png", 
               f"{folder}/small_cards_jfitz_selected.png", f"{folder}/small_cards_joker_selected.png", f"{folder}/small_card_jfitz_back.png",
               f"{folder}/big_cards_jfitz.png", f"{folder}/big_cards_joker.png", f"{folder}/big_cards_jfitz_selected.png",
               f"{folder}/big_cards_joker_selected.png", f"{folder}/big_card_jfitz_back.png"]
    from card import Hand, Card, RANKS, SUITS, card_seq_increment

screen_size = "Normal" #pylint: disable=invalid-name

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image(img_src[0])
card_joker = simplegui.load_image(img_src[1])
card_images_selected = simplegui.load_image(img_src[2])
card_joker_selected = simplegui.load_image(img_src[3])
card_back = simplegui.load_image(img_src[4])


small_card_images = simplegui.load_image(img_src[5])
small_card_joker = simplegui.load_image(img_src[6])
small_card_images_selected = simplegui.load_image(img_src[7])
small_card_joker_selected = simplegui.load_image(img_src[8])
small_card_back = simplegui.load_image(img_src[9])


big_card_images = simplegui.load_image(img_src[10])
big_card_joker = simplegui.load_image(img_src[11])
big_card_images_selected = simplegui.load_image(img_src[12])
big_card_joker_selected = simplegui.load_image(img_src[13])
big_card_back = simplegui.load_image(img_src[14])

PLAYER_NAMES = ["Eric", "Julien", "Guillaume", "HongYu", "Francois", "Daniel",\
                "Philippe", "Simon", "Alexandre", "Jean-Serge", "Sepehr", 'Jerry',\
                "Charlou", "Raphael", "Nathan", "Antoine", "Hugues", "Carlos",
                "Jennifer", "Hadhami", "Marnie", "Caroline", "Catherine",\
                "Sara", "Anne", "Stephanie", "Perline", "Audree", "Louise",\
                "Marie", "Genevieve", "Chloee", "Helene", "Mika", "Myriam",\
                "Irma",  "Melanie", "Marlene", "Robert", "Amir", "Richard",\
                "Jim", "Moses", "Evan", "Emile", "Eduardo"]

def get_resize_item(val):
    """ resize_item """
    d_val = {"Big":1.5, "Normal":1, "Small":0.5}
    const = d_val[screen_size]
    tmp_x = val[0]*const
    tmp_y = val[1]*const
    return [tmp_x, tmp_y]

def get_resize(val):
    """ resize values in cellphone mode """
    out = []
    for count, _ in enumerate(val):
        out.append(get_resize_item(val[count]))
    return out

def draw_resize_line(canvas, line, pos, font, color):
    """ Resize line text """
    d_val = {"Big":1.5, "Normal":1, "Small":0.5}
    const = d_val[screen_size]
    canvas.draw_text(line, get_resize_item(pos), int(font*const), color)

def draw_resize_polygon(canvas, pos, width, color, color1):
    """ Resize polygon """
    canvas.draw_polygon(get_resize(pos),  width, color, color1)

def draw_resize_card(canvas, rank, suit, selected, pos):
    """ Resize card image """
    if rank == "O":
        d_card = { "Big": {False:big_card_joker, True:big_card_joker_selected},
                   "Normal": {False:card_joker, True:card_joker_selected},
                   "Small":  {False:small_card_joker, True:small_card_joker_selected}}
        card_loc = get_resize_item( CARD_CENTER )
    else :
        d_card = { "Big": {False:big_card_images, True:big_card_images_selected},
                   "Normal": {False:card_images, True:card_images_selected},
                   "Small":  {False:small_card_images, True:small_card_images_selected}}
        tmp_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(suit))
        card_loc = get_resize_item(tmp_loc)
    card_img = d_card[screen_size][selected]
    canvas.draw_image(card_img, card_loc, get_resize_item(CARD_SIZE),
                      get_resize_item([pos[0] +CARD_CENTER[0], pos[1] + CARD_CENTER[1]]),
                      get_resize_item(CARD_SIZE))

def get_names(nb=4):
    """ get player names """
    l_val = list(PLAYER_NAMES)
    random.shuffle(l_val)
    return l_val[:nb]

def gen_points(pos_x, pos_y, len_x, len_y, margin=0):
    """ generate list of coordinates """
    point = [ (pos_x         + margin, pos_y         + margin),
              (pos_x + len_x - margin, pos_y         + margin),
              (pos_x + len_x - margin, pos_y + len_y - margin),
              (pos_x         + margin, pos_y + len_y - margin)]
    return point

class Rectangle:
    """ create rectangle class """

    def __init__(self, posx, posy, lenx, leny, col1="black", col2 = "white", text="text", ctext="blue", font = 24):
        """ Create rectangle """
        self._x = posx
        self._y = posy
        self._lx = lenx
        self._ly = leny
        self._c1 = col1
        self._c2 = col2
        self._t  = text
        self._ct = ctext
        self._f  = font
        self._pt  = gen_points(self._x, self._y, self._lx, self._ly, 0)
        self._pt2 = gen_points(self._x, self._y, self._lx, self._ly, 2)
        self._pt3 = gen_points(self._x, self._y, self._lx, self._ly, 3)
        self._pt4 = gen_points(self._x, self._y, self._lx, self._ly, 4)
        self._sl = False

    def get_pos(self):
        """ return pos """
        return [self._x, self._y]

    def set_pos(self, posx, posy):
        """ return pos """
        self._x = posx
        self._y = posy
        self._pt  = gen_points(self._x, self._y, self._lx, self._ly, 0)
        self._pt2 = gen_points(self._x, self._y, self._lx, self._ly, 2)
        self._pt3 = gen_points(self._x, self._y, self._lx, self._ly, 3)
        self._pt4 = gen_points(self._x, self._y, self._lx, self._ly, 4)

    def set_selected(self, selected:bool):
        """ set text """
        self._sl = selected

    def get_selected(self):
        """ get text """
        return self._sl

    def set_text_color(self, ctext):
        """ set text """
        self._ct = ctext

    def get_text_color(self):
        """ get text """
        return str(self._ct)

    def set_text(self, text):
        """ set text """
        self._t = text

    def get_text(self):
        """ get text """
        return str(self._t)

    def draw(self, canvas):
        """ draw rectangle"""
        d_col = {True:self._ct, False:self._c2}
        draw_resize_polygon(canvas, self._pt,  1, self._c1, self._c1)
        draw_resize_polygon(canvas, self._pt2, 1, self._c2, self._c2)
        draw_resize_polygon(canvas, self._pt3, 1, self._c1, self._c1)
        draw_resize_polygon(canvas, self._pt4, 1, d_col[self._sl], d_col[self._sl])
        text = self._t.splitlines()
        d_col = {True:self._ct, False:self._c1}
        count = 1
        for line in text:
            if self._sl:
                color = self._c2
            else:
                color = d_col[count%2==1]
            draw_resize_line(canvas, line, [self._x + self._f, self._y + count*self._f], self._f, color)
            count += 1

    def is_click(self, pos):
        """ return true if click inside rectangle """
        d_val = {"Big":1.5, "Normal":1, "Small":0.5}
        const = d_val[screen_size]
        tmp = [0,0]
        tmp[0] = int(pos[0]/const)
        tmp[1] = int(pos[1]/const)
        pos = tmp
        val = False
        if  pos[0] >= self._x and pos[0] <= self._x + self._lx and \
            pos[1] >= self._y and pos[1] <= self._y + self._ly:
            val = True
        return val

class DrawTurn(Rectangle):
    """ create Draw Turn """

    def __init__(self, posx, posy):
        """ Create DrawCard """
        super().__init__(posx, posy, 600, 450, text="")
        self.count = 1
        self.l_players = []
        self.players = []
        self.hands = []

    def clear_hands(self):
        """ clean hands"""
        self.l_players = []
        self.players = []
        self.hands = []

    def increment_turn(self, count=False):
        """ increment turn """
        if count:
            self.count = count
        else:
            self.count += 1
        self.clear_hands()
        self.set_text(f"#{self.count}")

    def set_game_results(self, players):
        """ display game results """
        self.clear_hands()
        self.count = 0
        self.set_text("Result")
        for player in players:
            self.l_players.append( player )
            self.add_player_only(player)

    def add_player_only(self, player):
        """ Only add the player info """
        pos = self.get_pos()
        off = 100
        tmp = Rectangle(pos[0] , pos[1]  + off*(0.4 + len(self.players)), 150, 70, col2="grey", text=player.str_choice())
        d_val = {True:"Maroon", False:"Blue"}
        c_val = d_val[ player.is_human() ]
        tmp.set_text_color(c_val)
        self.players.append( tmp )

    def add_hand(self, player, hand):
        """ add hand """
        self.l_players.append( player )
        pos = self.get_pos()
        off = 100
        tmp = Rectangle(pos[0] , pos[1]  + off*(0.4 + len(self.hands)), 150, 70, col2="grey", text=player.str_choice())
        d_val = {True:"Maroon", False:"Blue"}
        c_val = d_val[ player.is_human() ]
        tmp.set_text_color(c_val)
        self.players.append( tmp )
        tmp2 = False
        if hand is False :
            tmp2 = Rectangle(pos[0] + 200, pos[1] + off*(0.4 + len(self.hands)), 150, 70, col2="grey", ctext="red", text="Pass")
        elif hand is not True:
            tmp2 = DrawHand(pos[0] + 200, pos[1] + off*(0.4 + len(self.hands)), hand)

        self.hands.append( tmp2 )

    def draw(self, canvas):
        """ canvas """
        super().draw(canvas)
        for _, hand in enumerate(self.hands):
            hand.draw(canvas)
        for pos, player in enumerate(self.players):
            player.set_text(self.l_players[pos].str_choice())
            player.draw(canvas)

    def get_sequence(self, all_players=False):
        """ return elements to test for sequence list """
        play_list = []
        card_list = []
        for pos, hand in enumerate(self.hands):
            if isinstance(hand, DrawHand):
                play_list.append(self.l_players[pos])
                card_list.append(hand.card_list())
        out = card_seq_increment(card_list, all_players)
        if out is False:
            return out
        l_give = [[], []]
        for pos, val in enumerate(out):
            l_give[0].append( play_list[pos] )
            if val and play_list[pos].nb_cards() != 0:
                if len(card_list) == 3:
                    val = len(card_list[2])
                elif len(card_list) == 4:
                    if pos == 3:
                        val = len(card_list[3])
                    else:
                        val = len(card_list[2])
                if val > play_list[pos].nb_cards():
                    val = play_list[pos].nb_cards()
            l_give[1].append( val )
        return l_give

class DrawCard(Rectangle):
    """ create card draw """

    def __init__(self, posx, posy, card:Card, istext=False, isselect=False):
        """ Create DrawCard """
        super().__init__(posx, posy, CARD_SIZE[0], CARD_SIZE[1], text=str(card))
        self._ca = card
        self._it = istext
        self.set_selected(isselect)

    def get_card(self):
        """ get card """
        return self._ca

    def set_text_mode(self, text:bool):
        """ text mode """
        self._it = text

    def draw(self, canvas):
        """ Draw Card """
        if self._it:
            super().draw(canvas)
        else:
            self.draw_img(canvas)

    def draw_img(self, canvas):
        """ draw card """
        rank = self._ca.get_rank()
        suit = self._ca.get_suit()
        pos  = self.get_pos()
        sel  = self.get_selected()
        draw_resize_card(canvas, rank, suit, sel, pos)

class DrawHand:
    """ Class to Draw Hand """

    def __init__(self, posx, posy, hand:Hand, istext=False):
        self._ha = hand
        self._x = posx
        self._y = posy
        self._it = istext
        self._lv = []
        self._lc = []
        self._old_sel = False
        self.update()

    def click_pos_play(self, c_pos, cards, equalize=False):
        """ return True if clicked on a card  """
        r_val, _ = self._ha.show_winning_choices(cards, equalize)
        if len(r_val) in [0, 1]:
            return
        card = self.is_click(c_pos)
        if card is False:
            return
        rank = card.get_card().get_rank()
        if rank not in r_val:
            return

        nb_input = len(cards)
        nb_out  = self._ha.nb_cards_rank(rank)
        out = card
        if rank == "O" or nb_input == 1 :
            self.unselect_all_cards()
            card.set_selected( True )
            return

        if rank == "2" and nb_input - 1 <= nb_out:
            if out.get_selected() and nb_input <= nb_out:
                out.set_selected( False )
                count = 0
            else :
                out.set_selected( True )
                count = 1
        else :
            out.set_selected( True )
            count = 1
        for _, card in enumerate(self._lv):
            if card.get_card().get_rank() == rank:
                if  out == card:
                    pass
                elif count < nb_input - 1:
                    count += 1
                    card.set_selected( True )
                elif count == nb_input - 1 and card.get_selected():
                    count += 1
                else :
                    card.set_selected( False )
            else:
                card.set_selected( False )

    def left_key_pos_play(self, equalize, cards):
        """ return True if clicked on a card  """
        self.key_pos_play(equalize, cards, left=True)

    def right_key_pos_play(self, equalize, cards):
        """ return True if clicked on a card  """
        self.key_pos_play(equalize, cards, left=False)

    def key_pos_play(self, equalize, cards, left=False):
        """ updated card selection based on key press  """
        r_val, r_cards = self._ha.show_winning_choices(cards, equalize)
        if len(r_val) in [0, 1]:
            return

        nb_cards, l_cards, _ = self.get_selected_index()
        if nb_cards == 0:
            return
        rank = l_cards[0].get_card().get_rank()

        d_val = {False:-1, True:1}
        index = r_val.index(rank)  + d_val[left]
        if index < 0:
            index = len(r_val) -1
        elif index == len(r_val):
            index = 0

        new_rank = r_val[index]
        count = 0
        max_count = len(r_cards[index])
        for _, card in enumerate(self._lv):
            if card.get_card().get_rank()==rank:
                card.set_selected(False)
            if card.get_card().get_rank()==new_rank and count < max_count:
                card.set_selected(True)
                count += 1

    def right_key_pos_give(self):
        """ return True if clicked on a card  """
        nb_cards, l_cards, l_index = self.get_selected_index()

        l_cards[0].set_selected(False)
        if nb_cards == 1:
            index = l_index[0] + 1
            if index == nb_cards:
                index = 0
            rank = self._lc[index].get_rank()
            for _, card in enumerate(self._lv):
                if card.get_card().get_rank()==rank:
                    card.set_selected(True)
        else :
            l_cards[0].set_selected(False)

    def left_key_pos_give(self):
        """ return True if clicked on a card  """
        nb_cards, l_cards, l_index = self.get_selected_index()

        l_cards[-1].set_selected(False)
        if nb_cards == 1:
            index = l_index[0] - 1
            if index == -1:
                index = nb_cards - 1
            rank = self._lc[index].get_rank()
            for _, card in enumerate(self._lv):
                if card.get_card().get_rank()==rank:
                    card.set_selected(True)

    def get_selected_index(self):
        """ get the selected index """
        l_cards = []
        l_index = []
        nb_cards = 0
        for pos, card in enumerate(self._lv):
            if card.get_selected():
                l_index.append(pos)
                l_cards.append(card)
                nb_cards += 1
        return nb_cards, l_cards, l_index

    def update_index(self, index, left=False):
        """ helper function to update new index """
        nb_cards = self._ha.nb_cards()
        d_val = {False:1, True:-1}
        index = index + d_val[left]
        if index == -1:
            index = nb_cards - 1
        elif index == nb_cards:
            index = 0
        return index

    def update_1_card_selected(self, l_index, left=False):
        """ update selected val based on key press """
        index = self.update_index(l_index[0], left)
        self.unselect_all_cards()
        self._lv[index].set_selected(True)

    def update_2_card_selected(self, nb_cards, l_index, left=False):
        """ update 2 cards selected based on key press """
        if nb_cards == len(self._lv):
            return
        index = self._old_sel
        if index not in l_index:
            index = l_index[0]
            pos = 0
        else :
            pos = l_index.index(index)

        new_index = self.update_index(index, left)
        if new_index in l_index:
            pos = (pos + 1) % nb_cards
            index = l_index[pos]
            new_index = self.update_index(index, left)

        l_index[pos]  = new_index
        self._old_sel = new_index

        self.unselect_all_cards()
        #cards = [ self._lv[l_index[0]], self._lv[l_index[1]] ]

        for _, index in enumerate(l_index):
            card = self._lv[index]
            card.set_selected(True)

    def down_key_sequence(self):
        """ change selected position """
        nb_cards, _, l_index = self.get_selected_index()
        if self._old_sel is False or self._old_sel not in l_index or nb_cards == 1:
            self._old_sel = l_index[0]
        else :
            index = l_index.index(self._old_sel) + 1
            if index >= nb_cards:
                index = 0
            self._old_sel = l_index[index]

    def left_key_pos_sequence(self):
        """ select card to give in case of sequence  """
        nb_cards, _, l_index = self.get_selected_index()
        if nb_cards == 1:
            self.update_1_card_selected(l_index, left=True)
        elif nb_cards == 2:
            self.update_2_card_selected(nb_cards, l_index, left=True)

    def right_key_pos_sequence(self):
        """ select card to give in case of sequence """
        nb_cards, _, l_index = self.get_selected_index()
        if nb_cards == 1:
            self.update_1_card_selected(l_index, left=False)
        elif nb_cards == 2:
            self.update_2_card_selected(nb_cards, l_index, left=False)


    def click_pos_give_cards(self, c_pos):
        """ click to select which card to give  """
        card = self.is_click(c_pos)
        if card is False:
            return
        _,  _, l_index = self.get_selected_index()

        out = card.get_card()
        self._old_sel = self._lv.index(card)
        if card.get_selected() is True:
            return out
        card.set_selected(True)
        if self._old_sel is False:
            t_pos = l_index[-1]
        elif l_index[0] == self._old_sel:
            t_pos = l_index[-1]
        else :
            t_pos = l_index[0]
        self._lv[t_pos].set_selected(False)
        return out


    def click_pos_give(self, c_pos, role):
        """ click to select which card to give at choice time  """
        if role > 1:
            return
        card = self.is_click(c_pos)
        if card is False:
            return
        _, _, l_index = self.get_selected_index()

        out = card.get_card()
        if card.get_selected() is True:
            return out
        card.set_selected(True)
        self._old_sel = self._lv.index(card)
        if role == 1: #1 card always selected
            self._lv[l_index[0]].set_selected(False)
        if role == 0: #2 cards always selected
            if self._old_sel is False:
                t_pos = l_index[-1]
            elif l_index[0] == self._old_sel:
                t_pos = l_index[1]
            else :
                t_pos = l_index[0]
            self._lv[t_pos].set_selected(False)
        return out

    def click_pos_start(self, pos):
        """ mouse click to select which card to play at the beginning of the turn  """
        self.click_pos(pos)

    def click_pos(self, pos):
        """ mouse click to select which card to play at the beginning of the turn  """
        orig = self.get_selected_cards()
        out = self.is_click(pos)
        if out is False:
            return
        rank = out.get_card().get_rank()
        if len(orig) == 0:
            for _, card in enumerate(self._lv):
                if card.get_card().get_rank() == rank:
                    card.set_selected( True )
        elif rank != orig[0].get_rank():
            self.unselect_all_cards()
            for _, card in enumerate(self._lv):
                if card.get_card().get_rank() == rank:
                    card.set_selected( True )
        elif len(orig) > 1:
            out.set_selected( not out.get_selected() )

    def is_click(self, pos):
        """ return card if clicked, False otherwise """
        out = False
        for _, card in enumerate(self._lv):
            if card.is_click(pos):
                out = card
                break
        return out

    def select_lowest(self):
        """ select lowest cards """
        rank = self._lv[-1].get_card().get_rank()
        for _, card in reversed(list(enumerate(self._lv))):
            if card.get_card().get_rank() == rank:
                card.set_selected(True)
            else:
                return

    def select_lowest_cards(self, nb_count=False):
        """ select lowest card """
        count = 0
        for _, card in reversed(list(enumerate(self._lv))):
            card.set_selected(True)
            count += 1
            if nb_count is not False and count == nb_count:
                return

    def unselect_all_cards(self):
        """ unselect all cards """
        for _, card in enumerate(self._lv):
            card.set_selected(False)

    def get_selected_cards(self):
        """ return selected cards """
        cards = []
        for _, card in enumerate(self._lv):
            if card.get_selected():
                cards.append(card.get_card())
        return cards

    def select_specific_cards(self, cards):
        """ select cards according to role """
        self.update()
        for _, card in enumerate(self._lv):
            if card.get_card() in cards:
                card.set_selected(True)
            else:
                card.set_selected(False)

    def select_cards_choice(self, role):
        """ select cards according to role """
        self.update()
        if role == 0:
            self._lv[-2].set_selected(True)
            self._lv[-1].set_selected(True)
        elif role == 1:
            self._lv[-1].set_selected(True)
        elif role == 2:
            self._lv[0].set_selected(True)
        elif role == 3:
            self._lv[0].set_selected(True)
            self._lv[1].set_selected(True)

    def give_choice(self, role):
        """ role """
        return self._ha.give_choice(role)

    def clear_hand(self):
        """ clear the hand """
        self.set_hand(Hand())

    def set_hand(self, hand:Hand):
        """ set hand """
        self._ha = hand
        self._lc = []
        self._lv = []
        self.update()

    def get_hand(self):
        """ return hand """
        return self._ha

    def card_list(self):
        """ Restart hand """
        return self._ha.card_list()

    def restart(self):
        """ Restart hand """
        self._ha = Hand()
        self._lc = []
        self._lv = []
        self.update()

    def get_card_list(self):
        """ return draw card list """
        return self._lv

    def add_cards(self, cards:Card, select:bool=False):
        """ add card """
        for card in cards:
            self.add_card(card, select=False)
        if select:
            self.select_specific_cards(cards)

    def add_card(self, card:Card, select:bool=False):
        """ add card """
        self._ha.add_card(card)
        self.update()
        if select:
            self.select_specific_cards([card])

    def give_card(self, low=True):
        """ give card """
        if low:
            val = self._ha.give_lowest()
        else:
            val = self._ha.give_highest()
        return val

    def update(self):
        """ update """
        l_cards = self._ha.card_list()
        if l_cards != self._lc:
            self._lc = l_cards
            self._lv = []
            for ind, card in enumerate(l_cards):
                tmp = DrawCard(self._x + ind*CARD_SIZE[0], self._y, card, self._it)
                self._lv.append(tmp)

    def set_text_mode(self, istext:bool):
        """ set text mode """
        self._it = istext
        for card, _ in enumerate(self._lv):
            card.set_text_mode(istext)

    def draw_backs(self, canvas ):
        """ draw backs of cards """
        self.update()
        nb_cards = len(self._lc)
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        for ind in range(nb_cards):
            pos2 =  [self._x + CARD_CENTER[0] + ind*CARD_SIZE[0], self._y + CARD_CENTER[1]]
            canvas.draw_image(card_back, card_loc, CARD_SIZE, pos2, CARD_SIZE)

    def draw(self, canvas):
        """ DrawHand """
        self.update()
        for pos, _ in enumerate(self._lv):
            self._lv[pos].draw(canvas)

class LanguageVal:
    """ Language Object """
    def __init__(self):
        self.lang  = "francais"
        self.rules = ""\
            "Rules of the President Game.\n"\
            "There are 4 players, the president, the vice, the concierge and the null.\n"\
            "The card order of value is 3,4,5,6,7,8,9,10,J,Q,K,A,2,Joker.\n"\
            "A joker can beat any double, triple or quadruple.\n"\
            "A 2 can beat any double, two 2 can beat a triple, 3 a quadruple.\n"\
            "The Nul can equalize any card in order to win the round.\n"\
            "Phase 1 Distribution. First round all cards are face up.\n"\
            "The President can accept or refuse the first 2 cards offered.\n"\
            "Phase 2 Exchange. Once all cards are distributed.\n"\
            "The President gives his 2 worst cards (or any card) and receives the 2 best cards of the Nul.\n"\
            "The President gives his worst card  (or any card) and receives the best cards of the Concierge.\n"\
            "Phase 3 Game. The first round is started by the President.\n"\
            "The winner of the last round starts the next. Each turn gives one chance to each player.\n"\
            "All players participating in a sequence give card(s)\n"\
            "Phase 4 Winning. The first player to win becomes President, the second the Vice.\n"\

        self.regle = ""\
            "Regle du jeu du President\n"\
            "Il y a 4 joueurs, le president, le vice, le concierge et le nul\n"\
            "L'ordre des valeurs est 3,4,5,6,7,8,9,10,J,Q,K,A,2,Joker.\n"\
            "Un joker peut battre n\'importe quel double, triple or quadruple.\n"\
            "Un 2 peut battre n\'importe quel double, deux 2 triple, troix 2 quadruple.\n"\
            "Le nul peut egaler n\'importe quelle carte pour gagner le tour\n"\
            "Phase 1 Distribution. Au premier tour toutes les cartes sont montrees\n"\
            "Le president peut accepter ou refuser les 2 premieres cartes offertes\n"\
            "Phase 2 Echange. Une fois toutes les cartes distribuees.\n"\
            "Le president donne 2 cartes au nul et recoit les 2 meilleures du nul\n"\
            "Le vice donne 1 carte au concierge et recoit la meilleure du concierge\n"\
            "Phase 3 Jeu. Le premier tour est commence par le president\n"\
            "Le gagnant du tour precedent commence le suivant. Un tour fait au plus chaque joueur\n"\
            "Tous les joueurs participants a une sequence donnent une ou des cartes\n"\
            "Phase 4 Gagner. Le premier joueur devient le president, le second le vice\n"\

        self.francais = { "title":"Jeu du President", "menu":"Menu", "language":"Language", "English":"English",
            "Francais":"Francais", "Sequence":"Donne carte\n si sequence", "No_Seq":"Desactivee", "3_Card":"3 joueurs",
            "4_Card":"4 joueurs", "choice":"Phase du choix", "1_choice":"President a 1 choix",
            "2_choice":"President a 2 choix\n Vice a 1 choix",
            "exchange":"Echange des cartes", "lowest":"Carte plus faible", "select":"Joueur decide",
            "position":"Jouer role", "pres":"President", "vice":"Vice", "conc":"Concierge", "nul":"Nul",
            "options": "Options", "main":"Menu Principal", "reset":"Redemarrer",
            "p_choices": "Phase de Choix", "Game":"Jeu", 'hint':"Indices",
            "accept": "Accepter", "reject": "Rejetter", "dist": "Distribution",
            "give":"Donner Cartes", "play":"Jouer", "pass":"Passer", "result":"Resultats de la partie",
            "next":"Suivant", "player_id":"Joueur 1", "next_game":"Partie Suivante",
            "seq_det":"Sequence Detectee", "seq_det2":"Sequence Detectee donner des cartes",
            "started":"Parties Demarrees", "ended":"Parties Terminees", "From":"De", "to": "a",
            "stats":"Statistiques",
            'hint2':"Indices\n\n"\
                "Le President donne\n 2 cartes au nul\n\n\n"\
                "Le Vice donne\n  1 carte au concierge\n\n\n"\
                "Le Concierge donne sa \nmeilleure carte au Vice\n\n\n"\
                "Le Nul donne ses 2\nmeilleures cartes au President\n",
            'hint_choice':"Indices\n\n"\
                "Le President recoit 2 cartes\nil peut refuser 1 fois\n\n\n"\
                "Le Vice recoit 2 cartes\n\n"\
                "Le Concierge 1 carte\n\n"\
                "Le Nul 1 carte\n",
            'hint_choice2':"Indices\n\n"\
                "Le President recoit 2 cartes\nil peut refuser 2 fois\n\n\n"\
                "Le Vice recoit 1 carte\nil peut refuser 1 fois\n\n\n"\
                "Le Concierge 1 carte\n\n"\
                "Le Nul 1 carte\n",
            'hint_dist':"Indices\n\n"\
                "Vous pouvez utilisez les fleches\npour jouer plus aisement\n\n\n"\
                "Les fleches haut et bas\n"\
                "choix entre jouer et passer\nchoix entre accepter ou refuser\n\n"\
                "Gauche et droite pour\nselectionner des cartes\n",
            "start":"Demarrer Partie", "rules":self.regle, "Rules":"Regles"}

        self.english = {"title": "President\'s Game", "menu":"Menu", "language":"Language", "English":"English",
            "Francais":"Francais", "Sequence":"Give card\n if sequence", "No_Seq":"Deactivate",
            "3_Card":"3 players", "4_Card":"4 players",
            "choice":"Choice Phase", "1_choice":"President has 1 choice",
            "2_choice":"President has 2 choice\n Vice has 1 choice",
            "exchange":"Card exchange", "lowest":"Lowest Card", "select":"Player decides",
            "position":"Play as", "pres":"President", "vice":"Vice", "conc":"Concierge", "nul":"Nul",
            "options": "Options", "main":"Main menu", "reset":"Restart",
            "p_choices": "Choice Phase", "Game":"Game", "hint":"hint",
            "accept": "accept", "reject": "reject", "dist": "Distribution",
            "next":"next turn", "player_id":"Player 1", "next_game":"Next Game",
            "give":"Give choice", "play":"Play", "pass":"Pass", "result":"Game results",
            "seq_det":"Sequence Detected", "seq_det2":"Sequence Detected Giving Cards",
            "started":"Games Started", "ended":"Games Completed", "From":"From", "to": "to",
            "stats":"Statistics",
            'hint2':"Hints\n\n"\
                "The President gives\n 2 cards to the nul\n\n\n"\
                "The Vice gives\n 1 card to the concierge\n\n\n"\
                "The Concierge gives his\n best card to the Vice\n\n\n"\
                "The Nul gives his\n 2 best cards to the President\n",
            'hint_choice':"Hints\n\n"\
                "The President receives 2 cards\nhe can refuse 1 time\n\n\n"\
                "The Vice receives 2 cards\n\n"\
                "The Concierge 1 card\n\n"\
                "The Nul 1 card\n",
            'hint_choice2':"Hints\n\n"\
                "The President receives 2 cards\nhe can refuse 2 times\n\n\n"\
                "The Vice receives 1 card\nhe can refuse 1 time\n\n\n"\
                "The Concierge 1 card\n\n"\
                "The Nul 1 card\n",
            'hint_dist':"Hints\n\n"\
                "You can use the arrows \nfacilitate your play\n\n\n"\
                "Up and Down arrows to\n"\
                "choose play or pass\nchoose accept or reject\n\n"\
                "Left and Right to select a card\n",
            "start":"Start Game", "rules":self.rules, "Rules":"Rules"}

        self.l_val = {"Francais": self.francais, "English": self.english }

class DrawStatus:
    """ Class that draws the player list status """
    def __init__(self, players, posx=0, posy=60):
        """ init choice """
        self.posx = posx
        self.posy = posy
        self.players = players

        self.rect = []
        for val in range(4):
            text = self.players[val].str_status()
            self.rect.append(Rectangle(self.posx, self.posy +100*val, 150, 85,text=text))

    def draw(self, canvas):
        """ Update """
        d_val = {True:"Maroon", False:"Blue"}
        for pos, val in enumerate(self.rect):
            text = self.players[pos].str_status()
            val.set_text(text)
            c_val = d_val[ self.players[pos].is_human() ]
            val.set_text_color(c_val)
            val.draw(canvas)
