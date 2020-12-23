import file_input
lines = file_input.get_input(22)

i = lines.index("Player 2:\n")
crab_cards = [int(line.strip()) for line in lines[1:i-1]]
my_cards = [int(line.strip()) for line in lines[i+1:]]

def score(cards):
    n = len(cards)
    score = 0
    for i, card in enumerate(cards):
        score += (n - i) * card
    return score

def combat(my_cards, crab_cards):
    while len(my_cards) > 0 and len(crab_cards) > 0:
        mine = my_cards.pop(0)
        crab = crab_cards.pop(0)
        if mine > crab:
            my_cards.append(mine)
            my_cards.append(crab)
        else:
            crab_cards.append(crab)
            crab_cards.append(mine)
    winner = my_cards if len(my_cards) > 0 else crab_cards
    print(score(winner))

def recursive_combat(my_cards, crab_cards, print_score):
    visited_states = set()
    while len(my_cards) > 0 and len(crab_cards) > 0:
        state = str(my_cards) + str(crab_cards)
        if state in visited_states:
            return False # crab = player 1
        visited_states.add(state)
        mine = my_cards.pop(0)
        crab = crab_cards.pop(0)
        if len(my_cards) >= mine and len(crab_cards) >= crab:
            i_won = recursive_combat(my_cards[:mine], crab_cards[:crab], False)
        else:
            i_won = (mine > crab)
        if i_won:
            my_cards.append(mine)
            my_cards.append(crab)
        else:
            crab_cards.append(crab)
            crab_cards.append(mine)
    if print_score:
        winner = my_cards if len(my_cards) > 0 else crab_cards
        print(score(winner))
    return (len(my_cards) > 0)

combat(my_cards.copy(), crab_cards.copy())
recursive_combat(my_cards.copy(), crab_cards.copy(), True)
