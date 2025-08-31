import streamlit as st

st.title("Wanna Earn Online?")
st.subheader("Broke in the middle of the month? Netflix due, Maggi stock khatam, aur UPI pe ‘low balance’ 😭 Chill, we gotchu being an Engineering pookie I can relate 🚀 Chill, we cooked up the fix 🔥")

st.markdown("""
### What you can earn:
- 🎓 **Students** → up to **₹20,000/month**  
- 💻 **Freelancers** → up to **₹50,000/month**  
- ✍️ **Bloggers** → up to **₹10,000/month**  
- 🎥 **Content creators** → up to **₹5,000/month
- 🍆 🍑**Porn Star**  → up to **1,00,00,000/months

⚡ Limited-time offer — don’t miss out!
""")

CHOOSE = "👉 Choose one"
YES = "Yes"
NO = "No"

fill_form = st.radio("Wanna fill the form?", [CHOOSE, YES, NO], index=0)

if fill_form == NO:
    st.markdown("### 👋 Who cares, born gareeb die gareeb 😎")

elif fill_form == YES:
    st.markdown("### Great Fill your form ASAP! 🚀")
    st.markdown("### 🤝 We are here to help you! 😎")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    networth = st.number_input("EFNT Estimatedfuture networth", min_value=0)
    goal = st.selectbox("Choose your category:", ["Student", "Freelancer", "Blogger", "Content Creator","Porn Star"])

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

st.markdown("### 🚀 Are you ready to earn?\nlets move ahead 🚀")
if st.radio("Are you ready to earn?", [CHOOSE,YES, NO], index=0):
    st.markdown("### 👋 Let's get started!")
else:
    st.info("👆 Please select Yes or No to continue.")

