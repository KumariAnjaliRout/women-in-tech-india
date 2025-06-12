import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Women in Tech – India | Participation Analysis")

# Load the data directly (you can also use pd.read_csv if reading from file)
data = {
    "State": ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
              "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
              "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi"],
    "Total_Students": [74000, 8000, 35000, 69000, 27000, 9000, 71000, 45000, 8000, 27000,
                       88000, 62000, 67000, 100000, 5000, 4000, 3000, 2500, 63000, 42000,
                       80000, 2000, 95000, 72000, 6000, 91000, 32000, 77000, 55000],
    "Female_Students": [31000, 3100, 14500, 19000, 11500, 4200, 22000, 16000, 3200, 10000,
                        32000, 29000, 23000, 37000, 2400, 1600, 1200, 1100, 26000, 18000,
                        27000, 900, 41000, 25000, 2600, 28000, 13000, 34000, 23000],
    "Female_Percentage": [41.9, 38.75, 41.43, 27.5, 42.59, 46.66, 31.0, 35.55, 40.0, 37.03,
                          36.4, 46.77, 34.32, 37.0, 48.0, 40.0, 40.0, 44.0, 41.3, 42.85,
                          33.75, 45.0, 43.1, 34.7, 43.3, 30.8, 40.63, 44.15, 41.82]
}

df = pd.DataFrame(data)

# --- Female Percentage by State (All States Bar Chart) ---
st.subheader("📊 Women in Tech – Percentage of Female Students by State")

fig_all = px.bar(
    df.sort_values(by="Female_Percentage", ascending=False),
    x="Female_Percentage",
    y="State",
    orientation="h",
    color="Female_Percentage",
    color_continuous_scale="reds",
    title="Female Participation (%) in Tech by State"
)
fig_all.update_layout(
    yaxis=dict(categoryorder='total ascending'),
    xaxis_title="Female Participation (%)",
    yaxis_title="State"
)
st.plotly_chart(fig_all, use_container_width=True)


# --- Top 10 States by Female % ---
st.subheader("🔝 Top 10 States by Female Participation (%)")
top_10 = df.sort_values(by="Female_Percentage", ascending=False).head(10)

fig_top = px.bar(
    top_10,
    x="Female_Percentage",
    y="State",
    orientation="h",
    color="Female_Percentage",
    color_continuous_scale="RdPu",
    title="Top 10 States by Female Participation in Tech (%)"
)
fig_top.update_layout(yaxis=dict(categoryorder='total ascending'))
st.plotly_chart(fig_top, use_container_width=True)

# --- Bottom 10 States by Female % ---
st.subheader("🔻 Bottom 10 States by Female Participation (%)")
bottom_10 = df.sort_values(by="Female_Percentage", ascending=True).head(10)

fig_bottom = px.bar(
    bottom_10,
    x="Female_Percentage",
    y="State",
    orientation="h",
    color="Female_Percentage",
    color_continuous_scale="sunsetdark",
    title="Bottom 10 States by Female Participation in Tech (%)"
)
fig_bottom.update_layout(yaxis=dict(categoryorder='total ascending'))
st.plotly_chart(fig_bottom, use_container_width=True)
