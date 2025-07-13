

import my_methods_csv as mm


if __name__ == "__main__":

    path_raw_read = r"D:\DOC_2024\Ad_cost_daily\Mar_24\mar_1_10"
    path_read = mm.path_edit(path_raw_read)
    dir_list = mm.os.listdir(path_read)

    path_raw_write = r"D:\DOC_2024\Ad_cost_daily\Mar_24\mar_1_10"
    path_write = mm.path_edit(path_raw_write)

    tag_start = "Nagorik-"
    tag_mid = "-Ad-Account-"
    tag_null = ")"
    tag_result = "actions:offsite_conversion"
    #tag_date = "-8-Jun-20248-Jun-2024"
    usd = 126.00

    date = "10"
    month = "Mar"
    year = "2024"
    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year
    
    file_to_write = "ad_count_google"
    u_tag = "Campaign report Mar 1_10"

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

    l_hoophop = []
    l_candy = []

    l_shark = []


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
    heroic	=	0
    hoophop     =       0
    candy       =       0
    shark = 0


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

##    for x in dir_list:
##        if ".csv" in x and ")" not in x and tag_null not in x and tag_date in x:
##            a = path_read + "//" + x
##            l.append([a])

    for x in dir_list:
        if u_tag in x:
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
            conversion = data[row][22]
                
            cost_per_participated_in_app_action = data[row][23]


            if "shera" in campaign and cost > 0:
                shera=shera+1
                l_shera.append([ impression, cost, conversion ])
                    

            if ("tukhor" in campaign or "tukhr" in campaign) and cost > 0:
                tukhor=tukhor+1
                l_tukhor.append([ impression, cost, conversion ])
                    

            if "medha" in campaign and cost > 0:
                medha=medha+1
                l_medha.append([ impression, cost, conversion ])
                    

            if "tota" in campaign and cost > 0:
                tota=tota+1
                l_tota.append([ impression, cost, conversion ])
                    

            if ("quizgiri" in campaign or "quiz giri" in campaign or "qg" in campaign ) and cost > 0: # and tag_result in campaign_type and cost > 0:
                quizgiri=quizgiri+1
                l_quizgiri.append([ impression, cost, conversion ])
                    

            if ("quize" in campaign or "quizee" in campaign ) and cost > 0: # and tag_result in campaign_type and cost > 0:
                quizee=quizee+1
                l_quizee.append([ impression, cost, conversion ])
                    
                
            if "jeeto" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                jeeto=jeeto+1
                l_jeeto.append([ impression, cost, conversion ])
                    

            if ("quizchamp" in campaign or "quizmind" in campaign or "quiztime" in campaign or "qc" in campaign or "qm" in campaign or "qt" in campaign or "quiz champ" in campaign or "quiz mind" in campaign or "quiz time" in campaign) and cost > 0:
                quizchamp=quizchamp+1
                l_quizchamp.append([ impression, cost, conversion ])


            if "tetris" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                tetris=tetris+1
                l_tetris.append([ impression, cost, conversion ])
                    

            if "npuzzle" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                npuzzle=npuzzle+1
                l_npuzzle.append([ impression, cost, conversion ])
                    

            if "gotham" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                gotham=gotham+1
                l_gotham.append([ impression, cost, conversion ])
                    

            if "surfing" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                surfing=surfing+1
                l_surfing.append([ impression, cost, conversion ])
                    

            if "panda" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                panda=panda+1
                l_panda.append([ impression, cost, conversion ])
                    

            if "space" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                space=space+1
                l_space.append([ impression, cost, conversion ])
                    

            if "rise" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                rise=rise+1
                l_rise.append([ impression, cost, conversion ])
                    

            if "super runner" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                runner=runner+1
                l_runner.append([ impression, cost, conversion ])
                    

            if "ninja" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                ninja=ninja+1
                l_ninja.append([ impression, cost, conversion ])
                    

            if ("circle pong" in campaign) and cost > 0: # or "c.pong" in campaign) and tag_result in campaign_type and cost > 0:
                pong=pong+1
                l_pong.append([ impression, cost, conversion ])
                    

            if "samurai" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                samurai=samurai+1
                l_samurai.append([ impression, cost, conversion ])
                
