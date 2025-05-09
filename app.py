import re
import streamlit as st

# page styling
st.set_page_config(page_title = "Password Strength checker" ,page_icon = "🔑")

# page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter Your password below to check its security level. 🔍")

# function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score
    else:
        feedback.append("❌Password should be **8 character long**.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z], password"):
        score += 1
    else:
        feedback.append("❌ Password should include **both upper case (A-Z) and lower case (a-z) letters**.")
    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9) **.") 

    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌Include ** at least one special character (!@#$%^&*)**.")        

     #display pasword strength
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more feature.")    
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it.")

     #feedback
    if feedback:
        with st.expander("🔍**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password:", type="password", help="Ensure Your Password is strong 🔐") 

# Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")    