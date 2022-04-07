from DB import SQLMaker
import threading

db = SQLMaker("database/map_pr")
lock = threading.Lock()


def investigationSet(month, poezd):
    # '202112', '0054055945001035'
    edges = db.get_edges_train(month, poezd)
    stantion = []
    if len(edges) == 0:
        return []

    for edge in edges:
        if edge[2] == 'null':
            edge[2] = 0
        if edge[3] == 'null':
            edge[3] = 0
        row = {'poezd': poezd, 'MONTH': month, 'LAT': edge[2], 'LON': edge[3], 'STANTION': edge[0], 'NAME': edge[1],
               'NUMBER': int(edge[-1])}
        stantion.append(row)
        if int(edge[-1]) == 0:
            row = {'poezd': poezd, 'MONTH': month, 'LAT': edge[6], 'LON': edge[7], 'STANTION': edge[4], 'NAME': edge[5],
                   'NUMBER': int(edge[-1])}
            stantion.append(row)

    row = {'poezd': poezd, 'MONTH': month, 'LAT': edges[-1][6], 'LON': edges[-1][7], 'STANTION': edges[-1][4],
           'NAME': edges[-1][5], 'NUMBER': (int(edges[-1][-1]) + 1)}
    stantion.append(row)
    return stantion


def investigationSFSet(poezd, month):
    data = db.get_InvestigationSFSet(poezd, month)
    if len(data) == 0:
        return []
    data_row = data[0]
    row = {'poezd': data_row[0],
           'MONTH': data_row[1],
           'POEZD_NAME': data_row[2],
           'LAT_START': data_row[3],
           'LON_START': data_row[4],
           'STANTION_START': data_row[5],
           'NAME_START': data_row[6],
           'LAT_FINISH': data_row[7],
           'LON_FINISH': data_row[8],
           'STANTION_FINISH': data_row[9],
           'NAME_FINISH': data_row[10]}
    result_set = [row]
    return result_set


def stNumberingSet(month, poezd):
    data = db.get_StNumberingSet(month, poezd)
    if len(data) == 0:
        return []
    result_set = []
    for line in data:
        row = {'poezd': line[0], 'MONTH': line[1], 'STANTION_START': line[2],
               'STANTION_FINISH': line[3], 'NUMBER': int(line[4]), 'CASAR': line[5], 'CHET': line[6]}
        result_set.append(row)
    return result_set


def poezdSuggestSet(poezd):
    with lock:
        data = db.get_poezdSuggestSet(poezd)
    if len(data) == 0:
        return []
    result_set = []
    for line in data:
        # row = {'poezd': line[0]}
        result_set.append(line[0])
    return result_set

