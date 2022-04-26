import requests

from .constants import *


def train_delay(train_id):
    train = requests.get(f'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
                         f'cercaNumeroTrenoTrenoAutocomplete/{train_id}').text
    station_id, midnight = parse_train(train)[1], parse_train(train)[2]
    current_delay = requests.get(f'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
                                 f'andamentoTreno/{station_id}/{train_id}/{midnight}').json()

    # TRAIN DETAILS USING lefreccie API

    # start = 'NOVARA'
    # end = 'MILANO%20PORTA%20GARIBALDI'
    # end = 'MILANO%20CENTRALE'
    # arflag = 'A'
    # date = '12/04/2022'
    # time = '13'
    # offset = ''
    # adults = '1'
    # children = '0'
    # direction = 'A'
    # frecce = 'false'
    # regionals = 'false'

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
    # solution_id = request[0]['idsolution']
    # train_details = session.get(f'https://www.lefrecce.it/msite/api/'
    #                             f'solutions/{solution_id}/details').text

    return current_delay['ritardo']


def delay_message(train_id):
    train_delay_minutes = train_delay(train_id)
    train_delay_message = 'Your train is '
    if train_delay_minutes < 0:
        train_delay_minutes = abs(train_delay_minutes)
        train_delay_message = train_delay_message + f'<b>{train_delay_minutes} minutes</b> early!'
    elif train_delay_minutes > 0:
        train_delay_message = train_delay_message + f'delayed by <b>{train_delay_minutes} minutes</b> :(.'
    else:
        train_delay_message = train_delay_message + 'on time!'
    return train_delay_message


def parse_train(train):
    train_data = train.replace('\n', '').split('|', maxsplit=1)
    return train_data[1].split('-')
