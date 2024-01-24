""" President game """""" card api for president's game """
# "president" - generates the screen and the gameplay
#
# I was trying to generate a playable version of the french canadian card game
# I am using  CodeSkulptor and SimpleGUI from An Introduction to Interactive Programming in Python
# Since it keeps the game has browser based therefore accessible to all devicess
# Please enjoy the game
#
# Programming - Samuel Paul (samuelspaul@gmail.com)
#
# Current Version (v1.0 - 23 January 2024):
#pylint: disable=wildcard-import,line-too-long,unused-wildcard-import
#pylint: disable=wildcard-import,unused-wildcard-import,line-too-long, too-many-lines
# pyright: reportMissingImports=false

# File saved in https://py3.codeskulptor.org/#user309_3lX3GsAY38_9.py
# Github project : https://github.com/spaul044/PresidentGame

try:
    import simplegui

    import user309_Qz4BBPIZtH_16 as draw
    from user309_Qz4BBPIZtH_16 import LanguageVal, Rectangle, DrawTurn, DrawHand, DrawStatus, get_names
    from user309_Kd3jylJSQd_0 import Player, Hand, Deck, POSITIONS
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    import draw
    from card import Player, Hand, Deck, POSITIONS
    from draw import LanguageVal, Rectangle, DrawTurn, DrawHand, DrawStatus, get_names

KEY_ENTER = 13
KEY_UP   =  simplegui.KEY_MAP["up"]
KEY_DOWN = simplegui.KEY_MAP["down"]
KEY_LEFT   =  simplegui.KEY_MAP["left"]
KEY_RIGHT  = simplegui.KEY_MAP["right"]
KEY_ALL = [KEY_ENTER, KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT, KEY_RIGHT]
KEY_A  = simplegui.KEY_MAP["a"]
KEY_S  = simplegui.KEY_MAP["s"]
KEY_D  = simplegui.KEY_MAP["d"]
KEY_W  = simplegui.KEY_MAP["w"]
KEY_ALL = [KEY_ENTER, KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT, KEY_RIGHT,\
            KEY_W, KEY_A, KEY_S, KEY_D]

class Screen:
    """ Screen """

    def __init__(self, settings:dict, lan:LanguageVal):
        """ init function """
        self._set   = settings
        self._lan   = lan
        self._disp  = {}
        self._tog   = {}
        self._func  = {}
        self._blink = {}
        self.count  = 0

    def set_display(self, disp:dict, toggle:dict, func:dict, blink:list):
        """ update display """
        tmp = {}
        for key, vv in disp.items():
            tmp[key] = Rectangle(vv[0], vv[1], vv[2], vv[3], vv[4], vv[5], vv[6], vv[7], vv[8])

        for _, item in self._set.items():
            if item in tmp:
                tmp[item].set_selected(True)

        self._disp  = tmp
        self._tog   = toggle
        self._func  = func
        self._blink = blink

        self.update_language()

    def key_handler(self, key): #pylint: disable=unused-argument
        """ update name """
        return

    def force_restart(self):
        """ force restart of game """
        self._set["restart"] = True

    def text_val(self, obj_id):
        """ return the text value of an item """
        lang  = self._set["language"]
        d_val = self._lan.l_val[lang]
        t_val = obj_id
        if obj_id in d_val:
            t_val = d_val[obj_id]
        return t_val

    def update_language(self):
        """ update language """
        lang  = self._set["language"]
        d_val = self._lan.l_val[lang]
        for key, val in self._disp.items():
            if key in d_val:
                text = d_val[key]
                val.set_text(text)

    def update_list(self, key, list_val, pos, func=False, force=False):
        """ update a list of boxes """
        for val in list_val:
            if val in self._disp and (force is True or self._disp[val].is_click(pos) ):
                for tmp in list_val:
                    self._disp[tmp].set_selected(False)
                self._disp[val].set_selected(True)
                self._set[key] = val
                if func:
                    func()

    def update_click(self, key, func, pos):
        """ select callback if item clicked """
        if key in self._disp and self._disp[key].is_click(pos):
            if func:
                func()

    def draw(self, canvas):
        """ draw function """
        self.count += 1
        for key in self._blink:
            if key in self._disp:
                if self.count%60 == 0:
                    val = self._disp[key].get_selected()
                    self._disp[key].set_selected(not val)

        for _, val in self._disp.items():
            val.draw(canvas)

    def click_pos(self, pos):
        """ click handler function """
        for key, l_val in self._tog.items():
            self.update_list(key, l_val[0], pos, l_val[1])
        for key, func in self._func.items():
            self.update_click(key, func, pos)

class MenuOptions(Screen):
    """ class Menu Options """

    def __init__(self, settings:dict, lan:LanguageVal, update):
        """ Init Menu """
        super().__init__(settings, lan)

        self.d_in  = {}
        self.d_in["title"]    = (    0,    0,  300,  50, "black", "white", "", "blue",  32)
        self.d_in["language"] = (    0,  100,  200,  60, "black", "white", "", "blue",  28)
        self.d_in["Francais"] = (  300,  100,  200,  60, "black", "white", "", "Black", 32)
        self.d_in["English"]  = (  600,  100,  200,  60, "black", "white", "", "Black", 32)
        self.d_in["Sequence"] = (    0,  180,  200,  60, "black", "white", "", "blue",  24)
        self.d_in["No_Seq"]   = (  300,  180,  200,  60, "black", "white", "", "Black", 28)
        self.d_in["3_Card"]   = (  600,  180,  200,  60, "black", "white", "", "Black", 28)
        self.d_in["4_Card"]   = (  900,  180,  200,  60, "black", "white", "", "Black", 28)
        self.d_in["choice"]   = (    0,  260,  200,  60, "black", "white", "", "blue",  24)
        self.d_in["1_choice"] = (  300,  260,  200,  60, "black", "white", "", "Black", 16)
        self.d_in["2_choice"] = (  600,  260,  200,  60, "black", "white", "", "Black", 16)
        self.d_in["exchange"] = (    0,  340,  200,  60, "black", "white", "", "blue",  20)
        self.d_in["lowest"]   = (  300,  340,  200,  60, "black", "white", "", "Black", 22)
        self.d_in["select"]   = (  600,  340,  200,  60, "black", "white", "", "Black", 22)
        self.d_in["position"] = (    0,  420,  200,  60, "black", "white", "", "blue",  30)
        self.d_in["pres"]     = (  250,  420,  180,  60, "black", "white", "", "Black", 30)
        self.d_in["vice"]     = (  450,  420,  180,  60, "black", "white", "", "Black", 30)
        self.d_in["conc"]     = (  650,  420,  180,  60, "black", "white", "", "Black", 30)
        self.d_in["nul"]      = (  850,  420,  180,  60, "black", "white", "", "Black", 30)
        self.d_in["options"]  = (  500,    0,  180,  50, "black", "white", "", "Red",   32)
        self.d_in["main"]   = ( 950,   0,  200,  40, "black", "blue",  "", "white", 16)
        self.d_in["Game"] = ( 850,   0,  100,  40, "black", "blue",  "", "white", 20)

        self.d_tog = {}
        self.d_tog["language"] = [  ["Francais", "English"] , self.update_language]
        self.d_tog["Sequence"] = [  ["No_Seq",   "3_Card", "4_Card"]  , False]
        self.d_tog["exchange"] = [  ["lowest",   "select"  ]  , False]
        self.d_tog["choice"]   = [  ["1_choice", "2_choice"]  , False]
        self.d_tog["position"] = [  ["pres", "vice", "conc", "nul"]  , self.force_restart]

        self.d_func  = { "main":self.s_main, "Game":self.s_game}
        self.l_blink = [ "main" ]
        self.set_display(self.d_in, self.d_tog, self.d_func, self.l_blink)
        self.update = update

    def draw(self, canvas):
        super().draw(canvas)
        if self.count == 1:
            for key, l_val in self._tog.items():
                self.update_list(key, l_val[0], False, l_val[1], force=True)
    def s_main(self):
        """ start function """
        self._set["state"] = "MAIN"
        self.update()

    def s_game(self):
        """ start function """
        self._set["state"] = "GAME"
        self.update()

