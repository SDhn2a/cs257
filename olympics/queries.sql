SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'table_name';

SELECT DISTINCT teams.NOC
FROM teams
ORDER BY teams.NOC;

SELECT DISTINCT athletes.name
FROM athletes, athletes_teams, teams
WHERE athletes.athlete_id = athletes_teams.athlete_id
AND athletes_teams.NOC = teams.NOC
AND teams.team LIKE 'Kenya';

SELECT medals.year, athletes.name, medals.event, medals.medal
FROM medals, athletes
WHERE medals.athlete_id = athletes.athlete_id
AND athletes.name LIKE '%Louganis'
AND medals.medal NOT LIKE 'NA'
ORDER BY medals.year;

SELECT DISTINCT athletes_teams.NOC, COUNT(DISTINCT(medals.year, medals.event))
FROM medals, athletes_teams
WHERE medals.year = athletes_teams.year
AND medals.season = athletes_teams.season
AND medals.athlete_id = athletes_teams.athlete_id
AND medals.medal LIKE 'Gold'
GROUP BY athletes_teams.NOC
ORDER BY COUNT(DISTINCT(medals.year, medals.event)) desc;
