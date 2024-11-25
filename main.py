import streamlit as st
import langchain_helper
import re

# Set page configuration
st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Main application title
st.title("🍽️ Restaurant Name & Menu Generator")
st.markdown(
    """
    Welcome to the **Restaurant Name Generator**! 🎉  
    Select a cuisine from the sidebar, and we'll generate a creative restaurant name and a delicious menu for you.  
    """,
    unsafe_allow_html=True,
)

# Sidebar section
st.sidebar.header("Customize Your Restaurant")
cuisine = st.sidebar.selectbox(
    "🌎 Choose a Cuisine",
    ("Indian", "Mexican", "Italian", "American", "Chinese", "Arabic"),
    index=0,
)

st.sidebar.markdown(
    """
    _Explore a world of flavors! Pick a cuisine to get started._  
    **Tip:** Try them all to see which inspires you the most. 🍴
    """
)

# Generate response when a cuisine is selected
if cuisine:
    # Call the helper function
    response = langchain_helper.generate_restaurant_names_and_menu_items(cuisine)

    # Display restaurant name
    st.markdown("## 🍴 Restaurant Name")
    st.markdown(
        f"<h2 style='text-align: center; color: #FF6347;'>{response['restaurant_name'].strip()}</h2>",
        unsafe_allow_html=True,
    )

    # Process and display menu items
    st.markdown("### 📜 Menu Items")
    st.write(
        """
        _Here's a list of delectable dishes inspired by your chosen cuisine._  
        """
    )

    # Ensure menu items are separated correctly
    menu_raw = response['menu_items'].strip()
    menu_items = [item.strip() for item in menu_raw.replace("\n", ",").split(",") if item.strip()]

    # Preprocess menu items to remove prefixes
    def preprocess_item(item):
        # Remove unwanted prefixes (numbers, special characters, etc.)
        cleaned_item = re.sub(r'^\d+[\.\)]?\s*', '', item)  # Removes numbers like "1.", "2)", etc.
        return cleaned_item.strip()

    # Display menu with proper numbering
    st.markdown("---")
    for idx, item in enumerate(menu_items, 1):
        cleaned_item = preprocess_item(item)
        st.markdown(f"**{idx}.** {cleaned_item} 🍲")
    st.markdown("---")

    # Add a footer
    st.markdown(
        """
        <div style="text-align: center; font-size: 14px; margin-top: 50px;">
        Made with ❤️ by Sachin Kumar
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        ### 👈 Select a cuisine to get started!  
        _Ready to uncover the perfect restaurant idea? Choose a cuisine from the sidebar._
        """
    )