class Rules(Screen):
    """ Game Object """

    def __init__(self, settings:dict, lan:LanguageVal, update):
        """ init function """
        super().__init__(settings, lan)
        self.d_in  = {}
        self.d_in["title"]   = (    0,    0,   300,  50, "black", "white", "", "blue",  32)
        self.d_in["main"]    = (  850,    0,   300,  40, "black", "blue",  "", "white", 30)
        self.d_in["rules"]   = (    0,  100,  1000, 400, "black", "white", "", "blue",  24)
        self.d_in["Rules"]   = (  500,    0,   150,  50, "black", "white", "", "Red",   32)

        self.d_tog = {}
        self.d_func = { "main":self.s_main}
        self.l_blink = [ "main" ]
        self.set_display(self.d_in, self.d_tog, self.d_func, self.l_blink)
        self.update = update

    def s_main(self):
        """ start function """
        self._set["state"] = "MAIN"
        self.update()

class Stats(Screen):
    """ Game Object """

    def __init__(self, settings:dict, lan:LanguageVal, update, stats):
        """ init function """
        super().__init__(settings, lan)
        self.d_in  = {}
        self.d_in["title"]   = (    0,    0,   300,  50, "black", "white", "", "blue",  32)
        self.d_in["main"]    = (  850,    0,   300,  40, "black", "blue",  "", "white", 30)
        self.d_in["stats"]   = (  500,    0,   250,  50, "black", "white", "", "Red",   32)
        self.d_in["empty"]   = (    0,  100,  1000, 400, "black", "white", "", "blue",  24)
        self.stats = stats

        self.d_tog = {}
        self.d_func = { "main":self.s_main}
        self.l_blink = [ "main" ]
        self.set_display(self.d_in, self.d_tog, self.d_func, self.l_blink)
        self.update = update

    def s_main(self):
        """ start function """
        self._set["state"] = "MAIN"
        self.update()

    def draw(self, canvas):
        super().draw(canvas)
        started = self.stats["nb_start"]
        completed = self.stats["nb_complete"]
        d_val = self._lan.l_val[self._set["language"]]
        s_1 = d_val["started"]
        s_2 = d_val["ended"]
        s_3 = d_val["From"]
        s_4 = d_val["to"]
        str_val = f"{s_1} {started}  /  {s_2} {completed}\n\n"
        for count, val in enumerate(self.stats["last_games"]):
            pos_0 = POSITIONS[val[0]]
            pos_1 = POSITIONS[val[1]]
            str_val += f"({count:2d})  {s_3}   {pos_0 : <12}  {s_4} {pos_1 : <12} \n"
        self._disp["empty"].set_text(str_val)

class MainMenu(Screen):
    """ Game Object """

    def __init__(self, settings:dict, lan:LanguageVal, update):
        """ init function """
        super().__init__(settings, lan)
        self.d_in  = {}
        self.d_in["title"]    = (    0,    0,  300,  50, "black", "white", "", "blue",  32)
        self.d_in["options"]  = (  400,  100,  300,  60, "black", "blue", "", "white",  32)
        self.d_in["Rules"]    = (  400,  170,  300,  60, "black", "blue", "", "white",  32)
        self.d_in["stats"]    = (  400,  240,  300,  60, "black", "blue", "Stats", "white",  32)
        self.d_in["start"]    = (  400,  400,  300,  60, "black", "blue", "", "white",  32)

        self.d_tog = {}
        self.d_func = { "options":self.s_menu, "Rules":self.s_rules, "start":self.s_game,"stats":self.s_stats}
        self.l_blink = [ "start" ]
        self.set_display(self.d_in, self.d_tog, self.d_func, self.l_blink)
        self.update = update

    def s_menu(self):
        """ start function """
        self._set["state"] = "MENU"
        self.update()

    def s_rules(self):
        """ start function """
        self._set["state"] = "RULES"
        self.update()

    def s_game(self):
        """ start function """
        self._set["state"] = "GAME"
        self.update()

    def s_stats(self):
        """ start function """
        self._set["state"] = "Stats"
        self.update()

