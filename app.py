import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Mental Health in Tech Survey",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# TITLE AND INTRODUCTION
# --------------------------------------------------
st.title("🧠 Mental Health in Tech Survey Analysis")

st.write(
    "This interactive dashboard explores mental health attitudes, "
    "treatment, workplace support, and employee experiences in the "
    "technology sector."
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
df = pd.read_csv("survey.csv")

# Create a copy for cleaning
df_clean = df.copy()

# Remove unrealistic age values
df_clean = df_clean[
    (df_clean["Age"] >= 18) &
    (df_clean["Age"] <= 100)
]

# Handle missing values
df_clean["state"] = df_clean["state"].fillna("Not Applicable")
df_clean["self_employed"] = df_clean["self_employed"].fillna("Unknown")
df_clean["work_interfere"] = df_clean["work_interfere"].fillna("Unknown")
df_clean["comments"] = df_clean["comments"].fillna("No Comment")

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("Filter Data")

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df_clean["Country"].dropna().unique().tolist())
)

selected_remote = st.sidebar.selectbox(
    "Remote Work",
    ["All", "Yes", "No"]
)

selected_treatment = st.sidebar.selectbox(
    "Treatment",
    ["All", "Yes", "No"]
)

# Create filtered dataset
filtered_df = df_clean.copy()

if selected_country != "All":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

if selected_remote != "All":
    filtered_df = filtered_df[
        filtered_df["remote_work"] == selected_remote
    ]

if selected_treatment != "All":
    filtered_df = filtered_df[
        filtered_df["treatment"] == selected_treatment
    ]

# --------------------------------------------------
# SURVEY OVERVIEW
# --------------------------------------------------
st.subheader("Survey Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Respondents",
        len(filtered_df)
    )

with col2:
    average_age = (
        round(filtered_df["Age"].mean(), 1)
        if not filtered_df.empty else 0
    )
    st.metric(
        "Average Age",
        average_age
    )

with col3:
    treatment_yes = (
        filtered_df["treatment"] == "Yes"
    ).sum()

    st.metric(
        "Sought Treatment",
        treatment_yes
    )

with col4:
    countries = filtered_df["Country"].nunique()

    st.metric(
        "Countries",
        countries
    )

st.divider()

# --------------------------------------------------
# CHART 1 - TREATMENT DISTRIBUTION
# --------------------------------------------------
st.subheader("1. Mental Health Treatment")

fig1, ax1 = plt.subplots(figsize=(7, 4))

sns.countplot(
    data=filtered_df,
    x="treatment",
    ax=ax1
)

ax1.set_title("Mental Health Treatment Distribution")
ax1.set_xlabel("Sought Treatment")
ax1.set_ylabel("Number of Respondents")

st.pyplot(fig1)

st.write(
    "This chart shows the distribution of respondents who have "
    "and have not sought treatment for a mental health condition."
)

st.divider()

# --------------------------------------------------
# CHART 2 - FAMILY HISTORY AND TREATMENT
# --------------------------------------------------
st.subheader("2. Family History and Treatment")

fig2, ax2 = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=filtered_df,
    x="family_history",
    hue="treatment",
    ax=ax2
)

ax2.set_title("Family History vs Mental Health Treatment")
ax2.set_xlabel("Family History")
ax2.set_ylabel("Number of Respondents")

st.pyplot(fig2)

st.write(
    "This chart examines the association between family history "
    "of mental illness and treatment-seeking behaviour."
)

st.divider()

# --------------------------------------------------
# CHART 3 - WORK INTERFERENCE AND TREATMENT
# --------------------------------------------------
st.subheader("3. Work Interference and Treatment")

fig3, ax3 = plt.subplots(figsize=(9, 4))

sns.countplot(
    data=filtered_df,
    x="work_interfere",
    hue="treatment",
    ax=ax3
)

ax3.set_title("Work Interference vs Mental Health Treatment")
ax3.set_xlabel("Frequency of Work Interference")
ax3.set_ylabel("Number of Respondents")

st.pyplot(fig3)

st.write(
    "This chart compares how frequently mental health interferes "
    "with work with treatment-seeking behaviour."
)

st.divider()

# --------------------------------------------------
# CHART 4 - EMPLOYER BENEFITS
# --------------------------------------------------
st.subheader("4. Mental Health Benefits")

fig4, ax4 = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=filtered_df,
    x="benefits",
    ax=ax4
)

ax4.set_title("Mental Health Benefits Provided by Employers")
ax4.set_xlabel("Mental Health Benefits")
ax4.set_ylabel("Number of Respondents")

st.pyplot(fig4)

st.write(
    "This chart shows respondents' awareness of mental health "
    "benefits provided by their employers."
)

