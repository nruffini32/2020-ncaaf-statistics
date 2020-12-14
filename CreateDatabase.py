import sqlite3
import os
import requests
from bs4 import BeautifulSoup

"""This file will create database 'ncaaf2020stats.db' with all 2020 ncaaf team and statistics """

# Returns list of teams 
def get_teams():
    urls = ['https://www.ncaa.com/stats/football/fbs/current/team/29', 'https://www.ncaa.com/stats/football/fbs/current/team/29/p2', 'https://www.ncaa.com/stats/football/fbs/current/team/29/p3']

    teams = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        tags = soup.find_all('a', class_ = 'school')
        for tag in tags:
            school = tag.text
            teams.append(school)

    return teams

# Return dictionary with teams as keys and win-loss ratios as values
def get_wl_ratios():
    urls = ['https://www.ncaa.com/stats/football/fbs/current/team/742', 'https://www.ncaa.com/stats/football/fbs/current/team/742/p2', 'https://www.ncaa.com/stats/football/fbs/current/team/742/p3']
    
    teams = []
    wl_ratios = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        # Creating list of schools as teams
        schools = soup.find_all('a', class_ = 'school')
        for tag in schools:
            teams.append(tag.text)

        # Creating list of win-loss ratios as wl_ratios
        body = soup.find('tbody')
        tags = body.find_all('tr')
        for tag in tags:
            stats = tag.find_all('td')
            lst = [stat.text for stat in stats]
            wl_ratios.append(lst[5])

    # Creating dictionary
    wl_dic = {}
    for i in range(len(teams)):
        team = teams[i]
        wl = wl_ratios[i]
        wl_dic[team] = wl

    return wl_dic

# Returns dictionary with teams as keys and turnover margins as values
def get_turnover_margins():
    urls = ['https://www.ncaa.com/stats/football/fbs/current/team/29', 'https://www.ncaa.com/stats/football/fbs/current/team/29/p2', 'https://www.ncaa.com/stats/football/fbs/current/team/29/p3']
    
    teams = []
    turnover_margins = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        # Creating list of schools as teams
        schools = soup.find_all('a', class_ = 'school')
        for tag in schools:
            teams.append(tag.text)

        # Creating list of turnover margins as turnover_margins
        body = soup.find('tbody')
        tags = body.find_all('tr')
        for tag in tags:
            stats = tag.find_all('td')
            lst = [stat.text for stat in stats]
            turnover_margins.append(lst[9])

    # Creating dictonary
    t_dic = {}
    for i in range(len(teams)):
        team = teams[i]
        margin = turnover_margins[i]
        t_dic[team] = margin

    return t_dic

# Returns dictionary with teams as keys and redzone touchdown percentages as values
def get_redzonetd_percent():
    urls = ['https://www.ncaa.com/stats/football/fbs/current/team/703', 'https://www.ncaa.com/stats/football/fbs/current/team/703/p2', 'https://www.ncaa.com/stats/football/fbs/current/team/703/p3']

    teams = []
    rz_td_percents = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        # Creating list of schools as teams
        schools = soup.find_all('a', class_ = 'school')
        for tag in schools:
            teams.append(tag.text)

        # Creating list of red zone touchdown percentages as rz_td_percents
        body = soup.find('tbody')
        tags = body.find_all('tr')
        for tag in tags:
            stats = tag.find_all('td')
            lst = [stat.text for stat in stats]
            rz_td_percents.append(lst[8])

    # Creating dictionary
    td_dic = {}
    for i in range(len(teams)):
        team = teams[i]
        tdp = rz_td_percents[i]
        td_dic[team] = tdp

    return td_dic

