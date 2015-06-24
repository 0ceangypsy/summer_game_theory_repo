import numpy as np

from turn_class import TrustGameTurn
from game_class import TrustGame
from agent_class import Agent


def game_test(test_agent_1, test_agent_2, test_game, turns, expected_result,
              **params):

    result = test_game.play(test_agent_1, test_agent_2, turns, **params)
    assert isinstance(result, tuple)
    assert result == expected_result


def turn_test(test_agent_1, test_agent_2, test_turn, test_agent_1_history, 
              test_agent_2_history, expected_result, **params):

    result = test_turn.play(test_agent_1, test_agent_2, test_agent_1_history, 
                            test_agent_2_history, **params)

    assert isinstance(result, tuple)
    assert result == expected_result


def play_game_test():
    # Initialize test parameters
    params = {"A":1,
              "B":3,
              "C":1,
              "SWAP" : False, 
              "RESET" : False, 
              "MEMORY" : 2,
              "LOG" : False,
              "ENDOWMENT" : (2,0)}

    a = params["A"]
    b = params["B"]
    c = params["C"]
    memory = params["MEMORY"]
    LOG = params["LOG"]
    endowment = params["ENDOWMENT"]

    # Initialize test agents

    intial_genome_a_1 = np.array([[0,5,4,4,4,5,6,4,8,9,10,11,12,13,],
                                  [1,4,3,3,4,5,6,8,8,9,10,11,12,13,],
                                  [2,2,2,3,4,5,6,7,8,9,10,11,12,13,],
                                 ])

    intial_genome_b_1 = np.array([[0,1,2,3,4,5],
                                  [2,1,2,3,4,5],
                                  [0,4,2,0,4,5],
                                  [0,3,4,5,4,5],
                                  [0,0,2,6,4,5],
                                  [0,1,2,3,5,5],
                                  [0,1,2,3,4,6],                              
                                 ])

    test_agent_1 = Agent(intial_genome_a_1, intial_genome_b_1, ID = (0, 1), 
                         initial_gift = 1, **params)

    test_agent_2 = Agent(intial_genome_a_1, intial_genome_b_1, ID = (0, 2), 
                         initial_gift = 2, **params)

    # Initialize test turn
    test_turn = TrustGameTurn(a, b, c)

    # Initialize test game
    test_game = TrustGame(**params)

    # Test 1:
    test_agent_1.cash, test_agent_2.cash = endowment

    # Run turn tests
    turn_test(test_agent_1, test_agent_2, test_turn, [], [], (3, 1, 1, 2), 
              **params)
    turn_test(test_agent_1, test_agent_2, test_turn, [1], [2], (2, 0, 0, 0),
              **params)
    turn_test(test_agent_1, test_agent_2, test_turn, [1, 0], [2, 0], 
              (3, 3, 2, 3), **params)

    # Run game test
    game_test(test_agent_1, test_agent_2, test_game, 3, 
              (8.0/3,4.0/3,3.0/3,5.0/3), **params)

    # Test 2:
    test_agent_2.cash, test_agent_1.cash = endowment

    # Run turn tests
    turn_test(test_agent_2, test_agent_1, test_turn, [], [], (3, 3, 2, 3), 
              **params)
    turn_test(test_agent_2, test_agent_1, test_turn, [2], [3], (2, 0, 0, 0), 
              **params)
    turn_test(test_agent_2, test_agent_1, test_turn, [2, 0], [3, 0], (3,3,2,3), 
              **params)

    # Run game test
    game_test(test_agent_2, test_agent_1, test_game, 3, 
              (8.0/3,6.0/3,4.0/3,6.0/3), **params)


def main():
    play_game_test()
    print "Passed game tests."


if __name__ == "__main__":
    main()