from manual_allocation.views import Allocate, Save, Tune

routes = [
    ('GET', '/', Tune, 'tune'),
    ('POST', '/', Tune, 'save_settings'),
    ('GET', '/allocating', Allocate, 'allocate'),
    ('POST', '/allocating', Allocate, 'save_allocate'),
    ('GET', '/saved', Save, 'save'),
    ('POST', '/saved', Save, 'distribute'),
]
