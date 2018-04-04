from manual_allocation.views import Allocate

routes = [
    ('*', '/', Allocate, 'allocate'),
]
