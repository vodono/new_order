import xlrd
from invoke import task

from db.models import DenysOrders, DenysClients
from db.base import Session


@task
def excel_read(ctx):
    """
    read from excel file and fill the database
    """

    session = Session()
    session.query(DenysOrders).delete()
    session.query(DenysClients).delete()

    loc = '../task/ПримерМСКонтрагентыSQLAzure2.xlsx'

    wb = xlrd.open_workbook(loc)
    orders_sheet = wb.sheet_by_index(0)
    counterparty_sheet = wb.sheet_by_index(1)

    clients_list = []

    for i in range(1, counterparty_sheet.nrows):
        values = counterparty_sheet.row_values(i)
        clients_list.append(
            DenysClients(
                id=values[0],
                name=values[1],
            )
        )
    session.add_all(clients_list)
    session.commit()

    orders_list = []
    for i in range(1, orders_sheet.nrows):
        values = orders_sheet.row_values(i)
        orders_list.append(
            DenysOrders(
                id=values[0],
                name=values[1],
                description=values[2],
                moment=values[3],
                sum=values[4],
                counterparty_id=values[5],
            )
        )
    session.add_all(orders_list)
    session.commit()
