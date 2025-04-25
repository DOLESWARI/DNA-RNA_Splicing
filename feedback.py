import streamlit as st

def run():
    """Runs the Feedback Page application."""
    # Set the title of the feedback page
    st.title("Feedback Page")

    # Static list of previous feedbacks and images (no database)
    previous_feedback = [
        {
            'name': 'Alice',
            'email': 'alice@example.com',
            'feedback': 'Great app! Very useful and easy to navigate.',
            'image_url': 'https://www.example.com/alice.jpg'  # URL of Alice's image
        },
        {
            'name': 'Bob',
            'email': 'bob@example.com',
            'feedback': 'I love this app. The interface is simple, and it works perfectly.',
            'image_url': 'https://www.example.com/bob.jpg'  # URL of Bob's image
        },
        {
            'name': 'Charlie',
            'email': 'charlie@example.com',
            'feedback': 'Amazing experience! I use it daily.',
            'image_url': 'https://www.example.com/charlie.jpg'  # URL of Charlie's image
        }
    ]

    # Display previous feedback with images above the form
    st.write("### Previous Feedback:")
    for idx, feedback in enumerate(previous_feedback):
        st.write(f"**Feedback {idx + 1}:**")
        st.write(f"Name: {feedback['name']}")
        st.write(f"Email: {feedback['email']}")
        st.write(f"Feedback: {feedback['feedback']}")

        if feedback['image_url']:
            st.image(feedback['image_url'], width=100)  # Display the user's image
        st.write("-" * 50)

    # Create a form to collect new feedback
    with st.form(key='feedback_form'):
        name = st.text_input("Your Name (Optional)")
        email = st.text_input("Your Email (Optional)")
        feedback = st.text_area("Your Feedback")
        image_url = st.text_input("Image URL (Optional, leave blank for no image)")

        # Submit button for the form
        submit_button = st.form_submit_button(label='Submit Feedback')

    # Process the feedback submission
    if submit_button:
        st.write("Thank you for your feedback!")
        if name:
            st.write("Name:", name)
        if email:
            st.write("Email:", email)
        st.write("Feedback:", feedback)
        if image_url:
            st.image(image_url, width=100)  # Display the image submitted by the user

# Ensure compatibility with other scripts
if __name__ == "__main__":
    run()
