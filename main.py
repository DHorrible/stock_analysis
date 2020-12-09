from api.tinkoff.tinkoff_connector import TinkoffConnector
import tinvest

tinkoff_connector = TinkoffConnector()

test_tickets = [
    'APPL',
    'V',
    'VI',
]
print(f'Suspected tickets: {str.join(", ", test_tickets)}')

tinkoff_tickets = tinkoff_connector.check_tickets(test_tickets)
print(f'Tickets are provided by tinkoff: {str.join(", ", tinkoff_tickets)}')

