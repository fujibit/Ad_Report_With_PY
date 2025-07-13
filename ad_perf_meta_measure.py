

import my_methods_csv as mm


if __name__ == "__main__":

    path_raw_read = r"C:\Revenue & Cost\DOC_2024\Ad_cost_daily\Sep_24"
    path_read = mm.path_edit(path_raw_read)
    dir_list = mm.os.listdir(path_read)

    path_raw_write = r"C:\Revenue & Cost\DOC_2024\Ad_cost_daily\Sep_24"
    path_write = mm.path_edit(path_raw_write)

    tag_start = "Nagorik-"
    tag_mid = "-Ad-Account-"
    tag_null = "**"
    tag_result = "actions:offsite_conversion.custom"
    #tag_date = "-8-Jun-20238-Jun-2023"

    date = "11"
    month = "Sep"
    year = "2024"
    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year

    file_to_write = "ad_perf_index_meta_"

    #start_date = 20230601 # in 'x' number format --> int(yyyymmdd)
    #end_date = 20230630 # in 'x' number format --> int(yyyymmdd)

    l = []
    l_ratio = []

    l_shera = []
    l_tukhor = []
    l_medha = []
    l_tota = []
    l_quizgiri = []
    l_quizee = []
    l_jeeto = []
    l_quizchamp = []
    l_quizmind = []
    l_quiztime = []

    l_tetris = []
    l_npuzzle = []
    l_gotham = []
    l_surfing = []
    l_panda = []
    l_space = []
    l_rise = []
    l_runner = []
    l_ninja = []
    l_pong = []
    l_samurai = []

    l_ortho = []
    l_ludo = []
    l_dana = []
    l_ghoori = []

    l_tomb_runner = []
    l_bubble = []
    l_snow_surfer = []
    l_ping_pong = []
    l_dash = []

    l_hoophop = []
    l_candy = []

    l_shark = []
    l_deen = []
    l_water = []
    l_word = []

    l_quizbd = []


    shera	=	0
    tukhor	=	0
    medha	=	0
    tota	=	0
    quizgiri	=	0
    quizee	=	0
    jeeto	=	0
    quizchamp	=	0
    quizmind = 0
    quiztime = 0
    tetris	=	0
    npuzzle	=	0
    gotham	=	0
    surfing	=	0
    panda	=	0
    space	=	0
    rise	=	0
    runner	=	0
    ninja	=	0
    pong	=	0
    samurai	=	0
    ortho	=	0
    ludo	=	0
    dana	=	0
    ghoori	=	0
    tomb	=	0
    bubble	=	0
    snow	=	0
    ping	=	0
    dash	=	0

    hoophop = 0
    candy = 0
    shark = 0
    deen = 0
    water = 0
    word = 0
    quizbd = 0

    shera_x	=	0
    tukhor_x	=	0
    medha_x	=	0
    tota_x	=	0
    quizgiri_x	=	0
    quizee_x	=	0
    jeeto_x	=	0
    quizchamp_x	=	0
    quizmind_x = 0
    quiztime_x = 0
    tetris_x	=	0
    npuzzle_x	=	0
    gotham_x	=	0
    surfing_x	=	0
    panda_x	=	0
    space_x	=	0
    rise_x	=	0
    runner_x	=	0
    ninja_x	=	0
    pong_x	=	0
    samurai_x	=	0
    ortho_x	=	0
    ludo_x	=	0
    dana_x	=	0
    ghoori_x	=	0
    tomb_x	=	0
    bubble_x	=	0
    snow_x	=	0
    ping_x	=	0
    dash_x	=	0

    hoophop_x = 0
    candy_x = 0
    shark_x = 0
    deen_x = 0
    water_x = 0
    word_x = 0
    quizbd_x = 0


    for x in dir_list:
        if ".csv" in x and ")" not in x and tag_null not in x and tag_date in x:
            a = path_read + "//" + x
            l.append([a])


    #print(l)
    print(len(l))
    for i in range(len(l)):
        print(l[i])

    print("")

    for f in range(len(l)):

        src = l[f][0]
        data = mm.read_data(src)

        for row in range(1,len(data)):
            

            reporting_starts = data[row][0]
            reporting_ends = data[row][1]
            
            ad_name = data[row][2]
            ad_delivery = data[row][3]
            ad_set_name = data[row][4]
            ad = (ad_name + ad_set_name).lower() ## merge
            
            bid = data[row][5]
            bid_type = data[row][6]
            
            ad_set_budget = data[row][7]
            ad_set_budget_type = data[row][8]
            
            last_significant_edit = data[row][9]
            attribution_setting = data[row][10]
            
            result = data[row][11]
            result_indicator = data[row][12]

