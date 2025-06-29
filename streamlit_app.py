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
    page_title="IqroAI",
    page_icon="📚",
    layout="centered"
)

# Custom CSS for minimal styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: 300;
        margin-bottom: 2rem;
    }
    
    .description {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 3rem;
    }
    
    .link-container {
        text-align: center;
        margin: 2rem 0;
    }
    
    .custom-link {
        display: inline-block;
        padding: 12px 30px;
        background-color: #3498db;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: 500;
        transition: background-color 0.3s;
    }
    
    .custom-link:hover {
        background-color: #2980b9;
        text-decoration: none;
        color: white;
    }
    
    .footer {
        text-align: center;
        color: #bdc3c7;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #ecf0f1;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">IqroAI</h1>', unsafe_allow_html=True)

st.markdown("""
<p class="description">
To try the new version of IqroAI, please visit the following page:
</p>
""", unsafe_allow_html=True)

# Link to the new version
st.markdown("""
<div class="link-container">
    <a href="https://iqroai-web-wd5a2.ondigitalocean.app/" target="_blank" class="custom-link">
        Visit IqroAI New Version
    </a>
</div>
""", unsafe_allow_html=True)

# Additional information
st.markdown("""
<p class="description">
Experience the enhanced features and improved interface of IqroAI's latest update.
</p>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Thank you for using IqroAI</p>
</div>
""", unsafe_allow_html=True)
