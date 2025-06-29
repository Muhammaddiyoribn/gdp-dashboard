# import streamlit as st
# import pandas as pd
# import math
# from pathlib import Path

# # Set the title and favicon that appear in the Browser's tab bar.
# st.set_page_config(
#     page_title='GDP dashboard',
#     page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
# )

# # -----------------------------------------------------------------------------
# # Declare some useful functions.

# @st.cache_data
# def get_gdp_data():
#     """Grab GDP data from a CSV file.

#     This uses caching to avoid having to read the file every time. If we were
#     reading from an HTTP endpoint instead of a file, it's a good idea to set
#     a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
#     """

#     # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
#     DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
#     raw_gdp_df = pd.read_csv(DATA_FILENAME)

#     MIN_YEAR = 1960
#     MAX_YEAR = 2022

#     # The data above has columns like:
#     # - Country Name
#     # - Country Code
#     # - [Stuff I don't care about]
#     # - GDP for 1960
#     # - GDP for 1961
#     # - GDP for 1962
#     # - ...
#     # - GDP for 2022
#     #
#     # ...but I want this instead:
#     # - Country Name
#     # - Country Code
#     # - Year
#     # - GDP
#     #
#     # So let's pivot all those year-columns into two: Year and GDP
#     gdp_df = raw_gdp_df.melt(
#         ['Country Code'],
#         [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
#         'Year',
#         'GDP',
#     )

#     # Convert years from string to integers
#     gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

#     return gdp_df

# gdp_df = get_gdp_data()

# # -----------------------------------------------------------------------------
# # Draw the actual page

# # Set the title that appears at the top of the page.
# '''
# # :earth_americas: GDP dashboard

# Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
# notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
# But it's otherwise a great (and did I mention _free_?) source of data.
# '''

# # Add some spacing
# ''
# ''

# min_value = gdp_df['Year'].min()
# max_value = gdp_df['Year'].max()

# from_year, to_year = st.slider(
#     'Which years are you interested in?',
#     min_value=min_value,
#     max_value=max_value,
#     value=[min_value, max_value])

# countries = gdp_df['Country Code'].unique()

# if not len(countries):
#     st.warning("Select at least one country")

# selected_countries = st.multiselect(
#     'Which countries would you like to view?',
#     countries,
#     ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

# ''
# ''
# ''

# # Filter the data
# filtered_gdp_df = gdp_df[
#     (gdp_df['Country Code'].isin(selected_countries))
#     & (gdp_df['Year'] <= to_year)
#     & (from_year <= gdp_df['Year'])
# ]

# st.header('GDP over time', divider='gray')

# ''

# st.line_chart(
#     filtered_gdp_df,
#     x='Year',
#     y='GDP',
#     color='Country Code',
# )

# ''
# ''


# first_year = gdp_df[gdp_df['Year'] == from_year]
# last_year = gdp_df[gdp_df['Year'] == to_year]

# st.header(f'GDP in {to_year}', divider='gray')

# ''

# cols = st.columns(4)

# for i, country in enumerate(selected_countries):
#     col = cols[i % len(cols)]

#     with col:
#         first_gdp = first_year[gdp_df['Country Code'] == country]['GDP'].iat[0] / 1000000000
#         last_gdp = last_year[gdp_df['Country Code'] == country]['GDP'].iat[0] / 1000000000

#         if math.isnan(first_gdp):
#             growth = 'n/a'
#             delta_color = 'off'
#         else:
#             growth = f'{last_gdp / first_gdp:,.2f}x'
#             delta_color = 'normal'

#         st.metric(
#             label=f'{country} GDP',
#             value=f'{last_gdp:,.0f}B',
#             delta=growth,
#             delta_color=delta_color
#         )


import streamlit as st

# Page configuration
st.set_page_config(
    page_title="IqroAI - New Version",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling and 16:9 aspect ratio
st.markdown("""
<style>
    .main {
        padding: 0;
    }
    
    .block-container {
        padding: 0;
        max-width: 100%;
    }
    
    .fullscreen-container {
        width: 100vw;
        height: 100vh;
        aspect-ratio: 16/9;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0;
        position: relative;
        overflow: hidden;
    }
    
    .content-wrapper {
        background: rgba(255, 255, 255, 0.95);
        padding: 3rem 2rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        width: 90%;
        backdrop-filter: blur(10px);
    }
    
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .message {
        font-size: 1.3rem;
        color: #333;
        margin-bottom: 2.5rem;
        line-height: 1.6;
    }
    
    .link-button {
        background: linear-gradient(45deg, #1f77b4, #1565c0);
        color: white;
        padding: 15px 35px;
        text-decoration: none;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 1rem 0;
        box-shadow: 0 8px 20px rgba(31, 119, 180, 0.3);
        transform: translateY(0);
    }
    
    .link-button:hover {
        background: linear-gradient(45deg, #1565c0, #0d47a1);
        text-decoration: none;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(31, 119, 180, 0.4);
    }
    
    .footer {
        margin-top: 2rem;
        color: #666;
        font-size: 1rem;
    }
    
    /* Hide Streamlit elements */
    header[data-testid="stHeader"] {
        display: none;
    }
    
    .stApp > footer {
        display: none;
    }
    
    .stDeployButton {
        display: none;
    }
    
    #MainMenu {
        display: none;
    }
    
    @media (max-width: 768px) {
        .title {
            font-size: 2.2rem;
        }
        
        .message {
            font-size: 1.1rem;
        }
        
        .content-wrapper {
            padding: 2rem 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Main content with 16:9 ratio
st.markdown('<div class="fullscreen-container">', unsafe_allow_html=True)
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">🚀 IqroAI New Version</h1>', unsafe_allow_html=True)

# Message
st.markdown('''
<div class="message">
    <p>To try the new version of IqroAI, please visit the following page:</p>
</div>
''', unsafe_allow_html=True)

# Link button
st.markdown('''
<div style="text-align: center;">
    <a href="https://iqroai-web-wd5a2.ondigitalocean.app/" target="_blank" class="link-button">
        Visit IqroAI New Version
    </a>
</div>
''', unsafe_allow_html=True)

# Alternative using Streamlit's built-in link button
st.markdown("---")
st.markdown("### Or click the button below:")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌐 Go to IqroAI", type="primary", use_container_width=True):
        st.markdown('''
        <script>
            window.open('https://iqroai-web-wd5a2.ondigitalocean.app/', '_blank');
        </script>
        ''', unsafe_allow_html=True)

# Footer
st.markdown('''
<div class="footer">
    <p>Thank you for using IqroAI! 🙏</p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close content-wrapper
st.markdown('</div>', unsafe_allow_html=True)  # Close fullscreen-container

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)
