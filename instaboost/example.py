#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol
#from src import ihm





bot = InstaBot(
    login="thefrenchie_stitch_",
    password="",
    like_per_day=1100,
    comments_per_day=380,
    tag_list=['like4like', 'l:213336744', 'l:212901056','follow4follow'], #l: for location, check example in readme.md
    tag_blacklist=['frenchbulldog', 'frenchie', 'frenchieoftheday', 'frenchie', 'frenchbull', 'fransebulldog', 'frenchiepuppy', 'dogsofinstagram', 'frenchiesgram', 'frenchbulldogsofinstagram', 'ilovemyfrenchie', 'petsagram', 'puppylove', 'bulldogsofinstagram', 'bulldog', 'frenchielife', 'frenchiesoftheworld', 'frenchiesofinstagram', 'frenchiegram', 'frenchielove', 'thefrenchiepost', 'instafrenchie', 'instadogs', 'frenchies1', 'cutepuppy', 'husky', 'corgi', 'corgination', 'pettravel', 'instadog', 'dogs_of_instagram', 'dogsofinstagram', 'dogoftheday', 'mydog', 'ilovemydog', 'pup', 'Beagle', 'Beagle', 'boxer', 'poodle', 'labradoodle', 'bostonterrier', 'pug', 'puggle', 'pitbull', 'akita', 'bloodhound', 'AustralianShepherd', 'greatdane', 'siberianhusky', 'miniatureschnauzer', 'shihtzu', 'frenchton', 'bostonterrier'],
    user_blacklist={'twxxyzz':"", 'jacosaur42':"", 'meganhaleynelson':"", 'hlinkhart':""},
    max_like_for_one_tag=40,
    follow_per_day=600,
    follow_time=12 * 60 * 60,
    unfollow_per_day=660,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[['SO MUCH CUTENESS! <3', '😍😍', 'OMG 😍😍', 'Awh 🐾🐾', 'SO CUTE 🐾', '😍😍🐾', '<3 🐾', '🐾 :)', '🐶🐾', 'So cute 🐶', '🐶😍', 'AWH 🐶', 'SOOOO MUCH CUTENESS! 🐶', 'Adorable :)', 'Adorable 🐶', 'Adorable 😍', 'Adorable 🐾', 'Too Cute 🐶😍','<3<3 SO MUCH CUTENESS!', '😍😍😍', '😍 OMG 😍', '🐾 Awh 🐾', '🐾 SOOO CUTE ', '😍🐾😍', '🐾 <3 ', '🐾 :)🐾', '🐾🐶', '🐶 Sooo cute', '🐶😍', 'AWH 🐶', 'SOOOOOOOO MUCH CUTENESS! 😍', '🐶 Adorable 🐶', '😍 Adorable ', '🐾 Adorable🐾', '😍 Too Cute 🐶', '😍 Awh, Too Cute', '🐾Awhhh🐾', 'omg Awhhh', 'Awhhhhhh', 'Awhhhhhh so cute', 'Awhhhhhh too cute', 'omg 🐾 Awhhh', '🐾 Awhhhhhh', '🐾 Awhhhhhh so cute', '🐾 Awhhhhhh too cute', '<3<3 Awhhhhhh too cute', '<3<3 Awhhhhh', '<3<3 too cute', '<3<3 so cute', 'cuteness overload!', 'Awh Pawsome :)', 'OMG... cuteness overload!', 'Awh... cuteness overload!', '🐶 cuteness overload!', '🐾 cuteness overload!', '<3  cuteness overload!', '😍', '😍😍<3<3', 'Way Too Cute!! :)', 'Such a cutie :)', 'Such a cutie <3', 'Such a cutie!' , '😍 Such a cutie!' , '🐾 Such a cutie!' , '🐾 Such a cutie! <3', 'Awhh such a cutie! <3', 'OMG such a cutie! <3', '🐶 Such a cutie! <3', 'The Cutest!', 'The Cutest :)', 'Such a sweetie', 'Such a sweetie :)', 'Such a sweetie <3', 'Such a sweetie!' , '😍 Such a sweetie!' , '🐾 Such a sweetie!' , '🐾 Such a sweetie! <3', 'Awhh such a sweetie! <3', 'OMG such a sweetie! <3', '🐶 Such a sweetie! <3', '😍 Too sweet 🐶', '😍 Awh, Too sweet', 'Awhhhhhh so sweet', 'Awhhhhhh too sweet', '🐾 Awhhhhhh so sweet', '🐾 Awhhhhhh too sweet', '<3<3 Awhhhhhh too sweet', '<3<3 too sweet', '<3<3 so sweet']],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['alina_savvchenko', 'devintyler_', 'savannahbrito', 'kevn_15', 'faithashlee', 'princessbodhi'],
    UI = False)



while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)
    if  bot.login_status == False:
        break

    if mode == 0:
        bot.new_auto_mod()
    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)
    else:
        print("Wrong mode!")
