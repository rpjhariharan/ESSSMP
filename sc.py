import streamlit as st
from datetime import datetime

# Initialize session state for user interactions
if 'user' not in st.session_state:
    st.session_state.user = {
        'name': 'John Doe',
        'badges': ['🏅 Welcome Badge'],
        'points': 150,
        'joined_communities': ['Soccer', 'Basketball']  # Removed emojis
    }
if 'active_page' not in st.session_state:
        st.session_state.active_page = 'Home'
if 'selected_community' not in st.session_state:
    st.session_state.selected_community = None

# Initialize session state for posts if not already done
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            'id': 1,
            'user': 'Alice',
            'content': 'Great game last night! Go Team A! ⚽️',
            'image': 'https://via.placeholder.com/800x400.png?text=Soccer+Match',
            'reel': None,
            'timestamp': '2024-12-08 18:30',
            'likes': 120,
            'shares': 30,
            'comments': [
                {'user': 'Bob', 'comment': 'Absolutely thrilling!'},
                {'user': 'Charlie', 'comment': 'Can’t wait for the next match.'}
            ]
        },
        {
            'id': 2,
            'user': 'Bob',
            'content': "Can't wait for the upcoming match between Team C and Team D! 🏀",
            'image': None,
            'reel': 'https://via.placeholder.com/800x400.png?text=Basketball+Reel',
            'timestamp': '2024-12-07 16:45',
            'likes': 85,
            'shares': 20,
            'comments': [
                {'user': 'Alice', 'comment': "It's going to be intense!"},
                {'user': 'David', 'comment': 'Who do you think will win?'}
            ]
        },
        {
            'id': 3,
            'user': 'Charlie',
            'content': 'Check out this amazing goal! 🎥⚽️',
            'image': 'https://via.placeholder.com/800x400.png?text=Goal+Highlight',
            'reel': None,
            'timestamp': '2024-12-06 20:15',
            'likes': 200,
            'shares': 50,
            'comments': [
                {'user': 'Eve', 'comment': 'Incredible shot!'},
                {'user': 'Frank', 'comment': 'What a moment!'}
            ]
        }
    ]

# Initialize session state for articles and sources
if 'articles' not in st.session_state:
    st.session_state.articles = [
        {
            'id': 1,
            'headline': 'Team A Clinches the Championship!',
            'image': 'https://via.placeholder.com/800x400.png?text=Championship+Win',
            'sources': [
                {'name': 'ESPN', 'rating': 4.8, 'views': 1500, 'url': 'https://www.espn.com/article1'},
                {'name': 'Bleacher Report', 'rating': 4.5, 'views': 1200,
                 'url': 'https://www.bleacherreport.com/article1'},
                {'name': 'theScore', 'rating': 4.2, 'views': 900, 'url': 'https://www.thescore.com/article1'},
            ]
        },
        {
            'id': 2,
            'headline': 'Star Player X Breaks the World Record',
            'image': 'https://via.placeholder.com/800x400.png?text=World+Record+Break',
            'sources': [
                {'name': 'ESPN', 'rating': 4.9, 'views': 2000, 'url': 'https://www.espn.com/article2'},
                {'name': 'Bleacher Report', 'rating': 4.6, 'views': 1600,
                 'url': 'https://www.bleacherreport.com/article2'},
                {'name': 'theScore', 'rating': 4.3, 'views': 1100, 'url': 'https://www.thescore.com/article2'},
            ]
        },
        {
            'id': 3,
            'headline': 'Exciting Matches Scheduled for This Weekend',
            'image': 'https://via.placeholder.com/800x400.png?text=Upcoming+Matches',
            'sources': [
                {'name': 'ESPN', 'rating': 4.7, 'views': 1300, 'url': 'https://www.espn.com/article3'},
                {'name': 'Bleacher Report', 'rating': 4.4, 'views': 1000,
                 'url': 'https://www.bleacherreport.com/article3'},
                {'name': 'theScore', 'rating': 4.1, 'views': 800, 'url': 'https://www.thescore.com/article3'},
            ]
        }
    ]

