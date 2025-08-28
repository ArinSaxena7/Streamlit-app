import streamlit as st

st.title("💸 Wanna Earn Online?")
st.subheader("Stop doomscrolling, start cash-rolling! 🚀")

st.markdown("""
### What you can earn:
- 🎓 **Students** → up to **₹20,000/month**  
- 💻 **Freelancers** → up to **₹50,000/month**  
- ✍️ **Bloggers** → up to **₹10,000/month**  
- 🎥 **Content creators** → up to **₹5,000/month**  

⚡ Limited-time offer — don’t miss out!
""")

st.success("✅ Grab your dream side-hustle. Apply now!")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
goal = st.selectbox("Choose your category:", ["Student", "Freelancer", "Blogger", "Content Creator"])

if st.button("🚀 Apply Now"):
    st.info(f"Padhlo bhenke lodo Collge ka project bann nhi\nraha innse 20000 ke sappne dekh rahe haii chutiyee")
