""" card api for president's game """
# "card" - generates the cards, hands, and basic player for hte president games.
#
# I was trying to generate a playable version of the french canadian card game
# I am using  CodeSkulptor and SimpleGUI from An Introduction to Interactive Programming in Python
# Since it keeps the game has browser based therefore accessible to all devices
# Please enjoy the game
#
# Programming - Samuel Paul (samuelspaul@gmail.com)
#
# Current Version (v1.0 - 21 January 2024):
#pylint: disable=wildcard-import,line-too-long,unused-wildcard-import
# File saved in : https://py3.codeskulptor.org/#user309_Kd3jylJSQd_0.py
import random

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')

SUIT = {"H":1,"D":2,"C":3,"S":4,"R":5,"B":6}
RANK_VAL = {"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,
        "K":13,"A":14,"2":15,"O":16}

RANK_HIGH_LIST = ["O","2","A","K","Q","J","T","9","8","7","6","5","4","3"]
RANK_LOW_LIST  = ["3","4","5","6","7","8","9","T","J","Q","K","A","2","O"]


POSITIONS = ["President", "Vice", "Concierge", "Nul"]

class Card:
    """ Class card """

    def __init__(self, rank, suit):
        """ init card """
        if suit in SUIT and rank in RANK_VAL:
            self.__rank = rank
            self.__suit = suit
        else:
            self.__rank = "O"
            self.__suit = "R"

    def get_rank(self):
        """ get_rank """
        return self.__rank

    def get_suit(self):
        """ get_suit """
        return self.__suit

    def get_val(self):
        """ get_val """
        return RANK_VAL[self.__rank]

    def __str__(self):
        """ display card as a string """
        if self.__rank != "O":
            return f"{self.__rank}{self.__suit}"
        else:
            return "Jk"

class Deck:
    """ define deck class """
    def __init__(self, nb_deck=1, shuffle=True, joker=True):
        """ create a Deck object """
        self.cards = []
        for _ in range(nb_deck):
            self.add_deck(joker)
        if shuffle:
            self.shuffle()

    def nb_cards(self):
        """ return nb of cards """
        return len(self.cards)

    def add_deck(self, joker=True):
        """ add 1 full deck """
        for suit in SUITS :
            for rank in RANKS :
                card = Card(rank, suit)
                self.cards.append(card)
        if joker:
            self.cards.append(Card("O", "B"))
            self.cards.append(Card("O", "R"))

    def shuffle(self):
        """ shuffle the deck """
        random.shuffle(self.cards)

    def deal_card(self):
        """ deal a card object from the deck """
        return self.cards.pop()

    def deal_cards(self, nb_cards: int):
        """ deal cards """
        card_list = []
        for _ in range(nb_cards):
            card = self.cards.pop()
            card_list.append(card)
        return card_list

    def reinsert_card(self, card: Card):
        """ give the president choice """
        self.cards.insert(0, card)

    def reinsert_cards(self, card_list: list):
        """ give the president choice """
        for card in card_list:
            self.reinsert_card( card )

    def __str__(self):
        """ return a string representing the deck """
        msg = ""
        for card in self.cards:
            msg += str(card) + " "
        return msg


