

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

    date = "10"
    month = "Mar"
    year = "2024"
    tag_date = "-" + date + "-" + month + "-" + year + date + "-" + month + "-" + year
    date_x = date + " " + month + "," + " " + year
    
    file_to_write = "ad_count_"
    u_tag = "-Ads-1-Mar-202410-Mar-2024.csv"

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
            quality_ranking = data[row][16]
            engagement_rate_ranking = data[row][17]
            conversion_rate_ranking = data[row][18]
            
            amount_spent = data[row][19]
            ends = data[row][20]


            if "shera" in ad and len(amount_spent) > 0:
                shera=shera+1
                l_shera.append([ result, reach, impressions, amount_spent ])

            if ("tukhor" in ad or "tukhr" in ad) and len(amount_spent) > 0:
                tukhor=tukhor+1
                l_tukhor.append([ result, reach, impressions, amount_spent ])

            if "medha" in ad and len(amount_spent) > 0:
                medha=medha+1
                l_medha.append([ result, reach, impressions, amount_spent ])

            if ("tota" in ad and "total" not in ad) and len(amount_spent) > 0:
                tota=tota+1
                l_tota.append([ result, reach, impressions, amount_spent ])

            if ("quizgiri" in ad or "qg" in ad or "quiz giri" in ad) and len(amount_spent) > 0:
                quizgiri=quizgiri+1
                l_quizgiri.append([ result, reach, impressions, amount_spent ])

            if ("quize" in ad or "quizee" in ad ) and len(amount_spent) > 0:
                quizee=quizee+1
                l_quizee.append([ result, reach, impressions, amount_spent ])
                #print(amount_spent)

            if "jeeto" in ad and len(amount_spent) > 0:
                jeeto=jeeto+1
                l_jeeto.append([ result, reach, impressions, amount_spent ])

            if ("quizchamp" in ad or "quizmind" in ad or "quiztime" in ad or "qc" in ad or "qm" in ad or "qt" in ad or "quiz champ" in ad or "quiz mind" in ad or "quiz time" in ad) and len(amount_spent) > 0:
                quizchamp=quizchamp+1
                l_quizchamp.append([ result, reach, impressions, amount_spent ])
                

            if "tetris" in ad and len(amount_spent) > 0:
                tetris=tetris+1
                l_tetris.append([ result, reach, impressions, amount_spent ])

            if "npuzzle" in ad and len(amount_spent) > 0:
                npuzzle=npuzzle+1
                l_npuzzle.append([ result, reach, impressions, amount_spent ])

            if "gotham" in ad and len(amount_spent) > 0:
                gotham=gotham+1
                l_gotham.append([ result, reach, impressions, amount_spent ])
                
            if "surfing" in ad and len(amount_spent) > 0:
                surfing=surfing+1
                l_surfing.append([ result, reach, impressions, amount_spent ])

            if "panda" in ad and len(amount_spent) > 0:
                panda=panda+1
                l_panda.append([ result, reach, impressions, amount_spent ])

            if "space" in ad and len(amount_spent) > 0:
                space=space+1
                l_space.append([ result, reach, impressions, amount_spent ])

            if "rise" in ad and len(amount_spent) > 0:
                rise=rise+1
                l_rise.append([ result, reach, impressions, amount_spent ])

            if "super runner" in ad and len(amount_spent) > 0 and len(amount_spent) > 0:
                runner=runner+1
                l_runner.append([ result, reach, impressions, amount_spent ])

            if "ninja" in ad and len(amount_spent) > 0:
                ninja=ninja+1
                l_ninja.append([ result, reach, impressions, amount_spent ])

            if ("circle pong" in ad or "c.pong" in ad) and len(amount_spent) > 0:
                pong=pong+1
                l_pong.append([ result, reach, impressions, amount_spent ])

            if "samurai" in ad and tag_result in result_indicator and len(amount_spent) > 0:
                samurai=samurai+1
                l_samurai.append([ result, reach, impressions, amount_spent ])