##            if tag_result in result_indicator:
##                result = results
            
            reach = data[row][13]
            impressions = data[row][14]
            
            cost_per_results = data[row][15]
            if cost_per_results != "":
                cpc = float(cost_per_results.replace(",",""))

            quality_ranking = data[row][16]
            engagement_rate_ranking = data[row][17]
            conversion_rate_ranking = data[row][18]
            
            amount_spent = data[row][19]
            ends = data[row][20]


            if "shera" in ad:
                shera = shera + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    shera_x = shera_x + 1


            if "tukhor" in ad or "tukhr" in ad:
                tukhor =  tukhor + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    tukhor_x = tukhor_x + 1


            if "medha" in ad:
                medha =  medha + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    medha_x = medha_x + 1


            if "tota" in ad and "total"  not in ad:
                tota =  tota + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    tota_x = tota_x + 1

            if "quizgiri" in ad or "qg" in ad:
                quizgiri = quizgiri + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    quizgiri_x = quizgiri_x + 1

            if "quize" in ad or "quizee" in ad:
                quizee =  quizee + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    quizee_x = quizee_x + 1

            if "jeeto" in ad:
                jeeto =  jeeto + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    jeeto_x = jeeto_x + 1

            if "quizchamp" in ad or "qc" in ad or "quiz champ" in ad:
                quizchamp = quizchamp + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    quizchamp_x = quizchamp_x + 1

            if "quizmind" in ad or "qm" in ad or "quiz mind" in ad :
                quizmind = quizmind + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    quizmind_x = quiztime_x + 1

            if "quiztime" in ad or "qt" in ad or "quiz time" in ad :
                quiztime = quiztime + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    quiztime_x = quiztime_x + 1

            if "tetris" in ad:
                tetris = tetris + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    tetris_x = tetris_x + 1

            if "npuzzle" in ad:
                npuzzle = npuzzle + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    npuzzle_x = npuzzle_x + 1

            if "gotham" in ad:
                gotham = gotham + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    gotham_x = gotham_x + 1
                
            if "surfing" in ad or "surfin" in ad:
                surfing = surfing + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    surfing_x = surfing_x + 1

            if "panda" in ad:
                panda =  panda + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    panda_x = panda_x + 1

            if "space" in ad:
                space = space + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    space_x = space_x + 1

            if "rise" in ad:
                rise =  rise + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    rise_x = rise_x + 1

            if "super runner" in ad:
                runner = runner + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    runner_x = runner_x + 1

            if "ninja" in ad:
                ninja = ninja + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    ninja_x = ninja_x + 1

            if "circle pong" in ad or "c.pong" in ad:
                pong =  pong + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    pong_x = pong_x + 1

            if "samurai" in ad:
                samurai = samurai + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    samurai_x = samurai_x + 1
#
            if "ortho" in ad:
                ortho = ortho + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    ortho_x = ortho_x + 1
                    
            if "ludo" in ad:
                ludo = ludo + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    ludo_x = ludo_x + 1

            if "dana" in ad:
                dana =  dana + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    dana_x = dana_x + 1

            if "ghoori" in ad:
                ghoori = ghoori + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    ghoori_x = ghoori_x + 1

