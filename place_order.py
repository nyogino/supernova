#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" MODULES """

import pybitflyer


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

print(mid)

buy_btc = api.sendchildorder(product_code=product_code,
                             child_order_type="MARKET",
                             side="BUY",
                             size=0.001,
                             minute_to_expire=10000,
                             time_in_force="GTC"
                             )
print(buy_btc)
