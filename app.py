import streamlit as st
import pandas as pd
import requests


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Skill-for-a-Day",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyP1cYNf2kVgXXcwGG4d2pLUqD9rOl6nqmCscymAdYQhRdH5Hl2X9soh2S-FHjAQo9x/exec"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        padding-top: 1rem;
    }

    /* Hero */
    .hero {
        padding: 45px 40px;
        border-radius: 24px;
        background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 100%);
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
    }

    .hero h1 {
        font-size: 48px;
        margin: 0;
        font-weight: 750;
    }

    .hero h2 {
        font-size: 25px;
        font-weight: 400;
        margin-top: 8px;
        margin-bottom: 15px;
    }

    .hero p {
        font-size: 17px;
        line-height: 1.6;
        max-width: 800px;
    }

    /* Section heading */
    .section-title {
        font-size: 30px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 16px;
        margin-bottom: 20px;
    }

    /* Job card */
    .job-card {
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        background: white;
        margin-bottom: 10px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
    }

    .job-title {
        font-size: 23px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .job-location {
        color: #475569;
        margin-bottom: 12px;
    }

    .job-pay {
        font-size: 22px;
        font-weight: 700;
    }

    .job-meta {
        color: #475569;
        font-size: 14px;
    }

    /* Feature cards */
    .feature-card {
        padding: 24px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        background: #f8fafc;
        min-height: 170px;
    }

    .feature-card h3 {
        margin-top: 0;
    }

    /* Impact number */
    .impact-number {
        font-size: 32px;
        font-weight: 750;
        margin-bottom: 2px;
    }

    .impact-label {
        color: #64748b;
        font-size: 14px;
    }

    /* Accessibility box */
    .help-box {
        padding: 22px;
        border-radius: 18px;
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 35px 10px 10px 10px;
        color: #64748b;
        font-size: 14px;
    }

    /* Mobile */
    @media (max-width: 768px) {

        .hero {
            padding: 30px 22px;
        }

        .hero h1 {
            font-size: 36px;
        }

        .hero h2 {
            font-size: 21px;
        }

        .hero p {
            font-size: 15px;
        }

        .job-title {
            font-size: 20px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


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
        350,
        500,
        400,
        450,
        350,
        400,
        450,
        500,
        550,
        450
    ],

    "Hours": [
        5,
        6,
        5,
        6,
        4,
        5,
        5,
        4,
        6,
        5
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
# SKILLS DATA
# =========================================================

skills = {
    "Gardening": {
        "description": "Learn basic plant care, soil preparation and garden maintenance.",
        "jobs": "Garden Assistant"
    },

    "Painting": {
        "description": "Learn basic surface preparation, painting and finishing.",
        "jobs": "Painting Helper"
    },

    "Packing": {
        "description": "Learn safe, organised and efficient packaging techniques.",
        "jobs": "Packing Assistant"
    },

    "Delivery": {
        "description": "Learn basic delivery planning, communication and customer interaction.",
        "jobs": "Delivery Helper"
    },

    "Cleaning": {
        "description": "Learn professional cleaning, organisation and workplace hygiene.",
        "jobs": "Cleaning Assistant"
    },

    "Retail": {
        "description": "Learn customer service, stocking and basic shop management.",
        "jobs": "Shop Helper"
    },

    "Cooking": {
        "description": "Learn basic kitchen safety, preparation and food handling.",
        "jobs": "Kitchen Helper"
    },

    "Computer Basics": {
        "description": "Learn typing, spreadsheets, data entry and basic computer use.",
        "jobs": "Data Entry Assistant"
    },

    "Event Support": {
        "description": "Learn teamwork, organisation and event assistance.",
        "jobs": "Event Helper"
    },

    "Tailoring": {
        "description": "Learn basic stitching, measurements and garment handling.",
        "jobs": "Tailoring Assistant"
    }
}


# =========================================================
# SESSION STATE
# =========================================================

if "requested_page" not in st.session_state:
    st.session_state.requested_page = "Home"

if "selected_job" not in st.session_state:
    st.session_state.selected_job = None

if "language" not in st.session_state:
    st.session_state.language = "English"


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Skill-for-a-Day")

st.sidebar.caption("Earn today. Learn for tomorrow.")

language = st.sidebar.radio(
    "Language / भाषा",
    ["English", "हिन्दी"],
    index=0 if st.session_state.language == "English" else 1
)

st.session_state.language = language

st.sidebar.divider()

pages = [
    "Home",
    "Find Jobs",
    "My Applications",
    "Learn Skills",
    "About SDG 1"
]

if language == "हिन्दी":
    page_labels = [
        "होम",
        "काम खोजें",
        "मेरे आवेदन",
        "कौशल सीखें",
        "SDG 1 के बारे में"
    ]
else:
    page_labels = pages


current_index = pages.index(
    st.session_state.requested_page
)

selected_label = st.sidebar.radio(
    "Navigation / नेविगेशन",
    page_labels,
    index=current_index
)

selected_index = page_labels.index(selected_label)

page = pages[selected_index]

st.session_state.requested_page = page


# =========================================================
# HOME
# =========================================================

if page == "Home":

    if language == "हिन्दी":

        st.markdown(
            """
            <div class="hero">

                <h1>Skill-for-a-Day</h1>

                <h2>आज कमाएँ। कल के लिए सीखें।</h2>

                <p>
                    एक ऐसा सामुदायिक प्लेटफ़ॉर्म जो लोगों को
                    छोटे समय के भुगतान वाले कामों से जोड़ता है
                    और साथ ही उपयोगी कौशल सीखने में मदद करता है।
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([2, 1])

        with col1:

            st.markdown(
                '<div class="section-title">काम का अवसर, बेहतर भविष्य</div>',
                unsafe_allow_html=True
            )

            st.write(
                "छोटे समय के काम खोजें, कमाएँ और साथ-साथ "
                "नए कौशल सीखें।"
            )

            if st.button(
                "काम खोजें",
                type="primary",
                use_container_width=True
            ):
                st.session_state.requested_page = "Find Jobs"
                st.rerun()

        with col2:

            st.metric(
                "उपलब्ध काम",
                len(jobs)
            )

        st.divider()

        st.markdown(
            '<div class="section-title">हमारा प्रभाव</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("काम", len(jobs))

        with c2:
            st.metric("कौशल", jobs["Skill"].nunique())

        with c3:
            st.metric("स्थान", jobs["Location"].nunique())

        with c4:
            st.metric(
                "अधिकतम दैनिक भुगतान",
                f"₹{jobs['Pay'].max()}"
            )

        st.divider()

        st.markdown(
            '<div class="section-title">यह कैसे काम करता है?</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>01 · खोजें</h3>
                    <p>अपने आसपास उपलब्ध छोटे समय के काम देखें।</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>02 · आवेदन करें</h3>
                    <p>अपनी पसंद के काम के लिए आवेदन करें।</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>03 · कमाएँ और सीखें</h3>
                    <p>काम करें, कमाएँ और उपयोगी कौशल प्राप्त करें।</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.markdown(
            '<div class="section-title">मदद चाहिए?</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="help-box">
                <h3>आवेदन करने में परेशानी हो रही है?</h3>
                <p>
                    परिवार के सदस्य, स्थानीय स्वयंसेवक, NGO या
                    सामुदायिक केंद्र के व्यक्ति आपकी मदद कर सकते हैं।
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "Skill-for-a-Day SDG 1 — No Poverty से जुड़ा हुआ है।"
        )

    else:

        st.markdown(
            """
            <div class="hero">

                <h1>Skill-for-a-Day</h1>

                <h2>Earn today. Learn for tomorrow.</h2>

                <p>
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

            st.markdown(
                '<div class="section-title">Turn opportunity into progress</div>',
                unsafe_allow_html=True
            )

            st.write(
                "Find short-term work, earn an income and "
                "gain practical experience at the same time."
            )

            if st.button(
                "Find Jobs",
                type="primary",
                use_container_width=True
            ):
                st.session_state.requested_page = "Find Jobs"
                st.rerun()

        with col2:

            st.metric(
                "Jobs Available",
                len(jobs)
            )

        st.divider()

        st.markdown(
            '<div class="section-title">Our Impact</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Jobs", len(jobs))

        with c2:
            st.metric("Skills", jobs["Skill"].nunique())

        with c3:
            st.metric("Locations", jobs["Location"].nunique())

        with c4:
            st.metric(
                "Max Daily Pay",
                f"₹{jobs['Pay'].max()}"
            )

        st.divider()

        st.markdown(
            '<div class="section-title">How Skill-for-a-Day Works</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>01 · Find</h3>
                    <p>Browse short-term paid jobs available in your area.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>02 · Apply</h3>
                    <p>Choose an opportunity that matches your interests.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>03 · Learn & Earn</h3>
                    <p>Complete the work, earn income and gain experience.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.markdown(
            '<div class="section-title">Why Skill-for-a-Day?</div>',
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>Income</h3>
                    <p>
                        Short-term work can provide immediate
                        earning opportunities for people who need them.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                """
                <div class="feature-card">
                    <h3>Skills</h3>
                    <p>
                        Every opportunity can help people develop
                        useful practical skills and experience.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.markdown(
            '<div class="section-title">Connected to SDG 1 — No Poverty</div>',
            unsafe_allow_html=True
        )

        st.info(
            "Skill-for-a-Day supports Sustainable Development Goal 1 "
            "by connecting people with earning opportunities while "
            "encouraging practical skill development."
        )

        st.markdown(
            """
            <div class="footer">
                <h2>Earn → Learn → Grow</h2>
                <p>
                    Small opportunities today can create
                    better opportunities tomorrow.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FIND JOBS
# =========================================================

elif page == "Find Jobs":

    if language == "हिन्दी":

        st.title("काम खोजें")

        st.write(
            "अपने लिए सही छोटा काम खोजें और नए कौशल सीखें।"
        )

        search = st.text_input(
            "काम खोजें",
            placeholder="जैसे: पेंटिंग, गार्डनिंग..."
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            location = st.selectbox(
                "स्थान",
                ["सभी"] + sorted(jobs["Location"].unique())
            )

        with c2:
            skill = st.selectbox(
                "कौशल",
                ["सभी"] + sorted(jobs["Skill"].unique())
            )

        with c3:
            level = st.selectbox(
                "अनुभव",
                ["सभी"] + sorted(jobs["Level"].unique())
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

        if location != "सभी":
            filtered = filtered[
                filtered["Location"] == location
            ]

        if skill != "सभी":
            filtered = filtered[
                filtered["Skill"] == skill
            ]

        if level != "सभी":
            filtered = filtered[
                filtered["Level"] == level
            ]

        st.divider()

        st.write(f"**{len(filtered)} काम उपलब्ध हैं**")

    else:

        st.title("Find Jobs")

        st.write(
            "Find a suitable short-term job and build useful skills."
        )

        search = st.text_input(
            "Search for a job",
            placeholder="Example: painting, gardening..."
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            location = st.selectbox(
                "Location",
                ["All"] + sorted(jobs["Location"].unique())
            )

        with c2:
            skill = st.selectbox(
                "Skill",
                ["All"] + sorted(jobs["Skill"].unique())
            )

        with c3:
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

        st.write(f"**{len(filtered)} job(s) available**")


    # -----------------------------------------------------
    # JOB RESULTS
    # -----------------------------------------------------

    if filtered.empty:

        if language == "हिन्दी":
            st.warning(
                "कोई काम नहीं मिला। फ़िल्टर बदलकर देखें।"
            )
        else:
            st.warning(
                "No jobs found. Try changing your filters."
            )

    else:

        for index, job in filtered.iterrows():

            with st.container(border=True):

                col1, col2 = st.columns([4, 1])

                with col1:

                    st.markdown(
                        f'<div class="job-title">{job["Job"]}</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f'<div class="job-location">Location: {job["Location"]}</div>',
                        unsafe_allow_html=True
                    )

                    m1, m2, m3 = st.columns(3)

                    with m1:
                        st.markdown(
                            f"""
                            <div class="job-pay">
                                ₹{job["Pay"]}
                            </div>
                            <div class="job-meta">
                                {"दैनिक भुगतान" if language == "हिन्दी" else "Daily pay"}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with m2:
                        st.markdown(
                            f"""
                            <div class="job-pay">
                                {job["Hours"]} hrs
                            </div>
                            <div class="job-meta">
                                {"काम का समय" if language == "हिन्दी" else "Work duration"}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with m3:
                        st.markdown(
                            f"""
                            <div class="job-pay">
                                {job["Level"]}
                            </div>
                            <div class="job-meta">
                                {"स्तर" if language == "हिन्दी" else "Experience"}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.write(
                        f"**Skill / कौशल:** {job['Skill']}"
                    )

                with col2:

                    st.write("")

                    if language == "हिन्दी":
                        button_text = "आवेदन करें"
                    else:
                        button_text = "Apply Now"

                    if st.button(
                        button_text,
                        key=f"apply_{index}",
                        type="primary",
                        use_container_width=True
                    ):
                        st.session_state.selected_job = job["Job"]
                        st.rerun()


            # -------------------------------------------------
            # APPLICATION FORM
            # -------------------------------------------------

            if st.session_state.selected_job == job["Job"]:

                st.markdown("---")

                if language == "हिन्दी":

                    st.subheader(
                        f"{job['Job']} के लिए आवेदन"
                    )

                    st.info(
                        f"भुगतान: ₹{job['Pay']} | "
                        f"समय: {job['Hours']} घंटे | "
                        f"स्थान: {job['Location']}"
                    )

                    with st.form(
                        f"application_form_{index}"
                    ):

                        name = st.text_input(
                            "आपका नाम"
                        )

                        phone = st.text_input(
                            "मोबाइल नंबर"
                        )

                        reason = st.text_area(
                            "आप इस काम के लिए सही क्यों हैं?"
                        )

                        submitted = st.form_submit_button(
                            "आवेदन जमा करें",
                            type="primary"
                        )

                else:

                    st.subheader(
                        f"Apply for {job['Job']}"
                    )

                    st.info(
                        f"Pay: ₹{job['Pay']} | "
                        f"Duration: {job['Hours']} hours | "
                        f"Location: {job['Location']}"
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
                            "Submit Application",
                            type="primary"
                        )


                if submitted:

                    if not name.strip() or not phone.strip():

                        if language == "हिन्दी":
                            st.error(
                                "कृपया अपना नाम और मोबाइल नंबर दर्ज करें।"
                            )
                        else:
                            st.error(
                                "Please enter your name and phone number."
                            )

                    else:

                        application = {
                            "ID": phone.strip(),
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

                                if language == "हिन्दी":

                                    st.success(
                                        "आवेदन सफलतापूर्वक जमा हो गया!"
                                    )

                                    st.info(
                                        "आपका आवेदन सुरक्षित रूप से सेव हो गया है। "
                                        "आप My Applications में उसी मोबाइल नंबर "
                                        "से इसे देख सकते हैं।"
                                    )

                                else:

                                    st.success(
                                        "Application submitted successfully!"
                                    )

                                    st.info(
                                        "Your application has been saved. "
                                        "You can view it later from "
                                        "My Applications using the same phone number."
                                    )

                                st.session_state.selected_job = None

                            else:

                                st.error(
                                    "Could not save the application. "
                                    "Please try again."
                                )

                        except Exception:

                            st.error(
                                "Connection error. Please try again."
                            )


    # -----------------------------------------------------
    # HELP SECTION
    # -----------------------------------------------------

    st.divider()

    if language == "हिन्दी":

        st.markdown(
            """
            <div class="help-box">

                <h3>आवेदन करने में मदद चाहिए?</h3>

                <p>
                    यदि आपको वेबसाइट पढ़ने या आवेदन करने में
                    परेशानी हो रही है, तो परिवार के सदस्य,
                    स्वयंसेवक, NGO या सामुदायिक केंद्र से मदद लें।
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="help-box">

                <h3>Need help applying?</h3>

                <p>
                    If someone has difficulty reading or using the
                    website, a family member, volunteer, NGO or
                    community centre can help them apply.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# MY APPLICATIONS
# =========================================================

elif page == "My Applications":

    if language == "हिन्दी":

        st.title("मेरे आवेदन")

        st.write(
            "अपने आवेदन देखने के लिए वही मोबाइल नंबर डालें "
            "जिसका इस्तेमाल आवेदन करते समय किया था।"
        )

        phone = st.text_input(
            "मोबाइल नंबर",
            placeholder="अपना मोबाइल नंबर दर्ज करें"
        )

        view_button = st.button(
            "मेरे आवेदन देखें",
            type="primary"
        )

    else:

        st.title("My Applications")

        st.write(
            "Enter the same phone number you used while applying "
            "to view your saved applications."
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number"
        )

        view_button = st.button(
            "View My Applications",
            type="primary"
        )


    if view_button:

        if not phone.strip():

            if language == "हिन्दी":
                st.warning("कृपया अपना मोबाइल नंबर दर्ज करें।")
            else:
                st.warning("Please enter your phone number.")

        else:

            try:

                response = requests.get(
                    GOOGLE_SCRIPT_URL,
                    params={
                        "id": phone.strip()
                    },
                    timeout=15
                )

                if response.status_code == 200:

                    data = response.json()

                    if data:

                        if language == "हिन्दी":
                            st.success(
                                f"{len(data)} आवेदन मिले।"
                            )
                        else:
                            st.success(
                                f"Found {len(data)} application(s)."
                            )

                        for application in data:

                            with st.container(border=True):

                                st.subheader(
                                    application["Job"]
                                )

                                c1, c2 = st.columns(2)

                                with c1:

                                    st.write(
                                        f"**Name / नाम:** "
                                        f"{application['Name']}"
                                    )

                                    st.write(
                                        f"**Location / स्थान:** "
                                        f"{application['Location']}"
                                    )

                                with c2:

                                    st.write(
                                        f"**Pay / भुगतान:** "
                                        f"₹{application['Pay']}"
                                    )

                                    st.write(
                                        "**Status / स्थिति:** "
                                        "Application Received"
                                    )

                                st.write(
                                    f"**Reason / कारण:** "
                                    f"{application['Reason']}"
                                )

                    else:

                        if language == "हिन्दी":
                            st.info(
                                "इस मोबाइल नंबर से कोई आवेदन नहीं मिला।"
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

    if language == "हिन्दी":

        st.title("कौशल सीखें")

        st.write(
            "यह प्लेटफ़ॉर्म केवल कमाई के बारे में नहीं है। "
            "यह उपयोगी कौशल सीखने में भी मदद करता है।"
        )

    else:

        st.title("Learn Skills")

        st.write(
            "Skill-for-a-Day is not only about earning money. "
            "It also helps people develop useful practical skills."
        )


    for skill_name, information in skills.items():

        with st.container(border=True):

            st.subheader(skill_name)

            if language == "हिन्दी":

                st.write(
                    information["description"]
                )

                st.caption(
                    f"संबंधित काम: {information['jobs']}"
                )

            else:

                st.write(
                    information["description"]
                )

                st.caption(
                    f"Related job: {information['jobs']}"
                )


# =========================================================
# ABOUT SDG 1
# =========================================================

elif page == "About SDG 1":

    if language == "हिन्दी":

        st.title("SDG 1 — गरीबी समाप्त करना")

        st.write(
            "Sustainable Development Goal 1 का उद्देश्य "
            "हर जगह गरीबी को समाप्त करना है।"
        )

        st.divider()

        st.header("समस्या")

        st.write(
            "गरीबी का सामना करने वाले कई लोगों के पास स्थायी "
            "रोज़गार, औपचारिक योग्यता या नए कौशल सीखने के "
            "पर्याप्त अवसर नहीं होते। दूसरी ओर, स्थानीय "
            "दुकानों, व्यवसायों और घरों को छोटे कामों के लिए "
            "मदद की आवश्यकता होती है।"
        )

        st.header("हमारा समाधान")

        st.write(
            "Skill-for-a-Day लोगों को छोटे समय के भुगतान वाले "
            "कामों से जोड़ता है और साथ ही उन्हें उपयोगी "
            "व्यावहारिक कौशल सीखने का अवसर देता है।"
        )

        st.header("अपेक्षित प्रभाव")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(
                """
                <div class="feature-card">
                    <h3>कमाई</h3>
                    <p>
                        लोगों को कम समय में आय कमाने
                        के अवसर मिल सकते हैं।
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                """
                <div class="feature-card">
                    <h3>कौशल</h3>
                    <p>
                        लोगों को ऐसे व्यावहारिक कौशल सीखने
                        में मदद मिलती है जो भविष्य के काम में
                        उपयोगी हो सकते हैं।
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.success(
            "कमाएँ → सीखें → आगे बढ़ें"
        )

    else:

        st.title("SDG 1 — No Poverty")

        st.write(
            "Sustainable Development Goal 1 aims to end "
            "poverty in all its forms everywhere."
        )

        st.divider()

        st.header("The Problem")

        st.write(
            "Many people facing poverty may not have access "
            "to stable employment, formal qualifications or "
            "opportunities to learn useful skills. At the same "
            "time, households and local businesses often need "
            "help with small tasks."
        )

        st.header("Our Solution")

        st.write(
            "Skill-for-a-Day creates a community system where "
            "people can find short-term paid work opportunities "
            "while gaining useful practical skills."
        )

        st.header("Expected Impact")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(
                """
                <div class="feature-card">
                    <h3>Income</h3>
                    <p>
                        Provides short-term earning opportunities
                        for people who need them.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                """
                <div class="feature-card">
                    <h3>Skills</h3>
                    <p>
                        Helps people develop practical skills that
                        can improve future employment opportunities.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.success(
            "Skill-for-a-Day connects opportunity, income "
            "and skill development to help communities move "
            "towards a future with less poverty."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Skill-for-a-Day · A community initiative supporting SDG 1
    </div>
    """,
    unsafe_allow_html=True
)