#
            if "tomb" in ad:
                tomb = tomb + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    tomb_x = tomb_x + 1

            if "bubble" in ad:
                bubble = bubble + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    bubble_x = bubble_x + 1

            if "snow" in ad:
                snow = snow + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    snow_x = snow_x + 1

            if "ping " in ad or "ping pong" in ad:
                ping = ping + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    ping_x = ping_x + 1

            if "dash" in ad or "heroic" in ad:
                dash = dash + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    dash_x = dash_x + 1

            if "hoophop" in ad or "hoop hop" in ad or " hop" in ad or " hoop" in ad:
                hoophop = hoophop + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    hoophop_x = hoophop_x + 1

            if "candy" in ad:
                candy = candy + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    candy_x = candy_x + 1

            if "shark" in ad or "enova" in ad:
                shark = shark + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    shark_x = shark_x + 1

            if "deen" in ad:
                deen = deen + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    deen_x = deen_x + 1

            if "water" in ad:
                water = water + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    water_x = water_x + 1

            if "word" in ad:
                word = word + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    word_x = word_x + 1

            if "quizbd" in ad or "quiz bd" in ad:
                quizbd = quizbd + 1
                if cpc > 40 and float(amount_spent) > 500: #"quizgiri" in ad:
                    quizbd_x = quizbd_x + 1

    l_ratio.append(["Meta:", date_x, " ", " " ])
    l_ratio.append(["Products", "Total_Ads", "Weak_Ads"])

    l_ratio.append([ "Shera", shera, shera_x ])
    l_ratio.append([ "Tukhor", tukhor, tukhor_x ])
    l_ratio.append([ "Medha", medha, medha_x ])
    l_ratio.append([ "Tota", tota, tota_x ])
    l_ratio.append([ "Quizgiri", quizgiri, quizgiri_x ])
    l_ratio.append([ "Quizee", quizee, quizee_x ])
    l_ratio.append([ "Jeeto", jeeto, jeeto_x ])
    l_ratio.append([ "Quizchamp", quizchamp, quizchamp_x ])
    l_ratio.append([ "Quizmind", quizmind, quizmind_x ])
    l_ratio.append([ "Quiztime", quiztime, quiztime_x ])
    
    l_ratio.append([ "Tetris", tetris, tetris_x ])
    l_ratio.append([ "Npuzzle", npuzzle, npuzzle_x ])
    l_ratio.append([ "Gotham", gotham, gotham_x ])
    l_ratio.append([ "Surfing", surfing, surfing_x ])
    l_ratio.append([ "Panda", panda, panda_x ])
    l_ratio.append([ "Space", space, space_x ])
    l_ratio.append([ "Rise", rise, rise_x ])
    l_ratio.append([ "Runner", runner, runner_x ])
    l_ratio.append([ "Ninja", ninja, ninja_x ])
    l_ratio.append([ "Pong", pong, pong_x ])
    l_ratio.append([ "Samurai", samurai, samurai_x ])
    l_ratio.append([ "Ortho", ortho, ortho_x ])
    l_ratio.append([ "Ludo", ludo, ludo_x ])
    l_ratio.append([ "Dana", dana, dana_x ])
    l_ratio.append([ "Ghoori", ghoori, ghoori_x ])
    l_ratio.append([ "Tomb", tomb, tomb_x ])
    l_ratio.append([ "Bubble", bubble, bubble_x ])
    l_ratio.append([ "Snow", snow, snow_x ])
    l_ratio.append([ "Ping", ping, ping_x ])
    l_ratio.append([ "Dash", dash, dash_x ])

    l_ratio.append([ "Hoophop", hoophop, hoophop_x ])
    l_ratio.append([ "Candy", candy, candy_x ])
    l_ratio.append([ "Shark", shark, shark_x ])
    l_ratio.append([ "Deen", deen, deen_x ])
    l_ratio.append([ "Water", water, water_x ])
    l_ratio.append([ "Word", word, word_x ])
    l_ratio.append([ "Quizbd", quizbd, quizbd_x ])


    w_file_ratio = file_to_write + year + "_" + month + "_" + date + ".csv"
    w_path_ratio = path_write + "//" + w_file_ratio
    mm.write_list( w_path_ratio, l_ratio)


