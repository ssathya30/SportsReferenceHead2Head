# SportsReference Head2Head Table

## Overview
The python script generates a formatted table displaying head-to-head win-loss records between teams, similar to sports standings matrices. 
You can pass in JSON input and it will render the team's win-loss record against other teams as matrix output.

## What It Does
The program reads team records from a JSON file and creates a matrix where:

Rows represent each team and Columns represent opponents.
Cells show the number of wins that row's (team) has against that column's (opponent).
Diagonal cells (team vs itself) display "--" because this cell represents a team playing itself.
Teams are sorted alphabetically for consistent ordering.

## Why This Approach
Data Structure: I used nested dictionaries from JSON because they provide O(1) lookup time for any team-opponent pair. This is more efficient than searching through lists.

Sorting: sorted(data.keys()) ensures consistent ordering regardless of how teams appear in the input file, making the output predictable and easy to read.

String Formatting: Python provides F-strings with right-alignment through:(f"{value:>3}") which create uniform column widths, allowing for proper alignment regardless of whether the numbers are single or double digit.

## Data Processing Steps

1. Load Data: Read JSON file containing team records
2. Sort Teams: Get alphabetically sorted list of all teams
3. Build Header: Create column headers with team codes
4. Iterate Rows: For each team, iterate through all opponents
5. Format Cells: Right-align wins in 3-character cells.
6. Add Footer: Repeat header at bottom for readability

## Testing
Tested with the provided sample data containing 8 teams (BRO, BSN, CHC, CIN, NYG, PHI, PIT, STL). 

Verified the correct alignment of single and double-digit numbers and win totals display correctly.

## Usage
$ python head2head.py

Make sure the json file is in the same directory as the script.

## Example Output
```
Tm  BRO BSN CHC CIN NYG PHI PIT STL
-----------------------------------
BRO  --  10  15  15  14  14  15  11 
BSN  12  --  13  13  13  14  12   9 
CHC   7   9  --  12   7  16   8  10 
CIN   7   9  10  --  13  13  13   8 
NYG   8   9  15   9  --  12  15  13 
PHI   8   8   6   9  10  --  13   8 
PIT   7  10  14   9   7   9  --   6 
STL  11  13  12  14   9  14  16  -- 
-----------------------------------
Tm  BRO BSN CHC CIN NYG PHI PIT STL
```
