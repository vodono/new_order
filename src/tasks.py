from invoke import Collection

from commons.tasks import shell
from excel_read.excel_read import excel_read
from db.tasks import db_update
from orders_import.orders_import import today_orders_import


ns = Collection()
ns.add_task(shell)
ns.add_task(excel_read)
ns.add_task(db_update)
ns.add_task(today_orders_import)
