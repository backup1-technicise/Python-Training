'''
Assignment 10 : Make a two-player Rock-Paper-Scissors game.
(Hint:
1. Ask for two player plays (using input),
2. Compare 2 players inputs
3. Print out a message of congratulations to the winner Otherwise continue.
4. Ask if the players want to start a new game.

Remember the rules:

    Rule 1: Rock beats scissors
    Rule 2: Scissors beats paper
    Rule 3: Paper beats rock

'''

# Specification of ROck - Paper - Scissors Game is as follows:
'''
Specification

The game is played by two players, playerA and playerB. Each player selects from among a set of three options
{null, rock, paper, scissors}. null is used to represent the state before a player has chosen.
Using an ordered pair (playerA_choice, playerB_choice) creates the possible game states:

 (null,    rock)
 (null,    paper)
 (null,    scissors)
 (rock,    null)
 (rock,    rock)
 (rock,    paper)
 (rock,    scissors)
 (paper,   null)
 (paper,   rock)
 (paper,   paper)
 (paper,   scissors)
 (scissors, null)
 (scissors, rock)
 (scissors, paper)
 (scissors, scissors)

 There are three final states (Rules) and three transition functions to them:

playerA_wins = (rock, scissors) | (paper, rock) | (scissors, paper)
playerB_wins = (rock, paper) | (paper, scissors) | (scissors, rock)
draw = (rock, rock) | (paper, paper) | (scissors, scissors)

The states ( Start state of Player A and Player B ):

 (null,    rock)
 (null,    paper)
 (null,    scissors)
 (rock,    null)
 (paper,   null)
 (scissors, null)


'''

playerA_choice = ''
playerB_choice = ''


def game_finish(state):
    if state in ("Game is a Draw", "Player A Wins", "Player B Wins"):
        print "Game is over !!! "
        Option = raw_input("Will you Continue game ? (y / n) : ")
        if Option == "y":
            # Simulate Initialization
            global playerA_choice
            playerA_choice = null
            global playerB_choice
            playerB_choice = null
            return True
        else:
            exit(0)
    else:
        return True

# Some Useful Names
null = "null"
rock = "rock"
paper = "paper"
scissors = "scissors"

# A Thesaurus (implemented as a dictionary)
synonyms = {"rock": rock,
            "paper": paper,
            "scissors": scissors,
            "stone": rock,
            "vellum": paper,
            "shears": scissors}

# Final States
game_is_draw = "Game is a Draw"

playerA_wins = "Player A Wins"

playerB_wins = "Player B Wins"

# Initial State
both_players_must_choose = "Both Players Must Choose"

# Transition States
playerA_must_choose = "Player A Must Choose"

playerB_must_choose = "Player B Must Choose"

# Transition Table (implemented as a dictionary)
transitions = {(null,    null): both_players_must_choose,
               (null,    rock): playerA_must_choose,
               (null,    paper): playerA_must_choose,
               (null,    scissors): playerA_must_choose,
               (rock,    null): playerB_must_choose,
               (rock,    rock): game_is_draw,
               (rock,    paper): playerB_wins,
               (rock,    scissors): playerA_wins,
               (paper,   null): playerB_must_choose,
               (paper,   rock): playerA_wins,
               (paper,   paper): game_is_draw,
               (paper,   scissors): playerB_wins,
               (scissors, null): playerB_must_choose,
               (scissors, rock): playerB_wins,
               (scissors, paper): playerA_wins,
               (scissors, scissors): game_is_draw}


# Simulate Initialization

''' Interactive Looping between two players for Rock - Paper - Scissors Game ....'''
print "Interactive Looping between two players for Rock - Paper - Scissors Game ...."
# Simulate Initialization

playerA_choice = null
playerB_choice = null

Continue_game = True   # Check the status of continuation of Game ..
print"\n"
while Continue_game:

    Input_Player_A = raw_input("\n Player A Choice (Choose among rock, paper and scissors) :")
    playerA_choice = synonyms[Input_Player_A]  # Map option of PlayerA to A Thesaurus

    # State transition using Transition Table and message printing...
    state = (playerA_choice, playerB_choice)
    print("\n State:", state, "and Transition:", transitions[state])
    Continue_game = game_finish(transitions[state])

    Input_Player_B = raw_input("\n Player B Choice (Choose among stone, vellum and shears) :")
    playerB_choice = synonyms[Input_Player_B]  # Map option of PlayerA to A Thesaurus

    # State transition using Transition Table and message printing...
    state = (playerA_choice, playerB_choice)
    print("\n State:", state, "and Transition:", transitions[state])
    Continue_game = game_finish(transitions[state])





