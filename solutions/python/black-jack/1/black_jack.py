"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

CARD_VALUES = {
    "A": 1,
    **{str(n): n for n in range(2, 11)},
    "J": 10, "Q": 10, "K": 10,
}

def value_of_card(card):
    return CARD_VALUES[card]

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    value_one, value_two = value_of_card(card_one), value_of_card(card_two)
    if value_one == value_two:
        return (card_one, card_two)
    elif value_one > value_two:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    if "A" in (card_one, card_two):
        return 1
    hand = value_of_card(card_one) + value_of_card(card_two)
    return 11 if hand<= 10 else 1

def is_blackjack(card_one, card_two):
    has_ace = "A" in (card_one, card_two)
    has_ten = value_of_card(card_one) == 10 or value_of_card(card_two) == 10
    return has_ace and has_ten

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) != value_of_card(card_two):
        return False
    return True


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    value_of_hand = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= value_of_hand <= 11
