import streamlit as st

from analyzer import analyze_password


# Page configuration
st.set_page_config(
    page_title="SecurePass",
    page_icon="🔐",
    layout="centered"
)


# Application heading
st.title("🔐 SecurePass")

st.subheader(
    "Password Strength & Security Analyzer"
)

st.write(
    "Check password characteristics and receive "
    "suggestions to improve password security."
)

st.warning(
    "Educational tool only. Do not enter a password "
    "that you currently use for a real account."
)


# Password input form
with st.form("password_form", clear_on_submit=True):

    password = st.text_input(
        "Enter a sample password",
        type="password",
        placeholder="Enter a test password"
    )

    submitted = st.form_submit_button(
        "Analyse Password"
    )


# Analyse after button is clicked
if submitted:

    if not password:

        st.error("Please enter a password to analyse.")

    else:

        result = analyze_password(password)

        st.divider()

        st.header("Analysis Results")

        # Display strength
        st.subheader("Password Strength")

        st.write(result["strength"])

        st.progress(result["score"] / 6)

        st.caption(
            f"Score: {result['score']} out of 6"
        )

        # Display password properties
        st.subheader("Password Characteristics")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                "Uppercase letters:",
                "✅" if result["uppercase"] else "❌"
            )

            st.write(
                "Lowercase letters:",
                "✅" if result["lowercase"] else "❌"
            )

            st.write(
                "Numbers:",
                "✅" if result["number"] else "❌"
            )

        with col2:

            st.write(
                "Special characters:",
                "✅" if result["special"] else "❌"
            )

            st.write(
                "Common password:",
                "❌ Detected" if result["common"] else "✅ Not detected"
            )

            st.write(
                "Repeated characters:",
                "❌ Detected" if result["repeated"] else "✅ Not detected"
            )

        st.write(
            "Password length:",
            result["length"],
            "characters"
        )

        # Entropy
        st.subheader("Estimated Password Entropy")

        st.metric(
            "Estimated entropy",
            f"{result['entropy']} bits"
        )

        st.caption(
            "This is a simplified theoretical estimate, "
            "not a guarantee of real-world password security."
        )

        # Suggestions
        st.subheader("Security Recommendations")

        for suggestion in result["suggestions"]:

            st.write("•", suggestion)


# Footer
st.divider()

st.caption(
    "SecurePass | Built with Python and Streamlit"
)