#
            if "ortho" in campaign and cost > 0:
                ortho=ortho+1
                l_ortho.append([ impression, cost, conversion ])
                    
            if "ludo" in campaign and cost > 0:
                ludo=ludo+1
                l_ludo.append([ impression, cost, conversion ])

            if "dana" in campaign or "quizpro" in campaign  or "quiz pro" in campaign or "valene" in campaign or "valane" in campaign and cost > 0:
                dana=dana+1
                l_dana.append([ impression, cost, conversion ])

            if "ghoori" in campaign and cost > 0:
                ghoori=ghoori+1
                l_ghoori.append([ impression, cost, conversion ])
                
#
            if "tomb" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                tomb=tomb+1
                l_tomb_runner.append([ impression, cost, conversion ])

            if "bubble" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                bubble=bubble+1
                l_bubble.append([ impression, cost, conversion ])

            if "snow" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                snow=snow+1
                l_snow_surfer.append([ impression, cost, conversion ])

            if "ping pong" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                ping=ping+1
                l_ping_pong.append([ impression, cost, conversion ])

            if "dash" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                heroic=heroic+1
                l_dash.append([ impression, cost, conversion ])

            if "heroic" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                heroic=heroic+1
                l_dash.append([ impression, cost, conversion ])

            if "hop" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                hoophop=hoophop+1
                l_hoophop.append([ impression, cost, conversion ])

            if "candy" in campaign and cost > 0: #and tag_result in campaign_type and cost > 0:
                candy=candy+1
                l_candy.append([ impression, cost, conversion ])

            if "shark" in campaign and cost > 0: # and tag_result in campaign_type and cost > 0:
                shark=shark+1
                l_shark.append([ impression, cost, conversion ])

    # [ result > 0, reach > 1, impressions > 2, amount_spent > 3 ]


