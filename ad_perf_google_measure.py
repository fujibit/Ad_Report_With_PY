

import my_methods_csv as mm


if __name__ == "__main__":

    path_raw_read = r"C:\Revenue & Cost\DOC_2024\Ad_cost_daily\Sep_24"
    path_read = mm.path_edit(path_raw_read)
    dir_list = mm.os.listdir(path_read)

    path_raw_write = r"C:\Revenue & Cost\DOC_2024\Ad_cost_daily\Sep_24"
    path_write = mm.path_edit(path_raw_write)


    date = "11"
    month = "Sep"
    year = "2024"

    tag_start = "Campaign report"
    tag_mid = "Sep " + date + ".csv"
    tag_null = "**"
    tag_result = "Performance Max"
    usd = 126.60

    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year

    file_to_write = "ad_perf_index_google_" + date_x + ".csv"

    u_tag = "-Ads-1-Mar-202410-Mar-2024.csv"
    
    #start_date = 20230601 # in 'x' number format --> int(yyyymmdd)
    #end_date = 20230631 # in 'x' number format --> int(yyyymmdd)


    l = []
    l_write = []
    #l_write.append([ "Ad_Name", "Cost", "Conversion", "CPC", "Impression", "Click_Success_Rate", "Opt_Score"]) ###
    
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
    l_dana =[]
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
    quizmind	=	0
    quiztime	=	0
    
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
    quizmind_x	=	0
    quiztime_x	=	0
    
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
        if ".csv" in x and ")" not in x and tag_null not in x and tag_start in x and tag_mid in x:
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

        for row in range(3,len(data)):

            campaign_status = data[row][0]
            campaign = data[row][1].lower()
            
            budget_name = data[row][2]
            currency_code = data[row][3]
            
            budget = data[row][4]
            budget_type = data[row][5]
            
            status = data[row][6]
            status_reasons = data[row][7]
            optimization_score = data[row][8]
            
            campaign_type = data[row][9]
            
            impression = data[row][10]
            interactions = data[row][11]
            interaction_rate = data[row][12]
            
            avg_cost = data[row][13]
            cost_raw = data[row][14]
            
            if cost_raw != "":
                cost = float(cost_raw)*usd
            else:
                pass

            conv_value = data[row][15]
            conv_value_cost = data[row][16]
            results = data[row][17]
            
            bid_strategy_type = data[row][18]
            participated_in_app_actions = data[row][19]
            clicks = data[row][20]
            
            conv_rate = data[row][21]
            #conversion = data[row][21]
            conversion = data[row][21]

##            if tag_result in campaign_type:
##                conversion = conversions
##            else:
##                pass

            #print(conversion)
            #print(campaign,conversion)
                
##            cost_per_participated_in_app_action = data[row][23]
####            avg_cpc = data[row][24]
##            cost_per_conv = data[row][25]
            cpc = mm.div_error(float(cost)*usd , float(conversion.replace(",",""))*usd)



            if "shera" in campaign and campaign_status == "Enabled":
                shera = shera + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign:
                    shera_x = shera_x + 1


            if ("tukhor" in campaign or "tukhr" in campaign) and campaign_status == "Enabled":
                tukhor =  tukhor + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    tukhor_x = tukhor_x + 1


            if "medha" in campaign and campaign_status == "Enabled":
                medha =  medha + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    medha_x = medha_x + 1


            if ("tota" in campaign and "total" not in campaign) and campaign_status == "Enabled":
                tota =  tota + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    tota_x = tota_x + 1

            if ("quizgiri" in campaign or "qg" in campaign or "quiz giri" in campaign ) and campaign_status == "Enabled":
                quizgiri = quizgiri + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    quizgiri_x = quizgiri_x + 1

            if ("quize" in campaign or "quizee" in campaign) and campaign_status == "Enabled":
                quizee =  quizee + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    quizee_x = quizee_x + 1

            if "jeeto" in campaign and campaign_status == "Enabled":
                jeeto =  jeeto + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    jeeto_x = jeeto_x + 1

            if ("quizchamp" in campaign or "qc" in campaign or "quiz champ" in campaign ) and campaign_status == "Enabled":
                quizchamp = quizchamp + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    quizchamp_x = quizchamp_x + 1

            if ("quizmind" in campaign or "qm" in campaign or "quiz mind" in campaign) and campaign_status == "Enabled":
                quizmind = quizmind + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    quizmind_x = quizmind_x + 1

            if ("quiztime" in campaign or "qt" in campaign or "quiz time" in campaign) and campaign_status == "Enabled":
                quiztime = quiztime + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    quiztime_x = quiztime_x + 1

            if "tetris" in campaign and campaign_status == "Enabled":
                tetris = tetris + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    tetris_x = tetris_x + 1

            if "npuzzle" in campaign and campaign_status == "Enabled":
                npuzzle = npuzzle + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    npuzzle_x = npuzzle_x + 1

            if "gotham" in campaign and campaign_status == "Enabled":
                gotham = gotham + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    gotham_x = gotham_x + 1
                
            if "surfing" in campaign and campaign_status == "Enabled":
                surfing = surfing + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    surfing_x = surfing_x + 1

            if "panda" in campaign and campaign_status == "Enabled":
                panda =  panda + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    panda_x = panda_x + 1

            if "space" in campaign and campaign_status == "Enabled":
                space = space + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    space_x = space_x + 1

            if "rise" in campaign and campaign_status == "Enabled":
                rise =  rise + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    rise_x = rise_x + 1

            if "super runner" in campaign and campaign_status == "Enabled":
                runner = runner + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    runner_x = runner_x + 1

            if "ninja" in campaign and campaign_status == "Enabled":
                ninja = ninja + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    ninja_x = ninja_x + 1

            if ("circle pong" in campaign or "c.pong" in campaign) and campaign_status == "Enabled":
                pong =  pong + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    pong_x = pong_x + 1

            if "samurai" in campaign and campaign_status == "Enabled":
                samurai = samurai + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    samurai_x = samurai_x + 1
