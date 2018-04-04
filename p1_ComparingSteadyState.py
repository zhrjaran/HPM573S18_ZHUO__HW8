import Parameters as P
import GamblingClasses as Cls
import SupportSteadyState as Support

# create a set of game when using fair coin
fairgame = Cls.SetOfGames (
    id=1,
    prob_head=P.FAIR_HEAD,
    n_games=P.SIM_GAME_SIZE)
# simulate the game
fairgameOutcome = fairgame.simulation()

# create a set of game when using unfair coin
unfairgame = Cls.SetOfGames(
    id=2,
    # the seed of generating cohorts, here is we don't have mechanism of paired X,Y; thus we can't use the same seed
    # we here need different seed to treat them as independent cohort(variable)
    prob_head=P.UNFAIR_HEAD,
    n_games=P.SIM_GAME_SIZE)
# simulate the game
unfairgameOutcome = unfairgame.simulation()

# print outcomes of each game
Support.print_outcomes(fairgameOutcome, 'When the coin is fair:')
Support.print_outcomes(unfairgameOutcome, 'When the coin is unfair:')

# draw histograms
Support.draw_histograms(fairgameOutcome, unfairgameOutcome)

# print comparative outcomes
Support.print_comparative_outcomes(fairgameOutcome, unfairgameOutcome)
