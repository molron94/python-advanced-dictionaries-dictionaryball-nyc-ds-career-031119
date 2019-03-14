home_player1={'number':0 ,'shoe':16 , 'points':22 ,'rebounds':12 , 'assists':12 , 'steals':3 ,'blocks': 1, 'slam_dunks': 1}
home_player2={'number':30 ,'shoe':14 , 'points':12 ,'rebounds':12 , 'assists':12 , 'steals':12 ,'blocks':12 , 'slam_dunks': 7}
home_player3={'number':11 ,'shoe':17 , 'points':17 ,'rebounds':19 , 'assists':10 , 'steals':3 ,'blocks':1 , 'slam_dunks': 15}
home_player4={'number':1 ,'shoe':19 , 'points':26 ,'rebounds':12 , 'assists':6 , 'steals':3 ,'blocks':8 , 'slam_dunks': 5}
home_player5={'number':31 ,'shoe':15 , 'points':19 ,'rebounds':2 , 'assists':2 , 'steals':4 ,'blocks':11 , 'slam_dunks': 1}

away_player1= {'number': 4,'shoe': 18, 'points': 10,'rebounds': 1, 'assists': 1, 'steals': 2,'blocks': 7, 'slam_dunks': 2}
away_player2= {'number': 0,'shoe': 16, 'points': 12,'rebounds': 4, 'assists': 7, 'steals': 7,'blocks': 15, 'slam_dunks': 10}
away_player3= {'number': 2,'shoe': 14, 'points': 24,'rebounds': 12, 'assists': 12, 'steals': 4,'blocks': 5, 'slam_dunks': 5}
away_player4= {'number': 8,'shoe': 15, 'points': 33,'rebounds': 3, 'assists': 2, 'steals': 1,'blocks': 1, 'slam_dunks': 0}
away_player5= {'number': 33,'shoe': 15, 'points': 6,'rebounds': 12, 'assists': 12, 'steals': 22,'blocks': 5, 'slam_dunks': 12}

def game_dict():
    game_dictionary = {
                      'home': {'team_name':'Brooklyn Nets','colors':['Black', 'White'],'players':{'Alan Anderson' : home_player1, 'Reggie Evans' : home_player2, 'Brook Lopez' : home_player3, 'Mason Plumlee' : home_player4, 'Jason Terry' : home_player5}},
                      'away': {'team_name':'Charlotte Hornets','colors':['Purple'],'players':{'Jeff Adrien' : away_player1, 'Bismak Biyombo' : away_player2, 'DeSagna Diop' : away_player3, 'Ben Gordon' : away_player4, 'Brendan Haywood' : away_player5}}
                     }
    return game_dictionary













def home_players():
    return list(game_dict()['home']['players'].keys())

def away_players():
    return list(game_dict()['away']['players'].keys())

def list_of_players():
    return home_players()+ away_players()

def find_player_dict(name):
    if name in home_players():
        return game_dict()['home']['players'][name]
    
    elif name in away_players():
        return game_dict()['away']['players'][name]   
    else: 
        return None
    
def is_home_away(team_name):
    if game_dict()['home']['team_name']==team_name:
        return 'home'
    elif game_dict()['away']['team_name']==team_name:
        return 'away'
    else: 
        return None
    
def team_stats(team_name, stat):
    r=[]
    if game_dict()['home']['team_name']==team_name:
        r= home_players()
    elif game_dict()['away']['team_name']==team_name:
        r= away_players()
        
    if r==[]:
        return None
    
    else:
        sum=0
        for player in r:
            sum+= find_player_dict(player)[stat]
    return sum
    
    
    
    
    
    
    
    
    
    
    
    
#1 
def num_points_scored(name):
    return find_player_dict(name)['points']

#2
def shoe_size(name):
    return find_player_dict(name)['shoe']

#3

def team_colors(team_name):
    return game_dict()[is_home_away(team_name)]['colors']

#4

def team_names():
    return [game_dict()['home']['team_name']] + [game_dict()['away']['team_name']]

#5

def jersey_number(team_name):
    if is_home_away(team_name)=='home':
        players= home_players()
        return list(map(lambda player:find_player_dict(player)['number'], players ))  
            
    elif is_home_away(team_name)=='away':
        players= away_players()
        return list(map(lambda player:find_player_dict(player)['number'], players ))  
    else:
        return None
    
#6

def player_stats(name):
    return find_player_dict(name)








#Bonus qs

#7

def big_shoe_rebounds():
    players=list_of_players()
    player_size=[]
    shoe_size=[]
    for player in players:
        shoe_size.append(find_player_dict(player)['shoe'])
        player_size.append([player, find_player_dict(player)['shoe'], str(find_player_dict(player)['rebounds'])+' rebounds'])
    m= max(shoe_size)
    
    
    return list(filter(lambda player: player[1]==m, player_size))

#8

def most_points_scored():
    players=list_of_players()
    points=[]
    player_points=[]
    for player in players:
        points.append(find_player_dict(player)['points'])
        player_points.append([player, find_player_dict(player)['points']])
    m= max(points)
    
    
    return list(filter(lambda player: player[1]==m, player_points))

#9
        
def winner():
    home= game_dict()['home']['team_name']
    away= game_dict()['away']['team_name']
    
    if team_stats(home, 'points')== team_stats(away, 'points'):
        return ['TIE!', (team_stats(home, 'points'), team_stats(away, 'points') )]
    
    elif team_stats(home, 'points')> team_stats(away, 'points'):
        return [home , (team_stats(home, 'points'), team_stats(away, 'points') )]
    else:
        return [away , (team_stats(away, 'points'), team_stats(home, 'points') )]   
    
#10
def player_with_longest_name():
    players=list_of_players()
    length=[]
    player_length=[]
    for player in players:
        length.append(len(player))
        player_length.append([player, len(player)])
    m= max(length)
    
    return list(filter(lambda player: player[1]==m, player_length))


















#11
    
def player_with_most_steals():
    players=list_of_players()
    steals=[]
    player_steals=[]
    for player in players:
        steals.append(find_player_dict(player)['steals'])
        player_steals.append([player, find_player_dict(player)['steals']])
    m= max(steals)
    
    return list(filter(lambda player: player[1]==m, player_steals))

def long_name_steals_a_ton():
    name_list = player_with_longest_name()
    steal_list = player_with_most_steals()
    names=[]
    steals=[]
    for name in name_list:
        names.append(name[0])
    for steal in steal_list:
        steals.append(steal[0])
    
    common=[]
    for name in names:
        if name in steals:
            common.append(name)
            
    return len(common)>0
    
    