

import my_methods_csv as mm


if __name__ == "__main__":

    path_raw_read = r"D:\DOC_2023\Ad_Reports\ad_oct_23"
    path_read = mm.path_edit(path_raw_read)
    dir_list = mm.os.listdir(path_read)

    path_raw_write = r"D:\DOC_2023\Ad_Reports\ad_oct_23"
    path_write = mm.path_edit(path_raw_write)


    date = "00"
    month = "Oct"
    year = "2023"

    tag_start = "Campaign report"
    tag_mid = "Oct " + date + ".csv"
    tag_null = "New"
    tag_result = "Performance Max"
    usd = 116.60

    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year

    uc_tag = "Campaign report month"

    file_to_write = "google_ad_performance_measure_monthly" + date_x + ".csv"
    
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
    
    shera	=	0
    tukhor	=	0
    medha	=	0
    tota	=	0
    quizgiri	=	0
    quizee	=	0
    jeeto	=	0
    quizchamp	=	0
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


    shera_x	=	0
    tukhor_x	=	0
    medha_x	=	0
    tota_x	=	0
    quizgiri_x	=	0
    quizee_x	=	0
    jeeto_x	=	0
    quizchamp_x	=	0
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


    for x in dir_list:
        if uc_tag in x:
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
            campaign = data[row][1]
            
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
            conversion = data[row][22]

##            if tag_result in campaign_type:
##                conversion = conversions
##            else:
##                pass

            #print(conversion)
            #print(campaign,conversion)
                
            cost_per_participated_in_app_action = data[row][23]
##            avg_cpc = data[row][24]
            cost_per_conv = data[row][25]
            cpc = mm.div_error(cost , float(conversion.replace(",","")))



            if "Shera" in campaign or "shera" in campaign or "SHERA" in campaign:
                shera = shera + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    shera_x = shera_x + 1


            if "Tukhr" in campaign or "Tukhor" in campaign or "tukhor" in campaign or "tukhr" in campaign:
                tukhor =  tukhor + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    tukhor_x = tukhor_x + 1


            if "Medha" in campaign or "medha" in campaign or "MEDHA" in campaign:
                medha =  medha + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    medha_x = medha_x + 1


            if "Tota" in campaign or "tota" in campaign or "TOTA" in campaign:
                tota =  tota + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    tota_x = tota_x + 1

            if "Quizgiri" in campaign or "quizgiri" in campaign or "QUIZGIRI" in campaign or "QG" in campaign or "qg" in campaign or "QuizGiri" in campaign:
                quizgiri = quizgiri + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    quizgiri_x = quizgiri_x + 1

            if "Quizee" in campaign or "quize" in campaign or "quizee" in campaign or "QUIZEE" in campaign:
                quizee =  quizee + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    quizee_x = quizee_x + 1

            if "Jeeto" in campaign or "jeeto" in campaign or "JEETO" in campaign:
                jeeto =  jeeto + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    jeeto_x = jeeto_x + 1

            if "Quizchamp" in campaign or "QUIZCHAMP" in campaign or "quizchamp" in campaign or "QuizChamp" in campaign or "Quizmind" in campaign or "QUIZMIND" in campaign or "quizmind" in campaign or "QuizMind" in campaign or "Quiztime" in campaign or "QUIZTIME" in campaign or "quiztime" in campaign or "QuizTime" in campaign or "QM" in campaign or "qm" in campaign or "qc" in campaign or "QC" in campaign or "QT" in campaign or "qt" in campaign:
                quizchamp = quizchamp + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    quizchamp_x = quizchamp_x + 1

            if "Tetris" in campaign or "tetris" in campaign or "TETRIS" in campaign:
                tetris = tetris + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    tetris_x = tetris_x + 1

            if "Npuzzle" in campaign or "npuzzle" in campaign or "NPUZZLE" in campaign or "NPuzzle" in campaign:
                npuzzle = npuzzle + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    npuzzle_x = npuzzle_x + 1

            if "Gotham" in campaign or "gotham" in campaign or "GOTHAM" in campaign:
                gotham = gotham + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    gotham_x = gotham_x + 1
                
            if "Surfing" in campaign or "surfing" in campaign or "SURFING" in campaign:
                surfing = surfing + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    surfing_x = surfing_x + 1

            if "Panda" in campaign or "panda" in campaign or "PANDA" in campaign or "Gamers" in campaign:
                panda =  panda + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    panda_x = panda_x + 1

            if "Space" in campaign or "space" in campaign or "SPACE" in campaign:
                space = space + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    space_x = space_x + 1

            if "Rise" in campaign or "rise" in campaign or "RISE" in campaign:
                rise =  rise + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    rise_x = rise_x + 1

            if "Super Runner" in campaign or "super runner" in campaign or "SUPER RUNNER" in campaign:
                runner = runner + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    runner_x = runner_x + 1

            if "Ninja" in campaign or "NINJA" in campaign or "ninja" in campaign:
                ninja = ninja + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    ninja_x = ninja_x + 1

            if "Circle Pong" in campaign or "circle pong" in campaign or "CIRCLE PONG" in campaign:
                pong =  pong + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    pong_x = pong_x + 1

            if "Samurai" in campaign or "SAMURAI" in campaign or "samurai" in campaign:
                samurai = samurai + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    samurai_x = samurai_x + 1
#
            if "Ortho" in campaign or "ortho" in campaign or "ORTHO" in campaign:
                ortho = ortho + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    ortho_x = ortho_x + 1
                    
            if "Ludo" in campaign or "ludo" in campaign or "LUDO" in campaign:
                ludo = ludo + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    ludo_x = ludo_x + 1

            if "Dana" in campaign or "dana" in campaign or "DANA" in campaign:
                dana =  dana + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    dana_x = dana_x + 1

            if "Ghoori" in campaign or "ghoori" in campaign or "GHOORI" in campaign:
                ghoori = ghoori + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    ghoori_x = ghoori_x + 1

#
            if "Tomb" in campaign or "tomb" in campaign or "TOMB" in campaign:
                tomb = tomb + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    tomb_x = tomb_x + 1

            if "Bubble" in campaign or "bubble" in campaign or "BUBBLE" in campaign:
                bubble = bubble + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    bubble_x = bubble_x + 1

            if "Snow" in campaign or "snow" in campaign or "SNOW" in campaign:
                snow = snow + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    snow_x = snow_x + 1

            if "Ping" in campaign or "ping" in campaign or "PING" in campaign:
                ping = ping + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    ping_x = ping_x + 1

            if "Dash" in campaign or "dash" in campaign or "DASH" in campaign:
                dash = dash + 1
                if cpc > 42 and float(cost) > 1000: #"quizgiri" in campaign:
                    dash_x = dash_x + 1


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


    w_path = path_write
    w_file = w_path + "//" + file_to_write
    mm.write_list(w_file, l_write)

