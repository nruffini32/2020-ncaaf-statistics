import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np

"""This file will colect data from database and 
create scatter plots to compare the statistics to win/loss ratios"""

# Creates database
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Return list of win loss ratios
def get_wl_data(cur):
    cur.execute('SELECT wl_ratio FROM ncaaf_2020')
    data = cur.fetchall()
    wl = [d[0] for d in data]
    return wl

# Return list of turnover margins
def get_turnover_data(cur):
    cur.execute('SELECT turnover_margin FROM ncaaf_2020')
    data = cur.fetchall()
    t = [d[0] for d in data]
    return t

# Returns list of redzone touchdown percentages
def get_rz_td_data(cur):
    cur.execute('SELECT redzone_td_percentage FROM ncaaf_2020')
    data = cur.fetchall()
    rz = [d[0] for d in data]
    return rz

# Return list of penalty yards
def get_penalty_yards_data(cur):
    cur.execute('SELECT penalty_yards FROM ncaaf_2020')
    data = cur.fetchall()
    yards = [d[0] for d in data]
    return yards

# Returns list punting yards
def get_punting_yards_data(cur):
    cur.execute('SELECT net_punting_yards FROM ncaaf_2020')
    data = cur.fetchall()
    yards = [d[0] for d in data]
    return yards

# Creates scatterplots
def create_visuals(wl, t, rz, pen, pun):
    fig = plt.figure(1, figsize = (10, 7 ))

    fig.suptitle('Team Statistics Compared to Win/Loss Ratios for 2020 NCAA Football Season').set_weight('bold')
    turnover = fig.add_subplot(221)
    redzone = fig.add_subplot(222)
    penalty = fig.add_subplot(223)
    punting = fig.add_subplot(224)

    turnover.scatter(t, wl, color = 'blue')
    turnover.set_xlabel('Tunover Margin').set_weight('bold')
    turnover.set_ylabel('Win Ratio').set_weight('bold')

    redzone.scatter(rz, wl, color = 'blue')
    redzone.set_xlabel('Red Zone Touchdown Ratio').set_weight('bold')
    redzone.set_ylabel('Win Ratio').set_weight('bold')

    penalty.scatter(pen, wl, color = 'blue')
    penalty.set_xlabel('Total Penalty Yards').set_weight('bold')
    penalty.set_ylabel('Win Ratio').set_weight('bold')

    punting.scatter(pun, wl, color = 'blue')
    punting.set_xlabel('NET Punting Yards').set_weight('bold')
    punting.set_ylabel('Win Ratio').set_weight('bold')
    
    plt.show()

# Gets correlation from two sets of data
def get_correlation(x_lst, y_lst):
    table = np.corrcoef(x_lst, y_lst)
    return round(table[0][1], 4)

def get_t_correlation(x, y):
    corr = get_correlation(x, y)
    print(f'The correlation between turnover margins and win/loss ratios is {corr}.')

def get_rz_correlation(x, y):
    corr = get_correlation(x, y)
    print(f'The correlation between redzone toucdown percentages and win/loss ratios is {corr}.')

def get_penalty_corr(x, y):
    corr = get_correlation(x, y)
    print(f'The correlation between total penalty yards and win/loss ratios is {corr}.')

def get_punting_corr(x, y):
    corr = get_correlation(x, y)
    print(f'The correlation between NET punting yards and win/loss ratios is {corr}.')


if __name__ == '__main__':
    cur, conn = set_up_database('ncaaf2020stats.db')
    wl_data = get_wl_data(cur)
    turnover_data = get_turnover_data(cur)
    rz_td_data = get_rz_td_data(cur)
    penalty_data = get_penalty_yards_data(cur)
    punting_data = get_punting_yards_data(cur)

    create_visuals(wl_data, turnover_data, rz_td_data, penalty_data, punting_data)

    get_t_correlation(turnover_data, wl_data)
    get_rz_correlation(rz_td_data, wl_data)
    get_penalty_corr(penalty_data, wl_data)
    get_punting_corr(punting_data, wl_data)
    
