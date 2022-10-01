class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
setattr(fig1, 'start_pt', (10, 5))
setattr(fig1, 'end_pt', (100, 20))
setattr(fig1, 'color', 'blue')
delattr(fig1, 'color') if 'color' in fig1.__dict__ else None
[print(_, end=' ') for _ in fig1.__dict__]