st.divider()

# --------------------------------------------------
# CHART 5 - SUPERVISOR DISCUSSION
# --------------------------------------------------
st.subheader("5. Willingness to Discuss Mental Health with Supervisor")

fig5, ax5 = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=filtered_df,
    x="supervisor",
    ax=ax5
)

ax5.set_title("Willingness to Discuss Mental Health with Supervisor")
ax5.set_xlabel("Response")
ax5.set_ylabel("Number of Respondents")

st.pyplot(fig5)

st.write(
    "This chart shows employees' willingness to discuss a mental "
    "health issue with their supervisor."
)

st.divider()

# --------------------------------------------------
# CHART 6 - MEDICAL LEAVE
# --------------------------------------------------
st.subheader("6. Ease of Taking Medical Leave")

fig6, ax6 = plt.subplots(figsize=(10, 4))

sns.countplot(
    data=filtered_df,
    x="leave",
    ax=ax6
)

ax6.set_title("Ease of Taking Medical Leave for Mental Health")
ax6.set_xlabel("Difficulty of Taking Leave")
ax6.set_ylabel("Number of Respondents")

plt.xticks(rotation=20)

st.pyplot(fig6)

st.write(
    "This chart shows how respondents perceive the difficulty "
    "of taking medical leave for a mental health condition."
)

st.divider()

# --------------------------------------------------
# CHART 7 - CARE OPTIONS AND TREATMENT
# --------------------------------------------------
st.subheader("7. Mental Health Care Options and Treatment")

fig7, ax7 = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=filtered_df,
    x="care_options",
    hue="treatment",
    ax=ax7
)

ax7.set_title("Mental Health Care Options vs Treatment")
ax7.set_xlabel("Awareness of Care Options")
ax7.set_ylabel("Number of Respondents")

st.pyplot(fig7)

st.write(
    "This chart examines the association between awareness of "
    "mental health care options and treatment-seeking behaviour."
)

st.divider()

# --------------------------------------------------
# CHART 8 - REMOTE WORK AND TREATMENT
# --------------------------------------------------
st.subheader("8. Remote Work and Treatment")

fig8, ax8 = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=filtered_df,
    x="remote_work",
    hue="treatment",
    ax=ax8
)

ax8.set_title("Remote Work vs Mental Health Treatment")
ax8.set_xlabel("Remote Work")
ax8.set_ylabel("Number of Respondents")

st.pyplot(fig8)

st.write(
    "This chart compares treatment-seeking behaviour between "
    "respondents who work remotely and those who do not."
)

st.divider()

# --------------------------------------------------
# CHART 9 - COMPANY SIZE AND TREATMENT
# --------------------------------------------------
st.subheader("9. Mental Health Treatment by Company Size")

fig9, ax9 = plt.subplots(figsize=(10, 5))

sns.countplot(
    data=filtered_df,
    x="no_employees",
    hue="treatment",
    ax=ax9
)

ax9.set_title("Mental Health Treatment by Company Size")
ax9.set_xlabel("Number of Employees")
ax9.set_ylabel("Number of Respondents")

plt.xticks(rotation=20)

st.pyplot(fig9)

st.write(
    "This chart compares mental health treatment-seeking behaviour "
    "across different company sizes."
)

st.divider()

# --------------------------------------------------
# CHART 10 - CONSEQUENCES AND SUPERVISOR
# --------------------------------------------------
st.subheader(
    "10. Mental Health Consequences and Supervisor Discussion"
)

fig10, ax10 = plt.subplots(figsize=(9, 4))

sns.countplot(
    data=filtered_df,
    x="mental_health_consequence",
    hue="supervisor",
    ax=ax10
)

ax10.set_title(
    "Mental Health Consequences vs Willingness to Discuss with Supervisor"
)

ax10.set_xlabel("Expected Mental Health Consequences")
ax10.set_ylabel("Number of Respondents")

st.pyplot(fig10)

st.write(
    "This chart examines the relationship between expected negative "
    "workplace consequences and willingness to discuss mental health "
    "with a supervisor."
)

# --------------------------------------------------
# CONCLUSION
# --------------------------------------------------
st.divider()

st.subheader("Key Takeaways")

st.write(
    """
    The dashboard highlights differences in mental health treatment,
    workplace support, awareness of care options, and willingness to
    discuss mental health concerns. Family history, work interference,
    workplace benefits, care options, and perceptions of workplace
    consequences show useful associations with mental health attitudes
    and treatment-seeking behaviour.

    These visualizations show patterns and associations in the survey
    data and should not be interpreted as proving direct causation.
    """
)

st.caption(
    "Mental Health in Tech Survey | Exploratory Data Analysis Dashboard"
)