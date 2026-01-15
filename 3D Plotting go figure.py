import plotly.graph_objects as go

fig_new = go.Figure(data=[go.Scatter3d(x=x,y=y,z=z,mode='markers', marker=dict(size=2,color=z))])
fig_new.update_layout(title='Earthquake locations',autosize=False,width=800, height=800)
fig_new.update_layout(scene = dict(xaxis_title='longitude',yaxis_title='latitude',zaxis_title='depth')) 
fig_new.show()