class Hand:
    """ Class Hand """

    def __init__(self, cards=False):
        """ init class Hand """
        self._cards = {}
        if cards:
            self.add_cards(cards)

    def clear(self):
        """ clear hand """
        self._cards = {}


    def nb_cards_rank(self, rank):
        """ returns nb of cards in hand """
        count = 0
        if rank in self._cards:
            count = len(self._cards[rank])
        return count

    def nb_cards(self):
        """ returns nb of cards in hand """
        count = 0
        for _, cards in self._cards.items():
            count += len(cards)
        return count

    def hand_empty(self):
        """ returns True if Hand is empty """
        return self.nb_cards()==0

    def card_list(self, lowest=False):
        """ create card list """
        l_out = []
        d_val = {False:RANK_HIGH_LIST, True:RANK_LOW_LIST}
        l_val = d_val[lowest]
        for rank in l_val:
            if rank in self._cards:
                for card in self._cards[rank]:
                    l_out.append(card)
        return l_out

    def __str__(self):
        """ display card as a string """
        str_val = ""
        l_val = RANK_HIGH_LIST
        for rank in l_val:
            if rank in self._cards:
                for card in self._cards[rank]:
                    str_val += f"{card}  "
        return str_val

    def add_cards(self, cards):
        """ add card """
        for card in cards:
            self.add_card(card)

    def add_card(self, card:Card):
        """ add card """
        if card is False:
            return
        rank = card.get_rank()
        if rank in self._cards:
            self._cards[rank].append(card)
        else :
            self._cards[rank] = [card]

    def is_rank(self, rank):
        """ is card of that rank available """
        out = False
        if rank in self._cards:
            out = len(self._cards[rank])
        return out

    def give_specific_cards(self, cards:list):
        """ give specific cards """
        if cards is False:
            return False
        out = []
        for card in cards:
            tmp = self.give_specific_card(card)
            if tmp is not False:
                out.append(tmp)
        return out

    def give_specific_card(self, card:Card):
        """ remove specific card """
        out = False
        rank = card.get_rank()
        if rank in self._cards:
            for pos, t_card in enumerate(self._cards[rank]):
                if card == t_card:
                    out =self._cards[rank].pop(pos)
        return out

    def get_cards(self, rank, nb_cards=1):
        """ get selected card """
        card_list = False
        if rank in self._cards:
            if len(self._cards[rank]) >= nb_cards:
                card_list = self._cards[rank][:nb_cards]
                self._cards[rank] = self._cards[rank][nb_cards:]
                if len(self._cards[rank]) == 0:
                    del self._cards[rank]
        return card_list

    def show_rank(self, lowest=False, l_size=1, only_size=False):
        """ show card lowest or highest """
        d_val = {False:RANK_HIGH_LIST, True:RANK_LOW_LIST}
        l_val = d_val[lowest]
        for rank in l_val:
            if rank in self._cards:
                if ( len(self._cards[rank]) == l_size ) or \
                    ( only_size is False and len(self._cards[rank]) > l_size):
                    return rank
        return False

    def give_lowest(self, not_double=False):
        """ give lowest card """
        if self.hand_empty() is True:
            return False
        rank = self.show_rank(lowest=True)
        if not_double is True:
            tmp_rank = self.show_rank(lowest=True, only_size=not_double)
            if tmp_rank is not False:
                rank = tmp_rank

        card = self._cards[rank].pop()
        if len( self._cards[rank] ) == 0:
            del self._cards[rank]
        return card

    def give_highest(self):
        """ give highest card """
        if self.hand_empty() is True:
            return False
        rank = self.show_rank(lowest=False)

        card = self._cards[rank].pop()
        if len( self._cards[rank] ) == 0:
            del self._cards[rank]
        return card


    def start_turn(self):
        """ play lowest card """
        rank = self.show_rank(lowest=True)
        card_list = self._cards[rank]
        del self._cards[rank]
        return card_list

    def show_better_rank(self, target, l_size=1, only_size=False ):
        """ show card lowest or highest """
        val = RANK_VAL[target]
        l_val = RANK_LOW_LIST
        for rank in l_val:
            if rank in self._cards and  RANK_VAL[rank] > val:
                if  ( len(self._cards[rank]) == l_size ) or \
                    ( only_size is False and len(self._cards[rank]) > l_size):
                    return rank
        return False

    def show_winning_choices(self, card_list:list, equalize=False):
        """ show list of winning combination """
        r_val = []
        r_cards = []
        target = card_list[0].get_rank()
        val = RANK_VAL[target]
        l_val = RANK_LOW_LIST
        if len(card_list) == 0:
            return r_val, r_cards


        for rank in l_val:
            if rank in self._cards and len(self._cards[rank]) >= 1:
                if len(card_list) >= 2 and rank == "2" and target != "2":
                    if "2" in self._cards and len(self._cards["2"]) >= len(card_list)-1:
                        r_val.append("2")
                        r_cards.append(self._cards["2"][:len(card_list)-1])
                    elif "2" in self._cards and len(self._cards["2"]) >= len(card_list):
                        r_val.append("2")
                        r_cards.append(self._cards["2"][:len(card_list)])
                elif equalize and target in self._cards and\
                       len(self._cards[target]) >= len(card_list):
                    r_val.append(rank)
                    r_cards.append(self._cards[target][:len(card_list)])
                elif rank in self._cards and "O" == rank and len(self._cards["O"]) != 0:
                    r_val.append("O")
                    r_cards.append([self._cards["O"][0]])
                elif rank in self._cards and RANK_VAL[rank] > val and\
                        len(self._cards[rank]) >= len(card_list):
                    r_val.append(rank)
                    r_cards.append(self._cards[rank][:len(card_list)])


        return r_val, r_cards

    def hand_scan(self):
        """ scan the hands """
        d_val = {}
        l_val = {}

        d_val["nb_types"] = len(self._cards)
        l_val["nb_types"] = self._cards.keys()

        d_val["nb_cards"] = self.nb_cards()
        l_val["nb_cards"] = list(self._cards)

        for val in range(1,5):
            d_val[val] = 0
            l_val[val] = []

        for _, cards in self._cards.items():
            if len(cards) >= 1:
                d_val[val] += 1
                l_val[val].append(cards)

        if "2" in self._cards and self._cards["2"] >= 1:
            d_val["nb_2"] = len(self._cards["2"])
            l_val["nb_2"] = self._cards["2"]

        if "O" in self._cards and self._cards["O"] >= 1:
            d_val["nb_2"] = len(self._cards["O"])
            l_val["nb_2"] = self._cards["O"]

    def play_turn(self, card_list:list, equalize=False):
        """ play lowest  """
        target = card_list[0].get_rank()
        rank = False
        cards_out = False

        if target == "O":
            return cards_out
        elif target == "2":
            if equalize:
                cards_out = self.get_cards("2", len(card_list))
                if cards_out:
                    return cards_out
            cards_out = self.get_cards("O")
            if cards_out:
                return cards_out

        if equalize:
            cards_out = self.get_cards(target, len(card_list))
            if cards_out:
                return cards_out

        rank = self.show_better_rank(target, len(card_list), only_size=False)
        if len(card_list) == 1:
            cards_out = self.get_cards(rank, len(card_list))
            if cards_out:
                return cards_out

        if rank == "O":
            cards_out = self.get_cards(rank, 1)
        elif rank == "2":
            if target != "2":
                cards_out = self.get_cards(rank, len(card_list)-1)
        elif rank is not False:
            cards_out = self.get_cards(rank, len(card_list))
        else:
            if target != "2":
                cards_out = self.get_cards("2", len(card_list)-1)
            if not cards_out:
                cards_out = self.get_cards("O", 1)

        return cards_out

    def give_choice(self, role):
        """ give cards at the begiining of the game """
        card_list = [ ]

        if role == 0:
            card_list.append( self.give_lowest() )
            card_list.append( self.give_lowest() )
        elif role == 1:
            card_list.append( self.give_lowest() )
        elif role == 2:
            card_list.append( self.give_highest() )
        elif role == 3:
            card_list.append( self.give_highest() )
            card_list.append( self.give_highest() )

        return card_list

