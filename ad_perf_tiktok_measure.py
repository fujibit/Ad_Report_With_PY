

import my_methods_csv as mm


if __name__ == "__main__":

    path_raw_read = r"C:\Revenue & Cost\DOC_2024\Ad_cost_daily\Sep_24\tiktok_sep_11"
    path_read = mm.path_edit(path_raw_read)
    dir_list = mm.os.listdir(path_read)

    path_raw_write = r"C:\Revenue & Cost\DOC_2024\Ad_cost_daily\Sep_24"
    path_write = mm.path_edit(path_raw_write)


    date = "11"
    month = "Sep"
    year = "2024"
    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year

    file_to_write = "ad_perf_index_tiktok_"
    usd = 126.00

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
        if ".csv" in x:
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
            
            
            ad = data[row][0].lower()
            status = data[row][1]
            
            cost = float(data[row][3])*usd
            conversion = data[row][9]
            cpc = float(data[row][10])*usd
            


            if "shera" in ad and status == "Active":
                shera = shera + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    shera_x = shera_x + 1


            if "tukhor" in ad or "tukhr" in ad and status == "Active":
                tukhor =  tukhor + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    tukhor_x = tukhor_x + 1


            if "medha" in ad and status == "Active":
                medha =  medha + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    medha_x = medha_x + 1


            if "tota" in ad and "total"  not in ad and status == "Active":
                tota =  tota + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    tota_x = tota_x + 1

            if ("quizgiri" in ad or "qg" in ad or "quiz giri" in ad) and status == "Active":
                quizgiri = quizgiri + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    quizgiri_x = quizgiri_x + 1

            if ("quize" in ad or "quizee" in ad) and status == "Active":
                quizee =  quizee + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    quizee_x = quizee_x + 1

            if "jeeto" in ad and status == "Active":
                jeeto =  jeeto + 1
                #print(jeeto,cpc,cost)
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    jeeto_x = jeeto_x + 1
                    #print(cpc)

            if ("quizchamp" in ad or "qc" in ad or "quiz champ" in ad) and status == "Active":
                quizchamp = quizchamp + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    quizchamp_x = quizchamp_x + 1

            if ("quizmind" in ad or "qm" in ad or "quiz mind" in ad) and status == "Active":
                quizmind = quizmind + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    quizmind_x = quizmind_x + 1

            if ("quiztime" in ad or "qt" in ad or "quiz time" in ad) and status == "Active":
                quiztime = quiztime + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    quiztime_x = quiztime_x + 1

            if "tetris" in ad and status == "Active":
                tetris = tetris + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    tetris_x = tetris_x + 1

            if "npuzzle" in ad and status == "Active":
                npuzzle = npuzzle + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    npuzzle_x = npuzzle_x + 1

            if "gotham" in ad and status == "Active":
                gotham = gotham + 1
                print(gotham,"",cpc,"",cost,"",conversion)
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    gotham_x = gotham_x + 1
                
            if ("surfing" in ad or "surfin" in ad) and status == "Active":
                surfing = surfing + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    surfing_x = surfing_x + 1

            if "panda" in ad and status == "Active":
                panda =  panda + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    panda_x = panda_x + 1

            if "space" in ad and status == "Active":
                space = space + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    space_x = space_x + 1

            if "rise" in ad and status == "Active":
                rise =  rise + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    rise_x = rise_x + 1

            if "super runner" in ad and status == "Active":
                runner = runner + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    runner_x = runner_x + 1

            if "ninja" in ad and status == "Active":
                ninja = ninja + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    ninja_x = ninja_x + 1

            if ("circle pong" in ad or "c.pong" in ad) and status == "Active":
                pong =  pong + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    pong_x = pong_x + 1

            if "samurai" in ad and status == "Active":
                samurai = samurai + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    samurai_x = samurai_x + 1
#
            if "ortho" in ad and status == "Active":
                ortho = ortho + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    ortho_x = ortho_x + 1
                    
            if "ludo" in ad and status == "Active":
                ludo = ludo + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    ludo_x = ludo_x + 1

            if "dana" in ad and status == "Active":
                dana =  dana + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    dana_x = dana_x + 1

            if "ghoori" in ad and status == "Active":
                ghoori = ghoori + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    ghoori_x = ghoori_x + 1

#
            if "tomb" in ad and status == "Active":
                tomb = tomb + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    tomb_x = tomb_x + 1

            if "bubble" in ad and status == "Active":
                bubble = bubble + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    bubble_x = bubble_x + 1

            if "snow" in ad and status == "Active":
                snow = snow + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    snow_x = snow_x + 1

            if ("ping pong" in ad or "ping " in ad) and status == "Active":
                ping = ping + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    ping_x = ping_x + 1

            if ("dash" in ad or "heroic" in ad) and status == "Active":
                dash = dash + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    dash_x = dash_x + 1

            if ("hoophop" in ad or "hoop hop" in ad or " hop" in ad or " hoop" in ad) and status == "Active":
                hoophop = hoophop + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    hoophop_x = hoophop_x + 1

            if "candy" in ad and status == "Active":
                candy = candy + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    candy_x = candy_x + 1

            if ("shark" in ad or "enova" in ad) and status == "Active":
                shark = shark + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    shark_x = shark_x + 1

            if "deen" in ad and status == "Active":
                deen = deen + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    deen_x = deen_x + 1

            if "water" in ad and status == "Active":
                water = water + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    water_x = water_x + 1

            if "word" in ad and status == "Active":
                word = word + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    word_x = word_x + 1

            if "quizbd" in ad and status == "Active":
                quizbd = quizbd + 1
                if cpc > 40 and float(cost) > 500: #"quizgiri" in ad and status == "Active":
                    quizbd_x = quizbd_x + 1

    l_ratio.append(["Tiktok:", date_x, " ", " " ])
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


