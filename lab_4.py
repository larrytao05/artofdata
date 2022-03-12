import altair as alt
import pandas as pd

executions = pd.read_csv("Datasets/executions.csv")

race_color = alt.Color("Race:N") # Notice that we can pull this out into a separate variable!
plot = alt.Chart(executions).mark_circle().encode(
    y="Age:Q",
    x='Execution Method:N',
    color=race_color
    
    
).interactive()

executions