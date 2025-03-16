from RequestsModule import *
import pandas as pd

sources_affiliations = pd.DataFrame({"Left": pd.Series(["AlterNet", "The Atlantic", "Democracy Now", "Daily Beast",
                                              "Huff Post", "The Intercept", "Jacobin", "Mother Jones", "MSNBC"
                                              "The New Yorker", "The New York Times", "The Nation", "Slate", "Vox"]),
                                     "Left Leaning": pd.Series(["ABC News", "AP", "AXIOS", "Bloomberg", "CBS News", "CNN",
                                     "The Guardian", "Insider", "NBC News", "NPR", "Politico",
                                     "Propublica", "Semafor", "Time", "The Washington Post",
                                                      "USA Today", "Yahoo! News"]),
                                     "Center": pd.Series(["BBC News", "The Christian Science Monitor", "CNBC", "Forbes",
                                                "MarketWatch", "Newsweek", "Reason", "Reuters", "RealClear Politics",
                                                "The Hill", "The Wall Street Journal"]),
                                    "Right Leaning": pd.Series(["The Dispatch", "The Epoch Times", "The Free Press",
                                                      "Fox Business", "Just The News", "National Review",
                                                      "New York Post", "Washington Examiner", "The Washington Times",
                                                      "Zero Hedge"]),
                                     "Right": pd.Series(["The American Conservative", "The American Spectator", "Breitbart",
                                               "Blaze Media", "CBN", "Daily Caller", "Daily Mail", "The Daily Wire",
                                               "The Post Millenial", "Fox News", "The Federalist",
                                               "Independent Journal Review", "National Review", "Newsmax",
                                               "The Washington Free Beacon"])})


def source_bias_comparator(dictionary):
    score_total = 0
    story_sources = list(dictionary.values())[-1][0].articles
    generic_df = {"Left": '', "Left Leaning": '', "Center": '', "Right Leaning": '', "Right": ''}
    for key in sources_affiliations:
        sources = []
        list(dictionary.values())[-1][0].sources_bias[key] = 0
        for element in list(story_sources.keys()):
            for name in list(sources_affiliations[key]):
                if element == name:
                    sources.append(element)
                    score_total += 1
                    list(dictionary.values())[-1][0].sources_bias[key] += 1
        generic_df[key] = sources
    for element in generic_df:
        generic_df[element] = pd.Series([generic_df[element]])
    generic_df = pd.DataFrame([generic_df])
    bias_scores = []
    for key in list(dictionary.values())[-1][0].sources_bias:
        if list(dictionary.values())[-1][0].sources_bias[key] != 0:
            list(dictionary.values())[-1][0].sources_bias[key] = 1 / (score_total / list(dictionary.values())[-1][0].
                                                                      sources_bias[key]) * 100
            bias_scores = [value for value in list(dictionary.values())[-1][0].sources_bias.values()]
    list(dictionary.values())[-1][1].source_bias = bias_scores
    print(bias_scores)



def uncategorized_source_parser(dictionary):
    uncategorized_sources = dictionary
    uncategorized_sources_list = list(dictionary.keys())
    for key in sources_affiliations:
        categorised_sources = list(sources_affiliations[key])
        for name in categorised_sources:
            for element in uncategorized_sources_list:
                if name == element:
                    uncategorized_sources.pop(name)
    return uncategorized_sources


def categorised_sources_df_struct(dictionary):
    categorised_sources = {}
    sources_dataframes = {}
    for value in list(dictionary.values())[-1].sources_bias:
        categorised_sources.__setitem__(value, list(dictionary.values())[-1].articles[value])
    for key in categorised_sources:
        index = categorised_sources[key].split()
        columns = [name for name in list(uncategorized_source_parser(list(dictionary.values())[-1].
                                                                     articles))]
        source_df = pd.DataFrame(index=index, columns=columns)
        sources_dataframes.__setitem__(key, source_df)


