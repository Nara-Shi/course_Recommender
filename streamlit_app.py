import streamlit as st

st.set_page_config(page_title="Course Recommender", page_icon="📚", layout="centered")

COURSES = [
    {
        "title": "Python Fundamentals",
        "level": "Beginner",
        "duration": 4,
        "tags": {"python", "programming", "automation", "data"},
        "description": "Build a foundation in Python syntax, functions, collections, and small scripts.",
    },
    {
        "title": "Web Development Foundations",
        "level": "Beginner",
        "duration": 6,
        "tags": {"web", "html", "css", "javascript", "design"},
        "description": "Learn how page structure, styling, and browser code work together.",
    },
    {
        "title": "Data Analysis with Python",
        "level": "Intermediate",
        "duration": 6,
        "tags": {"python", "data", "visualization", "statistics"},
        "description": "Explore tabular data, basic analysis, and clear visual summaries.",
    },
    {
        "title": "Machine Learning Concepts",
        "level": "Intermediate",
        "duration": 8,
        "tags": {"python", "data", "machine learning", "statistics"},
        "description": "Understand a practical machine-learning workflow, from features to evaluation.",
    },
    {
        "title": "Frontend Application Design",
        "level": "Intermediate",
        "duration": 7,
        "tags": {"web", "javascript", "design", "accessibility"},
        "description": "Plan responsive interfaces and build reusable browser components.",
    },
    {
        "title": "Algorithms and Data Structures",
        "level": "Intermediate",
        "duration": 8,
        "tags": {"programming", "algorithms", "java", "problem solving"},
        "description": "Practice common data structures, algorithm patterns, and complexity analysis.",
    },
    {
        "title": "Applied AI Systems",
        "level": "Advanced",
        "duration": 10,
        "tags": {"python", "machine learning", "ai", "data"},
        "description": "Study the components and evaluation choices behind applied AI products.",
    },
    {
        "title": "Backend APIs",
        "level": "Advanced",
        "duration": 8,
        "tags": {"web", "javascript", "apis", "databases"},
        "description": "Design API boundaries, validate inputs, and work with persistent data.",
    },
]

INTERESTS = sorted({tag for course in COURSES for tag in course["tags"]})

st.title("📚 Course Recommender")
st.write(
    "Choose a few topics and your current level. The app ranks a small sample catalog "
    "by topic overlap and shows why each course matched."
)
st.info("This is a local prototype with sample course data; it does not enroll you in courses.")

with st.form("recommendation_form"):
    interests = st.multiselect("What would you like to learn?", INTERESTS)
    level = st.selectbox("Current level", ["Any level", "Beginner", "Intermediate", "Advanced"])
    max_weeks = st.slider("Maximum course length (weeks)", min_value=2, max_value=12, value=8)
    submitted = st.form_submit_button("Find courses", type="primary")

if submitted:
    if not interests:
        st.warning("Choose at least one topic so the recommendations have something to match.")
    else:
        selected = set(interests)
        ranked = []
        for course in COURSES:
            if level != "Any level" and course["level"] != level:
                continue
            if course["duration"] > max_weeks:
                continue
            matched = selected & course["tags"]
            if matched:
                ranked.append((len(matched), course, sorted(matched)))

        ranked.sort(key=lambda item: (-item[0], item[1]["duration"], item[1]["title"]))
        if not ranked:
            st.warning("No courses matched those choices. Try another level or a longer duration.")
        else:
            st.subheader("Recommended for you")
            for score, course, matched in ranked[:5]:
                with st.container(border=True):
                    st.markdown(f"### {course['title']}")
                    st.caption(f"{course['level']} · about {course['duration']} weeks")
                    st.write(course["description"])
                    st.write("**Why it matched:** " + ", ".join(matched))

with st.expander("How recommendations are ranked"):
    st.write(
        "The prototype counts how many selected topics match each sample course. "
        "It filters by level and maximum duration, then sorts by topic matches, "
        "shorter duration, and course title. No personal data or external AI service is used."
    )
