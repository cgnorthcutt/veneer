# veneer - Privacy for GitHub

`veneer` obscures your commit history on GitHub by automatically logging a commit everyday.

You can alter the `sunday_write_frac = 0.75` variable to choose how often to register activity on Sundays.

## Installation

1. Clone this repository:
`git clone https://github.com/cgnorthcutt/veneer.git`
2. Add a crontab job:
`crontab -e`
3. Add this line to the bottom:
`@daily /path/to/veneer/crontab_script.bash`
