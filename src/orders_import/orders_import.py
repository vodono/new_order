from datetime import datetime, date
from invoke import task
from requests import get
from requests.auth import HTTPBasicAuth

from config import settings
from db.base import Session
from db.models import DenysOrders, DenysClients

@task
def today_orders_import(ctx):
    """
    read orders from url and write new today orders into database
    """

    url = 'https://online.moysklad.ru/api/remap/1.1/entity/customerorder'
    login = 'admin@max69'
    password = '61ae20975e'

    resp = get(url, auth=HTTPBasicAuth(login, password))
    get_orders = resp.json()

    session_orders = Session()
    session_clients = Session()

    if settings.debug:
        today = date(2019, 2, 15)
    else:
        today = datetime.today().date()

    for i in get_orders['rows']:
        if datetime.strptime(i['moment'], "%Y-%m-%d %H:%M:%S").date() == today:
            if not session_orders.query(DenysOrders).filter(DenysOrders.id == i['id']).all():
                client_data = get(i['agent']['meta']['href'], auth=HTTPBasicAuth(login, password)).json()

                if not session_clients.query(DenysClients).filter(DenysClients.id == client_data['id']).all():
                    session_clients.add(
                        DenysClients(
                            id=client_data['id'],
                            name=client_data['name'],
                        )
                    )

                session_orders.add(
                    DenysOrders(
                        id=i['id'],
                        name=i['name'],
                        # description =
                        moment=i['moment'],
                        sum=i['sum'],
                        counterparty_id=client_data['id'],
                    )
                )
    session_clients.commit()
    session_orders.commit()
