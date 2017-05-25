#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" MODULES """

import pybitflyer
import math
# from time import sleep


""" VARIABLES """


api = pybitflyer.API(
    api_key="7viZ9zampR4nh62Gm8ihsU",
    api_secret="PwruY4uEPtO9qT96TAydZIKfZgS15sP57Ybdkm7hKlU=")

product_code = "FX_BTC_JPY"


""" SUBROUTINES """


def board_dict():
    board = api.board(product_code=product_code)
    return(board["mid_price"], board["asks"], board["bids"])

def gap_calc(*args, **kwargs):
    count = args[0]
    ask_list = bid_list = []

    for ask in asks[0:count]:
        ask_list.append(ask["size"] * ask["price"])
    for bid in bids[0:count]:
        bid_list.append(bid["size"] * bid["price"])

    print("ask gap from mid", abs(mid - sum(ask_list)/2))
    print("bid gap from mid", abs(mid - sum(bid_list)/2))


""" MAIN """


mid, asks, bids = board_dict()

print(mid)
print("--")

gap_calc(2, mid=mid, asks=asks, bids=bids)
