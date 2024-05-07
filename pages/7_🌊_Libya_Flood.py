import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A use case for visualizing Libya Flood Event in Sept 2023.
<https://www.unicef.org/emergencies/devastating-flooding-libya>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Devastating Floods in Libya Sept 2023")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
        after = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
        m.split_map(
            left_layer = before, right_layer = after, left_label="July01,2023_Libya", right_label="Sept13,2023_Libya"
        )
        

m.to_streamlit(height=700)