class Player:
    """ Basic Player Class """

    def __init__(self, name, role, ishuman=False):
        self.__name = name
        self._role = role
        self._hand = Hand()
        self._human = ishuman

    def show_winning_choices(self, card_list:list, equalize=False):
        """ show list of winning combination """
        equalize = self._role == 3
        return self._hand.show_winning_choices(card_list, equalize=equalize)

    def get_cards(self, rank, nb_cards=1):
        """ get specific cards """
        return self._hand.get_cards(rank, nb_cards)

    def set_hand(self, hand):
        """ set hand """
        self._hand = hand

    def get_hand(self):
        """ get hand """
        return self._hand

    def set_human(self, val:bool):
        """ set human """
        self._human = val

    def is_human(self):
        """ return is human """
        return self._human

    def clear_hand(self):
        """ clear hand for new game """
        self._hand = Hand()

    def set_role(self, role):
        """ set role """
        self._role = int(role)

    def get_role(self):
        """ get role """
        return self._role

    def set_name(self, name):
        """ set name """
        self.__name = name

    def get_name(self):
        """ get role """
        return self.__name

    def nb_cards(self):
        """ returns nb cards """
        return self._hand.nb_cards()

    def str_status(self):
        """ string to display during Choice """
        str_val = self.str_choice()
        str_val += f"\n{self.nb_cards()} cards"
        return str_val

    def give_specific_cards(self, cards: list):
        """ get selected card """
        return self._hand.give_specific_cards(cards)

    def give_specific_card(self, card: Card):
        """ get selected card """
        return self._hand.give_specific_card(card)

    def str_choice(self):
        """ string to display during Choice """
        if self._role >= len(POSITIONS):
            return " "
        str_val = POSITIONS[self._role] + f"\n({self.__name})"
        return str_val

    def __str__(self):
        """ string function """
        str_val = f"Player ({self._role})"
        if self.__name != "":
            str_val = f"{self.__name} ({self._role})"
            str_val += f" (Cards:{self._hand.nb_cards()})"
        return str_val

    def hand_empty(self):
        """ returns True if Hand is empty """
        return self._hand.hand_empty()

    def print_hand(self):
        """ print hand  """
        str_val = str(self)
        str_val += f"  {self._hand}"
        return str_val

    def choice(self, cards:list):
        """ VP or President Choice  """
        if len(cards) == 2: #President choice
            return self.president_choice(cards[0], cards[1])
        elif len(cards) == 1: #Vice choice
            return RANK_VAL[cards[0].get_rank()] >= 10
        else:
            return False #This state should never happen

    def president_choice(self, card_1:Card, card_2:Card):
        """ accept or refuse president choice """
        best_choice = ["2", "O"]
        if card_1.get_rank() in best_choice or card_2.get_rank() in best_choice:
            return True
        if card_1.get_rank() == card_2.get_rank() and RANK_VAL[card_1.get_rank()] >= 8:
            return True
        if RANK_VAL[card_1.get_rank()] + RANK_VAL[card_2.get_rank()] >= 20:
            return True
        return False

    def add_card(self, card:Card):
        """ receive card """
        self._hand.add_card(card)

    def add_cards(self, card_list:list):
        """ receive card """
        for card in card_list:
            self._hand.add_card(card)

    def give_card(self, nb_val):
        """ give cards """
        card_list =  [ ]
        for _ in range(nb_val):
            card_list.append( self._hand.give_lowest() )
        return card_list

    def give_choice(self):
        """ give cards at the begiining of the game """
        return self._hand.give_choice(self._role)

    def card_list(self):
        """ return card list """
        return self._hand.card_list()

    def start_turn(self):
        """ start turn usually by playing the lowest card or cards in the Hand """
        return self._hand.start_turn()

    def play_turn(self, card_list:list):
        """ play your turn if  """
        equalize = self._role == 3
        card_play = self._hand.play_turn(card_list, equalize=equalize)
        return card_play


