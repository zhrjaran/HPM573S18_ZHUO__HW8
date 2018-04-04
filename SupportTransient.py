import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    rewards_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean game rewards and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          rewards_mean_PI_text)


def draw_histograms(multi_cohort_fair, multi_cohort_unfair):
    """ draws the histograms of average survival time
    :param multi_cohort_fair: multiple cohorts simulated when using fair coins
    :param multi_cohort_unfair: multiple cohorts simulated when using unfair coins
    """

    # histograms of average survival times
    set_of_game_rewards = [
        multi_cohort_fair.get_all_total_rewards(),
        multi_cohort_unfair.get_all_total_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of average game rewards',
        x_label='Game rewards',
        y_label='Counts',
        legend=['Fair coin', 'Unfair coin'],
        transparency=0.5,
        x_range=[0, 20]
    )


def print_comparative_outcomes(multi_cohort_fair, multi_cohort_unfair):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_fair: multiple cohorts simulated when using fair coins
    :param multi_cohort_unfair: multiple cohorts simulated when using unfair coins
    """

    # change in game rewards
    change = Stat.DifferenceStatIndp(   #HR: here we assume X and Y are independent
        name='Change in mean game rewards',
        x=multi_cohort_unfair.get_all_total_rewards(),
        y_ref=multi_cohort_fair.get_all_total_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=change.get_mean(),
        interval=change.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean game rewards and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