class PlayTurn:
    """ Play each turn of the game """

    def __init__(self, players:list, turn:DrawTurn, hand:DrawHand, lang:dict, settings:dict, stats:dict ):
        """ """
        self.settings = settings
        self.choice = True
        self.lang  = lang
        self.refresh  = 30 # 30 fps / 30 = 1 frame / second
        self.count    = 30
        self.players  = players
        self.player   = Player("", 0)
        self.pos      = 0
        self.p_pos    = 0
        self.first    = True
        self.seq_data = False
        self.seq_pos  = 0
        self.stats    = stats
        for pos, player in enumerate(players):
            if player.is_human():
                self.player = player
                self.p_pos = pos

        self.d_turn = turn
        self.d_hand = hand
        self.d_next = Rectangle(850, 280, 250, 170, ctext="blue", text="", font=40)
        self.d_play = Rectangle(850, 200, 250,  115, ctext="blue", text="", font=40)
        self.d_pass = Rectangle(850, 335, 250, 115, ctext="blue", text="", font=40)
        self.hint   = Rectangle(850, 80, 250, 200, ctext="blue", font = 14)
        self.hint.set_text(self.lang['hint_dist'])

        self.player_state = "HUMAN_WAIT"
        self.state      = "FIRST"
        self.count      = 0
        self.turn_count = 0
        self.start_pos  = 0
        self.next_start = 0
        self.pos        = 0
        self.winners    = []
        self.hand_turn  = []
        self.card_play  = []
        self.player_card = False
        self.t_list = {self.d_play:"play", self.d_pass:"pass", self.d_next:"next"}
        #self.d_turn.increment_turn(0)

        self.update_language(self.lang)

    def update_language(self, lang:dict):
        """ update language """
        self.lang  = lang
        for obj, name in self.t_list.items():
            if name in self.lang:
                obj.set_text(self.lang[name])
        self.hint.set_text(self.lang['hint_dist'])

    def update_players(self, players):
        """ update players list """
        self.refresh    = 30 # 30 fps / 30 = 1 frame / second
        self.count      = 0
        self.turn_count = 0
        self.start_pos  = 0
        self.next_start = 0
        self.pos        = 0
        self.winners    = []
        self.hand_turn  = []
        self.card_play  = []
        self.player_card= False
        self.seq_data   = False
        self.seq_pos    = 0
        self.d_turn.increment_turn(count=0)

        self.player   = Player("", 0)
        self.pos      = 0
        self.p_pos    = 0
        for pos, player in enumerate(players):
            if player.is_human():
                self.player = player
                self.p_pos = pos

        self.players = players
        self.count += 1
        self.state = "PLAY"
        self.player_state = "HUMAN_WAIT"
        self.d_hand.unselect_all_cards()

    def update_turn(self):
        """ click handler """
        if self.state in ["WAIT", "NEXT", "NEXT_GAME", "PLAY_NEXT", "FIRST"]:
            return
        elif self.state == "SEQUENCE_GIVE":
            player   = self.seq_data[0][self.seq_pos]
            nb_cards = self.seq_data[1][self.seq_pos]
            if nb_cards is not False:
                if player.is_human() is False :
                    cards = player.give_card(nb_cards)
                    if cards is not False :
                        self.d_turn.add_hand(player, Hand(cards))
                    if player.nb_cards() == 0:
                        self.winners.append(player)
                    self.seq_pos += 1
                else:
                    if self.player_state == "HUMAN_WAIT":
                        self.d_play.set_pos( 850, 200, 250, 250 )
                        self.d_hand.unselect_all_cards()
                        self.d_hand.select_lowest_cards(nb_cards)
                        if player.nb_cards() == 0:
                            self.player_state = "HUMAN_DONE"
                            self.seq_pos += 1
                        else:
                            self.player_state = "HUMAN_SEQ_VALIDATE"
                    elif self.player_state == "HUMAN_DONE":
                        self.d_play.set_pos( 850, 200, 250, 115 )
                        self.d_pass.set_pos( 850, 335, 250, 115 )
                        if player.nb_cards() == 0:
                            self.seq_pos += 1
                            return
                        cards = self.d_hand.get_selected_cards()
                        self.d_turn.add_hand(player, Hand(cards))
                        player.give_specific_cards(cards)
                        if player.nb_cards() == 0:
                            self.winners.append(player)
                        self.seq_pos += 1
            else:
                self.seq_pos += 1

            if self.seq_pos == len(self.seq_data[0]):
                self.state = "PLAY_NEXT"
        elif len(self.hand_turn) == 0:
            for count in range(self.start_pos, self.start_pos + len(self.players)):
                pos = count % len(self.players)
                player = self.players[pos]
                if player.nb_cards() != 0:
                    self.hand_turn.append(pos)
                self.pos = 0
                self.player_state = "HUMAN_WAIT"
                self.d_hand.unselect_all_cards()
            if len(self.hand_turn) == 0:
                self.state = "NEXT_GAME"
                self.stats["nb_complete"] += 1
                orig = 0
                end = 0
                for pos, player in enumerate(self.players):
                    if player.is_human():
                        orig = pos
                for pos, player in enumerate(self.winners):
                    if player.is_human():
                        end = pos
                self.stats["last_games"].insert(0, (orig,end))
                if len(self.stats["last_games"]) > 10:
                    del self.stats["last_games"][10:]
        else :
            if self.pos == 0:
                pos = self.hand_turn[0]
                player = self.players[pos]
                if not player.is_human() or len(self.hand_turn) == 1: #pylint: disable=using-constant-test
                    cards = player.start_turn()
                    hand = Hand(cards)
                    self.pos += 1
                    self.d_turn.add_hand(player, hand)
                    self.card_play.append(cards)
                    if cards[0].get_rank() == "O":
                        self.state = "NEXT"
                    if len(self.hand_turn) == 1:
                        self.state = "PLAY"
                    if player.hand_empty():
                        self.winners.append(player)
                else :
                    if self.player_state == "HUMAN_WAIT":
                        self.d_hand.unselect_all_cards()
                        self.d_hand.select_lowest()
                        self.player_state = "HUMAN_VALIDATE_START"
                        self.d_play.set_pos( 850, 200, 250, 250  )
                    elif self.player_state == "HUMAN_DONE":
                        self.d_play.set_pos( 850, 200, 250, 115 )
                        self.d_pass.set_pos( 850, 335, 250, 115 )
                        cards = self.d_hand.get_selected_cards()
                        player.give_specific_cards(cards)
                        hand = Hand(cards)
                        self.d_turn.add_hand(player, hand)
                        self.card_play.append(cards)
                        self.pos += 1
                        if cards[0].get_rank() == "O":
                            self.state = "NEXT"
                        if len(self.hand_turn) == 1:
                            self.state = "PLAY"
                        if player.hand_empty():
                            self.winners.append(player)
                        self.player_state = "HUMAN_WAIT"
            elif self.pos < len(self.hand_turn):
                pos = self.hand_turn[self.pos]
                player = self.players[pos]
                old_cards = self.card_play[-1]
                cards = False
                if not player.is_human(): #pylint: disable=using-constant-test
                    cards = player.play_turn(old_cards)
                    self.pos += 1
                    if cards is not False:
                        hand = Hand(cards)
                        self.d_turn.add_hand(player, hand)
                        self.card_play.append(cards)
                        self.start_pos = pos
                        if cards[0].get_rank() == old_cards[0].get_rank():
                            self.state = "NEXT"
                        if cards[0].get_rank() == "O":
                            self.state = "NEXT"
                        if player.hand_empty():
                            self.winners.append(player)
                    else :
                        self.d_turn.add_hand(player, False)
                else :
                    old_cards = self.card_play[-1]
                    if self.player_state == "HUMAN_WAIT":
                        self.d_hand.unselect_all_cards()
                        r_val, r_cards = self.player.show_winning_choices(old_cards)
                        if len(r_val) != 0:
                            self.d_hand.select_specific_cards(r_cards[0])
                            self.player_state = "HUMAN_VALIDATE"
                            self.d_play.set_pos( 850, 200, 250, 115 )
                            self.d_pass.set_pos( 850, 335, 250, 115 )
                        else :
                            self.player_state = "HUMAN_PASS"
                            self.d_play.set_pos( 850, 200, 250, 250  )
                    elif self.player_state == "HUMAN_DONE":
                        self.first = False
                        cards = self.d_hand.get_selected_cards()
                        self.pos += 1
                        if len(cards) != 0:
                            hand = Hand(cards)
                            player.give_specific_cards(cards)
                            self.d_turn.add_hand(player, hand)
                            self.card_play.append(cards)
                            self.start_pos = pos
                            if cards[0].get_rank() == old_cards[0].get_rank():
                                self.state = "NEXT"
                            if player.hand_empty():
                                self.winners.append(player)
                        else :
                            self.d_turn.add_hand(player, False)
                        self.player_state = "HUMAN_WAIT"
            if (self.pos == len(self.hand_turn) and len(self.hand_turn) != 0):
                self.state = "NEXT"
            if self.state == "NEXT" and self.settings["Sequence"]!="No_Seq":
                out = self.d_turn.get_sequence(self.settings["Sequence"]=="4_Card")
                self.seq_data  = False
                if out is not False:
                    self.d_turn.set_text(self.lang["seq_det"])
                    self.state = "SEQUENCE"
                    self.seq_data  = out
                    self.seq_pos  = 0

    def click_pos(self, c_pos):
        """ click handler function """
        if self.state == "FIRST" and self.d_next.is_click(c_pos):
            self.first = False
            self.state = "PLAY"

        if self.state == "PLAY_START":
            self.d_hand.click_pos(c_pos)

        if self.player_state == "HUMAN_VALIDATE_START":
            self.d_hand.click_pos_start(c_pos)
            if self.d_play.is_click(c_pos):
                self.player_state = "HUMAN_DONE"
        if self.player_state == "HUMAN_PASS":
            if self.d_pass.is_click(c_pos):
                self.d_hand.unselect_all_cards()
                self.player_state = "HUMAN_DONE"
        if self.player_state == "HUMAN_VALIDATE":
            player = self.players[self.hand_turn[self.pos]]
            self.d_hand.click_pos_play(c_pos, self.card_play[-1], player.get_role()==3)
            if self.d_play.is_click(c_pos):
                self.player_state = "HUMAN_DONE"
            elif self.d_pass.is_click(c_pos):
                self.d_hand.unselect_all_cards()
                self.player_state = "HUMAN_DONE"
        if self.state == "SEQUENCE":
            if self.d_next.is_click(c_pos):
                self.state = "SEQUENCE_GIVE"
                self.d_turn.clear_hands()
                self.d_turn.set_text(self.lang["seq_det2"])
        elif self.state == "SEQUENCE_GIVE":
            if self.player_state == "HUMAN_SEQ_VALIDATE" and self.d_hand.get_selected_cards() is not False:
                self.d_hand.click_pos_give_cards(c_pos)
                if self.d_play.is_click(c_pos):
                    self.player_state = "HUMAN_DONE"
        elif self.state in ["NEXT", "NEXT_PLAY"] or (self.pos == len(self.hand_turn) and len(self.hand_turn) != 0):
            if self.d_next.is_click(c_pos):
                self.state = "PLAY"
                self.hand_turn = []
                self.d_turn.increment_turn()
                self.pos = 0

    def key_handler(self, key):
        """ update name """
        p_val = simplegui.KEY_MAP["p"]
        j_val = simplegui.KEY_MAP["j"]
        s_val = simplegui.KEY_MAP["s"]
        n_val = simplegui.KEY_MAP["n"]

        if self.state == "FIRST" and (key in [s_val, p_val, n_val] or key in KEY_ALL):
            self.first = False
            self.state = "PLAY"

        if self.player_state == "HUMAN_VALIDATE_START":
            if key in [KEY_LEFT, KEY_A]:
                self.d_hand.left_key_pos_give()
            if key in [KEY_RIGHT, KEY_D]:
                self.d_hand.right_key_pos_give()
            if key in [ p_val, j_val, KEY_UP, KEY_ENTER, KEY_DOWN, KEY_W, KEY_S ]:
                self.player_state = "HUMAN_DONE"
        if self.player_state == "HUMAN_PASS":
            if key in [ p_val]  or key in KEY_ALL:
                self.d_hand.unselect_all_cards()
                self.player_state = "HUMAN_DONE"
        if self.player_state == "HUMAN_VALIDATE":
            role  = self.players[self.hand_turn[self.pos]].get_role()
            cards = self.card_play[-1]
            if key in [KEY_LEFT, KEY_A]:
                self.d_hand.left_key_pos_play(role==3, cards)
            if key in [KEY_RIGHT, KEY_D]:
                self.d_hand.right_key_pos_play(role==3, cards)
            if key in [j_val, KEY_ENTER, KEY_UP, KEY_W]:
                self.player_state = "HUMAN_DONE"
            elif key in [p_val, KEY_DOWN, KEY_S]:
                self.d_hand.unselect_all_cards()
                self.player_state = "HUMAN_DONE"

        if self.state == "SEQUENCE":
            if  key in [s_val, p_val, n_val] or key in KEY_ALL:
                self.state = "SEQUENCE_GIVE"
                self.d_turn.clear_hands()
                self.d_turn.set_text(self.lang["seq_det2"])
        elif self.state == "SEQUENCE_GIVE":
            if self.player_state == "HUMAN_SEQ_VALIDATE" and len(self.d_hand.get_selected_cards()) != 0 :
                if key in [KEY_UP, KEY_W] :
                    self.player_state = "HUMAN_DONE"
                elif key in [KEY_DOWN, KEY_S]:
                    self.d_hand.down_key_sequence()
                elif key in [KEY_LEFT, KEY_A]:
                    self.d_hand.left_key_pos_sequence()
                elif key in [KEY_RIGHT, KEY_D]:
                    self.d_hand.right_key_pos_sequence()
        elif self.state in ["NEXT", "NEXT_PLAY"] or\
               (self.pos == len(self.hand_turn) and len(self.hand_turn) != 0):
            if key in [s_val, p_val, n_val] or key in KEY_ALL:
                self.state = "PLAY"
                self.hand_turn = []
                self.d_turn.increment_turn()
                self.pos = 0
        if key in KEY_ALL:
            self.refresh = 0

    def draw(self, canvas):
        """ update status every second -- draw status every frame """
        if self.first:
            self.hint.draw(canvas)

        if self.state in ["NEXT", "SEQUENCE", "FIRST"] or (self.pos == len(self.hand_turn) and len(self.hand_turn) != 0):
            if self.refresh == 0:
                self.d_next.set_selected(not self.d_next.get_selected())
            self.d_next.draw(canvas)

        if self.player_state == "HUMAN_VALIDATE_START":
            self.d_play.draw(canvas)
            if self.refresh == 0:
                self.d_play.set_selected(not self.d_play.get_selected())

        if self.player_state == "HUMAN_VALIDATE":
            if self.refresh == 0:
                self.d_play.set_selected(not self.d_play.get_selected())
                self.d_pass.set_selected(not self.d_play.get_selected())
            self.d_play.draw(canvas)
            self.d_pass.draw(canvas)

        if self.player_state == "HUMAN_PASS":
            if self.refresh == 0:
                self.d_pass.set_selected(not self.d_pass.get_selected())
            self.d_pass.draw(canvas)

        if self.refresh == 0:
            if self.state == "NEXT" and (self.player.hand_empty() or len(self.hand_turn) == 1):
                self.state = "PLAY"
                self.hand_turn = []
                self.d_turn.increment_turn()
                self.pos = 0
            self.update_turn()
            self.refresh = 30
        self.refresh -=1