##    cost_shera = mm.sum_list_array_n(l_shera,1)
##    cost_tukhor = mm.sum_list_array_n(l_tukhor,1)
##    cost_medha = mm.sum_list_array_n(l_medha,1)
##    cost_tota = mm.sum_list_array_n(l_tota,1)
##    cost_quizgiri = mm.sum_list_array_n(l_quizgiri,1)
##    cost_quizee = mm.sum_list_array_n(l_quizee,1)
##    cost_jeeto = mm.sum_list_array_n(l_jeeto,1)
##    cost_quizchamp = mm.sum_list_array_n(l_quizchamp,1)
##    cost_tetris = mm.sum_list_array_n(l_tetris,1)
##    cost_npuzzle = mm.sum_list_array_n(l_npuzzle,1)
##    cost_gotham = mm.sum_list_array_n(l_gotham,1)
##    cost_surfing = mm.sum_list_array_n(l_surfing,1)
##    cost_panda = mm.sum_list_array_n(l_panda,1)
##    cost_space = mm.sum_list_array_n(l_space,1)
##    cost_rise = mm.sum_list_array_n(l_rise,1)
##    cost_runner = mm.sum_list_array_n(l_runner,1)
##    cost_ninja = mm.sum_list_array_n(l_ninja,1)
##    cost_pong = mm.sum_list_array_n(l_pong,1)
##    cost_samurai = mm.sum_list_array_n(l_samurai,1)    
##    cost_ortho = mm.sum_list_array_n(l_ortho,1)
##    cost_ludo = mm.sum_list_array_n(l_ludo,1)
##    cost_dana = mm.sum_list_array_n(l_dana,1)
##    cost_ghoori = mm.sum_list_array_n(l_ghoori,1)
##    cost_tomb = mm.sum_list_array_n(l_tomb_runner,1)
##    cost_bubble = mm.sum_list_array_n(l_bubble,1)
##    cost_snow = mm.sum_list_array_n(l_snow_surfer,1)
##    cost_ping = mm.sum_list_array_n(l_ping_pong,1)
##    cost_dash = mm.sum_list_array_n(l_dash,1)
##    cost_hop = mm.sum_list_array_n(l_hoophop,1)
##    cost_candy = mm.sum_list_array_n(l_candy,1)
##    cost_shark = mm.sum_list_array_n(l_shark,1)
##    
##    conversion_shera = mm.sum_list_array_n(l_shera,2)
##    conversion_tukhor = mm.sum_list_array_n(l_tukhor,2)
##    conversion_medha = mm.sum_list_array_n(l_medha,2)
##    conversion_tota = mm.sum_list_array_n(l_tota,2)
##    conversion_quizgiri = mm.sum_list_array_n(l_quizgiri,2)
##    conversion_quizee = mm.sum_list_array_n(l_quizee,2)
##    conversion_jeeto = mm.sum_list_array_n(l_jeeto,2)
##    conversion_quizchamp = mm.sum_list_array_n(l_quizchamp,2)
##    conversion_tetris = mm.sum_list_array_n(l_tetris,2)
##    conversion_npuzzle = mm.sum_list_array_n(l_npuzzle,2)
##    conversion_gotham = mm.sum_list_array_n(l_gotham,2)
##    conversion_surfing = mm.sum_list_array_n(l_surfing,2)
##    conversion_panda = mm.sum_list_array_n(l_panda,2)
##    conversion_space = mm.sum_list_array_n(l_space,2)
##    conversion_rise = mm.sum_list_array_n(l_rise,2)
##    conversion_runner = mm.sum_list_array_n(l_runner,2)
##    conversion_ninja = mm.sum_list_array_n(l_ninja,2)
##    conversion_pong = mm.sum_list_array_n(l_pong,2)
##    conversion_samurai = mm.sum_list_array_n(l_samurai,2)    
##    conversion_ortho = mm.sum_list_array_n(l_ortho,2)
##    conversion_ludo = mm.sum_list_array_n(l_ludo,2)
##    conversion_dana = mm.sum_list_array_n(l_dana,2)
##    conversion_ghoori = mm.sum_list_array_n(l_ghoori,2)
##    conversion_tomb = mm.sum_list_array_n(l_tomb_runner,2)
##    conversion_bubble = mm.sum_list_array_n(l_bubble,2)
##    conversion_snow = mm.sum_list_array_n(l_snow_surfer,2)
##    conversion_ping = mm.sum_list_array_n(l_ping_pong,2)
##    conversion_dash = mm.sum_list_array_n(l_dash,2)
##    conversion_hop = mm.sum_list_array_n(l_hoophop,2)
##    conversion_candy = mm.sum_list_array_n(l_candy,2)
##    conversion_shark = mm.sum_list_array_n(l_shark,2)
##
##
##    cpc_shera  = mm.ratio_list_array_n( l_shera,1,2 )
##    cpc_tukhor  = mm.ratio_list_array_n( l_tukhor,1,2 )
##    cpc_medha  = mm.ratio_list_array_n( l_medha,1,2 )
##    cpc_tota  = mm.ratio_list_array_n( l_tota,1,2 )
##    cpc_quizgiri  = mm.ratio_list_array_n( l_quizgiri,1,2 )
##    cpc_quizee  = mm.ratio_list_array_n( l_quizee,1,2 )
##    cpc_jeeto  = mm.ratio_list_array_n( l_jeeto,1,2 )
##    cpc_quizchamp  = mm.ratio_list_array_n( l_quizchamp,1,2 )
##    cpc_tetris  = mm.ratio_list_array_n( l_tetris,1,2 )
##    cpc_npuzzle  = mm.ratio_list_array_n( l_npuzzle,1,2 )
##    cpc_gotham  = mm.ratio_list_array_n( l_gotham,1,2 )
##    cpc_surfing  = mm.ratio_list_array_n( l_surfing,1,2 )
##    cpc_panda  = mm.ratio_list_array_n( l_panda,1,2 )
##    cpc_space  = mm.ratio_list_array_n( l_space,1,2 )
##    cpc_rise  = mm.ratio_list_array_n( l_rise,1,2 )
##    cpc_runner  = mm.ratio_list_array_n( l_runner,1,2 )
##    cpc_ninja  = mm.ratio_list_array_n( l_ninja,1,2 )
##    cpc_pong  = mm.ratio_list_array_n( l_pong,1,2 )
##    cpc_samurai  = mm.ratio_list_array_n( l_samurai,1,2 )    
##    cpc_ortho = mm.ratio_list_array_n(l_ortho,1,2)
##    cpc_ludo = mm.ratio_list_array_n(l_ludo,1,2)
##    cpc_dana = mm.ratio_list_array_n(l_dana,1,2)
##    cpc_ghoori = mm.ratio_list_array_n(l_ghoori,1,2)
##    cpc_tomb = mm.ratio_list_array_n(l_tomb_runner,1,2)
##    cpc_bubble = mm.ratio_list_array_n(l_bubble,1,2)
##    cpc_snow = mm.ratio_list_array_n(l_snow_surfer,1,2)
##    cpc_ping = mm.ratio_list_array_n(l_ping_pong,1,2)
##    cpc_dash = mm.ratio_list_array_n(l_dash,1,2)
##    cpc_hop = mm.ratio_list_array_n(l_hoophop,1,2)
##    cpc_candy = mm.ratio_list_array_n(l_candy,1,2)
##    cpc_shark = mm.ratio_list_array_n(l_shark,1,2)
##
##
##    icr_shera  = mm.ratio_list_array_n( l_shera,0,1 )
##    icr_tukhor  = mm.ratio_list_array_n( l_tukhor,0,1 )
##    icr_medha  = mm.ratio_list_array_n( l_medha,0,1 )
##    icr_tota  = mm.ratio_list_array_n( l_tota,0,1 )
##    icr_quizgiri  = mm.ratio_list_array_n( l_quizgiri,0,1 )
##    icr_quizee  = mm.ratio_list_array_n( l_quizee,0,1 )
##    icr_jeeto  = mm.ratio_list_array_n( l_jeeto,0,1 )
##    icr_quizchamp  = mm.ratio_list_array_n( l_quizchamp,0,1 )
##    icr_tetris  = mm.ratio_list_array_n( l_tetris,0,1 )
##    icr_npuzzle  = mm.ratio_list_array_n( l_npuzzle,0,1 )
##    icr_gotham  = mm.ratio_list_array_n( l_gotham,0,1 )
##    icr_surfing  = mm.ratio_list_array_n( l_surfing,0,1 )
##    icr_panda  = mm.ratio_list_array_n( l_panda,0,1 )
##    icr_space  = mm.ratio_list_array_n( l_space,0,1 )
##    icr_rise  = mm.ratio_list_array_n( l_rise,0,1 )
##    icr_runner  = mm.ratio_list_array_n( l_runner,0,1 )
##    icr_ninja  = mm.ratio_list_array_n( l_ninja,0,1 )
##    icr_pong  = mm.ratio_list_array_n( l_pong,0,1 )
##    icr_samurai  = mm.ratio_list_array_n( l_samurai,0,1 )
##    icr_ortho   = mm.ratio_list_array_n( l_ortho ,0,1 )
##    icr_ludo   = mm.ratio_list_array_n( l_ludo ,0,1 )
##    icr_dana   = mm.ratio_list_array_n( l_dana ,0,1 )
##    icr_ghoori   = mm.ratio_list_array_n( l_ghoori ,0,1 )
##    icr_tomb   = mm.ratio_list_array_n( l_tomb_runner ,0,1 )
##    icr_bubble   = mm.ratio_list_array_n( l_bubble ,0,1 )
##    icr_snow   = mm.ratio_list_array_n( l_snow_surfer ,0,1 )
##    icr_ping   = mm.ratio_list_array_n( l_ping_pong ,0,1 )
##    icr_dash   = mm.ratio_list_array_n( l_dash ,0,1 )
##    icr_hop   = mm.ratio_list_array_n( l_hoophop ,0,1 )
##    icr_candy   = mm.ratio_list_array_n( l_candy ,0,1 )
##    icr_shark   = mm.ratio_list_array_n( l_shark ,0,1 )
##
##    irr_shera  = mm.ratio_list_array_n( l_shera,0,2 )
##    irr_tukhor  = mm.ratio_list_array_n( l_tukhor,0,2 )
##    irr_medha  = mm.ratio_list_array_n( l_medha,0,2 )
##    irr_tota  = mm.ratio_list_array_n( l_tota,0,2 )
##    irr_quizgiri  = mm.ratio_list_array_n( l_quizgiri,0,2 )
##    irr_quizee  = mm.ratio_list_array_n( l_quizee,0,2 )
##    irr_jeeto  = mm.ratio_list_array_n( l_jeeto,0,2 )
##    irr_quizchamp  = mm.ratio_list_array_n( l_quizchamp,0,2 )
##    irr_tetris  = mm.ratio_list_array_n( l_tetris,0,2 )
##    irr_npuzzle  = mm.ratio_list_array_n( l_npuzzle,0,2 )
##    irr_gotham  = mm.ratio_list_array_n( l_gotham,0,2 )
##    irr_surfing  = mm.ratio_list_array_n( l_surfing,0,2 )
##    irr_panda  = mm.ratio_list_array_n( l_panda,0,2 )
##    irr_space  = mm.ratio_list_array_n( l_space,0,2 )
##    irr_rise  = mm.ratio_list_array_n( l_rise,0,2 )
##    irr_runner  = mm.ratio_list_array_n( l_runner,0,2 )
##    irr_ninja  = mm.ratio_list_array_n( l_ninja,0,2 )
##    irr_pong  = mm.ratio_list_array_n( l_pong,0,2 )
##    irr_samurai  = mm.ratio_list_array_n( l_samurai,0,2 )
##    irr_ortho   = mm.ratio_list_array_n( l_ortho ,0,2 )
##    irr_ludo   = mm.ratio_list_array_n( l_ludo ,0,2 )
##    irr_dana   = mm.ratio_list_array_n( l_dana ,0,2 )
##    irr_ghoori   = mm.ratio_list_array_n( l_ghoori ,0,2 )
##    irr_tomb   = mm.ratio_list_array_n( l_tomb_runner ,0,2 )
##    irr_bubble   = mm.ratio_list_array_n( l_bubble ,0,2 )
##    irr_snow   = mm.ratio_list_array_n( l_snow_surfer ,0,2 )
##    irr_ping   = mm.ratio_list_array_n( l_ping_pong ,0,2 )
##    irr_dash   = mm.ratio_list_array_n( l_dash ,0,2 )
##    irr_hop   = mm.ratio_list_array_n( l_hoophop ,0,2 )
##    irr_candy   = mm.ratio_list_array_n( l_candy ,0,2 )
##    irr_shark   = mm.ratio_list_array_n( l_shark ,0,2 )
##
##    print("")
##    l_ratio.append(["Google:", date_x, " ", " " ])
##    l_ratio.append(["Products", "Cost", "Conversion", "CPC", "ICR", "IRR"])
##    l_ratio.append(["Shera", cost_shera, conversion_shera, cpc_shera, icr_shera, irr_shera])
##    l_ratio.append(["Tukhor", cost_tukhor, conversion_tukhor, cpc_tukhor, icr_tukhor, irr_tukhor])
##    l_ratio.append(["Medha(Subs.)", cost_medha, conversion_medha, cpc_medha, icr_medha, irr_medha])
##    l_ratio.append(["Tota(Install)", cost_tota, conversion_tota, cpc_tota, icr_tota, irr_tota])
##    l_ratio.append(["Quizgiri", cost_quizgiri, conversion_quizgiri, cpc_quizgiri, icr_quizgiri, irr_quizgiri])
##    l_ratio.append(["Quizee", cost_quizee, conversion_quizee, cpc_quizee, icr_quizee, irr_quizee])
##    l_ratio.append(["Jeeto", cost_jeeto, conversion_jeeto, cpc_jeeto, icr_jeeto, irr_jeeto])
##    l_ratio.append(["QC + QM + QT", cost_quizchamp, conversion_quizchamp, cpc_quizchamp, icr_quizchamp, irr_quizchamp])
##    l_ratio.append(["Tetris", cost_tetris, conversion_tetris, cpc_tetris, icr_tetris, irr_tetris])
##    l_ratio.append(["Npuzzle", cost_npuzzle, conversion_npuzzle, cpc_npuzzle, icr_npuzzle, irr_npuzzle])
##    l_ratio.append(["Gotham", cost_gotham, conversion_gotham, cpc_gotham, icr_gotham, irr_gotham])
##    l_ratio.append(["Surfing", cost_surfing, conversion_surfing, cpc_surfing, icr_surfing, irr_surfing])
##    l_ratio.append(["Panda", cost_panda, conversion_panda, cpc_panda, icr_panda, irr_panda])
##    l_ratio.append(["Space", cost_space, conversion_space, cpc_space, icr_space, irr_space])
##    l_ratio.append(["Rise", cost_rise, conversion_rise, cpc_rise, icr_rise, irr_rise])
##    l_ratio.append(["Runner", cost_runner, conversion_runner, cpc_runner, icr_runner, irr_runner])
##    l_ratio.append(["Ninja", cost_ninja, conversion_ninja, cpc_ninja, icr_ninja, irr_ninja])
##    l_ratio.append(["Pong", cost_pong, conversion_pong, cpc_pong, icr_pong, irr_pong])
##    l_ratio.append(["Samurai", cost_samurai, conversion_samurai, cpc_samurai, icr_samurai, irr_samurai])
##    l_ratio.append(["Ortho(Install)", cost_ortho, conversion_ortho, cpc_ortho, icr_ortho, irr_ortho])
##    l_ratio.append(["Ludo(Install)", cost_ludo, conversion_ludo, cpc_ludo, icr_ludo, irr_ludo])
##    l_ratio.append(["Dana(Install)", cost_dana, conversion_dana, cpc_dana, icr_dana, irr_dana])
##    l_ratio.append(["Ghoori", cost_ghoori, conversion_ghoori, cpc_ghoori, icr_ghoori, irr_ghoori])
##
##    l_ratio.append(["Tomb Runner", cost_tomb, conversion_tomb, cpc_tomb, icr_tomb, irr_tomb])
##    l_ratio.append(["Bubble", cost_bubble, conversion_bubble, cpc_bubble, icr_bubble, irr_bubble])
##    l_ratio.append(["Snow Surfer", cost_snow, conversion_snow, cpc_snow, icr_snow, irr_snow])
##    l_ratio.append(["P. Pong", cost_ping, conversion_ping, cpc_ping, icr_ping, irr_ping])
##    l_ratio.append(["S.S Dash", cost_dash, conversion_dash, cpc_dash, icr_dash, irr_dash])
##
##    l_ratio.append(["Hoophop", cost_hop, conversion_hop, cpc_hop, icr_hop, irr_hop])
##    l_ratio.append(["Sweet Candy", cost_candy, conversion_candy, cpc_candy, icr_candy, irr_candy])
##    l_ratio.append(["Shark VPN (Install)", cost_shark, conversion_shark, cpc_shark, icr_shark, irr_shark])
##
##
##    w_file_ratio = "google_ad_performance_" + year + "_" + month + "_" + date + ".csv"
##    w_path_ratio = path_write + "//" + w_file_ratio
##    mm.write_list( w_path_ratio, l_ratio)

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
    l_ratio.append([ "Dash", heroic, dash_x ])
    l_ratio.append([ "Hoophop", hoophop, dash_x ])
    l_ratio.append([ "Candy", candy, dash_x ])


    w_file_ratio = file_to_write + year + "_" + month + "_" + date + ".csv"
    w_path_ratio = path_write + "//" + w_file_ratio
    mm.write_list( w_path_ratio, l_ratio)

