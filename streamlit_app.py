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
import webbrowser

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="IqroAI Yangi Versiya",
    page_icon="🚀",
    layout="centered"
)

# CSS stillar
st.markdown("""
<style>
    .main-container {
        text-align: center;
        padding: 2rem;
    }
    
    .title {
        color: #1e3a8a;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        color: #475569;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .description {
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        line-height: 1.6;
    }
    
    .link-button {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 1rem 2rem;
        border-radius: 12px;
        text-decoration: none;
        font-size: 1.3rem;
        font-weight: bold;
        display: inline-block;
        transition: all 0.3s ease;
        margin: 1rem;
    }
    
    .link-button:hover {
        background: linear-gradient(135deg, #2563eb, #1e40af);
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    
    .features {
        background: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        margin: 2rem 0;
    }
    
    .feature-item {
        margin: 1rem 0;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Asosiy sahifa
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Sarlavha
st.markdown('<h1 class="title">🚀 IqroAI</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Yangi Versiya Taqdim Etildi!</h2>', unsafe_allow_html=True)

# Tavsif
st.markdown("""
<div class="description">
IqroAI ning yangi va yaxshilangan versiyasini sinab ko'rish uchun quyidagi sahifaga tashrif buyuring. 
Yangi imkoniyatlar va yaxshilanishlar sizni kutmoqda!
</div>
""", unsafe_allow_html=True)

# Xususiyatlar
st.markdown("""
<div class="features">
    <h3 style="color: #1e3a8a; text-align: center; margin-bottom: 1.5rem;">🌟 Yangi Imkoniyatlar</h3>
    <div class="feature-item">✨ Yaxshilangan foydalanuvchi interfeysi</div>
    <div class="feature-item">🚀 Tezroq ishlash va javob berish</div>
    <div class="feature-item">🔧 Yangi funksiyalar va vositalar</div>
    <div class="feature-item">📊 Yaxshilangan tahlil imkoniyatlari</div>
</div>
""", unsafe_allow_html=True)

# Link tugmasi
target_url = "https://iqroai-web-wd5a2.ondigitalocean.app/"

st.markdown(f"""
<div style="text-align: center; margin: 3rem 0;">
    <a href="{target_url}" target="_blank" class="link-button">
        🔗 IqroAI Yangi Versiyasini Sinab Ko'ring
    </a>
</div>
""", unsafe_allow_html=True)

# Qo'shimcha ma'lumot
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #6b7280;">
    <p>Agar yuqoridagi tugma ishlamasa, quyidagi linkni to'g'ridan-to'g'ri brauzeringizga nusxalang:</p>
    <code style="background: #f3f4f6; padding: 0.5rem; border-radius: 6px;">
        https://iqroai-web-wd5a2.ondigitalocean.app/
    </code>
</div>
""", unsafe_allow_html=True)

# Streamlit tugmasi (zaxira variant)
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 IqroAI ga O'tish", use_container_width=True, type="primary"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={target_url}">', unsafe_allow_html=True)
        js = f"window.open('{target_url}')"
        st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)
        st.success("IqroAI sahifasi yangi oynada ochilmoqda...")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; background: #f1f5f9; border-radius: 12px;">
    <p style="color: #475569; margin: 0;">
        💡 <strong>IqroAI</strong> - Sun'iy intellekt yordamida ta'lim va o'rganish
    </p>
</div>
""", unsafe_allow_html=True)
