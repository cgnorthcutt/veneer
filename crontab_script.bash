SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd "$SCRIPTPATH"
python veneer.py
git pull
git commit veneer.txt -m "Auto daily commit."
git push
