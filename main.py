#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" MODULES """

import pybitflyer
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


""" MAIN """


mid, asks, bids = board_dict()


# for bid in bids[0:5]:
#     print(bid)

print("--")
print(mid)
print("--")

ask_1to5 = []
for ask in asks[0:5]:
    ask_1to5.append(ask["price"])

# average gap from mid
print("ask gap 5 units:", sum(ask_1to5)/5.0 - mid)