class Distribute:
    """ Choose which card to give """

    def __init__(self, players:list, turn:DrawTurn, hand:DrawHand, lang:dict, settings:dict ):
        """ """
        self.settings = settings
        self.choice = self.settings["exchange"] == "select"
        self.lang  = lang
        self.count = 30
        self.players  = players
        self.player   = Player("", 0)
        self.pos      = 0
        self.p_pos    = 0
        for pos, player in enumerate(players):
            if player.is_human():
                self.player = player
                self.p_pos = pos

        self.d_turn   = turn
        self.d_hand   = hand
        self.hint = Rectangle(850, 80, 250, 250, ctext="blue", font = 14)
        self.dist = Rectangle(850, 330, 250, 100, ctext="blue", text="Give Choice", font = 34)
        self.t_list = {self.hint:"hint2", self.dist:"give", self.d_turn:"dist"}

        self.update_language(self.lang)

    def update_language(self, lang:dict):
        """ update language """
        self.lang  = lang
        for obj, name in self.t_list.items():
            if name in self.lang:
                obj.set_text(self.lang[name])

    def restart(self, choice=False):
        """ start distribution """
        self.choice = choice
        self.d_turn.clear_hands()
        self.d_turn.set_text(self.lang["dist"])
        self.pos      = 0
        for pos, player in enumerate(self.players):
            if player.is_human():
                self.player = player
                self.p_pos = pos

        self.d_hand.select_cards_choice(self.p_pos)
        self.update_language(self.lang)

    def click_pos(self, c_pos):
        """ click handler function """
        if self.p_pos in [0, 1] and self.choice and self.p_pos == self.pos:
            self.d_hand.click_pos_give(c_pos, self.player.get_role())
        if self.dist.is_click(c_pos) and self.pos == 0:
            l_cards = []
            for pos in range(4):
                if self.players[pos].is_human():
                    cards = self.d_hand.get_selected_cards()
                    self.players[pos].give_specific_cards(cards)
                    l_cards.insert( 0, cards )
                else:
                    l_cards.insert( 0, self.players[pos].give_choice() )
            for pos, cards in enumerate(l_cards):

                if self.players[pos].is_human():
                    self.d_hand.set_hand( self.players[pos].get_hand())
                    self.d_hand.add_cards(cards, True)
                else :
                    self.players[pos].add_cards(cards)
            self.dist.set_text(self.lang["start"])
            self.pos += 1
        if self.dist.is_click(c_pos) and self.pos == 1:
            self.pos += 1

    def key_handler(self, key):
        """ update name """
        l_val = [ simplegui.KEY_MAP["d"], simplegui.KEY_MAP["j"],\
                 simplegui.KEY_MAP["g"] , simplegui.KEY_MAP["n"] ]

        if self.p_pos in [0, 1] and self.choice and self.p_pos == self.pos:
            if key in [KEY_DOWN, KEY_S]:
                self.d_hand.down_key_sequence()
            elif key in [KEY_LEFT, KEY_A]:
                self.d_hand.left_key_pos_sequence()
            elif key in [KEY_RIGHT, KEY_D]:
                self.d_hand.right_key_pos_sequence()
        if (key in l_val or key in [KEY_UP, KEY_W]) and self.pos == 0:
            l_cards = []
            for pos in range(4):
                if self.players[pos].is_human():
                    cards = self.d_hand.get_selected_cards()
                    self.players[pos].give_specific_cards(cards)
                    l_cards.insert( 0, cards )
                else:
                    l_cards.insert( 0, self.players[pos].give_choice() )
            for pos, cards in enumerate(l_cards):
                if self.players[pos].is_human():
                    self.d_hand.set_hand( self.players[pos].get_hand())
                    self.d_hand.add_cards(cards, True)
                else :
                    self.players[pos].add_cards(cards)
            self.dist.set_text(self.lang["start"])
            self.pos += 1
        elif ( key in l_val or key in KEY_ALL) and self.pos == 1:
            self.pos += 1


    def draw(self, canvas):
        """ update status every second -- draw status every frame """
        self.hint.draw(canvas)
        if self.pos in [ 0, 1 ]:
            self.dist.draw(canvas)

        if self.count == 0 :
            self.count = 30
            if self.pos in [ 0, 1 ]:
                self.dist.set_selected(not self.dist.get_selected())
        self.count -= 1

