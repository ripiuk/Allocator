from manual_allocation.views import Allocate, Save

routes = [
    ('GET', '/', Allocate, 'allocate'),
    ('POST', '/', Allocate, 'save_allocate'),
    ('GET', '/saved', Save, 'save'),
]
