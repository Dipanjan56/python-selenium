""""""

"""How to retry failed scenario in Behave using python"""

"""
Approach 1:

The behave library actually has a RerunFormatter which can help you rerun the failing scenarios of your previous test-run. It creates a text file of all your failing scenarios like:

# -- file:rerun.features
# RERUN: Failing scenarios during last test run.
features/auth.feature:10
features/auth.feature:42
features/notifications.feature:67
To use the RerunFormatter all you need to do is put it in your behave configuration file (behave.ini):

# -- file:behave.ini
[behave]
format   = rerun
outfiles = rerun_failing.features
To rerun the failing scenarios, use this command:

behave @rerun_failing.features
"""

"""
Approach 2:

I know that's a later answer but it could help others.

There is another approach that also could help, it's implementing it under the environment.py file, you could do the retry by a specific tag.

Provides support functionality to retry scenarios a number of times before their failure is accepted. This functionality can be helpful when you use behave tests in an unreliable server/network infrastructure.

For example, I am running tag "@smoke_test" on CI, so I choose this tag to patch with retry condition.

First, on your environment.py import the following:

# -- file: environment.py
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
Then add the method:

# -- file:environment.py
#
def before_feature(context, feature):
    for scenario in feature.scenarios:
        if "smoke_test" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=3)
*max_attempts are by default set as 3. I just described there to make it explicit that you can actually set how many retries you want.
"""