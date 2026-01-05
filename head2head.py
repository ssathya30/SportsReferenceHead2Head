import json

def build_h2h_matrix(data):
    teams = sorted(data.keys())
    
    header = "Tm  " + " ".join(f"{team:>3}" for team in teams)
    separator = "-" * len(header)
    
    rows = [header, separator]
    for team in teams:
        row = f"{team:>3} "
        for opponent in teams:
            if team == opponent:
                cell = " -- "
            else:
                w = data[team][opponent]['W']
                cell = f"{w:>3} "
            row += cell
        rows.append(row)
    
    rows.append(separator)
    rows.append(header)
    
    return "\n".join(rows)


def display(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print(build_h2h_matrix(data))

if __name__ == "__main__":
    # Manually pass in json file here for demo
    display('./ex_sport.json')