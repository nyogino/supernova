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


def board_dict(category):
    """
        Returns list of given information on the board
            Default: mid_price
            Optimal: asks, bids
    """
    board = api.board(product_code=product_code)
    return(board[category])


""" MAIN """


for count in range(10):
    mid = board_dict("mid_price")
    print(mid)
    sleep(5)

mid = board_dict("mid_price")
asks = board_dict("asks")
bids = board_dict("bids")
#
# print(mid)
# print(asks)
# print(bids)
