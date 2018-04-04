import Parameters as P
import GamblingClasses as Cls
import SupportTransient as Support

# create multiple games for when the use fair coin
# create multiple games for when the use fair coin
multiGamefair = Cls.MultipleGameSets(
    ids= range(P.NUM_SIM_GAMES),
    n_games_in_a_set=P.REAL_GAME_SIZE,
    prob_head=P.FAIR_HEAD)

# simulate all cohorts
multiGamefair.simulation()

# create multiple cohorts for when the drug is available
multiGameunfair = Cls.MultipleGameSets(
    ids = range(P.NUM_SIM_GAMES, 2*P.NUM_SIM_GAMES),
    n_games_in_a_set=P.REAL_GAME_SIZE,
    prob_head=P.UNFAIR_HEAD)

# simulate all cohorts
multiGameunfair.simulation()

# print outcomes of each game
Support.print_outcomes(multiGamefair, 'When use fair coin:')
Support.print_outcomes(multiGameunfair, 'When use unfair coin')

# draw histograms of average game rewards
Support.draw_histograms(multiGamefair, multiGameunfair)

# print comparative outcomes
Support.print_comparative_outcomes(multiGamefair, multiGameunfair)
