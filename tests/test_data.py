import git
import pytest
import forecastcards


def gitDiff(branch1, branch2):
    format = '--name-only'
    commits = []
    g = git.Git('/path/to/git/repo')
    differ = g.diff('%s..%s' % (branch1, branch2), format).split("\n")
    for line in differ:
        if len(line):
            commits.append(line)

    #for commit in commits:
    #    print '*%s' % (commit)
    return commits



testdata_card_locs = {
       "poi": ['https://raw.github.com/e-lo/forecast-cards/master/forecastcards/examples/emeraldcitydot-rx123-yellowbrickroadhov/poi-rx123.csv'],
       "scenario": ['https://raw.github.com/e-lo/forecast-cards/master/forecastcards/examples/emeraldcitydot-rx123-yellowbrickroadhov/scenarios-rx123.csv'],
       "project": ['https://raw.github.com/e-lo/forecast-cards/master/forecastcards/examples/emeraldcitydot-rx123-yellowbrickroadhov/project-rx123.csv'],
       "observations": ['https://raw.github.com/e-lo/forecast-cards/master/forecastcards/examples/emeraldcitydot-rx123-yellowbrickroadhov/observations/observations-1935.csv',
                        'https://raw.github.com/e-lo/forecast-cards/master/forecastcards/examples/emeraldcitydot-rx123-yellowbrickroadhov/observations/observations-1960.csv',
       ],
       "forecast": ['https://raw.github.com/e-lo/forecast-cards/master/forecastcards/examples/emeraldcitydot-rx123-yellowbrickroadhov/forecasts/forecast-A1-1960-1940-F1.csv'],
}

schema_locs = { 'poi':'https://raw.github.com/e-lo/forecast-cards/master/spec/en/poi-schema.json',
                "scenario": "https://raw.github.com/e-lo/forecast-cards/master/spec/en/scenario-schema.json",
                "project": "https://raw.github.com/e-lo/forecast-cards/master/spec/en/project-schema.json",
                "observations": "https://raw.github.com/e-lo/forecast-cards/master/spec/en/observations-schema.json",
                "forecast": "https://raw.github.com/e-lo/forecast-cards/master/spec/en/forecast-schema.json",
}
@pytest.mark.master
@pytest.mark.basic
def test_tests():
    forecastcards.validate_cards(testdata_card_locs,schema_locs)

@pytest.mark.skip(reason="forecastcards needs functionality to read local files")
@pytest.mark.master
def test_all_cards():
    repo_card_locs = map_cards(repo_loc=default_repo_api,subdirs=['data'],repo_raw=default_raw_url)
    forecastcards.validate_cards(repo_card_locs,schema_locs)

@pytest.mark.skip(reason="need to figure out how to get list of new projects")
@pytest.mark.basic
def test_new_projs():

    new_proj_card_locs = {}
    forecastcards.validate_cards(new_proj_card_locs,schema_locs)

@pytest.mark.skip(reason="need to figure out how to get list of projects that were touched")
@pytest.mark.basic
def test_altered_projs():

    alt_proj_card_locs = {}

    forecastcards.validate_cards(alt_proj_card_locs,schema_locs)
