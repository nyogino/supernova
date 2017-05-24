#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" MODULES """

import pybitflyer
from time import sleep


""" VARIABLES """


api = pybitflyer.API(
    api_key="7viZ9zampR4nh62Gm8ihsU",
    api_secret="PwruY4uEPtO9qT96TAydZIKfZgS15sP57Ybdkm7hKlU=")

product_code = "FX_BTC_JPY"


""" SUBROUTINES """


def board_dict():
    board = api.board(product_code=product_code)
    return(board["mid_price"], board["asks"], board["bids"])


""" MAIN """


# for count in range(10):
#     mid, asks, bids = board_dict()
#     print(mid)
#     sleep(1)

mid, asks, bids = board_dict()

for ask in asks[0:5]:
    print(ask)

print("--")
print(mid)
print("--")

for bid in bids[0:5]:
    print(bid)