#
            if "ortho" in ad and len(amount_spent) > 0:
                ortho=ortho+1
                l_ortho.append([ result, reach, impressions, amount_spent ])
                    
            if "ludo" in ad and len(amount_spent) > 0:
                ludo=ludo+1
                l_ludo.append([ result, reach, impressions, amount_spent ])

            if "dana" in ad or "quizpro" in ad  or "quiz pro" in ad or "valene" in ad or "valane" in ad and len(amount_spent) > 0:
                dana=dana+1
                l_dana.append([ result, reach, impressions, amount_spent ])

            if "ghoori" in ad and len(amount_spent) > 0:
                ghoori=ghoori+1
                l_ghoori.append([ result, reach, impressions, amount_spent ])

#
            if "tomb" in ad and len(amount_spent) > 0:
                tomb=tomb+1
                l_tomb_runner.append([ result, reach, impressions, amount_spent ])

            if "bubble" in ad and len(amount_spent) > 0:
                bubble=bubble+1
                l_bubble.append([ result, reach, impressions, amount_spent ])

            if "snow" in ad and len(amount_spent) > 0:
                snow=snow+1
                l_snow_surfer.append([ result, reach, impressions, amount_spent ])

            if "ping pong" in ad and len(amount_spent) > 0:
                ping=ping+1
                l_ping_pong.append([ result, reach, impressions, amount_spent ])

            if "dash" in ad and len(amount_spent) > 0:
                heroic=heroic+1
                l_dash.append([ result, reach, impressions, amount_spent ])

            if "heroic" in ad and len(amount_spent) > 0:
                heroic=heroic+1
                l_dash.append([ result, reach, impressions, amount_spent ])

            if "hop" in ad and len(amount_spent) > 0:
                hoophop=hoophop+1
                l_hoophop.append([ result, reach, impressions, amount_spent ])
            
            if "candy" in ad and len(amount_spent) > 0:
                candy=candy+1

                l_candy.append([ result, reach, impressions, amount_spent ])

            if "shark" in ad and len(amount_spent) > 0:
                shark=shark+1
                l_shark.append([ result, reach, impressions, amount_spent ])

    # [ result > 0, reach > 1, impressions > 2, amount_spent > 3 ]


    cost_shera = mm.sum_list_array_n(l_shera,3)
    cost_tukhor = mm.sum_list_array_n(l_tukhor,3)
    cost_medha = mm.sum_list_array_n(l_medha,3)
    cost_tota = mm.sum_list_array_n(l_tota,3)
    cost_quizgiri = mm.sum_list_array_n(l_quizgiri,3)
    cost_quizee = mm.sum_list_array_n(l_quizee,3)
    cost_jeeto = mm.sum_list_array_n(l_jeeto,3)
    cost_quizchamp = mm.sum_list_array_n(l_quizchamp,3)
    cost_tetris = mm.sum_list_array_n(l_tetris,3)
    cost_npuzzle = mm.sum_list_array_n(l_npuzzle,3)
    cost_gotham = mm.sum_list_array_n(l_gotham,3)
    cost_surfing = mm.sum_list_array_n(l_surfing,3)
    cost_panda = mm.sum_list_array_n(l_panda,3)
    cost_space = mm.sum_list_array_n(l_space,3)
    cost_rise = mm.sum_list_array_n(l_rise,3)
    cost_runner = mm.sum_list_array_n(l_runner,3)
    cost_ninja = mm.sum_list_array_n(l_ninja,3)
    cost_pong = mm.sum_list_array_n(l_pong,3)
    cost_samurai = mm.sum_list_array_n(l_samurai,3)    
    cost_ortho = mm.sum_list_array_n(l_ortho,3)
    cost_ludo = mm.sum_list_array_n(l_ludo,3)
    cost_dana = mm.sum_list_array_n(l_dana,3)
    cost_ghoori = mm.sum_list_array_n(l_ghoori,3)
    cost_tomb = mm.sum_list_array_n(l_tomb_runner,3)
    cost_bubble = mm.sum_list_array_n(l_bubble,3)
    cost_snow = mm.sum_list_array_n(l_snow_surfer,3)
    cost_ping = mm.sum_list_array_n(l_ping_pong,3)
    cost_dash = mm.sum_list_array_n(l_dash,3)
    cost_hop = mm.sum_list_array_n(l_hoophop,3)
    cost_candy = mm.sum_list_array_n(l_candy,3)
    cost_shark = mm.sum_list_array_n(l_shark,3)

    
    conversion_shera = mm.sum_list_array_n(l_shera,0)
    conversion_tukhor = mm.sum_list_array_n(l_tukhor,0)
    conversion_medha = mm.sum_list_array_n(l_medha,0)
    conversion_tota = mm.sum_list_array_n(l_tota,0)
    conversion_quizgiri = mm.sum_list_array_n(l_quizgiri,0)
    conversion_quizee = mm.sum_list_array_n(l_quizee,0)
    conversion_jeeto = mm.sum_list_array_n(l_jeeto,0)
    conversion_quizchamp = mm.sum_list_array_n(l_quizchamp,0)
    conversion_tetris = mm.sum_list_array_n(l_tetris,0)
    conversion_npuzzle = mm.sum_list_array_n(l_npuzzle,0)
    conversion_gotham = mm.sum_list_array_n(l_gotham,0)
    conversion_surfing = mm.sum_list_array_n(l_surfing,0)
    conversion_panda = mm.sum_list_array_n(l_panda,0)
    conversion_space = mm.sum_list_array_n(l_space,0)
    conversion_rise = mm.sum_list_array_n(l_rise,0)
    conversion_runner = mm.sum_list_array_n(l_runner,0)
    conversion_ninja = mm.sum_list_array_n(l_ninja,0)
    conversion_pong = mm.sum_list_array_n(l_pong,0)
    conversion_samurai = mm.sum_list_array_n(l_samurai,0)    
    conversion_ortho = mm.sum_list_array_n(l_ortho,0)
    conversion_ludo = mm.sum_list_array_n(l_ludo,0)
    conversion_dana = mm.sum_list_array_n(l_dana,0)
    conversion_ghoori = mm.sum_list_array_n(l_ghoori,0)
    conversion_tomb = mm.sum_list_array_n(l_tomb_runner,0)
    conversion_bubble = mm.sum_list_array_n(l_bubble,0)
    conversion_snow = mm.sum_list_array_n(l_snow_surfer,0)
    conversion_ping = mm.sum_list_array_n(l_ping_pong,0)
    conversion_dash = mm.sum_list_array_n(l_dash,0)
    conversion_hop = mm.sum_list_array_n(l_hoophop,0)
    conversion_candy = mm.sum_list_array_n(l_candy,0)
    conversion_shark = mm.sum_list_array_n(l_shark,0)
    

    cpc_shera  = mm.ratio_list_array_n( l_shera,3,0 )
    cpc_tukhor  = mm.ratio_list_array_n( l_tukhor,3,0 )
    cpc_medha  = mm.ratio_list_array_n( l_medha,3,0 )
    cpc_tota  = mm.ratio_list_array_n( l_tota,3,0 )
    cpc_quizgiri  = mm.ratio_list_array_n( l_quizgiri,3,0 )
    cpc_quizee  = mm.ratio_list_array_n( l_quizee,3,0 )
    cpc_jeeto  = mm.ratio_list_array_n( l_jeeto,3,0 )
    cpc_quizchamp  = mm.ratio_list_array_n( l_quizchamp,3,0 )
    cpc_tetris  = mm.ratio_list_array_n( l_tetris,3,0 )
    cpc_npuzzle  = mm.ratio_list_array_n( l_npuzzle,3,0 )
    cpc_gotham  = mm.ratio_list_array_n( l_gotham,3,0 )
    cpc_surfing  = mm.ratio_list_array_n( l_surfing,3,0 )
    cpc_panda  = mm.ratio_list_array_n( l_panda,3,0 )
    cpc_space  = mm.ratio_list_array_n( l_space,3,0 )
    cpc_rise  = mm.ratio_list_array_n( l_rise,3,0 )
    cpc_runner  = mm.ratio_list_array_n( l_runner,3,0 )
    cpc_ninja  = mm.ratio_list_array_n( l_ninja,3,0 )
    cpc_pong  = mm.ratio_list_array_n( l_pong,3,0 )
    cpc_samurai  = mm.ratio_list_array_n( l_samurai,3,0 )    
    cpc_ortho = mm.ratio_list_array_n(l_ortho,3,0)
    cpc_ludo = mm.ratio_list_array_n(l_ludo,3,0)
    cpc_dana = mm.ratio_list_array_n(l_dana,3,0)
    cpc_ghoori = mm.ratio_list_array_n(l_ghoori,3,0)
    cpc_tomb = mm.ratio_list_array_n(l_tomb_runner,3,0)
    cpc_bubble = mm.ratio_list_array_n(l_bubble,3,0)
    cpc_snow = mm.ratio_list_array_n(l_snow_surfer,3,0)
    cpc_ping = mm.ratio_list_array_n(l_ping_pong,3,0)
    cpc_dash = mm.ratio_list_array_n(l_dash,3,0)
    cpc_hop = mm.ratio_list_array_n(l_hoophop,3,0)
    cpc_candy = mm.ratio_list_array_n(l_candy,3,0)
    cpc_shark = mm.ratio_list_array_n(l_shark,3,0)

    icr_shera  = mm.ratio_list_array_n( l_shera,2,3 )
    icr_tukhor  = mm.ratio_list_array_n( l_tukhor,2,3 )
    icr_medha  = mm.ratio_list_array_n( l_medha,2,3 )
    icr_tota  = mm.ratio_list_array_n( l_tota,2,3 )
    icr_quizgiri  = mm.ratio_list_array_n( l_quizgiri,2,3 )
    icr_quizee  = mm.ratio_list_array_n( l_quizee,2,3 )
    icr_jeeto  = mm.ratio_list_array_n( l_jeeto,2,3 )
    icr_quizchamp  = mm.ratio_list_array_n( l_quizchamp,2,3 )
    icr_tetris  = mm.ratio_list_array_n( l_tetris,2,3 )
    icr_npuzzle  = mm.ratio_list_array_n( l_npuzzle,2,3 )
    icr_gotham  = mm.ratio_list_array_n( l_gotham,2,3 )
    icr_surfing  = mm.ratio_list_array_n( l_surfing,2,3 )
    icr_panda  = mm.ratio_list_array_n( l_panda,2,3 )
    icr_space  = mm.ratio_list_array_n( l_space,2,3 )
    icr_rise  = mm.ratio_list_array_n( l_rise,2,3 )
    icr_runner  = mm.ratio_list_array_n( l_runner,2,3 )
    icr_ninja  = mm.ratio_list_array_n( l_ninja,2,3 )
    icr_pong  = mm.ratio_list_array_n( l_pong,2,3 )
    icr_samurai  = mm.ratio_list_array_n( l_samurai,2,3 )
    icr_ortho   = mm.ratio_list_array_n( l_ortho ,2,3 )
    icr_ludo   = mm.ratio_list_array_n( l_ludo ,2,3 )
    icr_dana   = mm.ratio_list_array_n( l_dana ,2,3 )
    icr_ghoori   = mm.ratio_list_array_n( l_ghoori ,2,3 )
    icr_tomb   = mm.ratio_list_array_n( l_tomb_runner ,2,3 )
    icr_bubble   = mm.ratio_list_array_n( l_bubble ,2,3 )
    icr_snow   = mm.ratio_list_array_n( l_snow_surfer ,2,3 )
    icr_ping   = mm.ratio_list_array_n( l_ping_pong ,2,3 )
    icr_dash   = mm.ratio_list_array_n( l_dash ,2,3 )
    icr_hop   = mm.ratio_list_array_n( l_hoophop ,2,3 )
    icr_candy   = mm.ratio_list_array_n( l_candy ,2,3 )
    icr_shark   = mm.ratio_list_array_n( l_shark ,2,3 )
    
    irr_shera  = mm.ratio_list_array_n( l_shera,2,0 )
    irr_tukhor  = mm.ratio_list_array_n( l_tukhor,2,0 )
    irr_medha  = mm.ratio_list_array_n( l_medha,2,0 )
    irr_tota  = mm.ratio_list_array_n( l_tota,2,0 )
    irr_quizgiri  = mm.ratio_list_array_n( l_quizgiri,2,0 )
    irr_quizee  = mm.ratio_list_array_n( l_quizee,2,0 )
    irr_jeeto  = mm.ratio_list_array_n( l_jeeto,2,0 )
    irr_quizchamp  = mm.ratio_list_array_n( l_quizchamp,2,0 )
    irr_tetris  = mm.ratio_list_array_n( l_tetris,2,0 )
    irr_npuzzle  = mm.ratio_list_array_n( l_npuzzle,2,0 )
    irr_gotham  = mm.ratio_list_array_n( l_gotham,2,0 )
    irr_surfing  = mm.ratio_list_array_n( l_surfing,2,0 )
    irr_panda  = mm.ratio_list_array_n( l_panda,2,0 )
    irr_space  = mm.ratio_list_array_n( l_space,2,0 )
    irr_rise  = mm.ratio_list_array_n( l_rise,2,0 )
    irr_runner  = mm.ratio_list_array_n( l_runner,2,0 )
    irr_ninja  = mm.ratio_list_array_n( l_ninja,2,0 )
    irr_pong  = mm.ratio_list_array_n( l_pong,2,0 )
    irr_samurai  = mm.ratio_list_array_n( l_samurai,2,0 )
    irr_ortho   = mm.ratio_list_array_n( l_ortho ,2,0 )
    irr_ludo   = mm.ratio_list_array_n( l_ludo ,2,0 )
    irr_dana   = mm.ratio_list_array_n( l_dana ,2,0 )
    irr_ghoori   = mm.ratio_list_array_n( l_ghoori ,2,0 )
    irr_tomb   = mm.ratio_list_array_n( l_tomb_runner ,2,0 )
    irr_bubble   = mm.ratio_list_array_n( l_bubble ,2,0 )
    irr_snow   = mm.ratio_list_array_n( l_snow_surfer ,2,0 )
    irr_ping   = mm.ratio_list_array_n( l_ping_pong ,2,0 )
    irr_dash   = mm.ratio_list_array_n( l_dash ,2,0 )
    irr_hop   = mm.ratio_list_array_n( l_hoophop ,2,0 )
    irr_candy   = mm.ratio_list_array_n( l_candy ,2,0 )
    irr_shark   = mm.ratio_list_array_n( l_shark ,2,0 )
    
