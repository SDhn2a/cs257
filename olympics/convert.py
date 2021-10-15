import csv

count = 0
medal_table = {''} # contains athlete ID, year + season, event, medal (at olympics X, athlete Y won medal Z)
athlete_team_links = {''} # contains athlete ID, NOC, year + season (at olympics X, athlete Y was associated with NOC Z)
location_table = {''} # contains year + season, city (olympics X was held at location Y)
event_table = {''} # contains event, sport (event X is a subcategory of sport Y)
athlete_table = {''} # contains ID, name, sex, height, weight, birth year (athlete X has these characteristics)
team_table = {''} # contains NOC, year + season, name (at olympics X, NOC Y went by name Z)

with open('archive/athlete_events.csv') as olympics_csv:
    reader = csv.DictReader(olympics_csv)
    for row in reader:
        count += 1
        medal_table.add((row['ID'],row['Year'],row['Season'],row['Event'],row['Medal']))
        athlete_team_links.add((row['ID'],row['Year'],row['Season'],row['NOC']))
        location_table.add((row['Year'],row['Season'],row['City']))
        event_table.add((row['Event'],row['Sport']))
        athlete_table.add((row['ID'],row['Name'],row['Sex'],row['Height'],row['Weight']))
        team_table.add((row['NOC'],row['Year'],row['Season'],row['Team']))



with open('output/medal_table.csv', 'w') as output_file:
    mlinks = csv.writer(output_file)
    for link in medal_table:
        mlinks.writerow(link)
with open('output/athlete_team_links.csv', 'w') as output_file:
    atlinks = csv.writer(output_file)
    for link in athlete_team_links:
        atlinks.writerow(link)
with open('output/location_table.csv', 'w') as output_file:
    ltable = csv.writer(output_file)
    for entry in location_table:
        ltable.writerow(entry)
with open('output/event_table.csv', 'w') as output_file:
    etable = csv.writer(output_file)
    for entry in event_table:
        etable.writerow(entry)
with open('output/athlete_table.csv', 'w') as output_file:
    atable = csv.writer(output_file)
    for entry in athlete_table:
        atable.writerow(entry)
with open('output/team_table.csv', 'w') as output_file:
    ttable = csv.writer(output_file)
    for entry in team_table:
        ttable.writerow(entry)