def distribute(players):
    """ distribute all cards """
    dk = Deck()
    nb_cards = dk.nb_cards()
    for pos in range(nb_cards):
        players[int(pos % 4)].add_card(dk.deal_card())

    l_1 = players[0].give_choice()
    l_2 = players[1].give_choice()
    players[0].add_cards( players[3].give_choice() )
    players[1].add_cards( players[2].give_choice() )
    players[2].add_cards( l_1 )
    players[3].add_cards( l_2 )

def is_cardlist_better(list1, list2, isequal:bool=False):
    """ is card list better """
    target = list1[0].get_rank()
    dest   = list2[0].get_rank()

    if dest == "O":
        return True

    if dest == "2" and  not target in ["2", "O"]:
        if len(list2) == len(list1) or len(list2) == len(list1) -1:
            return True

    if RANK_VAL[dest] > RANK_VAL[target] and len(list1) == len(list2):
        return True

    if isequal:
        if RANK_VAL[dest] == RANK_VAL[target] and len(list1) == len(list2):
            return True

    return False

def card_seq_increment(card_list, all_players=False):
    """ test if card sequence is incremental
        if there is a sequence of 3 cards of rank growing by the same increment
        then there the players included in the sequence can drop cards
        ex: 4-5-6-8  (the first 3 players can drop 1 card)
        ex: 8 8 - 9 9 - 10 10  - J J (all 4 players drop 2 cards)
    """
    len_list = len(card_list)
    if len_list < 3 :
        return False

    l_val = []
    for _, val in enumerate(card_list):
        l_val.append(RANK_VAL[val[0].get_rank()])

    l_diff = []
    for index in range(1, len(card_list)):
        l_diff.append( l_val[index] - l_val[index-1] )

    if not all_players:
        if len_list == 3:
            if l_diff[0] == l_diff[1]:
                return  [True, True, True]
        if len_list == 4:
            if l_diff[0] == l_diff[1] and l_diff[1] == l_diff[2]:
                return [True, True, True, True]
            if l_diff[0] == l_diff[1]:
                return [True, True, True, False]
            if l_diff[1] == l_diff[2]:
                return [False, True, True, True]
    else :
        if len_list == 4:
            if l_diff[0] == l_diff[1] and l_diff[1] == l_diff[2]:
                return [True, True, True, True]

    return False
