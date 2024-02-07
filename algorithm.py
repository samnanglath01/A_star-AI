import math
import sys
def get_coordinates():
    coordinates = {}
    with open('coordinates.txt', 'r') as file:
        for line in file : 
            city, coord = line.strip().split (":")
            lat, lon = coord.strip("()").split(",")
            coordinates[city] = (float (lat), float(lon))
    return coordinates
def straight_line(start, goal):                       #H(n) = straight line distance from start to goal
    r = 3958.8
    coordinatesCity= get_coordinates()
    lat1,lon1= coordinatesCity[start]              #coordinates start city
    lat2, lon2=coordinatesCity[goal]           #coordinates  goal city
    phi1, phi2 = math.radians(lat1),  math.radians(lat2) #convert to radians
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0)**2 +  math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1 - a))
    distance = r * c
    return distance
def get_graph():
     graph = {}
     with open ("map.txt", "r") as file: 
         for line in file:
             city, adj_city= line.strip ().split('-')
             adj = adj_city. split(',')
             if city not in graph:
                 graph[city] = {}
             for i in adj:
                 destination, distance = i. split('(')
                 distance = float (distance.rstrip(')'))
                 graph [city][destination]= distance
     return graph
def a_star(start, goal):
    graph = get_graph()
    open_set = [{'city':  start, 'g_cost': 0, 'f_cost': straight_line(start, goal), 'path': [start]}]
    visited = set()
    while open_set:
        current_node = min(open_set, key=lambda x: x['f_cost']) #select the node with the lowest f_cost
        open_set.remove(current_node)
        current_city = current_node['city']

        if current_city == goal:
            return current_node ['path'], current_node['g_cost']
        visited.add(current_city)
        	#check all the adjacent cities and start the process again
        for adj, distance in graph[current_city] .items():
            if adj in visited:
                continue

            adj_g_cost = current_node ['g_cost'] + distance
            adj_f_cost = adj_g_cost + straight_line (adj, goal)

            if not any (node['city'] == adj and node['f_cost'] <= adj_f_cost for node in open_set):
                open_set.append({'city': adj, 'g_cost': adj_g_cost, 'f_cost': adj_f_cost, 'path': current_node['path'] + [adj]})    
    return None
  
start_city=sys.argv[1]
goal_city=sys.argv[2]
optimal_route = a_star(start_city, goal_city)
##print(f"Optimal route from {start_city} to {goal_city}: {optimal_route}")
print ("From City: ", start_city)
print ("To City: ", goal_city)
print ("Best Route: ", optimal_route[0])
print ("Total Distance: ", optimal_route[1], "mi")





