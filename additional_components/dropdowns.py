from formatting.colors import (DROP_DOWN_PURPLE, DROPDOWN_BLUE, DROPDOWN_GREEN, DROPDOWN_GREY, 
                                                  DROPDOWN_GREY_BLUE, DROPDOWN_LIME, DROPDOWN_ORANGE, DROPDOWN_RED, 
                                                  DROPDOWN_SALMON, DROPDOWN_TEAL, DROPDOWN_YELLOW, DROPDOWN_LIGHT_PURPLE)
ENGINEER = {
    "values": ["---", "Casey", "Alec", "Jacob", "Kent", "Shannon", "Doug", "Stephen", "Alex", "Will", "Ryan"],
    "column_letter": "F",
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': 5,
        'startRowIndex': 6,
        'endColumnIndex': 6,
        'endRowIndex': 19
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': 5,
        'startRowIndex': 21,
        'endColumnIndex': 6,
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': 5,
        'startRowIndex': 40,
        'endColumnIndex': 6,
        'endRowIndex': 73
    },
    "colors":{
        "---": DROPDOWN_GREY, 
        "Casey": DROPDOWN_BLUE, 
        "Alec": DROPDOWN_GREEN, 
        "Jacob": DROPDOWN_ORANGE, 
        "Kent": DROP_DOWN_PURPLE, 
        "Shannon": DROPDOWN_YELLOW, 
        "Doug": DROPDOWN_GREY_BLUE, 
        "Stephen": DROPDOWN_TEAL, 
        "Alex": DROPDOWN_LIME, 
        "Will": DROPDOWN_RED,
        "Ryan": DROPDOWN_LIGHT_PURPLE,
    }
}

QE = {
    "values": ["---", "Will", "Alex"],
    "column_letter": "G",
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': 6,
        'startRowIndex': 6,
        'endColumnIndex': 7,
        'endRowIndex': 19
    },
    "phase_two": {
        'sheetId': 0,
        'startRowIndex': 21,
        'endRowIndex': 38,
        'startColumnIndex': 6,
        'endColumnIndex': 7
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': 6,
        'startRowIndex': 40,
        'endColumnIndex': 7,
        'endRowIndex': 73
    },
    "colors": {
        "---": DROPDOWN_GREY,
        "Will": DROPDOWN_RED,
        "Alex": DROPDOWN_LIME
    }
}

FORKED = {
    "values": ["Yes", "No"],
    "column_letter": "H",
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': 7,
        'startRowIndex': 6,
        'endColumnIndex': 8,
        'endRowIndex': 19,
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': 7,
        'startRowIndex': 21,
        'endColumnIndex': 8,
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': 7,
        'startRowIndex': 40,
        'endColumnIndex': 8,
        'endRowIndex': 73
    },
    "colors": {
        "yes": DROPDOWN_SALMON,
        "no": DROPDOWN_GREY
    }
}

SC_UPDATED = {
    "values": ["Yes", "No", "---"],
    "column_letter": "I",
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': 8,
        'startRowIndex': 6,
        'endColumnIndex': 9,
        'endRowIndex': 19,
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': 8,
        'startRowIndex': 21,
        'endColumnIndex': 9,
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': 8,
        'startRowIndex': 40,
        'endColumnIndex': 9,
        'endRowIndex': 73
    }, 
    "colors": {
        "Yes": DROPDOWN_GREEN,
        "No": DROPDOWN_YELLOW, 
        "---": DROPDOWN_GREY
    }
}

DEPLOYED = {
    "values": ["Not Started", "In Progress", "Troubleshooting", "Done", "---"],
    "column_letter": ["L", "M", "Q"],
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': [11,12, 16],
        'startRowIndex': 6,
        'endColumnIndex': [12, 13,17],
        'endRowIndex': 19
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': [11,12, 16],
        'startRowIndex': 21,
        'endColumnIndex': [12, 13,17],
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': [11,12, 16],
        'startRowIndex': 40,
        'endColumnIndex': [12, 13,17],
        'endRowIndex': 73
    },
    "colors": {
        "Not Started": DROPDOWN_SALMON, 
        "In Progress": DROPDOWN_BLUE, 
        "Troubleshooting": DROPDOWN_YELLOW, 
        "Done": DROPDOWN_GREEN, 
        "---": DROPDOWN_GREY
    }
}

IQETESTED = {
    "values": ["N/A", "Yes", "No", "---"],
    "column_letter": "N",
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': 13,
        'startRowIndex': 6,
        'endColumnIndex': 14,
        'endRowIndex': 19
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': 13,
        'startRowIndex': 21,
        'endColumnIndex': 14,
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': 13,
        'startRowIndex': 40,
        'endColumnIndex': 14,
        'endRowIndex': 73
    }, 
    "colors": {
        "N/A": DROPDOWN_GREY_BLUE, 
        "Yes": DROPDOWN_GREEN,
        "No": DROPDOWN_YELLOW, 
        "---": DROPDOWN_GREY
    }
}

UITESTED = {
    "values": ["N/A", "Not Started", "In Progress", "Troubleshooting", "Done", "---"],
    "column_letter": ["O", "R"],
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': [14, 17],
        'startRowIndex': 6,
        'endColumnIndex': [15, 18],
        'endRowIndex': 19
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': [14, 17],
        'startRowIndex': 21,
        'endColumnIndex': [15, 18],
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': [14, 17],
        'startRowIndex': 40,
        'endColumnIndex': [15, 18],
        'endRowIndex': 73
    },
    "colors": {
        "N/A": DROPDOWN_GREY_BLUE, 
        "Not Started": DROPDOWN_SALMON, 
        "In Progress": DROPDOWN_BLUE, 
        "Troubleshooting": DROPDOWN_YELLOW, 
        "Done": DROPDOWN_GREEN, 
        "---": DROPDOWN_GREY
    }
}

CCB = {
    "values": ["Awaiting CCB Approval", "Approved | SC Branch Needs Updating", "Done"],
    "column_letter": "P",
    "phase_one": {
        'sheetId': 0,
        'startColumnIndex': 15,
        'startRowIndex': 6,
        'endColumnIndex': 16,
        'endRowIndex': 19
    },
    "phase_two": {
        'sheetId': 0,
        'startColumnIndex': 15,
        'startRowIndex': 21,
        'endColumnIndex': 16,
        'endRowIndex': 38
    },
    "phase_three": {
        'sheetId': 0,
        'startColumnIndex': 15,
        'startRowIndex': 40,
        'endColumnIndex': 16,
        'endRowIndex': 73
    },
    "colors": {
        "Awaiting CCB Approval": DROPDOWN_YELLOW, 
        "Approved | SC Branch Needs Updating": DROPDOWN_BLUE, 
        "Done": DROPDOWN_GREEN
    }
}