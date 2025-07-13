

import my_methods_csv as mm


if __name__ == "__main__":

    path_raw_read = r"D:\DOC_2023\Ad_Reports\ad_oct_23"
    path_read = mm.path_edit(path_raw_read)
    dir_list = mm.os.listdir(path_read)

    path_raw_write = r"D:\DOC_2023\Ad_Reports\ad_oct_23"
    path_write = mm.path_edit(path_raw_write)

    tag_start = "Nagorik-"
    tag_mid = "-Ad-Account-"
    tag_null = "New"
    tag_result = "actions:offsite_conversion.custom"
    #tag_date = "-8-Jun-20238-Jun-2023"

    date = "00"
    month = "Oct"
    year = "2023"
    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year

    uc_tag = "-Ads-1-Oct-202331-Oct-2023.csv"

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


            if "Shera" in ad or "shera" in ad or "SHERA" in ad:
                shera = shera + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    shera_x = shera_x + 1


            if "Tukhr" in ad or "Tukhor" in ad or "tukhor" in ad or "tukhr" in ad:
                tukhor =  tukhor + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    tukhor_x = tukhor_x + 1


            if "Medha" in ad or "medha" in ad or "MEDHA" in ad:
                medha =  medha + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    medha_x = medha_x + 1


            if "Tota" in ad or "tota" in ad or "TOTA" in ad:
                tota =  tota + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    tota_x = tota_x + 1

            if "Quizgiri" in ad or "quizgiri" in ad or "QUIZGIRI" in ad or "QG" in ad or "qg" in ad or "QuizGiri" in ad:
                quizgiri = quizgiri + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    quizgiri_x = quizgiri_x + 1

            if "Quizee" in ad or "quize" in ad or "quizee" in ad or "QUIZEE" in ad:
                quizee =  quizee + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    quizee_x = quizee_x + 1

            if "Jeeto" in ad or "jeeto" in ad or "JEETO" in ad:
                jeeto =  jeeto + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    jeeto_x = jeeto_x + 1

            if "Quizchamp" in ad or "QUIZCHAMP" in ad or "quizchamp" in ad or "QuizChamp" in ad or "Quizmind" in ad or "QUIZMIND" in ad or "quizmind" in ad or "QuizMind" in ad or "Quiztime" in ad or "QUIZTIME" in ad or "quiztime" in ad or "QuizTime" in ad or "QC" in ad or "qc" in ad or "qm" in ad or "QM" in ad or "QT" in ad or "qt" in ad:
                quizchamp = quizchamp + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    quizchamp_x = quizchamp_x + 1

            if "Tetris" in ad or "tetris" in ad or "TETRIS" in ad:
                tetris = tetris + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    tetris_x = tetris_x + 1

            if "Npuzzle" in ad or "npuzzle" in ad or "NPUZZLE" in ad or "NPuzzle" in ad:
                npuzzle = npuzzle + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    npuzzle_x = npuzzle_x + 1

            if "Gotham" in ad or "gotham" in ad or "GOTHAM" in ad:
                gotham = gotham + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    gotham_x = gotham_x + 1
                
            if "Surfing" in ad or "surfing" in ad or "SURFING" in ad:
                surfing = surfing + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    surfing_x = surfing_x + 1

            if "Panda" in ad or "panda" in ad or "PANDA" in ad or "Gamers" in ad:
                panda =  panda + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    panda_x = panda_x + 1

            if "Space" in ad or "space" in ad or "SPACE" in ad:
                space = space + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    space_x = space_x + 1

            if "Rise" in ad or "rise" in ad or "RISE" in ad:
                rise =  rise + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    rise_x = rise_x + 1

            if "Super Runner" in ad or "super runner" in ad or "SUPER RUNNER" in ad:
                runner = runner + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    runner_x = runner_x + 1

            if "Ninja" in ad or "NINJA" in ad or "ninja" in ad:
                ninja = ninja + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    ninja_x = ninja_x + 1

            if "Circle Pong" in ad or "circle pong" in ad or "CIRCLE PONG" in ad:
                pong =  pong + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    pong_x = pong_x + 1

            if "Samurai" in ad or "SAMURAI" in ad or "samurai" in ad:
                samurai = samurai + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    samurai_x = samurai_x + 1
#
            if "Ortho" in ad or "ortho" in ad or "ORTHO" in ad:
                ortho = ortho + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    ortho_x = ortho_x + 1
                    
            if "Ludo" in ad or "ludo" in ad or "LUDO" in ad:
                ludo = ludo + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    ludo_x = ludo_x + 1

            if "Dana" in ad or "dana" in ad or "DANA" in ad:
                dana =  dana + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    dana_x = dana_x + 1

            if "Ghoori" in ad or "ghoori" in ad or "GHOORI" in ad:
                ghoori = ghoori + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    ghoori_x = ghoori_x + 1

#
            if "Tomb" in ad or "tomb" in ad or "TOMB" in ad:
                tomb = tomb + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    tomb_x = tomb_x + 1

            if "Bubble" in ad or "bubble" in ad or "BUBBLE" in ad:
                bubble = bubble + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    bubble_x = bubble_x + 1

            if "Snow" in ad or "snow" in ad or "SNOW" in ad:
                snow = snow + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    snow_x = snow_x + 1

            if "Ping" in ad or "ping" in ad or "PING" in ad:
                ping = ping + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    ping_x = ping_x + 1

            if "Dash" in ad or "dash" in ad or "DASH" in ad:
                dash = dash + 1
                if cpc > 42 and float(amount_spent) > 1000: #"quizgiri" in ad:
                    dash_x = dash_x + 1


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


    w_file_ratio = "meta_ad_perf_measure_monthly_" + year + "_" + month + "_" + date + ".csv"
    w_path_ratio = path_write + "//" + w_file_ratio
    mm.write_list( w_path_ratio, l_ratio)


