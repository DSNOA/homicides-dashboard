import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_homicide_data(fp):
    try:
        print("Loading data...")

        df = pd.read_csv(fp, encoding="ISO-8859-1")
        df = df.drop(columns=["uid", "lat", "lon"])
        print("Done...")
        df["reported_date"] = pd.to_datetime(
            df["reported_date"].astype(str), format="%Y%m%d", errors="coerce"
        ).dt.date

        df["reported_date"].fillna("2007-01-01", inplace=True)

        #######################################################################

        df["reported_date"] = pd.to_datetime(df["reported_date"], format="%Y-%m-%d")
        df["year"] = df["reported_date"].dt.year
        df["month"] = df["reported_date"].dt.month
        gb_month_year = df.groupby(["year", "month"]).size().reset_index(name="count")

        gb_month_year["date"] = (
            gb_month_year["year"].astype(str)
            + "-"
            + gb_month_year["month"].astype(str).str.zfill(2)
        )

        fig_date = px.line(
            gb_month_year,
            y="count",
            x="date",
            title="Homicides Timeline",
            labels={"count": "# of Homicides", "date": "Date"},
            height=600,
        )
        fig_date.update_layout(title_x=0.45)
        st.plotly_chart(fig_date, use_container_width=True)

        #######################################################################

        df["state"] = df["state"].str.upper()
        gb_state = df.groupby("state").size().reset_index(name="count")
        fig_state = px.bar(
            gb_state,
            y="count",
            x="state",
            title="Homicides By State",
            labels={"count": "# of Homicides", "state": "State"},
            color="state",
            color_discrete_sequence=px.colors.qualitative.Set1,
            height=600,
        )
        fig_state.update_xaxes(tickangle=0)
        fig_state.update_layout(title_x=0.45, showlegend=False)
        st.plotly_chart(fig_state, use_container_width=True)

        #######################################################################

        df["victim_age"] = df["victim_age"].replace("Unknown", np.nan)
        gb_age = df.groupby("victim_age").size().reset_index(name="count")
        fig_age = px.bar(
            gb_age,
            y="count",
            x="victim_age",
            title="Homicides by Age",
            labels={"count": "# of Homicides", "victim_age": "Age"},
            color="count",
            color_discrete_sequence=px.colors.qualitative.Set1,
            height=600,
        )

        fig_age.update_layout(title_x=0.45, showlegend=False)
        st.plotly_chart(fig_age, use_container_width=True)

        #######################################################################

        gb_race = df.groupby("victim_race").size().reset_index(name="count")
        fig_race = px.bar(
            gb_race,
            y="count",
            x="victim_race",
            title="Homicides By Race",
            labels={"count": "# of Homicides", "victim_race": "Race"},
            color="victim_race",
            color_discrete_sequence=px.colors.qualitative.Set1,
            height=600,
        )
        fig_race.update_layout(title_x=0.45, showlegend=False)

        st.plotly_chart(fig_race, use_container_width=True)

        #######################################################################

        gb_disposition = df.groupby("disposition").size().reset_index(name="count")
        fig_disposition = px.bar(
            gb_disposition,
            y="count",
            x="disposition",
            title="Homicides by Disposition",
            labels={"count": "# of Homicides", "disposition": "Disposition"},
            color="disposition",
            color_discrete_sequence=px.colors.qualitative.Set1,
            height=600,
        )
        fig_disposition.update_layout(title_x=0.45, showlegend=False)
        st.plotly_chart(fig_disposition, use_container_width=True)

        #######################################################################

        return
    except Exception as e:
        print(e)


fp = "data/homicides.csv"
df = load_homicide_data(fp)
