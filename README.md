# veneer - Slightly More Privacy for GitHub

`veneer` obscures your commit history on GitHub by automatically logging 1-3 commits everyday.

You can alter the `sunday_write_frac = 0.75`  in `veneer.py` variable to choose how often to register activity on Sundays.

Currently in alpha (expect issues).

## Installation

1. Clone this repository:

`git clone https://github.com/cgnorthcutt/veneer.git`

2. Add a crontab job:

`crontab -e`

3. Add this line to the bottom:

`0 */6 * * * /path/to/veneer/crontab_script.bash # Runs every six hours` 

## FAQ

1. You can test to see if things are working by just running:

`/path/to/veneer/crontab_script.bash`

2. If you have issues because the file is not executable, run:

`chmod 776 /path/to/veneer/crontab_script.bash`
`chmod 776 veneer.py`

3. You can run a single job a day if you like:

`@daily /path/to/veneer/crontab_script.bash # Runs everday at midnight.`

Just be sure to set `prob_do_nothing = 0.`  in `veneer.py`.