class Choice:
    """ Process choice """

    def __init__(self, players:list, deck:Deck, turn:DrawTurn, hand:DrawHand, lang:dict, settings:dict):
        """ init function """
        self.refresh  = 30 # 30 fps / 30 = 1 frame / second
        self.pos      = 0
        self.cards    = []
        self.players  = players
        self.deck     = deck
        self.d_turn   = turn
        self.d_hand   = hand
        self.settings = settings
        self.lang     = lang
        self.response = 0
        self.d_order  = ["President", "Vice", "Concierge", "Nul", "Done", "Give"]
        self.d_choice = { True: {"President":[2, 1], "Vice":[2, 0], "Concierge":[1,0], "Nul":[1,0], "Done":[0,0]},
                          False:{"President":[2, 2], "Vice":[1, 1], "Concierge":[1,0], "Nul":[1,0], "Done":[0,0]} }
        self.acc  = Rectangle(600, 50, 180, 40, ctext="black", text="")
        self.rej  = Rectangle(600, 90, 180, 40, ctext="black", text="")
        self.acc1 = Rectangle(600, 50+96, 180, 40, ctext="black", text="")
        self.rej1 = Rectangle(600, 90+96, 180, 40, ctext="black", text="")
        self.dist = Rectangle(850, 330, 250, 100, ctext="blue", text="", font=32)
        self.hint = Rectangle(850, 80, 250, 250, ctext="blue", font = 14)
        self.acc2  = Rectangle(850, 330, 250, 110, ctext="blue", text="")
        self.rej2  = Rectangle(850, 440, 250, 110, ctext="blue", text="")

        self.t_list = {self.acc:"accept", self.rej:"reject",
                       self.acc1:"accept", self.rej1:"reject",
                       self.acc2:"accept", self.rej2:"reject", self.dist:"dist"}

        self.l_acc = [self.acc, self.acc1]
        self.l_rej = [self.rej, self.rej1]
        self.l_blink = []
        choice = self.settings["choice"] == "1_choice" and self.settings["position"] == "pres"
        self.d_val = self.d_choice[choice]
        self.count = 0
        self.restart(deck)

    def update_language(self, lang:dict):
        """ update language """
        self.lang  = lang
        for obj, name in self.t_list.items():
            if name in self.lang:
                obj.set_text(self.lang[name])

        d_val = { "1_choice": "hint_choice", "2_choice": "hint_choice2" }
        val = d_val[self.settings["choice"]]
        self.hint.set_text( lang[val] )

    def restart(self, deck:Deck):
        """ restart game  """
        for hand in self.d_turn.hands:
            hand.restart()
        self.update_language(self.lang)
        choice = self.settings["choice"] == "1_choice" and self.settings["position"] == "pres"
        self.d_val = self.d_choice[choice]
        self.pos      = 0
        self.deck     = deck
        self.d_val    = self.d_choice[choice]
        state         = self.d_order[self.pos]
        self.count    = self.d_val[self.d_order[self.pos]][1]
        self.response = "INPUT"

        for player in self.players:
            player.clear_hand()
        self.d_hand.clear_hand()

        self.count      = self.d_val[state][1]
        for pos in range(2):
            self.l_acc[pos].set_selected(False)
            self.l_rej[pos].set_selected(False)

    def update_status(self):
        """ update status """
        state = self.d_order[self.pos]
        if state in [ "Done", "Give" ]:
            return

        nb_cards = self.d_val[state][0]
        player   = self.players[self.pos]

        if player.is_human():
            if self.response == "INPUT":
                self.cards  = self.deck.deal_cards( nb_cards )
                self.d_turn.hands[self.pos].clear_hand()
                self.d_turn.hands[self.pos].add_cards(self.cards)
                if self.count == 0:
                    self.response = True
                    cards = self.cards
                else:
                    self.l_acc[self.pos].set_selected(False)
                    self.l_rej[self.pos].set_selected(False)
                    self.response = "WAIT"
                    return
            elif self.response == "WAIT":
                return
            else:
                s_val = self.response
                cards = self.cards
                self.response = "INPUT"
        else :
            cards  = self.deck.deal_cards( nb_cards )
            s_val  = True
            if self.count > 0:
                s_val = player.choice(cards)
                self.l_acc[self.pos].set_selected(s_val)
                self.l_rej[self.pos].set_selected(not s_val)

        player.clear_hand()
        self.d_turn.hands[self.pos].clear_hand()
        if self.count == 0 or s_val is True:
            self.d_turn.hands[self.pos].add_cards(cards)
            player.add_cards(cards)
            self.pos += 1
            state = self.d_order[self.pos]
            self.count = self.d_val[state][1]
        else:
            if s_val is False:
                self.d_hand.add_cards(cards)
                self.d_turn.hands[self.pos].add_cards(cards)
            self.count -= 1


    def click_pos(self, c_pos):
        """ click handler function """
        for pos in range(2):
            if self.pos == pos and self.players[pos].is_human():
                if self.l_acc[pos].is_click(c_pos) or self.acc2.is_click(c_pos):
                    self.response = True
                elif self.l_rej[pos].is_click(c_pos) or self.rej2.is_click(c_pos):
                    self.response = False
                if self.response is True or self.response is False:
                    self.l_acc[pos].set_selected(self.response)
                    self.l_rej[pos].set_selected(not self.response)

        if self.pos == 4:
            if self.dist.is_click(c_pos):
                self.deck.reinsert_cards( self.d_hand.card_list() )
                nb_cards = self.deck.nb_cards()
                self.pos += 1
                self.d_hand.clear_hand()
                for pos in range(nb_cards):
                    self.players[pos%4].add_card(self.deck.deal_card())
                for pos in range(4):
                    if self.players[pos].is_human():
                        self.d_hand.add_cards(self.players[pos].card_list())
                    self.d_turn.hands[pos].clear_hand()

    def key_handler(self, key):
        """ update name """
        d_val = [ simplegui.KEY_MAP["d"] ]
        a_val = [ simplegui.KEY_MAP["a"], simplegui.KEY_MAP["up"] ]
        r_val = [ simplegui.KEY_MAP["r"], simplegui.KEY_MAP["down"] ]


        if key in KEY_ALL:
            self.refresh = 1

        for pos in range(2):
            if self.response == "WAIT" and self.pos == pos and self.players[pos].is_human():
                if key in a_val  or key in [KEY_UP, KEY_W, KEY_ENTER, KEY_RIGHT, KEY_D] :
                    self.response = True
                elif key in r_val or key in [KEY_DOWN, KEY_S]:
                    self.response = False
                if self.response is True or self.response is False:
                    self.l_acc[pos].set_selected(self.response)
                    self.l_rej[pos].set_selected(not self.response)

        if self.pos == 4:
            if key in d_val or key in KEY_ALL:
                self.deck.reinsert_cards( self.d_hand.card_list() )
                nb_cards = self.deck.nb_cards()
                self.pos += 1
                self.d_hand.clear_hand()
                for pos in range(nb_cards):
                    self.players[pos%4].add_card(self.deck.deal_card())
                for pos in range(4):
                    if self.players[pos].is_human():
                        self.d_hand.add_cards(self.players[pos].card_list())
                    self.d_turn.hands[pos].clear_hand()

    def draw(self, canvas):
        """ update status every second -- draw status every frame """
        self.refresh -= 1
        if self.refresh == 0:
            self.refresh = 30
            self.update_status()
            if self.pos in [0, 1] and self.players[self.pos].is_human():
                self.acc2.set_selected(not self.acc2.get_selected())
                self.rej2.set_selected(not self.acc2.get_selected())
            if self.pos == 4:
                self.dist.set_selected( not self.dist.get_selected() )

        self.hint.draw(canvas)
        if self.pos <= 4:
            self.acc.draw(canvas)
            self.rej.draw(canvas)

        if self.pos in [0, 1] and self.players[self.pos].is_human():
            self.acc2.draw(canvas)
            self.rej2.draw(canvas)

        if self.pos >= 1 and  self.d_val[self.d_order[1]][1] == 1:
            #Draw VP option, if he has a choice
            self.acc1.draw(canvas)
            self.rej1.draw(canvas)

        if self.pos == 4:
            # blink to remind the next state
            self.dist.draw(canvas)

        d_val = { "1_choice": "hint_choice", "2_choice": "hint_choice2" }
        val = d_val[self.settings["choice"]]
        self.hint.set_text( self.lang[val] )



