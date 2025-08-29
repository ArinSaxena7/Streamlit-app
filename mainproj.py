import streamlit as st

st.title("Wanna Earn Online?")
st.subheader('Broke in the middle of the month? Netflix due, Maggi stock khatam, aur UPI pe ‘low balance’ 😭 Chill, we gotchu being an Engineering pookie I can relate with you🚀')
st.subheader('chill, we cooked up the fix 🔥')
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
networth = st.number_input("Your wannabe future networth")
goal = st.selectbox("Choose your category:", ["Student", "Freelancer", "Blogger", "Content Creator"])


if st.button("🚀 Apply Now"):
    st.markdown(f"""
    name:{name}
    email:{email}
    networth:{networth}
    goal:{goal}""")
