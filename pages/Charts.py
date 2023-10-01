import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


@st.cache_data
def load_homicide_data(fp):
    try:
        print('Loading data...')

        df = pd.read_csv(fp, encoding='ISO-8859-1')
        df = df.drop(columns=['uid', 'lat', 'lon'])

        # df['new_date'] = pd.to_datetime(
        #     df['reported_date'].astype(str), format='%Y%m%d', errors='coerce')

        # # inplace=True because fillna gives back a copy by default.
        # df['new_date'].fillna(pd.Timestamp('2007-01-01'), inplace=True)

        # df['year'] = pd.to_datetime(
        #     df['new_date'].astype(str), format='%Y%m%d', errors='coerce').dt.year.astype(int).astype(str)

        df['reported_date'] = pd.to_datetime(
            df['reported_date'].astype(str), format='%Y%m%d', errors='coerce').dt.date

        df['reported_date'].fillna('2007-01-01', inplace=True)
        # df['month_year'] = df['reported_date'].dt.strftime('%Y-%m')

        gb_race = df.groupby('victim_race').size().reset_index(name='count')
        fig_race = px.bar(gb_race,
                          y='count',
                          x='victim_race',
                          title='# of Homicides By Race',
                          labels={'count': '# of Homicides',
                                  'victim_race': 'Race'}
                          )
        st.plotly_chart(fig_race,
                        use_container_width=True)

        gb_date = df.groupby('reported_date').size().reset_index(name='count')
        fig_date = px.area(gb_date,
                           y='count',
                           x='reported_date',
                           title='# of Homicides By Date',
                           labels={'count': '# of Homicides',
                                   'reported_date': 'Date'},
                           height=600
                           )
        st.plotly_chart(fig_date,
                        use_container_width=True)

        gb_state = df.groupby('state').size().reset_index(name='count')
        fig_state = px.bar(gb_state,
                           y='state',
                           x='count',
                           title='# of Homicides By State',
                           labels={'count': '# of Homicides',
                                   'state': 'State'},
                           height=600
                           )

        st.plotly_chart(fig_state,
                        use_container_width=True)

        return (df)
    except Exception as e:
        print(e)


fp = '../data/homicide.csv'
df = load_homicide_data(fp)
