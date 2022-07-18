'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    c = social_graph.keys()
    d = list(c)
    if from_member not in d and to_member not in d:
        social_graph[from_member] = {'following':[]}
        social_graph[to_member] = {'following':[]}
        a = social_graph[from_member]['following']
        res = [ele for ele in a if(ele in to_member)]
        b = social_graph[to_member]['following']
        qes = [el for el in b if(el in from_member)]
        value_res = str(bool(res))
        value_qes = str(bool(qes))
        if value_res == 'True' and value_qes == 'True':
            return 'friends'
        elif value_res == 'False' and value_qes == 'True':
            return 'followed by'
        elif value_res == 'True' and value_qes == 'False':
            return 'follower'
        elif value_res == 'False' and value_qes == 'False':
            return 'no relationship'
        else:
            return 'Elevate'
    elif from_member not in d:
        social_graph[from_member] = {'following':[]}
        a = social_graph[from_member]['following']
        res = [ele for ele in a if(ele in to_member)]
        b = social_graph[to_member]['following']
        qes = [el for el in b if(el in from_member)]
        value_res = str(bool(res))
        value_qes = str(bool(qes))
        if value_res == 'True' and value_qes == 'True':
            return 'friends'
        elif value_res == 'False' and value_qes == 'True':
            return 'followed by'
        elif value_res == 'True' and value_qes == 'False':
            return 'follower'
        elif value_res == 'False' and value_qes == 'False':
            return 'no relationship'
        else:
            return 'Elevate'
    elif to_member not in d:
        social_graph[to_member] = {'following':[]}
        a = social_graph[from_member]['following']
        res = [ele for ele in a if(ele in to_member)]
        b = social_graph[to_member]['following']
        qes = [el for el in b if(el in from_member)]
        value_res = str(bool(res))
        value_qes = str(bool(qes))
        if value_res == 'True' and value_qes == 'True':
            return 'friends'
        elif value_res == 'False' and value_qes == 'True':
            return 'followed by'
        elif value_res == 'True' and value_qes == 'False':
            return 'follower'
        elif value_res == 'False' and value_qes == 'False':
            return 'no relationship'
        else:
            return 'Elevate'
    else:
        a = social_graph[from_member]['following']
        res = [ele for ele in a if(ele in to_member)]
        b = social_graph[to_member]['following']
        qes = [el for el in b if(el in from_member)]
        value_res = str(bool(res))
        value_qes = str(bool(qes))
        if value_res == 'True' and value_qes == 'True':
            return 'friends'
        elif value_res == 'False' and value_qes == 'True':
            return 'followed by'
        elif value_res == 'True' and value_qes == 'False':
            return 'follower'
        elif value_res == 'False' and value_qes == 'False':
            return 'no relationship'
        else:
            return 'Elevate'


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result = "NO WINNER"
    def boom(line):
        check = set()
        for a in line:
            check.add(a)
        if len(check) == 1:
            wincombo = list(check)
            if wincombo[0] != "":
                return(str(wincombo[0]))
    for hori in board:
        if boom(hori) != None:
            result = boom(hori)
    for vert in list(zip(*board)):
        if boom(vert) != None:
            result = boom(vert)
    updolist = []
    for u in range(len(board)):
        updolist.append(board[u][u])
    if boom(updolist) != None:
            result = boom(updolist)
    duplist = []
    for d in range(len(board)):
        duplist.append(board[len(board)-1-d][d])
    if boom(duplist) != None:
            result = boom(duplist)
    return result

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    boom = (first_stop, second_stop)
    total_time = 0
    if boom in list(route_map.keys()):
        return route_map[boom]["travel_time_mins"]
    elif first_stop == second_stop:
        for same in list(route_map.values()):
            total_time += same["travel_time_mins"]
        return total_time
    else:
        map = list()
        for b in list(route_map):
            map.append(b[0])
        wherenow = map.index(first_stop)
        whereto = map.index(second_stop)
        now = wherenow
        bang = [wherenow]
        while now != whereto:
            now += 1
            if now > len(route_map)-1:
                now = 0
            bang.append(now)
        bang.pop()
        stops = list()
        x = list(route_map)
        for stop in bang:
            stops.append(x[stop])
        for stop in stops:
            total_time += route_map[stop]["travel_time_mins"]        
        return(total_time)