class MainGame(Screen):
    """ Game Object """

    def __init__(self, settings:dict, lan:LanguageVal, update, players, reorder_players, stats):
        """ init function """
        super().__init__(settings, lan)
        self.states = {0:"CHOICE", 1:"DISTRIBUTE", 2:"TURNS", 3:"END", 4:"STATS"}
        self.state = 0
        self.reorder_players = reorder_players
        self.players = players
        self.stats = stats
        self.deck  = Deck()
        self.d_in  = {}
        self.d_in["main"]   = ( 950,   0,  200,  40, "black", "blue",  "", "white", 16)
        self.d_in["special"] = ( 850,   0,  100,  40, "black", "blue",  "", "white", 16)
        self.d_in["reset"]   = ( 850,  40,  300,  40, "black", "blue",  "", "white", 30)

        self.frame_count = 30
        self.d_next = Rectangle(850, 330, 250, 100, ctext="blue", text="")
        self.d_status = DrawStatus(players, 0, 0)
        self.d_turn   = DrawTurn(200,  0)
        d_val = {True:20, False:46}
        c_val = self._set["choice"] == "2_choice" and self._set["position"] != "pres"
        self.d_hand   = DrawHand(d_val[c_val], 452, Hand([]))
        for _, player in enumerate(players):
            self.d_turn.add_hand(player, Hand([]))

        self.lang  = self._lan.l_val[self._set["language"]]
        self.d_next.set_text( self.lang["next_game"] )
        self.d_choice = Choice(players,self.deck, self.d_turn, self.d_hand, self.lang, settings)

        self.d_dist = Distribute(players, self.d_turn, self.d_hand, self.lang, settings)
        self.d_play = PlayTurn(self.players, self.d_turn, self.d_hand, self.lang, self._set, self.stats)

        self.d_tog = {}
        self.d_func = { "main":self.s_main, "reset":self.force_restart, "special":self.change_language}
        self.l_blink = []
        self.set_display(self.d_in, self.d_tog, self.d_func, self.l_blink)
        self.update = update
        d_val = { "Francais":"English", "English":"Francais" }
        self._disp["special"].set_text( d_val[ self._set["language"] ] )

    def update_language(self):
        """ update langues including non Screen variables """
        super().update_language()
        self.lang  = self._lan.l_val[self._set["language"]]
        self.d_choice.update_language(self.lang)
        self.d_dist.update_language(self.lang)
        self.d_play.update_language(self.lang)
        self.d_next.set_text( self.lang["next_game"] )

    def draw(self, canvas):
        """ draw background """
        super().draw(canvas)
        self.d_turn.draw(canvas)
        self.d_status.draw(canvas)
        self.d_hand.draw(canvas)
        if self.state == 0:
            t_val = self.text_val("p_choices")
            self.d_turn.set_text(t_val)
            self.d_choice.draw(canvas)
            if self.d_choice.pos == 5:
                self.lang   = self._lan.l_val[self._set["language"]]
                c_val = self._set["exchange"] == "select"
                self.d_dist = Distribute(self.players, self.d_turn, self.d_hand, self.lang, self._set)
                self.d_dist.restart(c_val)
                self.state = 1
        elif self.state == 1:
            self.d_dist.draw(canvas)
            if self.d_dist.pos == 2:
                self.state = 2
                self.d_play = PlayTurn(self.players, self.d_turn, self.d_hand, self.lang, self._set, self.stats)
        elif self.state == 2:
            self.d_play.draw(canvas)
            if self.d_play.state == "NEXT_GAME":
                self.state = 3
                self.players = self.d_play.winners
                d_titles = {0:"pres", 1:"vice", 2:"conc", 3:"nul"}
                for count, player in enumerate(self.players):
                    player.set_role(count)
                    if player.is_human():
                        self._set["position"] = d_titles[count]
                self.d_turn.set_game_results(self.players)
                self.d_status = DrawStatus(self.players, 0, 0)
                self.frame_count = 30
        elif self.state == 3:
            self.d_next.draw(canvas)
            self.frame_count -= 1
            if self.frame_count == 0:
                self.frame_count = 30
                self.d_next.set_selected(not self.d_next.get_selected())


    def key_handler(self, key):
        """ update name """
        r_val = [ simplegui.KEY_MAP["R"]]
        m_val = [ simplegui.KEY_MAP["M"]]
        o_val = [ simplegui.KEY_MAP["O"]]

        if self.state == 0:
            self.d_choice.key_handler(key)
        if self.state == 1:
            self.d_dist.key_handler(key)
        if self.state == 2:
            self.d_play.key_handler(key)
        if self.state == 3 and key in KEY_ALL:
            self.restart()
        if key in r_val:
            self.restart()
        if key in m_val:
            self.s_main()
        if key in o_val:
            self.change_language()

    def click_pos(self, pos):
        """ click event """
        super().click_pos(pos)
        if self.state == 0:
            self.d_choice.click_pos(pos)
        if self.state == 1:
            self.d_dist.click_pos(pos)
        if self.state == 2:
            self.d_play.click_pos(pos)
        if self.state == 3:
            if self.d_next.is_click(pos):
                self.restart()


    def restart(self, reorder_players=False):
        """ start function """
        self.stats["nb_start"] += 1
        self.deck  = Deck()
        if reorder_players:
            self.players = self.reorder_players()
        self.d_status = DrawStatus(self.players, 0, 0)
        self.d_turn   = DrawTurn(200,  0)
        d_val = {True:46, False:20}
        c_val = self._set["choice"] == "1_choice" and self._set["position"] == "pres"
        self.d_hand   = DrawHand(d_val[c_val], 452, Hand([]))
        for _, player in enumerate(self.players):
            self.d_turn.add_hand(player, Hand([]))
        self.lang  = self._lan.l_val[self._set["language"]]
        self.d_choice = Choice(self.players, self.deck, self.d_turn, self.d_hand, self.lang, self._set)
        self.d_choice.restart(self.deck)
        self.d_dist = Distribute(self.players, self.d_turn, self.d_hand, self.lang, self._set)
        self.d_play = PlayTurn(self.players, self.d_turn, self.d_hand, self.lang, self._set, self.stats)
        self.state = 0


    def s_main(self):
        """ start function """
        self._set["state"] = "MAIN"
        self.update()

    def change_language(self):
        """ start function """
        d_val = { "Francais":"English", "English":"Francais" }
        old = self._set["language"]
        new = d_val[ old ]
        self._set["language"] = new
        self._disp["special"].set_text(old)
        self.update_language()
        self.update()

