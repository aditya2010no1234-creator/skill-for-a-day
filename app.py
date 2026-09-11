import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Skill-for-a-Day",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# DATA
# -----------------------------

jobs = pd.DataFrame({
    "Job": [
        "Garden Assistant",
        "Painting Helper",
        "Packing Assistant",
        "Delivery Helper",
        "Cleaning Assistant",
        "Shop Helper",
        "Kitchen Helper",
        "Data Entry Assistant",
        "Event Helper",
        "Tailoring Assistant"
    ],
    "Location": [
        "Ghaziabad", "Delhi", "Ghaziabad", "Noida", "Delhi",
        "Noida", "Ghaziabad", "Noida", "Delhi", "Ghaziabad"
    ],
    "Pay": [350, 500, 400, 450, 350, 400, 450, 500, 550, 450],
    "Hours": [5, 6, 5, 6, 4, 5, 5, 4, 6, 5],
    "Skill": [
        "Gardening", "Painting", "Packing", "Delivery", "Cleaning",
        "Retail", "Cooking", "Computer Basics", "Event Support", "Tailoring"
    ],
    "Level": [
        "Beginner", "Beginner", "Beginner", "Intermediate", "Beginner",
        "Beginner", "Beginner", "Beginner", "Beginner", "Intermediate"
    ]
})

# -----------------------------
# SESSION STATE
# -----------------------------

if "applications" not in st.session_state:
    st.session_state.applications = []

if "selected_job" not in st.session_state:
    st.session_state.selected_job = None

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Skill-for-a-Day")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Find Jobs", "My Applications", "Learn Skills", "About SDG 1"]
)

# -----------------------------
# HOME
# -----------------------------

if page == "Home":

    st.title("Skill-for-a-Day")
    st.subheader("Earn today. Learn for tomorrow.")

    st.write(
        "A community platform that connects people with short paid work "
        "opportunities while helping them develop useful skills."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Jobs Available", len(jobs))

    with col2:
        st.metric("Skills Offered", jobs["Skill"].nunique())

    with col3:
        st.metric("Locations", jobs["Location"].nunique())

    st.divider()

    st.header("How it works")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("1. Find")
        st.write("Browse short-term jobs available in your area.")

    with c2:
        st.subheader("2. Apply")
        st.write("Choose a suitable opportunity and submit your application.")

    with c3:
        st.subheader("3. Learn & Earn")
        st.write("Complete the work, earn income and gain practical experience.")

    st.info(
        "Our goal is to create opportunities for people who may not have "
        "formal qualifications but have the willingness to work and learn."
    )

# -----------------------------
# FIND JOBS
# -----------------------------

elif page == "Find Jobs":

    st.title("Find Jobs")
    st.write("Find short-term paid work opportunities.")

    search = st.text_input(
        "Search for a job",
        placeholder="Example: painting, gardening..."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        location = st.selectbox(
            "Location",
            ["All"] + sorted(jobs["Location"].unique())
        )

    with col2:
        skill = st.selectbox(
            "Skill",
            ["All"] + sorted(jobs["Skill"].unique())
        )

    with col3:
        level = st.selectbox(
            "Experience Level",
            ["All"] + sorted(jobs["Level"].unique())
        )

    filtered = jobs.copy()

    if search:
        filtered = filtered[
            filtered["Job"].str.contains(search, case=False, na=False)
        ]

    if location != "All":
        filtered = filtered[filtered["Location"] == location]

    if skill != "All":
        filtered = filtered[filtered["Skill"] == skill]

    if level != "All":
        filtered = filtered[filtered["Level"] == level]

    st.divider()

    if filtered.empty:
        st.warning("No jobs found. Try changing your filters.")

    else:
        for index, job in filtered.iterrows():

            with st.container(border=True):

                col1, col2 = st.columns([4, 1])

                with col1:
                    st.subheader(job["Job"])

                    st.write(
                        f"**Location:** {job['Location']}  \n"
                        f"**Pay:** ₹{job['Pay']}  \n"
                        f"**Duration:** {job['Hours']} hours  \n"
                        f"**Skill:** {job['Skill']}  \n"
                        f"**Level:** {job['Level']}"
                    )

                with col2:
                    if st.button(
                        "Apply",
                        key=f"apply_{index}"
                    ):
                        st.session_state.selected_job = job["Job"]

            if st.session_state.selected_job == job["Job"]:

                st.subheader(f"Apply for {job['Job']}")

                with st.form(f"form_{index}"):

                    name = st.text_input("Your Name")
                    phone = st.text_input("Phone Number")
                    experience = st.text_area(
                        "Why are you suitable for this job?"
                    )

                    submitted = st.form_submit_button("Submit Application")

                    if submitted:

                        if name and phone:
                            st.session_state.applications.append({
                                "Name": name,
                                "Phone": phone,
                                "Job": job["Job"],
                                "Location": job["Location"],
                                "Pay": job["Pay"]
                            })

                            st.success(
                                "Application submitted successfully!"
                            )

                        else:
                            st.error(
                                "Please enter your name and phone number."
                            )

# -----------------------------
# MY APPLICATIONS
# -----------------------------

elif page == "My Applications":

    st.title("My Applications")

    if len(st.session_state.applications) == 0:

        st.info("You haven't applied for any jobs yet.")

    else:

        applications_df = pd.DataFrame(
            st.session_state.applications
        )

        st.dataframe(
            applications_df,
            use_container_width=True,
            hide_index=True
        )

# -----------------------------
# LEARN SKILLS
# -----------------------------

elif page == "Learn Skills":

    st.title("Learn Skills")

    st.write(
        "The platform is not only about earning money. "
        "It also helps people build practical skills."
    )

    skills = {
        "Gardening": "Learn basic plant care, soil preparation and garden maintenance.",
        "Painting": "Learn basic wall preparation, painting and finishing.",
        "Packing": "Learn safe and efficient packaging techniques.",
        "Delivery": "Learn basic delivery planning and customer interaction.",
        "Cleaning": "Learn professional cleaning and organization techniques.",
        "Retail": "Learn customer service, stocking and basic shop management.",
        "Cooking": "Learn basic kitchen safety, preparation and food handling.",
        "Computer Basics": "Learn typing, spreadsheets, data entry and basic computer use.",
        "Event Support": "Learn teamwork, organization and event assistance.",
        "Tailoring": "Learn basic stitching, measurements and garment handling."
    }

    for skill_name, description in skills.items():

        with st.container(border=True):
            st.subheader(skill_name)
            st.write(description)

# -----------------------------
# ABOUT SDG 1
# -----------------------------

elif page == "About SDG 1":

    st.title("SDG 1 — No Poverty")

    st.write(
        "Sustainable Development Goal 1 aims to end poverty in all its "
        "forms everywhere."
    )

    st.header("The Problem")

    st.write(
        "Many people facing poverty may not have access to stable employment, "
        "formal qualifications or opportunities to learn new skills. "
        "At the same time, households and local businesses often need help "
        "with small tasks."
    )

    st.header("Our Solution")

    st.write(
        "Skill-for-a-Day creates a community system where people can find "
        "short paid work opportunities while gaining useful practical skills."
    )

    st.header("Expected Impact")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Income")
        st.write(
            "Provides short-term earning opportunities for people who need them."
        )

    with col2:
        st.subheader("Skills")
        st.write(
            "Helps people develop practical skills that can improve future employment opportunities."
        )

    st.divider()

    st.success(
        "Skill-for-a-Day connects opportunity, income and skill development "
        "to help move communities towards a future with less poverty."
    )
