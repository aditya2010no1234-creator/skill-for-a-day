import streamlit as st
import pandas as pd
import requests


# =========================================================
# SETTINGS
# =========================================================

st.set_page_config(
    page_title="Skill-for-a-Day",
    page_icon="💼",
    layout="wide"
)

admin_mode = st.query_params.get("admin") == "true"

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyP1cYNf2kVgXXcwGG4d2pLUqD9rOl6nqmCscymAdYQhRdH5Hl2X9soh2S-FHjAQo9x/exec"

ADMIN_PIN = "9911"


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
        5, 5, 5, 6, 5
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

if "selected_skill" not in st.session_state:
    st.session_state.selected_skill = None

if "requested_page" not in st.session_state:
    st.session_state.requested_page = "Home"


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Skill-for-a-Day")

language = st.sidebar.radio(
    "Language",
    ["English", "हिन्दी"]
)

pages = [
    "Home",
    "Find Jobs",
    "My Applications",
    "Learn Skills",
    "About SDG 1"
]

current_page = st.session_state.requested_page

if current_page not in pages:
    current_page = "Home"

page = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(current_page)
)

st.session_state.requested_page = page


# =========================================================
# HOME
# =========================================================

if page == "Home":

    if language == "English":

        # Hero
        st.markdown(
            """<div style="padding:45px 35px; border-radius:20px; background:linear-gradient(135deg, #0f172a, #1e3a8a); color:white; margin-bottom:30px;">
<h1 style="font-size:48px; margin-bottom:8px;">Skill-for-a-Day</h1>
<h2 style="font-size:25px; font-weight:400; margin-bottom:15px;">Earn today. Learn for tomorrow.</h2>
<p style="font-size:18px; max-width:800px; line-height:1.6;">A community platform connecting people with short-term paid work while helping them build practical skills for better opportunities.</p>
</div>""",
            unsafe_allow_html=True
        )

        # Main introduction
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

                st.session_state.requested_page = "Find Jobs"
                st.rerun()

        with col2:

            st.metric(
                "Jobs Available",
                len(jobs)
            )

        st.divider()

        # Impact
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

        # How it works
        st.subheader("How Skill-for-a-Day Works")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("### 01 · Find")
            st.write(
                "Browse short-term paid jobs available "
                "in your area."
            )

        with c2:
            st.markdown("### 02 · Apply")
            st.write(
                "Choose an opportunity that matches your "
                "interests and submit your application."
            )

        with c3:
            st.markdown("### 03 · Learn & Earn")
            st.write(
                "Complete the work, earn income and gain "
                "practical experience."
            )

        st.divider()

        # Why Skill-for-a-Day
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

        # SDG 1
        st.subheader("Connected to SDG 1 — No Poverty")

        st.info(
            "Skill-for-a-Day supports Sustainable Development "
            "Goal 1 by connecting people with earning opportunities "
            "while encouraging practical skill development."
        )

        # Final message
        st.markdown(
            """<div style="text-align:center; padding:25px; margin-top:20px;">
<h2>Earn → Learn → Grow</h2>
<p style="font-size:17px;">Small opportunities today can create better opportunities tomorrow.</p>
</div>""",
            unsafe_allow_html=True
        )


    else:

        # Hero
        st.markdown(
            """<div style="padding:45px 35px; border-radius:20px; background:linear-gradient(135deg, #0f172a, #1e3a8a); color:white; margin-bottom:30px;">
<h1 style="font-size:48px; margin-bottom:8px;">स्किल-फॉर-ए-डे</h1>
<h2 style="font-size:25px; font-weight:400; margin-bottom:15px;">आज कमाएँ। कल के लिए सीखें।</h2>
<p style="font-size:18px; max-width:800px; line-height:1.6;">एक सामुदायिक मंच जो लोगों को थोड़े समय के भुगतान वाले काम से जोड़ता है और बेहतर अवसरों के लिए उपयोगी कौशल सीखने में मदद करता है।</p>
</div>""",
            unsafe_allow_html=True
        )

        # Main introduction
        col1, col2 = st.columns([2, 1])

        with col1:

            st.subheader("अवसर को प्रगति में बदलें")

            st.write(
                "सरल और कम समय वाले काम खोजें, आय कमाएँ और "
                "साथ ही व्यावहारिक अनुभव प्राप्त करें।"
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

        # Impact
        st.subheader("हमारा प्रभाव")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("काम", len(jobs))

        with col2:
            st.metric("कौशल", jobs["Skill"].nunique())

        with col3:
            st.metric("स्थान", jobs["Location"].nunique())

        with col4:
            st.metric("अधिकतम दैनिक भुगतान", f"₹{jobs['Pay'].max()}")

        st.divider()

        # How it works
        st.subheader("स्किल-फॉर-ए-डे कैसे काम करता है")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("### 01 · खोजें")
            st.write(
                "अपने क्षेत्र में उपलब्ध कम समय वाले "
                "भुगतान वाले काम देखें।"
            )

        with c2:
            st.markdown("### 02 · आवेदन करें")
            st.write(
                "अपनी रुचि के अनुसार काम चुनें और "
                "आवेदन जमा करें।"
            )

        with c3:
            st.markdown("### 03 · सीखें और कमाएँ")
            st.write(
                "काम पूरा करें, आय कमाएँ और "
                "व्यावहारिक अनुभव प्राप्त करें।"
            )

        st.divider()

        # Why Skill-for-a-Day
        st.subheader("स्किल-फॉर-ए-डे क्यों?")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### आय")
            st.write(
                "कम समय वाले काम उन लोगों के लिए "
                "तुरंत आय कमाने के अवसर दे सकते हैं जिन्हें इसकी आवश्यकता है।"
            )

        with col2:
            st.markdown("### कौशल")
            st.write(
                "हर काम लोगों को उपयोगी व्यावहारिक "
                "कौशल और अनुभव विकसित करने में मदद कर सकता है।"
            )

        st.divider()

        # SDG 1
        st.subheader("SDG 1 — गरीबी समाप्त करना")

        st.info(
            "स्किल-फॉर-ए-डे लोगों को आय कमाने के अवसरों "
            "से जोड़कर और व्यावहारिक कौशल के विकास को बढ़ावा देकर "
            "सतत विकास लक्ष्य 1 का समर्थन करता है।"
        )

        # Final message
        st.markdown(
            """<div style="text-align:center; padding:25px; margin-top:20px;">
<h2>कमाएँ → सीखें → आगे बढ़ें</h2>
<p style="font-size:17px;">आज के छोटे अवसर कल के बेहतर अवसर बना सकते हैं।</p>
</div>""",
            unsafe_allow_html=True
        )

# =========================================================
# FIND JOBS
# =========================================================

elif page == "Find Jobs":

    if language == "English":

        st.title("Find Jobs")

        st.write(
            "Find short-term paid work opportunities "
            "and build useful skills."
        )

        # Search
        search = st.text_input(
            "Search for a job",
            placeholder="Example: painting, gardening..."
        )

        # Filters
        col1, col2, col3 = st.columns(3)

        with col1:

            location = st.selectbox(
                "Location",
                ["All"] + sorted(
                    jobs["Location"].unique()
                )
            )

        with col2:

            skill = st.selectbox(
                "Skill",
                ["All"] + sorted(
                    jobs["Skill"].unique()
                )
            )

        with col3:

            level = st.selectbox(
                "Experience Level",
                ["All"] + sorted(
                    jobs["Level"].unique()
                )
            )

        # Filter jobs
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

        # Job results
        if filtered.empty:

            st.warning(
                "No jobs found. Try changing your filters."
            )

        else:

            st.write(
                f"**{len(filtered)} job(s) available**"
            )

            for index, job in filtered.iterrows():

                with st.container(border=True):

                    col1, col2 = st.columns([4, 1])

                    with col1:

                        st.subheader(
                            job["Job"]
                        )

                        st.write(
                            f"**Location:** {job['Location']}"
                        )

                        st.write(
                            f"**Pay:** ₹{job['Pay']}"
                        )

                        st.write(
                            f"**Duration:** {job['Hours']} hours"
                        )

                        st.write(
                            f"**Skill:** {job['Skill']}"
                        )

                        st.write(
                            f"**Experience:** {job['Level']}"
                        )

                    with col2:

                        st.write("")

                        if st.button(
                            "Apply",
                            key=f"apply_{index}",
                            use_container_width=True
                        ):

                            st.session_state.selected_job = job["Job"]

                        if st.button(
                            "Learn Skill",
                            key=f"learn_skill_{index}",
                            use_container_width=True
                        ):

                            st.session_state.selected_skill = job["Skill"]
                            st.session_state.requested_page = "Learn Skills"
                            st.rerun()

                    # Application form
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
                                        "Please enter your name "
                                        "and phone number."
                                    )

                                else:

                                    application = {

                                        "ID": phone.strip(),

                                        "Name": name.strip(),

                                        "Phone": phone.strip(),

                                        "Job": job["Job"],

                                        "Location": job["Location"],

                                        "Pay": job["Pay"],

                                        "Reason": reason.strip(),
                                    
                                        "Status": "Applied"
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
                                                "Your application has been "
                                                "saved permanently. You can "
                                                "view it later from My Applications "
                                                "using the same phone number."
                                            )

                                            st.session_state.selected_job = None

                                        else:

                                            st.error(
                                                "Could not save the application. "
                                                "Please try again."
                                            )

                                    except Exception:

                                        st.error(
                                            "Connection error. "
                                            "Please try again."
                                        )


    else:

        st.title("काम खोजें")

        st.write(
            "कम समय वाले भुगतान वाले काम खोजें "
            "और उपयोगी कौशल सीखें।"
        )

        # Search
        search = st.text_input(
            "काम खोजें",
            placeholder="उदाहरण: पेंटिंग, बागवानी..."
        )

        # Filters
        col1, col2, col3 = st.columns(3)

        with col1:

            location = st.selectbox(
                "स्थान",
                ["सभी"] + sorted(
                    jobs["Location"].unique()
                )
            )

        with col2:

            skill = st.selectbox(
                "कौशल",
                ["सभी"] + sorted(
                    jobs["Skill"].unique()
                )
            )

        with col3:

            level = st.selectbox(
                "अनुभव का स्तर",
                ["सभी"] + sorted(
                    jobs["Level"].unique()
                )
            )

        # Filter jobs
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

        # Job results
        if filtered.empty:

            st.warning(
                "कोई काम नहीं मिला। फ़िल्टर बदलकर देखें।"
            )

        else:

            st.write(
                f"**{len(filtered)} काम उपलब्ध हैं**"
            )

            for index, job in filtered.iterrows():

                with st.container(border=True):

                    col1, col2 = st.columns([4, 1])

                    with col1:

                        st.subheader(
                            job["Job"]
                        )

                        st.write(
                            f"**स्थान:** {job['Location']}"
                        )

                        st.write(
                            f"**भुगतान:** ₹{job['Pay']}"
                        )

                        st.write(
                            f"**अवधि:** {job['Hours']} घंटे"
                        )

                        st.write(
                            f"**कौशल:** {job['Skill']}"
                        )

                        st.write(
                            f"**अनुभव:** {job['Level']}"
                        )

                    with col2:

                        st.write("")

                        if st.button(
                            "आवेदन करें",
                            key=f"apply_{index}",
                            use_container_width=True
                        ):

                            st.session_state.selected_job = job["Job"]

                        if st.button(
                            "कौशल सीखें",
                            key=f"learn_skill_{index}",
                            use_container_width=True
                        ):

                            st.session_state.selected_skill = job["Skill"]
                            st.session_state.requested_page = "Learn Skills"
                            st.rerun()

                    # Application form
                    if st.session_state.selected_job == job["Job"]:

                        st.subheader(
                            f"{job['Job']} के लिए आवेदन करें"
                        )

                        with st.form(
                            f"application_form_{index}"
                        ):

                            name = st.text_input(
                                "आपका नाम"
                            )

                            phone = st.text_input(
                                "फ़ोन नंबर"
                            )

                            reason = st.text_area(
                                "आप इस काम के लिए उपयुक्त क्यों हैं?"
                            )

                            submitted = st.form_submit_button(
                                "आवेदन जमा करें"
                            )

                            if submitted:

                                if not name or not phone:

                                    st.error(
                                        "कृपया अपना नाम और "
                                        "फ़ोन नंबर दर्ज करें।"
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

                                            st.success(
                                                "आवेदन सफलतापूर्वक जमा हो गया!"
                                            )

                                            st.info(
                                                "आपका आवेदन स्थायी रूप से "
                                                "सहेज लिया गया है। आप बाद में "
                                                "उसी फ़ोन नंबर से अपने आवेदन "
                                                "देख सकते हैं।"
                                            )

                                            st.session_state.selected_job = None

                                        else:

                                            st.error(
                                                "आवेदन सहेजा नहीं जा सका। "
                                                "कृपया फिर से प्रयास करें।"
                                            )

                                    except Exception:

                                        st.error(
                                            "कनेक्शन में समस्या हुई। "
                                            "कृपया फिर से प्रयास करें।"
                                        )


# =========================================================
# MY APPLICATIONS
# =========================================================


elif page == "My Applications":

    if language == "English":

        st.title("My Applications")

        st.write(
            "Enter the same phone number you used while applying "
            "to view your saved applications."
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number"
        )

        if st.button(
            "View My Applications",
            type="primary"
        ):

            if not phone:

                st.warning(
                    "Please enter your phone number."
                )

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

                            st.success(
                                f"Found {len(data)} application(s)."
                            )

                            for application in data:

                                with st.container(
                                    border=True
                                ):

                                    st.subheader(
                                        application["Job"]
                                    )

                                    st.write(
                                        f"**Name:** "
                                        f"{application['Name']}"
                                    )

                                    st.write(
                                        f"**Location:** "
                                        f"{application['Location']}"
                                    )

                                    st.write(
                                        f"**Pay:** "
                                        f"₹{application['Pay']}"
                                    )

                                    status = application.get("Status", "Applied")

                                    if status == "Accepted":
                                        st.success("Status: Accepted")
                                    elif status == "Rejected":
                                        st.error("Status: Rejected")
                                    elif status == "Under Review":
                                        st.warning("Status: Under Review")
                                    else:
                                        st.info("Status: Applied")

                                    st.write(
                                        f"**Status:** "
                                        f"{application['Status']}"
                                    )

                        else:

                            st.info(
                                "No applications were found "
                                "for this phone number."
                            )

                    else:

                        st.error(
                            "Could not retrieve applications."
                        )

                except Exception:

                    st.error(
                        "Connection error. Please try again."
                    )


    else:

        st.title("मेरे आवेदन")

        st.write(
            "अपने सहेजे गए आवेदन देखने के लिए वही "
            "फ़ोन नंबर दर्ज करें जिसका उपयोग आपने आवेदन करते समय किया था।"
        )

        phone = st.text_input(
            "फ़ोन नंबर",
            placeholder="अपना फ़ोन नंबर दर्ज करें"
        )

        if st.button(
            "मेरे आवेदन देखें",
            type="primary"
        ):

            if not phone:

                st.warning(
                    "कृपया अपना फ़ोन नंबर दर्ज करें।"
                )

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

                            st.success(
                                f"{len(data)} आवेदन मिले।"
                            )

                            for application in data:

                                with st.container(
                                    border=True
                                ):

                                    st.subheader(
                                        application["Job"]
                                    )

                                    st.write(
                                        f"**नाम:** "
                                        f"{application['Name']}"
                                    )

                                    st.write(
                                        f"**स्थान:** "
                                        f"{application['Location']}"
                                    )

                                    st.write(
                                        f"**भुगतान:** "
                                        f"₹{application['Pay']}"
                                    )

                                    st.write(
                                        f"**कारण:** "
                                        f"{application['Reason']}"
                                    )

                                    status = application.get("Status", "Applied")

                                    if status == "Accepted":
                                        st.success("स्थिति: स्वीकृत")
                                    elif status == "Rejected":
                                        st.error("स्थिति: अस्वीकृत")
                                    elif status == "Under Review":
                                        st.warning("स्थिति: समीक्षा में")
                                    else:
                                        st.info("स्थिति: आवेदन किया गया")

                        else:

                            st.info(
                                "इस फ़ोन नंबर के लिए "
                                "कोई आवेदन नहीं मिला।"
                            )

                    else:

                        st.error(
                            "आवेदन प्राप्त नहीं किए जा सके।"
                        )

                except Exception:

                    st.error(
                        "कनेक्शन में समस्या हुई। "
                        "कृपया फिर से प्रयास करें।"
                    )
                    

# =========================================================
# LEARN SKILLS
# =========================================================


elif page == "Learn Skills":

    if language == "English":

        st.title("Learn Skills")

        st.write(
            "Build practical skills that can help you perform jobs "
            "and prepare for better opportunities."
        )

        skill_lessons = {

            "Gardening": {
                "title": "Gardening Basics",
                "description": (
                    "Learn how to care for plants and maintain a garden."
                ),
                "steps": [
                    "Understand basic plant care.",
                    "Learn how to prepare and maintain soil.",
                    "Learn basic watering and plant maintenance.",
                    "Keep the garden clean and organized."
                ]
            },

            "Painting": {
                "title": "Painting Basics",
                "description": (
                    "Learn the basic process of preparing and painting surfaces."
                ),
                "steps": [
                    "Prepare and clean the surface.",
                    "Understand basic painting tools.",
                    "Learn how to apply paint evenly.",
                    "Keep the work area clean and organized."
                ]
            },

            "Packing": {
                "title": "Packing Basics",
                "description": (
                    "Learn how to pack items safely and efficiently."
                ),
                "steps": [
                    "Identify the item and choose suitable packaging.",
                    "Place the item securely inside the package.",
                    "Protect fragile items properly.",
                    "Check the package before it is moved or delivered."
                ]
            },

            "Delivery": {
                "title": "Delivery Basics",
                "description": (
                    "Learn basic delivery planning and customer interaction."
                ),
                "steps": [
                    "Check the delivery details carefully.",
                    "Plan the route before starting.",
                    "Handle the package carefully.",
                    "Communicate politely with the customer."
                ]
            },

            "Cleaning": {
                "title": "Cleaning Basics",
                "description": (
                    "Learn basic cleaning and organization techniques."
                ),
                "steps": [
                    "Understand the area that needs cleaning.",
                    "Organize the cleaning tools.",
                    "Clean surfaces systematically.",
                    "Keep the area organized after finishing."
                ]
            },

            "Retail": {
                "title": "Retail Basics",
                "description": (
                    "Learn basic customer service and shop assistance."
                ),
                "steps": [
                    "Greet customers politely.",
                    "Learn how products are organized.",
                    "Keep shelves and products organized.",
                    "Assist customers clearly and respectfully."
                ]
            },

            "Cooking": {
                "title": "Kitchen Basics",
                "description": (
                    "Learn basic kitchen organization, preparation and safety."
                ),
                "steps": [
                    "Keep the workspace clean.",
                    "Understand basic kitchen tools.",
                    "Prepare ingredients carefully.",
                    "Follow safe food-handling practices."
                ]
            },

            "Computer Basics": {
                "title": "Computer Basics",
                "description": (
                    "Learn basic computer skills useful for data entry work."
                ),
                "steps": [
                    "Learn basic keyboard and mouse use.",
                    "Practice typing accurately.",
                    "Understand basic spreadsheet use.",
                    "Learn how to enter and organize information."
                ]
            },

            "Event Support": {
                "title": "Event Support Basics",
                "description": (
                    "Learn basic teamwork and organization for events."
                ),
                "steps": [
                    "Understand the event schedule.",
                    "Help organize materials and equipment.",
                    "Work cooperatively with the team.",
                    "Assist guests and complete assigned tasks."
                ]
            },

            "Tailoring": {
                "title": "Tailoring Basics",
                "description": (
                    "Learn basic stitching, measurements and garment handling."
                ),
                "steps": [
                    "Understand basic tailoring tools.",
                    "Learn how measurements are taken.",
                    "Practice basic stitching techniques.",
                    "Handle and organize garments carefully."
                ]
            }
        }

        # Show selected skill
        if st.session_state.selected_skill:

            selected_skill = st.session_state.selected_skill

            if selected_skill in skill_lessons:

                lesson = skill_lessons[selected_skill]

                st.subheader(
                    f"Learning: {lesson['title']}"
                )

                st.write(
                    lesson["description"]
                )

                st.markdown("### What you will learn")

                for number, step in enumerate(
                    lesson["steps"],
                    start=1
                ):

                    st.write(
                        f"**{number}.** {step}"
                    )

                st.divider()

                if st.button("View All Skills"):

                    st.session_state.selected_skill = None
                    st.rerun()

        # Show all skills
        if not st.session_state.selected_skill:

            st.subheader("Choose a Skill")

            for skill_name, lesson in skill_lessons.items():

                with st.container(border=True):

                    st.subheader(
                        lesson["title"]
                    )

                    st.write(
                        lesson["description"]
                    )

                    if st.button(
                        "Learn This Skill",
                        key=f"learn_{skill_name}"
                    ):

                        st.session_state.selected_skill = skill_name
                        st.rerun()


    else:

        st.title("कौशल सीखें")

        st.write(
            "ऐसे व्यावहारिक कौशल सीखें जो आपको काम करने "
            "और बेहतर अवसरों के लिए तैयार होने में मदद कर सकते हैं।"
        )

        skill_lessons = {

            "Gardening": {
                "title": "बागवानी की मूल बातें",
                "description": (
                    "पौधों की देखभाल करना और बगीचे को बनाए रखना सीखें।"
                ),
                "steps": [
                    "पौधों की मूल देखभाल समझें।",
                    "मिट्टी तैयार करना और उसकी देखभाल करना सीखें।",
                    "पानी देने और पौधों की देखभाल की मूल बातें सीखें।",
                    "बगीचे को साफ और व्यवस्थित रखें।"
                ]
            },

            "Painting": {
                "title": "पेंटिंग की मूल बातें",
                "description": (
                    "सतह तैयार करने और उस पर पेंट करने की मूल प्रक्रिया सीखें।"
                ),
                "steps": [
                    "सतह को तैयार और साफ करें।",
                    "पेंटिंग के मूल उपकरणों को समझें।",
                    "पेंट को समान रूप से लगाना सीखें।",
                    "काम की जगह को साफ और व्यवस्थित रखें।"
                ]
            },

            "Packing": {
                "title": "पैकिंग की मूल बातें",
                "description": (
                    "सामान को सुरक्षित और सही तरीके से पैक करना सीखें।"
                ),
                "steps": [
                    "सामान की पहचान करें और सही पैकिंग सामग्री चुनें।",
                    "सामान को पैकेज के अंदर सुरक्षित रखें।",
                    "नाज़ुक सामान की सही तरह से सुरक्षा करें।",
                    "सामान भेजने से पहले पैकेज की जाँच करें।"
                ]
            },

            "Delivery": {
                "title": "डिलीवरी की मूल बातें",
                "description": (
                    "डिलीवरी की योजना बनाना और ग्राहकों से बातचीत करना सीखें।"
                ),
                "steps": [
                    "डिलीवरी की जानकारी ध्यान से जाँचें।",
                    "शुरू करने से पहले रास्ते की योजना बनाएँ।",
                    "सामान को सावधानी से संभालें।",
                    "ग्राहक से विनम्रता से बात करें।"
                ]
            },

            "Cleaning": {
                "title": "सफाई की मूल बातें",
                "description": (
                    "सफाई और सामान व्यवस्थित रखने की मूल तकनीकें सीखें।"
                ),
                "steps": [
                    "जिस जगह की सफाई करनी है उसे समझें।",
                    "सफाई के उपकरण व्यवस्थित करें।",
                    "सतहों को सही तरीके से साफ करें।",
                    "काम पूरा होने के बाद जगह को व्यवस्थित रखें।"
                ]
            },

            "Retail": {
                "title": "दुकान के काम की मूल बातें",
                "description": (
                    "ग्राहक सेवा और दुकान में सहायता करने की मूल बातें सीखें।"
                ),
                "steps": [
                    "ग्राहकों का विनम्रता से स्वागत करें।",
                    "सामान को व्यवस्थित करने का तरीका सीखें।",
                    "अलमारियों और सामान को व्यवस्थित रखें।",
                    "ग्राहकों की स्पष्ट और सम्मानपूर्वक सहायता करें।"
                ]
            },

            "Cooking": {
                "title": "रसोई की मूल बातें",
                "description": (
                    "रसोई को व्यवस्थित रखना, तैयारी करना और सुरक्षा की मूल बातें सीखें।"
                ),
                "steps": [
                    "काम की जगह को साफ रखें।",
                    "रसोई के मूल उपकरणों को समझें।",
                    "सामग्री को सावधानी से तैयार करें।",
                    "भोजन को सुरक्षित तरीके से संभालने के नियमों का पालन करें।"
                ]
            },

            "Computer Basics": {
                "title": "कंप्यूटर की मूल बातें",
                "description": (
                    "डेटा एंट्री के काम के लिए उपयोगी कंप्यूटर कौशल सीखें।"
                ),
                "steps": [
                    "कीबोर्ड और माउस का मूल उपयोग सीखें।",
                    "सही तरीके से टाइप करने का अभ्यास करें।",
                    "स्प्रेडशीट के मूल उपयोग को समझें।",
                    "जानकारी दर्ज करना और व्यवस्थित करना सीखें।"
                ]
            },

            "Event Support": {
                "title": "कार्यक्रम सहायता की मूल बातें",
                "description": (
                    "कार्यक्रमों के लिए टीमवर्क और व्यवस्था की मूल बातें सीखें।"
                ),
                "steps": [
                    "कार्यक्रम की समय-सारणी समझें।",
                    "सामान और उपकरण व्यवस्थित करने में मदद करें।",
                    "टीम के साथ मिलकर काम करें।",
                    "मेहमानों की सहायता करें और दिए गए काम पूरे करें।"
                ]
            },

            "Tailoring": {
                "title": "सिलाई की मूल बातें",
                "description": (
                    "सिलाई, नाप और कपड़ों को संभालने की मूल बातें सीखें।"
                ),
                "steps": [
                    "सिलाई के मूल उपकरणों को समझें।",
                    "नाप लेने का तरीका सीखें।",
                    "सिलाई की मूल तकनीकों का अभ्यास करें।",
                    "कपड़ों को सावधानी से संभालें और व्यवस्थित रखें।"
                ]
            }
        }

        # Show selected skill
        if st.session_state.selected_skill:

            selected_skill = st.session_state.selected_skill

            if selected_skill in skill_lessons:

                lesson = skill_lessons[selected_skill]

                st.subheader(
                    f"सीख रहे हैं: {lesson['title']}"
                )

                st.write(
                    lesson["description"]
                )

                st.markdown("### आप क्या सीखेंगे")

                for number, step in enumerate(
                    lesson["steps"],
                    start=1
                ):

                    st.write(
                        f"**{number}.** {step}"
                    )

                st.divider()

                if st.button("सभी कौशल देखें"):

                    st.session_state.selected_skill = None
                    st.rerun()

        # Show all skills
        if not st.session_state.selected_skill:

            st.subheader("एक कौशल चुनें")

            for skill_name, lesson in skill_lessons.items():

                with st.container(border=True):

                    st.subheader(
                        lesson["title"]
                    )

                    st.write(
                        lesson["description"]
                    )

                    if st.button(
                        "यह कौशल सीखें",
                        key=f"learn_{skill_name}"
                    ):

                        st.session_state.selected_skill = skill_name
                        st.rerun()

# =========================================================
# ABOUT SDG 1
# =========================================================

elif page == "About SDG 1":

    if language == "English":

        st.title("SDG 1 — No Poverty")

        st.write(
            "Sustainable Development Goal 1 aims to end "
            "poverty in all its forms everywhere."
        )

        st.header("The Problem")

        st.write(
            "Many people facing poverty may not have access "
            "to stable employment, formal qualifications or "
            "opportunities to learn new skills. At the same time, "
            "households and local businesses often need help "
            "with small tasks."
        )

        st.header("Our Solution")

        st.write(
            "Skill-for-a-Day creates a community system where "
            "people can find short paid work opportunities while "
            "gaining useful practical skills."
        )

        st.header("Expected Impact")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Income")

            st.write(
                "Provides short-term earning opportunities "
                "for people who need them."
            )

        with col2:

            st.subheader("Skills")

            st.write(
                "Helps people develop practical skills that "
                "can improve future employment opportunities."
            )

        st.divider()

        st.success(
            "Skill-for-a-Day connects opportunity, income "
            "and skill development to help communities move "
            "towards a future with less poverty."
        )


    else:

        st.title("एसडीजी 1 — गरीबी समाप्त करना")

        st.write(
            "सतत विकास लक्ष्य 1 का उद्देश्य हर जगह "
            "हर प्रकार की गरीबी को समाप्त करना है।"
        )

        st.header("समस्या")

        st.write(
            "गरीबी का सामना कर रहे कई लोगों के पास स्थायी "
            "रोज़गार, औपचारिक योग्यताओं या नए कौशल सीखने "
            "के अवसरों तक पर्याप्त पहुँच नहीं होती। वहीं, "
            "घरों और स्थानीय व्यवसायों को अक्सर छोटे-मोटे "
            "कामों में सहायता की आवश्यकता होती है।"
        )

        st.header("हमारा समाधान")

        st.write(
            "स्किल-फॉर-ए-डे एक सामुदायिक व्यवस्था बनाता है "
            "जहाँ लोग कम समय वाले भुगतान किए गए काम के "
            "अवसर प्राप्त कर सकते हैं और साथ ही उपयोगी "
            "व्यावहारिक कौशल सीख सकते हैं।"
        )

        st.header("अपेक्षित प्रभाव")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("आय")

            st.write(
                "जिन लोगों को इसकी आवश्यकता है, उनके लिए "
                "कम समय में आय अर्जित करने के अवसर प्रदान करता है।"
            )

        with col2:

            st.subheader("कौशल")

            st.write(
                "लोगों को ऐसे व्यावहारिक कौशल विकसित करने में "
                "मदद करता है जो भविष्य में रोज़गार के अवसरों "
                "को बेहतर बना सकते हैं।"
            )

        st.divider()

        st.success(
            "स्किल-फॉर-ए-डे अवसर, आय और कौशल विकास को "
            "एक साथ जोड़कर समुदायों को कम गरीबी वाले "
            "बेहतर भविष्य की ओर बढ़ने में मदद करता है।"
        )

# =========================================================
# ADMIN DASHBOARD
# =========================================================

elif page == "Admin Dashboard":

    if language == "English":

        st.title("Admin Dashboard")

        st.write(
            "View applications and manage their status."
        )

        pin = st.text_input(
            "Admin PIN",
            type="password"
        )

        if pin != ADMIN_PIN:

            if pin:
                st.error("Incorrect Admin PIN.")

            st.info(
                "Enter the Admin PIN to access the dashboard."
            )

        else:

            st.success("Admin access granted.")

            try:

                response = requests.get(
                    GOOGLE_SCRIPT_URL,
                    params={"admin": "true"},
                    timeout=15
                )

                if response.status_code == 200:

                    data = response.json()

                    if data:

                        st.subheader(
                            f"Total Applications: {len(data)}"
                        )

                        status_filter = st.selectbox(
                            "Filter by Status",
                            [
                                "All",
                                "Applied",
                                "Under Review",
                                "Accepted",
                                "Rejected"
                            ]
                        )

                        filtered_apps = data

                        if status_filter != "All":

                            filtered_apps = [
                                app for app in data
                                if app.get("Status", "Applied") == status_filter
                            ]

                        st.write(
                            f"Showing {len(filtered_apps)} application(s)"
                        )

                        for number, application in enumerate(
                            filtered_apps
                        ):

                            with st.container(border=True):

                                st.subheader(
                                    application["Job"]
                                )

                                st.write(
                                    f"**Name:** "
                                    f"{application['Name']}"
                                )

                                st.write(
                                    f"**Phone:** "
                                    f"{application['Phone']}"
                                )

                                st.write(
                                    f"**Location:** "
                                    f"{application['Location']}"
                                )

                                st.write(
                                    f"**Pay:** "
                                    f"₹{application['Pay']}"
                                )

                                st.write(
                                    f"**Reason:** "
                                    f"{application['Reason']}"
                                )

                                current_status = application.get(
                                    "Status",
                                    "Applied"
                                )

                                new_status = st.selectbox(
                                    "Application Status",
                                    [
                                        "Applied",
                                        "Under Review",
                                        "Accepted",
                                        "Rejected"
                                    ],
                                    index=[
                                        "Applied",
                                        "Under Review",
                                        "Accepted",
                                        "Rejected"
                                    ].index(current_status),
                                    key=f"status_{number}_{application['ID']}"
                                )

                                if st.button(
                                    "Update Status",
                                    key=f"update_{number}_{application['ID']}",
                                    type="primary"
                                ):

                                    update_data = {
                                        "action": "update_status",
                                        "ID": application["ID"],
                                        "Status": new_status
                                    }

                                    update_response = requests.post(
                                        GOOGLE_SCRIPT_URL,
                                        json=update_data,
                                        timeout=15
                                    )

                                    if update_response.status_code == 200:

                                        st.success(
                                            "Status updated successfully!"
                                        )

                                        st.rerun()

                                    else:

                                        st.error(
                                            "Could not update status."
                                        )

                    else:

                        st.info(
                            "No applications have been submitted yet."
                        )

                else:

                    st.error(
                        "Could not retrieve applications."
                    )

            except Exception as e:

                st.error(
                    f"Connection error: {e}"
                )


    else:

        st.title("एडमिन डैशबोर्ड")

        st.write(
            "आवेदन देखें और उनकी स्थिति बदलें।"
        )

        pin = st.text_input(
            "एडमिन पिन",
            type="password"
        )

        if pin != ADMIN_PIN:

            if pin:
                st.error("गलत एडमिन पिन।")

            st.info(
                "डैशबोर्ड खोलने के लिए एडमिन पिन दर्ज करें।"
            )

        else:

            st.success("एडमिन एक्सेस मिल गया।")

            try:

                response = requests.get(
                    GOOGLE_SCRIPT_URL,
                    params={"admin": "true"},
                    timeout=15
                )

                if response.status_code == 200:

                    data = response.json()

                    if data:

                        st.subheader(
                            f"कुल आवेदन: {len(data)}"
                        )

                        status_filter = st.selectbox(
                            "स्थिति के अनुसार फ़िल्टर करें",
                            [
                                "सभी",
                                "Applied",
                                "Under Review",
                                "Accepted",
                                "Rejected"
                            ]
                        )

                        filtered_apps = data

                        if status_filter != "सभी":

                            filtered_apps = [
                                app for app in data
                                if app.get("Status", "Applied") == status_filter
                            ]

                        st.write(
                            f"{len(filtered_apps)} आवेदन दिखाए जा रहे हैं"
                        )

                        for number, application in enumerate(
                            filtered_apps
                        ):

                            with st.container(border=True):

                                st.subheader(
                                    application["Job"]
                                )

                                st.write(
                                    f"**नाम:** "
                                    f"{application['Name']}"
                                )

                                st.write(
                                    f"**फ़ोन:** "
                                    f"{application['Phone']}"
                                )

                                st.write(
                                    f"**स्थान:** "
                                    f"{application['Location']}"
                                )

                                st.write(
                                    f"**भुगतान:** "
                                    f"₹{application['Pay']}"
                                )

                                st.write(
                                    f"**कारण:** "
                                    f"{application['Reason']}"
                                )

                                current_status = application.get(
                                    "Status",
                                    "Applied"
                                )

                                new_status = st.selectbox(
                                    "आवेदन की स्थिति",
                                    [
                                        "Applied",
                                        "Under Review",
                                        "Accepted",
                                        "Rejected"
                                    ],
                                    index=[
                                        "Applied",
                                        "Under Review",
                                        "Accepted",
                                        "Rejected"
                                    ].index(current_status),
                                    key=f"status_hi_{number}_{application['ID']}"
                                )

                                if st.button(
                                    "स्थिति अपडेट करें",
                                    key=f"update_hi_{number}_{application['ID']}",
                                    type="primary"
                                ):

                                    update_data = {
                                        "action": "update_status",
                                        "ID": application["ID"],
                                        "Status": new_status
                                    }

                                    update_response = requests.post(
                                        GOOGLE_SCRIPT_URL,
                                        json=update_data,
                                        timeout=15
                                    )

                                    if update_response.status_code == 200:

                                        st.success(
                                            "स्थिति सफलतापूर्वक अपडेट हो गई!"
                                        )

                                        st.rerun()

                                    else:

                                        st.error(
                                            "स्थिति अपडेट नहीं की जा सकी।"
                                        )

                    else:

                        st.info(
                            "अभी तक कोई आवेदन जमा नहीं हुआ है।"
                        )

                else:

                    st.error(
                        "आवेदन प्राप्त नहीं किए जा सके।"
                    )

            except Exception as e:

                st.error(
                    f"कनेक्शन में समस्या: {e}"
                )
