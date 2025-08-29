import streamlit as st

st.title("Wanna Earn Online?")
st.subheader("Broke in the middle of the month? Netflix due, Maggi stock khatam, aur UPI pe ‘low balance’ 😭 Chill, we gotchu being an Engineering pookie I can relate 🚀")
st.subheader("Chill, we cooked up the fix 🔥")

st.markdown("""
### What you can earn:
- 🎓 **Students** → up to **₹20,000/month**  
- 💻 **Freelancers** → up to **₹50,000/month**  
- ✍️ **Bloggers** → up to **₹10,000/month**  
- 🎥 **Content creators** → up to **₹5,000/month**  

⚡ Limited-time offer — don’t miss out!
""")

YES = "Yes"
NO = "No"

fill_form = st.radio("Wanna fill the form?", [YES, NO], index=None)


if fill_form == YES:
    st.markdown("### 📝 Fill the form below to get started!")
else:
    st.markdown("### 👋 Who cares, born gareeb die gareeb 😎")
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    networth = st.number_input("Your wannabe future networth", min_value=0)
    goal = st.selectbox("Choose your category:", ["Student", "Freelancer", "Blogger", "Content Creator"])

    if st.button("🚀 Apply Now"):
        if not name or not email:
            st.error("⚠️ Please fill all fields before submitting.")
        else:
            st.success("✅ Your application has been submitted!")
            st.markdown(f"""
            **Name:** {name}  
            **Email:** {email}  
            **Future Networth:** {networth}  
            **Category:** {goal}  
            """)
            
    else:
     st.markdown("### 👋 Who cares, born gareeb die gareeb 😎")