##    print("")
##    l_ratio.append(["Meta:", date_x, " ", " " ])
##    l_ratio.append(["Products", "Cost", "Conversion", "CPC", "ICR", "IRR"])
##    l_ratio.append(["Shera", cost_shera, conversion_shera, cpc_shera, icr_shera, irr_shera])
##    l_ratio.append(["Tukhor", cost_tukhor, conversion_tukhor, cpc_tukhor, icr_tukhor, irr_tukhor])
##    l_ratio.append(["Medha(Subscription)", cost_medha, conversion_medha, cpc_medha, icr_medha, irr_medha])
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
##
##    l_ratio.append(["Tomb Runner", cost_tomb, conversion_tomb, cpc_tomb, icr_tomb, irr_tomb])
##    l_ratio.append(["Bubble", cost_bubble, conversion_bubble, cpc_bubble, icr_bubble, irr_bubble])
##    l_ratio.append(["Snow Surfer", cost_snow, conversion_snow, cpc_snow, icr_snow, irr_snow])
##    l_ratio.append(["P. Pong", cost_ping, conversion_ping, cpc_ping, icr_ping, irr_ping])
##    l_ratio.append(["S.S Dash", cost_dash, conversion_dash, cpc_dash, icr_dash, irr_dash])
##    l_ratio.append(["Hoophop", cost_hop, conversion_hop, cpc_hop, icr_hop, irr_hop])
##    l_ratio.append(["Sweet Candy", cost_candy, conversion_candy, cpc_candy, icr_candy, irr_candy])
##    l_ratio.append(["Shark VPN (Install)", cost_shark, conversion_shark, cpc_shark, icr_shark, irr_shark])

##    w_file_ratio = "meta_ad_performance_" + year + "_" + month + "_" + date + ".csv"
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

