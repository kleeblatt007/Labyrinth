from Labyrinth import *
from threeDLabyrinth import *
from fourthDLabyrinth import *

lab = Labyrinth(5, 0)
#lab.printLabPlotly()
#lab.printLab()
#lab.findWay(0,99)
lab.labToTxt([9,9])

lab2 = threeDLabyrinth(10, 0)
lab2.printLab()
#lab2.findWay(0,2)

#lab3 = fourthDLabyrinth(25,0)
#lab3.printLab()
#lab3.findWay(0,2)

'''
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot  # for IDE use

vol4 = np.random.randint(0, 27, size=(6, 5, 7, 4))

a, b, c = vol4.shape[1:]
X, Y, Z = np.mgrid[-1:1:a*1j, -1:1:b*1j, -1:1:c*1j]

fig = go.Figure(go.Volume(x=X.flatten(),
                          y=Y.flatten(),
                          z=Z.flatten(),
                          value=vol4[0].flatten(),
                          opacity=.25,
                          surface_count=12,
                          colorscale='turbo',
                          colorbar_len=0.8
    ))

frames=[go.Frame(data=go.Volume(
                               value=vol4[k].flatten()),
                 name=str(k)) for k in range(len(vol4))]


sliders = [dict(steps = [dict(method= 'animate',
                              args= [[f'{k}'],
                              dict(mode= 'immediate',
                                   frame= dict(duration=100, redraw=True),
                                   transition=dict(duration= 0))
                                 ],
                              label=f'{k+1}'
                             ) for k in range(len(vol4))],
                active=0,
                transition= dict(duration=0),
                x=0, # slider starting position
                y=0,
                currentvalue=dict(font=dict(size=12),
                                  prefix='frame: ',
                                  visible=True,
                                  xanchor= 'center'
                                 ),
                len=1.0) #slider length
           ]

fig.update_layout(width=700, height=700, sliders=sliders)
fig.update(frames=frames)
plot(fig, auto_open=True)
'''





