from manual_allocation.views import Allocate, SaveAllocation

routes = [
    ('*', '/', Allocate, 'allocate'),
    ('*', '/save', SaveAllocation, 'save')
]
