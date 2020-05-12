# -*- coding: utf-8 -*-

from .models import Enmax_load
from .utils.utils import gen_id


def map_enmax_load(item):
    load = Enmax_load()
    # load.id = gen_id(item['tou'] + str(item['date']))
    load.date = item['date']
    # load.tou = item['tou']
    load.load = item['load']
    return load
