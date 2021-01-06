# Reddit Analysis on Epidemics

Below can be found a list of data retrieval scripts that help make this work possible.

# Prerequisites

All scripts have been tested on Python 3.8.6.
The external modules that were used can be found in the `requirements.txt` file along with their versions.
**Note**: not all modules are required for all scripts.
If any of the modules are not already installed, the normal `pip install -r requirements.txt` from an _ADMIN_ shell process should be followed.
_After_ installing the `requirements.txt`, please follow the below steps:

1. Download NLTK package extensions.
   ```{ps1}
   python -c "import nltk;nltk.download('punkt')"
   ```
2. Log into Reddit and create a personal use script [app](https://www.reddit.com/prefs/apps/).
   Collect the `client_id` (in the upper left in bold under the heading _personal use script_) and the `client_secret` (left hand side beside the heading _secret_)
3. Make a blank file called `~/code/praw.ini` and copy the following code snipet, replacing your values.
   ```{txt}
   [DEFAULT]
   username={{my_user_name}}
   client_id={{my_client_id}}
   client_secret={{my_client_secret}}
   user_agent=script:RedditAnalysis:v1.0.0 (by u/%(username)s)
   ratelimit_seconds=5
   ```

## Scripts

Below is a brief summary of each of the scripts.
In order to fully regenerate the results, delete the cached folder and run the scripts in the order listed.
The pathing can be changed to any desired location.

1. Open a PowerShell window and change to the `~/code` folder.
   ```{ps1}
   cd "D:\repos\RedditEpidemicAnalysis\data\code"
   ```
2. [get_posts](./code/get_posts.py).
   ```{ps1}
   python get_posts.py -subreddit COVID19positive -out d:/datasets/reddit/posts.jsonl
   ```
