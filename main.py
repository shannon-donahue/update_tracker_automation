import yaml
import argparse
import os

from datetime import date

import gsheet

settings = yaml.safe_load(open('settings.yml', 'r'))


if __name__ == '__main__':
    today = date.today()
    update_tracker_title = f"ConsoleDot Update Tracker ({today.strftime('%m/%d/%Y')})"

    parser = argparse.ArgumentParser()
    parser.add_argument("--gsheet", 
                        type=bool,
                        const=True, 
                        nargs='?', 
                        help="Build update tracker google sheet")
    args = parser.parse_args()


    # Build google sheet
    if args.gsheet:
        google_sheet = gsheet.GoogleSheet(settings)
        google_sheet.generate(update_tracker_title)