#
            if "ortho" in campaign and campaign_status == "Enabled":
                ortho = ortho + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    ortho_x = ortho_x + 1
                    
            if "ludo" in campaign and campaign_status == "Enabled":
                ludo = ludo + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    ludo_x = ludo_x + 1

            if "dana" in campaign and campaign_status == "Enabled":
                dana =  dana + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    dana_x = dana_x + 1

            if "ghoori" in campaign and campaign_status == "Enabled":
                ghoori = ghoori + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    ghoori_x = ghoori_x + 1

#
            if "tomb" in campaign and campaign_status == "Enabled":
                tomb = tomb + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    tomb_x = tomb_x + 1

            if "bubble" in campaign and campaign_status == "Enabled":
                bubble = bubble + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    bubble_x = bubble_x + 1

            if "snow" in campaign and campaign_status == "Enabled":
                snow = snow + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    snow_x = snow_x + 1

            if ( "ping pong" in campaign or "ping " in campaign) and campaign_status == "Enabled":
                ping = ping + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    ping_x = ping_x + 1

            if ("dash" in campaign or "heroic" in campaign) and campaign_status == "Enabled":
                dash = dash + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    dash_x = dash_x + 1

            if ("hoophop" in campaign or "hoop hop" in campaign or " hop" in campaign or " hoop" in campaign) and campaign_status == "Enabled":
                hoophop = hoophop + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    hoophop_x = hoophop_x + 1

            if "candy" in campaign and campaign_status == "Enabled":
                candy = candy + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    candy_x = candy_x + 1

            if ("shark" in campaign or "enova" in campaign) and campaign_status == "Enabled":
                shark = shark + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    shark_x = shark_x + 1

            if "deen" in campaign and campaign_status == "Enabled":
                deen = deen + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    deen_x = deen_x + 1

            if "water" in campaign and campaign_status == "Enabled":
                water = water + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    water_x = water_x + 1

            if "word" in campaign and campaign_status == "Enabled":
                word = word + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    word_x = word_x + 1

            if ("quizbd" in campaign or "quiz bd" in campaign) and campaign_status == "Enabled":
                quizbd = quizbd + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in campaign and campaign_status == "Enabled":
                    quizbd_x = quizbd_x + 1


    l_write.append(["Google:", date_x, " ", " " ])
    l_write.append(["Products", "Total_Ads", "Weak_Ads"])

    l_write.append([ "Shera", shera, shera_x ])
    l_write.append([ "Tukhor", tukhor, tukhor_x ])
    l_write.append([ "Medha", medha, medha_x ])
    l_write.append([ "Tota", tota, tota_x ])
    l_write.append([ "Quizgiri", quizgiri, quizgiri_x ])
    l_write.append([ "Quizee", quizee, quizee_x ])
    l_write.append([ "Jeeto", jeeto, jeeto_x ])
    l_write.append([ "Quizchamp", quizchamp, quizchamp_x ])
    l_write.append([ "Quizmind", quizmind, quizmind_x ])
    l_write.append([ "Quiztime", quiztime, quiztime_x ])
    
    l_write.append([ "Tetris", tetris, tetris_x ])
    l_write.append([ "Npuzzle", npuzzle, npuzzle_x ])
    l_write.append([ "Gotham", gotham, gotham_x ])
    l_write.append([ "Surfing", surfing, surfing_x ])
    l_write.append([ "Panda", panda, panda_x ])
    l_write.append([ "Space", space, space_x ])
    l_write.append([ "Rise", rise, rise_x ])
    l_write.append([ "Runner", runner, runner_x ])
    l_write.append([ "Ninja", ninja, ninja_x ])
    l_write.append([ "Pong", pong, pong_x ])
    l_write.append([ "Samurai", samurai, samurai_x ])
    l_write.append([ "Ortho", ortho, ortho_x ])
    l_write.append([ "Ludo", ludo, ludo_x ])
    l_write.append([ "Dana", dana, dana_x ])
    l_write.append([ "Ghoori", ghoori, ghoori_x ])
    l_write.append([ "Tomb", tomb, tomb_x ])
    l_write.append([ "Bubble", bubble, bubble_x ])
    l_write.append([ "Snow", snow, snow_x ])
    l_write.append([ "Ping", ping, ping_x ])
    l_write.append([ "Dash", dash, dash_x ])

    l_write.append([ "Hoophop", hoophop, hoophop_x ])
    l_write.append([ "Candy", candy, candy_x ])
    l_write.append([ "Shark", shark, shark_x ])
    l_write.append([ "Deen", deen, deen_x ])
    l_write.append([ "Water", water, water_x ])
    l_write.append([ "Word", word, word_x ])
    l_write.append([ "Quizbd", quizbd, quizbd_x ])


    w_path = path_write
    w_file = w_path + "//" + file_to_write
    mm.write_list(w_file, l_write)