# Initialize session state for communities with polls and discussions
if 'communities_data' not in st.session_state:
    st.session_state.communities_data = {
        'Soccer': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Placeholder link
        },
        'Basketball': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Placeholder link
        },
        'Cricket': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Tennis': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Esports': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'American Football': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        # Adding new communities to match the emojis
        'Volleyball': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Table Tennis': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Rugby': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Boxing': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Badminton': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Hockey': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        'Martial Arts': {
            'polls': [],
            'discussions': [],
            'live_stream': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        }
    }

# Metadata and Page Configuration
st.set_page_config(
    page_title="Ultimate Sports Social Media Platform",
    page_icon="https://www.essentiallysports.com/favicon.ico",  # Replace with your favicon URL
    layout="wide"
)

# Custom CSS for Better Aesthetics
st.markdown("""
    <style>
    /* 1. Global Background and Text Color */
    html, body, [class*="css"]  {
        background-color: #000000 !important; /* Black background */
        color: #FFFFFF !important; /* White text */
    }

    /* Add top padding to the body to accommodate the Streamlit header */
    body {
        padding-top: 60px !important; /* Adjust the value as needed */
    }

    /* 2. Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #000000 !important; /* Black sidebar */
        color: #FFFFFF !important; /* White text */
        border: 2px solid #FF0000 !important; /* Red border */
        border-radius: 10px !important;
        box-shadow: 0 0 10px #FF0000; /* Red shadow for depth */
    }
    [data-testid="stSidebar"] a { /* Sidebar links */
        color: #FF0000 !important; /* Red links */
        text-decoration: none; /* Remove underline */
    }
    [data-testid="stSidebar"] a:hover {
        text-decoration: underline; /* Underline on hover */
    }

    /* 3. Main Content Area */
    .block-container {
        background-color: #000000 !important; /* Black background */
        color: #FFFFFF !important; /* White text */
        border: 2px solid #FF0000 !important; /* Red border */
        padding: 60px 20px 20px 20px !important; /* Increased top padding */
        border-radius: 10px !important;
        box-shadow: 0 0 10px #FF0000; /* Red shadow for depth */
    }

    /* 4. Buttons Styling */
    .stButton > button {
        background-color: #FF0000 !important; /* Red background */
        color: #FFFFFF !important; /* White text */
        border: 2px solid #FF0000 !important; /* Red border */
        border-radius: 8px;
        height: 40px;
        width: 100%;
        font-size: 14px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #CC0000 !important; /* Darker red on hover */
    }

    /* 5. Interaction Buttons (Like, Share, Comment) */
    button[data-baseweb="button"] {
        background-color: #FF0000 !important; /* Red background */
        color: #FFFFFF !important; /* White text */
        border: 2px solid #FF0000 !important; /* Red border */
        border-radius: 5px;
        padding: 5px 10px;
        margin-right: 10px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    button[data-baseweb="button"]:hover {
        background-color: #CC0000 !important; /* Darker red on hover */
    }

    /* 6. Input Fields Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #000000 !important; /* Black background */
        color: #FFFFFF !important; /* White text */
        border: 2px solid #FF0000 !important; /* Red border */
        border-radius: 5px;
    }

    /* 7. Link Styling */
    a {
        color: #FF0000 !important; /* Red links */
        border-bottom: 1px solid #FF0000 !important; /* Red underline */
    }

    a:hover {
        text-decoration: underline !important; /* Underline on hover */
    }

    /* 8. Header and Subheader Styling */
    .header-title {
        font-size: 2.5em;
        color: #FFFFFF !important; /* White color */
        text-align: center;
    }
    .header-subtitle {
        font-size: 1.2em;
        color: #FFFFFF !important; /* White color */
        text-align: center;
    }

    /* 9. Footer Styling */
    .footer {
        font-size: 0.9em;
        color: #FFFFFF !important; /* White text */
        text-align: center;
        margin-top: 50px;
        border-top: 2px solid #FF0000 !important; /* Red border */
    }

    /* 10. Cards Styling */
    .card {
        background-color: #1a1a1a !important; /* Dark grey background */
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #FF0000 !important; /* Red border */
        box-shadow: 0 4px 8px rgba(255,0,0,0.2); /* Red shadow */
        margin-bottom: 20px;
    }

    /* 11. Comment Section Styling */
    .comment-section {
        margin-top: 10px;
        padding-left: 20px;
        border-left: 2px solid #FF0000 !important; /* Red border */
    }

    /* 12. Headline Styling */
    .headline {
        font-size: 2em;
        color: #FFFFFF !important; /* White color */
        text-align: center;
        cursor: pointer;
    }

    /* 13. Image Styling */
    .headline-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
        border-radius: 10px;
        border: 2px solid #FF0000 !important; /* Red border */
        box-shadow: 0 4px 8px rgba(255,0,0,0.2);
    }

    /* 14. Progress Bar Styling */
    div[role="progressbar"] > div > div {
        background-color: #FF0000 !important; /* Red progress */
    }

    /* 15. Adjust Streamlit Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important; /* White headers */
    }

    /* 16. Adjust Streamlit Markdown Text */
    .css-1aumxhk, .css-qrbaxs, .css-1kiwrgv {
        color: #FFFFFF !important; /* White text in markdown */
    }

    /* 17. Expander Styling */
    .streamlit-expanderHeader {
        color: #FFFFFF !important; /* White expander headers */
    }
    .streamlit-expanderContent {
        color: #FFFFFF !important; /* White expander content */
    }

    /* 18. Additional Styling for Specific Components */
    .stRadio > div > label > div {
        color: #FFFFFF !important; /* White text for radio buttons */
    }

    .stCheckbox > label > div {
        color: #FFFFFF !important; /* White text for checkboxes */
    }

    .stSelectbox > label > div {
        color: #FFFFFF !important; /* White text for selectboxes */
    }

    /* 19. Ensure All Containers Have Red Borders */
    .stAlert > div {
        border: 2px solid #FF0000 !important; /* Red border for alerts */
        border-radius: 10px !important;
        background-color: #000000 !important; /* Black background */
        color: #FFFFFF !important; /* White text */
    }

    /* 20. Tables Styling */
    .stTable > div > table {
        border: 2px solid #FF0000 !important; /* Red border for tables */
        border-collapse: collapse;
    }
    .stTable > div > table th,
    .stTable > div > table td {
        border: 1px solid #FF0000 !important; /* Red borders for table cells */
        padding: 8px;
        color: #FFFFFF !important; /* White text */
    }
    .stTable > div > table th {
        background-color: #1a1a1a !important; /* Dark grey header background */
    }

    /* 21. Code Blocks Styling */
    .streamlit-expanderContent pre {
        background-color: #1a1a1a !important; /* Dark grey background for code */
        color: #FF0000 !important; /* Red text for code */
        border: 2px solid #FF0000 !important; /* Red border */
        border-radius: 5px !important;
        padding: 10px;
    }

    /* 22. Sports Icons Row Styling */
    .sports-icons {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 30px;
    }
    .sports-icons span {
        font-size: 2em;
    }

    </style>
    """, unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.markdown("<h2 style='text-align: center;'>Navigation</h2>", unsafe_allow_html=True)
sidenav_items = [
    {"name": "Home", "icon": "🏠"},
    {"name": "UGC", "icon": "🎤"},
    {"name": "Communities", "icon": "🌐"},
    {"name": "Gamification", "icon": "🏆"},
    {"name": "Profile", "icon": "👤"}
]

# Navigation Buttons
for item in sidenav_items:
    if st.sidebar.button(f"{item['icon']} {item['name']}"):
        st.session_state.active_page = item['name']

st.sidebar.markdown("---")
st.sidebar.markdown(f"**User:** {st.session_state.user['name']}")
st.sidebar.markdown(f"**Points:** {st.session_state.user['points']} 🏅")
st.sidebar.markdown("**Badges:**")
for badge in st.session_state.user['badges']:
    st.sidebar.markdown(f"- {badge}")

# Helper Functions
def like_post(post_id):
    for post in st.session_state.posts:
        if post['id'] == post_id:
            post['likes'] += 1
            st.session_state.user['points'] += 5  # Reward points for liking
            break

def share_post(post_id):
    for post in st.session_state.posts:
        if post['id'] == post_id:
            post['shares'] += 1
            st.session_state.user['points'] += 10  # Reward points for sharing
            break

def add_comment(post_id, comment_text):
    if comment_text:
        for post in st.session_state.posts:
            if post['id'] == post_id:
                post['comments'].append({'user': st.session_state.user['name'], 'comment': comment_text})
                st.session_state.user['points'] += 15  # Reward points for commenting
                break

# Function to display the Home page
def home():
    st.markdown("---")

    # 1. Sports Icons at the Top
    sports_icons = [
        "⚽️", "🏀", "🏈", "🎾", "🏐", "🏓", "🏉", "🥊", "🎮", "🏸", "🥅", "🥋"
    ]
    icons_html = ''.join([f"<span>{icon}</span>" for icon in sports_icons])
    st.markdown(f"<div class='sports-icons'>{icons_html}</div>", unsafe_allow_html=True)

    # Headline and Relevant Image
    if 'show_sources' not in st.session_state:
        st.session_state.show_sources = {}

    # Display Headline and Image for each article
    for article in st.session_state.articles:
        with st.container():
            # Headline as a clickable button
            if st.button(article['headline'], key=f"headline_{article['id']}"):
                st.session_state.show_sources[article['id']] = not st.session_state.show_sources.get(article['id'],
                                                                                                     False)

            # Relevant Image using HTML and CSS class
            st.markdown(f"""
                <img src="{article['image']}" class="headline-image" />
                """, unsafe_allow_html=True)

            # If show_sources is True for this article, display the sources
            if st.session_state.show_sources.get(article['id'], False):
                st.markdown("**Compare Sources:**")
                # Sort sources by rating and views
                sorted_sources = sorted(article['sources'], key=lambda x: (x['rating'], x['views']), reverse=True)
                for source in sorted_sources:
                    st.markdown(f"### {source['name']}")
                    st.markdown(f"**Rating:** {source['rating']} ⭐ | **Views:** {source['views']} 👁️")
                    st.markdown(f"[Read Full Article]({source['url']})")
                    st.markdown("---")

# Function to display the UGC page
def ugc():
    st.subheader("User-Generated Content 🎤")

    # Input for new post
    with st.form("new_post", clear_on_submit=True):
        post_type = st.selectbox("Select Post Type", ["Text", "Image", "Reel"], key="post_type")
        post_content = st.text_area("What's on your mind?", height=100, key='post_text')
        if post_type == "Image":
            post_image = st.text_input("Image URL", value="https://via.placeholder.com/800x400.png?text=Image+Post",
                                       key='post_image')
        elif post_type == "Reel":
            post_reel = st.text_input("Reel URL", value="https://via.placeholder.com/800x400.png?text=Reel+Video",
                                      key='post_reel')
        submitted = st.form_submit_button("Post 📨")
        if submitted:
            new_id = max([post['id'] for post in st.session_state.posts]) + 1 if st.session_state.posts else 1
            new_post = {
                'id': new_id,
                'user': st.session_state.user['name'],
                'content': post_content,
                'image': post_image if post_type == "Image" else None,
                'reel': post_reel if post_type == "Reel" else None,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'likes': 0,
                'shares': 0,
                'comments': []
            }
            st.session_state.posts.insert(0, new_post)
            st.session_state.user['points'] += 20  # Reward points for creating a post
            st.success("Your post has been shared!")

    # Displaying posts
    st.markdown("---")
    st.subheader("Recent Posts")

    for post in st.session_state.posts:
        with st.container():
            # Post Header
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{post['user']}**")
                st.markdown(f"*Posted on:* {post['timestamp']}")
            with col2:
                st.markdown(f"**{post['likes']} 👍 | {post['shares']} 🔄 | {len(post['comments'])} 💬**")

            # Post Content
            st.markdown(f"{post['content']}")
            if post['image']:
                # Use HTML to apply the 'headline-image' class with red border
                st.markdown(f"""
                    <img src="{post['image']}" style="width:100%; border-radius:10px; border:2px solid #FF0000; box-shadow: 0 4px 8px rgba(255,0,0,0.2);" />
                    """, unsafe_allow_html=True)
            if post['reel']:
                st.markdown(f"🎥 **Reel:** [Watch here]({post['reel']})")

            # Interaction Buttons
            col3, col4, col5 = st.columns([1, 1, 1])
            with col3:
                if st.button(f"👍 Like", key=f"like_{post['id']}"):
                    like_post(post['id'])
            with col4:
                if st.button(f"🔄 Share", key=f"share_{post['id']}"):
                    share_post(post['id'])
            with col5:
                if st.button(f"💬 Comment", key=f"comment_{post['id']}"):
                    st.session_state.active_page = 'UGC'
                    st.experimental_rerun()

            # Display Comments
            if len(post['comments']) > 0:
                st.markdown("**Comments:**")
                for comment in post['comments']:
                    st.markdown(f"- **{comment['user']}**: {comment['comment']}")

            # Add Comment Form
            with st.expander("Add a comment"):
                with st.form(f"comment_form_{post['id']}", clear_on_submit=True):
                    comment_text = st.text_area("Your Comment:", key=f"comment_text_{post['id']}")
                    submit_comment = st.form_submit_button("Submit 📝")
                    if submit_comment and comment_text:
                        add_comment(post['id'], comment_text)
                        st.experimental_rerun()

            st.markdown("---")

# Function to display the Communities page
def communities():
    st.subheader("Communities 🌐")

    # List of available communities with emojis
    available_communities = [
        {"name": "Soccer", "icon": "⚽️"},
        {"name": "Basketball", "icon": "🏀"},
        {"name": "American Football", "icon": "🏈"},
        {"name": "Tennis", "icon": "🎾"},
        {"name": "Volleyball", "icon": "🏐"},
        {"name": "Table Tennis", "icon": "🏓"},
        {"name": "Rugby", "icon": "🏉"},
        {"name": "Boxing", "icon": "🥊"},
        {"name": "Esports", "icon": "🎮"},
        {"name": "Badminton", "icon": "🏸"},
        {"name": "Hockey", "icon": "🥅"},
        {"name": "Martial Arts", "icon": "🥋"}
    ]

    # Display available communities as buttons with icons
    st.markdown("**Join a Community:**")
    cols = st.columns(4)
    for idx, community in enumerate(available_communities):
        with cols[idx % 4]:
            if community['name'] in st.session_state.user['joined_communities']:
                status = "✅ Joined"
            else:
                status = "➕ Join"
            if st.button(f"{community['icon']} {status} {community['name']}", key=community['name']):
                if community['name'] not in st.session_state.user['joined_communities']:
                    st.session_state.user['joined_communities'].append(community['name'])
                    st.session_state.user['points'] += 20  # Reward points for joining
                    st.success(f"You have joined the {community['name']} community!")
                else:
                    st.warning(f"You are already a member of the {community['name']} community.")

    st.markdown("---")

    st.markdown("**Community Actions:**")

    if not st.session_state.user['joined_communities']:
        st.info("Join a community to access interactive features.")
        return  # Exit the function early if no communities are joined

    # Three action buttons
    col_poll, col_discussion, col_streaming = st.columns(3)
    with col_poll:
        if st.button("📊 Poll"):
            st.session_state.active_page = 'Polls'
            st.experimental_rerun()
    with col_discussion:
        if st.button("💬 Live Match Discussion"):
            st.session_state.active_page = 'Discussions'
            st.experimental_rerun()
    with col_streaming:
        if st.button("🎥 Live Match Streaming"):
            st.session_state.active_page = 'Live Streaming'
            st.experimental_rerun()

    st.markdown("---")

# Function to display the Gamification page
def gamification():
    st.subheader("Gamification 🏆")
    st.markdown("**Your Badges:**")
    badges = st.session_state.user['badges']
    for badge in badges:
        st.markdown(f"- {badge}")

    st.markdown("---")
    st.markdown("**Leaderboard 🥇**")
    # Simulated leaderboard
    leaderboard = [
        {"user": "Alice", "points": 500},
        {"user": "Bob", "points": 450},
        {"user": "Charlie", "points": 400},
        {"user": st.session_state.user['name'], "points": st.session_state.user['points']},
    ]
    leaderboard = sorted(leaderboard, key=lambda x: x['points'], reverse=True)
    for rank, entry in enumerate(leaderboard, start=1):
        if entry['user'] == st.session_state.user['name']:
            st.markdown(f"**{rank}. {entry['user']} - {entry['points']} pts** 🏅")
        else:
            st.markdown(f"{rank}. {entry['user']} - {entry['points']} pts")

    st.markdown("---")
    st.markdown("**Your Points:**")
    progress = st.progress(min(st.session_state.user['points'], 1000) / 1000)
    st.markdown(f"{st.session_state.user['points']} / 1000 points")

# Function to display the Profile page
def profile():
    st.subheader("Your Profile 👤")
    st.markdown(f"**Name:** {st.session_state.user['name']}")
    st.markdown(f"**Points:** {st.session_state.user['points']} 🏅")
    st.markdown(f"**Badges:**")
    for badge in st.session_state.user['badges']:
        st.markdown(f"- {badge}")
    st.markdown(f"**Joined Communities:** {', '.join(st.session_state.user['joined_communities'])}")

    st.markdown("---")
    st.subheader("Settings ⚙️")
    with st.form("update_profile", clear_on_submit=True):
        new_name = st.text_input("Update Name", value=st.session_state.user['name'])
        update = st.form_submit_button("Update 📝")
        if update:
            st.session_state.user['name'] = new_name
            st.success("Profile updated successfully!")

# Function to display the Polls page
def polls():
    community = st.session_state.selected_community
    if not community:
        st.error("No community selected.")
        return
    st.subheader(f"Polls for {community}")
    community_data = st.session_state.communities_data.get(community, {})

    if not community_data:
        st.error(f"The selected community '{community}' does not exist in the data.")
        return

    # Display existing polls
    if community_data['polls']:
        for poll in community_data['polls']:
            st.markdown(f"**{poll['question']}**")
            selected_option = st.radio("Options:", list(poll['votes'].keys()),
                                       key=f"poll_option_{community}_{poll['id']}")
            if st.button("Vote", key=f"vote_{community}_{poll['id']}"):
                poll['votes'][selected_option] += 1
                st.session_state.user['points'] += 10  # Reward points for voting
                st.success("Your vote has been recorded!")
                st.experimental_rerun()
            st.markdown("**Votes:**")
            for option, votes in poll['votes'].items():
                st.write(f"{option}: {votes}")
            st.markdown("---")
    else:
        st.write("No polls available.")

    # Create a new poll
    st.markdown("**Create a New Poll**")
    with st.form("create_poll", clear_on_submit=True):
        poll_question = st.text_input("Poll Question")
        poll_options = st.text_input("Options (separated by commas)", "Option 1, Option 2")
        submit_poll = st.form_submit_button("Create Poll")
        if submit_poll and poll_question and poll_options:
            options = [opt.strip() for opt in poll_options.split(",") if opt.strip()]
            if len(options) < 2:
                st.error("Please provide at least two options.")
            else:
                new_poll_id = len(community_data['polls']) + 1
                new_poll = {
                    'id': new_poll_id,
                    'question': poll_question,
                    'options': options,
                    'votes': {option: 0 for option in options}
                }
                community_data['polls'].append(new_poll)
                st.session_state.user['points'] += 50  # Reward points for creating a poll
                st.success("Poll created successfully!")

# Function to display the Discussions page
def discussions():
    community = st.session_state.selected_community
    if not community:
        st.error("No community selected.")
        return
    st.subheader(f"Live Discussions for {community}")
    community_data = st.session_state.communities_data.get(community, {})

    if not community_data:
        st.error(f"The selected community '{community}' does not exist in the data.")
        return

    # Display existing discussions
    if community_data['discussions']:
        for discussion in community_data['discussions']:
            st.markdown(f"### {discussion['topic']}")
            for comment in discussion['comments']:
                st.markdown(f"- **{comment['user']}**: {comment['comment']}")
            st.markdown("---")
    else:
        st.write("No discussions available.")

    # Start a new discussion
    st.markdown("**Start a New Discussion**")
    with st.form("start_discussion", clear_on_submit=True):
        discussion_topic = st.text_input("Discussion Topic")
        discussion_content = st.text_area("Your Comment", height=100)
        submit_discussion = st.form_submit_button("Start Discussion")
        if submit_discussion and discussion_topic and discussion_content:
            new_discussion = {
                'topic': discussion_topic,
                'comments': [
                    {'user': st.session_state.user['name'], 'comment': discussion_content}
                ]
            }
            community_data['discussions'].append(new_discussion)
            st.session_state.user['points'] += 30  # Reward points for starting a discussion
            st.success("Discussion started successfully!")

# Function to display the Live Streaming page
def live_streaming():
    community = st.session_state.selected_community
    if not community:
        st.error("No community selected.")
        return
    st.subheader(f"Live Streaming for {community}")
    community_data = st.session_state.communities_data.get(community, {})

    if not community_data:
        st.error(f"The selected community '{community}' does not exist in the data.")
        return

    live_stream_url = community_data.get('live_stream', None)
    if live_stream_url:
        st.markdown(f"Watch the live stream below:")
        st.video(live_stream_url)
    else:
        st.warning("No live stream available for this community.")

    # Option to update live stream URL
    st.markdown("**Update Live Stream URL**")
    with st.form("update_live_stream", clear_on_submit=True):
        new_stream_url = st.text_input("Live Stream URL", value=live_stream_url)
        submit_stream = st.form_submit_button("Update Live Stream")
        if submit_stream and new_stream_url:
            community_data['live_stream'] = new_stream_url
            st.session_state.user['points'] += 100  # Reward points for updating live stream
            st.success("Live stream updated successfully!")

# Render the active page
if st.session_state.active_page == 'Home':
    home()
elif st.session_state.active_page == 'UGC':
    ugc()
elif st.session_state.active_page == 'Communities':
    communities()
elif st.session_state.active_page == 'Gamification':
    gamification()
elif st.session_state.active_page == 'Profile':
    profile()
elif st.session_state.active_page == 'Polls':
    polls()
elif st.session_state.active_page == 'Discussions':
    discussions()
elif st.session_state.active_page == 'Live Streaming':
    live_streaming()
else:
    home()

# Footer
st.markdown("""
    <div class="footer">
        <hr>
        <p>© 2024 EssentiallySports. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)
