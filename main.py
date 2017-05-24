#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pybitflyer

# -------------------------------------------------------------------------------------- #
# VARIABLES

api = pybitflyer.API(
    api_key="7viZ9zampR4nh62Gm8ihsU",
    api_secret="PwruY4uEPtO9qT96TAydZIKfZgS15sP57Ybdkm7hKlU=")

product_code = "FX_BTC_JPY"

# -------------------------------------------------------------------------------------- #
# SUBS
def board:
    """Returns list of given information on the board"""
    board = api.board(product_code=product_code)
    asks = board["asks"]
    mid_price = board["mid_price"]
    bids = board["bids"]
    return(asks, mid_price, bids)

# -------------------------------------------------------------------------------------- #
# CORE

board()

print(mid_price)

print("----------------------------")

print(len(asks))
print(len(bids))

# for ask in asks:
#     print(ask)

# for bid in bids:
#     print(bid["price"])

