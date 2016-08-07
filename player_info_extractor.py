import urllib2

response = urllib2.urlopen('http://baseball-data.com/stats/hitter-all/tpa-1.html')
html = response.read()

table_start_index = html.find('<tbody>')
table_end_index = html.find('</tbody>')

table_html = html[table_start_index:table_end_index]

players_info_list = []

player_line_list = table_html.split('<tr')
for playre_line in player_line_list[1:]:
    player_info_list = []
    player_status_list = playre_line.split('<td')
    for player_status in player_status_list[1:]:
        status_start_index = player_status.find('>') + 1
        status_end_index = player_status.find('</td>')
        player_info = player_status[status_start_index:status_end_index]
        if player_info.find('<a') != -1:
            href_start_index = player_info.find('"') + 1
            href_end_index = player_info.rfind('"')
            player_info_list.append(player_info[href_start_index:href_end_index])
            name_start_index = player_info.find('>') + 1
            name_end_index = player_info.rfind('</')
            player_info_list.append(player_info[name_start_index:name_end_index])
        else:
            player_info_list.append(player_info)
    players_info_list.append(player_info_list)

for player_info_list in players_info_list:
    for player_info in player_info_list:
        print player_info+',' ,
    print
