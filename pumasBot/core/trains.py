import requests

from .constants import *


def trains():
    # start = 'NOVARA'
    # end = 'MILANO%20PORTA%20GARIBALDI'
    # end = 'MILANO%20CENTRALE'
    # arflag = 'A'
    # date = '12/04/2022'
    # time = '13'
    # # offset = ''
    # adults = '1'
    # children = '0'
    # direction = 'A'
    # frecce = 'false'
    # regionals = 'false'
    # station_id = 'S00248'
    train_id = '2003'

    # train_number = '2003'
    # station_id = 'S00219'
    # train = requests.get('http://www.viaggiatreno.it/viaggiatrenomobile/pages/cercaTreno/'
    #                      'cercaTreno.jsp?treno=2003&origine=S00219&datapartenza=1649714400000').json()
    train = requests.get('http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
                         'cercaNumeroTrenoTrenoAutocomplete/2003').text
    station_id, midnight = parse_train(train)[1], parse_train(train)[2]
    print(midnight)
    train_status = requests.get(f'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
                                f'andamentoTreno/{station_id}/{train_id}/{midnight}').json()
    print(train_status)
    # train = requests.get(f'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
    #                      f'andamentoTreno/{station_id}/{train_number}')
    # train = requests.get('http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
    #                      'elencoStazioni/piemonte').content
    # session = requests.Session()
    # request = session.get(f'https://www.lefrecce.it/msite/api/solutions?'
    #                       f'origin={start}'
    #                       f'&destination={end}'
    #                       f'&arflag={arflag}'
    #                       f'&adate={date}'
    #                       f'&atime={time}'
    #                       # f'&offset={OFFSET}'
    #                       f'&adultno={adults}'
    #                       f'&childno={children}'
    #                       f'&direction={direction}'
    #                       f'&frecce={frecce}'
    #                       f'&onlyRegional={regionals}').json()
    # print(request)
    # solution_id = request[0]['idsolution']
    # print(solution_id)
    # train_details = session.get(f'https://www.lefrecce.it/msite/api/'
    #                             f'solutions/{solution_id}/details').text
    # print(train_details)
    return train_status['ritardo']


def parse_train(train):
    train_data = train.replace('\n', '').split('|', maxsplit=1)
    print(train_data)
    return train_data[1].split('-')
