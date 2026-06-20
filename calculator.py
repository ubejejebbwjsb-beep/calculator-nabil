import streamlit as st

# عنوان الصفحة وتنسيقها
st.set_page_config(page_title="آلة حاسبة ذكية", page_icon="🧮", layout="centered")

st.title("🧮 مشروع الآلة الحاسبة")
st.write("---")

# إدخال البيانات من المستخدم عبر واجهة الويب
num1 = st.number_input("أدخل الرقم الأول:", value=0.0)
prosess = st.selectbox("اختر العملية الحسابية:", ["+", "-", "*", "/"])
num2 = st.number_input("أدخل الرقم الثاني:", value=0.0)

result = None
error_message = None

# زر لتنفيذ العملية
if st.button("احسب النتيجة", type="primary"):
    if prosess == "+":
        result = num1 + num2
    elif prosess == "-":
        result = num1 - num2
    elif prosess == "*":
        result = num1 * num2
    elif prosess == "/":
        if num2 == 0:
            error_message = "لا يمكن القسمة على صفر!"
        else:
            result = num1 / num2

    # عرض النتائج للمستخدم
    st.write("---")
    if error_message:
        st.error(error_message)
    elif result is not None:
        st.success(f"النتيجة هي: {result}")