# Returns dictionary with teams as keys and penalty yards as values
def get_penalty_yards():
    urls = ['https://www.ncaa.com/stats/football/fbs/current/team/877', 'https://www.ncaa.com/stats/football/fbs/current/team/877/p2', 'https://www.ncaa.com/stats/football/fbs/current/team/877/p3']

    teams = []
    penalty_yards = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        # Creating list of schools as teams
        schools = soup.find_all('a', class_ = 'school')
        for tag in schools:
            teams.append(tag.text)

        # Creating list of penalty yards as penalty_yards
        body = soup.find('tbody')
        tags = body.find_all('tr')
        for tag in tags:
            stats = tag.find_all('td')
            lst = [stat.text for stat in stats]
            penalty_yards.append(lst[4])

    # Creating dictionary
    penalty_dic = {}
    for i in range(len(teams)):
        team = teams[i]
        penalty_yard = penalty_yards[i]
        penalty_dic[team] = penalty_yard

    return penalty_dic

# Creates dictionary with teams as keys and NET punting yards as values
def get_net_punting():
    urls = ['https://www.ncaa.com/stats/football/fbs/current/team/98', 'https://www.ncaa.com/stats/football/fbs/current/team/98/p2', 'https://www.ncaa.com/stats/football/fbs/current/team/98/p3']

    teams = []
    punting = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        # Creating list of schools as teams
        schools = soup.find_all('a', class_ = 'school')
        for tag in schools:
            teams.append(tag.text)

        # Creating list of NET punting yards as punting
        body = soup.find('tbody')
        tags = body.find_all('tr')
        for tag in tags:
            stats = tag.find_all('td')
            lst = [stat.text for stat in stats]
            punting.append(lst[7])

    # Creating dictionary
    punting_dic= {}
    for i in range(len(teams)):
        team = teams[i]
        yards = punting[i]
        punting_dic[team] = yards

    return punting_dic

# Creates database
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Creating 'ncaaf' table in database and adds schools
def create_schools_table(cur, conn, teams):
    cur.execute('CREATE TABLE IF NOT EXISTS ncaaf_2020 (school TEXT PRIMARY KEY, wl_ratio REAL, turnover_margin INTEGER, redzone_td_percentage REAL, penalty_yards INTEGER, net_punting_yards REAL)')

    for team in teams:
        try:
            cur.execute('INSERT INTO ncaaf_2020 (school) VALUES (?)', (team, ))
        except:
            None
    conn.commit()

# Adding win loss ratios to database
def add_wl_ratios(cur, conn, dic):
    for school in dic:
        cur.execute('UPDATE ncaaf_2020 SET wl_ratio = ? WHERE school = ?', (dic[school], school))
    conn.commit()

# Adding turnover margins to database
def add_turnovers(cur, conn, dic):
    for school in dic:
        cur.execute('UPDATE ncaaf_2020 SET turnover_margin = ? WHERE school = ?',  (dic[school], school))
    conn.commit()

# Adding redzone touchdown percentages to database
def add_td(cur, conn, dic):
    for school in dic:
        cur.execute('UPDATE ncaaf_2020 SET redzone_td_percentage = ? WHERE school = ?', (dic[school], school))
    conn.commit()

# Adding penalty yards to database
def add_penaltyards(cur, conn, dic):
    for school in dic:
        cur.execute('UPDATE ncaaf_2020 SET penalty_yards = ? WHERE school = ?', (dic[school], school))
    conn.commit()

# Adding net punting yards to database
def add_punting(cur, conn, dic):
    for school in dic:
        cur.execute('UPDATE ncaaf_2020 SET net_punting_yards = ? WHERE school = ?', (dic[school], school))
    conn.commit()

if __name__ == '__main__':
    team_lst = get_teams()
    wl_dic = get_wl_ratios()
    turnover_dic = get_turnover_margins()
    rz_td_dic = get_redzonetd_percent()
    py_dic = get_penalty_yards()
    net_punting_dic = get_net_punting()

    cur, conn = set_up_database('ncaaf2020stats.db')    
    create_schools_table(cur, conn, team_lst)
    add_wl_ratios(cur, conn, wl_dic)
    add_turnovers(cur, conn, turnover_dic)
    add_td(cur, conn, rz_td_dic)
    add_penaltyards(cur, conn, py_dic)
    add_punting(cur, conn, net_punting_dic)