import scr.FormatFunctions as Format
import numpy as np
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated game
    :param strategy_name: the name of the selected coin
    """

    # mean and confidence interval text of patient survival time
    rewards_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          rewards_mean_CI_text)


def draw_histograms(sim_output_fair, sim_output_unfair):
    """ draws the histograms of game rewards
    :param sim_output_fair: output of a game simulated when coin is fair
    :param sim_output_unfair: output of a game simulated when coin is unfair
    """

    # histograms of game rewards
    set_of_game_rewards = [
        sim_output_fair.get_rewards(),
        sim_output_unfair.get_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of game rewards',
        x_label='Game rewards',
        y_label='Counts',
        #bin_width=1,
        legend=['Fair Coin', 'Unfair Coin'],
        transparency=0.6
    )


def print_comparative_outcomes(sim_output_fair, sim_output_unfair):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_fair: output of a game simulated when coin is fair
    :param sim_output_unfair: output of a game simulated when coin is unfair
    """

    # Change in rewards
    change = Stat.DifferenceStatIndp(
        name='Change in Game Rewards when use unfair coin',
        x=sim_output_unfair.get_rewards(),
        y_ref=sim_output_fair.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=change.get_mean(),
        interval=change.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average change in game rewards when use unfair coin and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % change in game rewards
    relativeDeff = Stat.RelativeDifferenceIndp(
        name='Average % change in game rewards when use unfair coin',
        x=np.absolute(sim_output_unfair.get_rewards()),
        y_ref=np.absolute(sim_output_fair.get_rewards())
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relativeDeff.get_mean(),
        interval=relativeDeff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage change in game rewards when use unfair coin and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
