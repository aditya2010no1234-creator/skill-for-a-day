import streamlit as st
import pandas as pd
import requests
import uuid

# =========================================================
# SETTINGS
# =========================================================

st.set_page_config(
    page_title="Skill-for-a-Day",
    page_icon="💼",
    layout="wide"
)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyP1cYNf2kVgXXcwGG4d2pLUqD9rOl6nqmCscymAdYQhRdH5Hl2X9soh2S-FHjAQo9x/exec"


# =========================================================
# JOB DATA
# =========================================================

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
        "Ghaziabad",
        "Delhi",
        "Ghaziabad",
        "Noida",
        "Delhi",
        "Noida",
        "Ghaziabad",
        "Noida",
        "Delhi",
        "Ghaziabad"
    ],

    "Pay": [
        350, 500, 400, 450, 350,
        400, 450, 500, 550, 450
    ],

    "Hours": [
        5, 6, 5, 6, 4,
        5, 5, 4, 6, 5
    ],

    "Skill": [
        "Gardening",
        "Painting",
        "Packing",
        "Delivery",
        "Cleaning",
        "Retail",
        "Cooking",
        "Computer Basics",
        "Event Support",
        "Tailoring"
    ],

    "Level": [
        "Beginner",
        "Beginner",
        "Beginner",
        "Intermediate",
        "Beginner",
        "Beginner",
        "Beginner",
        "Beginner",
        "Beginner",
        "Intermediate"
    ]
})


# =========================================================
# SESSION STATE
# =========================================================

if "selected_job" not in st.session_state:
    st.session_state.selected_job = None


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Skill-for-a-Day")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Find Jobs",
        "My Applications",
        "Learn Skills",
        "About SDG 1"
    ],
    key="page"
)


# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.markdown(
        """
        <div style="
            padding: 45px 30px;
            border-radius: 18px;
            background: linear-gradient(135deg, #0f172a, #1e3a8a);
            color: white;
            margin-bottom: 30px;
        ">
            <h1 style="font-size: 48px; margin-bottom: 10px;">
                Skill-for-a-Day
            </h1>
            <h2 style="font-size: 25px; font-weight: 400;">
                Earn today. Learn for tomorrow.
            </h2>
            <p style="font-size: 18px; max-width: 750px;">
                A community platform connecting people with
                short-term paid work while helping them build
                practical skills for better opportunities.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("Turn opportunity into progress")

        st.write(
            "Find simple, short-term jobs, earn an income and "
            "gain practical experience at the same time."
        )

        if st.button(
            "Find Jobs",
            type="primary",
            use_container_width=True
        ):
            st.session_state.page = "Find Jobs"
            st.rerun()

    with col2:

        st.metric(
            "Jobs Available",
            len(jobs)
        )

    st.divider()

    st.subheader("Our Impact")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Jobs", len(jobs))

    with col2:
        st.metric("Skills", jobs["Skill"].nunique())

    with col3:
        st.metric("Locations", jobs["Location"].nunique())

    with col4:
        st.metric("Max Daily Pay", f"₹{jobs['Pay'].max()}")

    st.divider()

    st.subheader("How Skill-for-a-Day Works")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 01 · Find")
        st.write(
            "Browse short-term paid jobs available in your area."
        )

    with c2:
        st.markdown("### 02 · Apply")
        st.write(
            "Choose an opportunity that matches your interests "
            "and submit your application."
        )

    with c3:
        st.markdown("### 03 · Learn & Earn")
        st.write(
            "Complete the work, earn income and gain practical "
            "experience."
        )

    st.divider()

    st.subheader("Why Skill-for-a-Day?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Income")
        st.write(
            "Short-term work can provide immediate earning "
            "opportunities for people who need them."
        )

    with col2:
        st.markdown("### Skills")
        st.write(
            "Every opportunity can help people develop useful "
            "practical skills and experience."
        )

    st.divider()

    st.subheader("Connected to SDG 1 — No Poverty")

    st.info(
        "Skill-for-a-Day supports Sustainable Development Goal 1 "
        "by connecting people with earning opportunities while "
        "encouraging practical skill development."
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:25px;
            margin-top:25px;
        ">
            <h3>Earn → Learn → Grow</h3>
            <p>
                Small opportunities today can create better
                opportunities tomorrow.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
# =========================================================
# FIND JOBS
# =========================================================

elif page == "Find Jobs":

    st.title("Find Jobs")

    st.write(
        "Find short-term paid work opportunities and build useful skills."
    )

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
            filtered["Job"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if location != "All":
        filtered = filtered[
            filtered["Location"] == location
        ]

    if skill != "All":
        filtered = filtered[
            filtered["Skill"] == skill
        ]

    if level != "All":
        filtered = filtered[
            filtered["Level"] == level
        ]

    st.divider()

    if filtered.empty:

        st.warning(
            "No jobs found. Try changing your filters."
        )

    else:

        for index, job in filtered.iterrows():

            with st.container(border=True):

                col1, col2 = st.columns([4, 1])

                with col1:

                    st.subheader(job["Job"])

                    st.write(
                        f"**Location:** {job['Location']}\n\n"
                        f"**Pay:** ₹{job['Pay']}\n\n"
                        f"**Duration:** {job['Hours']} hours\n\n"
                        f"**Skill:** {job['Skill']}\n\n"
                        f"**Level:** {job['Level']}"
                    )

                with col2:

                    if st.button(
                        "Apply",
                        key=f"apply_{index}"
                    ):

                        st.session_state.selected_job = job["Job"]

            # -------------------------------------------------
            # APPLICATION FORM
            # -------------------------------------------------

            if st.session_state.selected_job == job["Job"]:

                st.subheader(
                    f"Apply for {job['Job']}"
                )

                with st.form(
                    f"application_form_{index}"
                ):

                    name = st.text_input(
                        "Your Name"
                    )

                    phone = st.text_input(
                        "Phone Number"
                    )

                    reason = st.text_area(
                        "Why are you suitable for this job?"
                    )

                    submitted = st.form_submit_button(
                        "Submit Application"
                    )

                    if submitted:

                        if not name or not phone:

                            st.error(
                                "Please enter your name and phone number."
                            )

                        else:

                            application_id = phone.strip()

                            application = {

                                "ID": application_id,

                                "Name": name.strip(),

                                "Phone": phone.strip(),

                                "Job": job["Job"],

                                "Location": job["Location"],

                                "Pay": job["Pay"],

                                "Reason": reason.strip()
                            }

                            try:

                                response = requests.post(
                                    GOOGLE_SCRIPT_URL,
                                    json=application,
                                    timeout=15
                                )

                                if response.status_code == 200:

                                    st.success(
                                        "Application submitted successfully!"
                                    )

                                    st.info(
                                        "Your application has been saved permanently. "
                                        "You can view it later from My Applications "
                                        "using the same phone number."
                                    )

                                    st.session_state.selected_job = None

                                else:

                                    st.error(
                                        "Could not save the application. "
                                        "Please try again."
                                    )

                            except Exception as e:

                                st.error(
                                    "Connection error. Please try again."
                                )


# =========================================================
# MY APPLICATIONS
# =========================================================

elif page == "My Applications":

    st.title("My Applications")

    st.write(
        "Enter the same phone number you used while applying "
        "to view your saved applications."
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="Enter your phone number"
    )

    if st.button("View My Applications"):

        if not phone:

            st.warning(
                "Please enter your phone number."
            )

        else:

            try:

                response = requests.get(
                    GOOGLE_SCRIPT_URL,
                    params={"id": phone.strip()},
                    timeout=15
                )

                if response.status_code == 200:

                    data = response.json()

                    if data:

                        application_df = pd.DataFrame(data)

                        application_df = application_df[
                            [
                                "Name",
                                "Phone",
                                "Job",
                                "Location",
                                "Pay",
                                "Reason"
                            ]
                        ]

                        st.success(
                            f"Found {len(data)} application(s)."
                        )

                        for application in data:

                            with st.container(border=True):

                                st.subheader(
                                    application["Job"]
                                )

                                st.write(
                                    f"**Name:** {application['Name']}"
                                )

                                st.write(
                                    f"**Location:** {application['Location']}"
                                )

                                st.write(
                                    f"**Pay:** ₹{application['Pay']}"
                                )

                                st.write(
                                    f"**Reason:** {application['Reason']}"
                                )

                    else:

                        st.info(
                            "No applications were found for this phone number."
                        )

                else:

                    st.error(
                        "Could not retrieve applications."
                    )

            except Exception:

                st.error(
                    "Connection error. Please try again."
                )


# =========================================================
# LEARN SKILLS
# =========================================================

elif page == "Learn Skills":

    st.title("Learn Skills")

    st.write(
        "Skill-for-a-Day is not only about earning money. "
        "It also helps people develop practical skills."
    )

    skills = {

        "Gardening":
            "Learn basic plant care, soil preparation and garden maintenance.",

        "Painting":
            "Learn basic wall preparation, painting and finishing.",

        "Packing":
            "Learn safe and efficient packaging techniques.",

        "Delivery":
            "Learn basic delivery planning and customer interaction.",

        "Cleaning":
            "Learn professional cleaning and organization techniques.",

        "Retail":
            "Learn customer service, stocking and basic shop management.",

        "Cooking":
            "Learn basic kitchen safety, preparation and food handling.",

        "Computer Basics":
            "Learn typing, spreadsheets, data entry and basic computer use.",

        "Event Support":
            "Learn teamwork, organization and event assistance.",

        "Tailoring":
            "Learn basic stitching, measurements and garment handling."
    }

    for skill_name, description in skills.items():

        with st.container(border=True):

            st.subheader(skill_name)

            st.write(description)


# =========================================================
# ABOUT SDG 1
# =========================================================

elif page == "About SDG 1":

    st.title("SDG 1 — No Poverty")

    st.write(
        "Sustainable Development Goal 1 aims to end poverty "
        "in all its forms everywhere."
    )

    st.header("The Problem")

    st.write(
        "Many people facing poverty may not have access to stable "
        "employment, formal qualifications or opportunities to learn "
        "new skills. At the same time, households and local businesses "
        "often need help with small tasks."
    )

    st.header("Our Solution")

    st.write(
        "Skill-for-a-Day creates a community system where people "
        "can find short paid work opportunities while gaining useful "
        "practical skills."
    )

    st.header("Expected Impact")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Income")

        st.write(
            "Provides short-term earning opportunities for people "
            "who need them."
        )

    with col2:

        st.subheader("Skills")

        st.write(
            "Helps people develop practical skills that can improve "
            "future employment opportunities."
        )

    st.divider()

    st.success(
        "Skill-for-a-Day connects opportunity, income and skill "
        "development to help communities move towards a future "
        "with less poverty."
    )