class Game:
    """ Game Object """

    def __init__(self, name):
        """ init function """
        state      = "GAME"
        self.name  = name
        self.l_val = []
        self.d_player = {}
        self.players  = []
        self.stats    = {"nb_start":1, "nb_complete":0, "last_games":[]}
        self.d_out  = { "language":"Francais", "Sequence":"3_Card","choice":"2_choice",\
                        "exchange":"lowest","position":"nul","state":state,\
                        "restart":False}
        self.lang   = LanguageVal()
        self.generate_players()
        self.menu   = MenuOptions(self.d_out, self.lang, self.update_language)
        self.rule   = Rules(self.d_out, self.lang, self.update_language)
        self.stat_m = Stats(self.d_out, self.lang, self.update_language, self.stats)
        self.main   = MainMenu(self.d_out, self.lang, self.update_language)
        self.game   = MainGame(self.d_out, self.lang, self.update_language, self.players, self.reorder_players, self.stats)
        self.d_stat = {"MENU":self.menu, "RULES":self.rule, "MAIN":self.main, "GAME":self.game, "Stats":self.stat_m}
        self.update_language()

    def generate_players(self):
        """ create names based on my friends names """
        self.l_val = get_names(3)
        for _, name in enumerate(self.l_val):
            self.d_player[name] = Player(name, 0, False)
        lang  = self.lang.l_val[self.d_out["language"]]
        self.name = lang["player_id"]
        self.d_player["PLAYER_1"] = Player(self.name, 0, True)
        self.reorder_players()

    def reorder_players(self):
        """ reorder the players """
        l_val = list(self.l_val)
        d_titles = {"pres":0, "vice":1, "conc":2, "nul":3}
        l_val.insert(d_titles[self.d_out["position"]], "PLAYER_1")


        self.players = []
        for val, name in enumerate(l_val):
            self.d_player[name].set_role(val)
            self.players.append(self.d_player[name])

        lang  = self.lang.l_val[self.d_out["language"]]
        for player in self.players:
            if player.is_human():
                player.set_name(lang["player_id"])
        return self.players

    def update_language(self):
        """ Update language in all menus """
        lang  = self.lang.l_val[self.d_out["language"]]
        for player in self.players:
            if player.is_human():
                player.set_name(lang["player_id"])

        for _, val in self.d_stat.items():
            val.update_language()


    def key_handler(self, key):
        """ update name """
        val = self.d_stat[self.d_out["state"]]
        val.key_handler(key)

    def update_name(self, name):
        """ update name """
        self.name  = name

    def draw(self, canvas):
        """ draw function """
        if self.d_out["restart"] and self.d_out["state"] == "GAME":
            self.game.restart(True)
            self.d_out["restart"] = False

        val = self.d_stat[self.d_out["state"]]
        val.draw(canvas)

    def click_pos(self, pos):
        """ click handler function """
        val = self.d_stat[self.d_out["state"]]
        val.click_pos(pos)

class Background():
    """ Define background for card game """

    def __init__(self, name, width, height, color):
        """ Initializes the background """
        d_val = {"Big":1.5, "Normal":1, "Small":0.5}
        const = d_val[draw.screen_size]

        self.frame = simplegui.create_frame(name, int(width*const), int(height*const), 0)
        self.default = "Player 1"
        self.game = Game(self.default)

        self.frame.set_keydown_handler(self.game.key_handler)
        self.frame.set_canvas_background(color)
        self.frame.set_mouseclick_handler(self.game.click_pos)
        self.frame.set_draw_handler(self.game.draw)
        self.frame.start()

def run_small_screen():
    """ run program with small screen resolution """
    draw.screen_size = "Small"
    Background("Jeu du President", 1100, 550, "Green")


def run_normal_screen():
    """ run program with small screen resolution """
    draw.screen_size = "Normal"
    Background("Jeu du President", 1100, 550, "Green")

def run_big_screen():
    """ run program with small screen resolution """
    draw.screen_size = "Big"
    Background("Jeu du President", 1100, 550, "Green")

run_big_screen()
