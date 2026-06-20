import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة ذكية", page_icon="🧮", layout="centered")

# 2. إضافة كود تنسيق (CSS) لتغيير لون الخلفية والنصوص وتنسيق الأزرار
st.markdown("""
    <style>
    /* تغيير خلفية الموقع بالكامل إلى اللون الأسود أو الرمادي الغامق */
    .stApp {
        background-color: #121212;
    }
    
    /* تعديل لون العناوين والنصوص لتبدو واضحة وملونة */
    h1 {
        color: #00ea98 !important; /* لون أخضر فسفوري مميز */
        text-align: center;
    }
    
    p, label, .stSelectbox label, .stNumberInput label {
        color: #ffffff !important; /* نصوص بيضاء */
        font-size: 18px !important;
    }
    
    /* تنسيق زر الحساب ليكون عريضاً وجذاباً */
    div.stButton > button:first-child {
        background-color: #007bff !important;
        color: white !important;
        width: 100%;
        border-radius: 8px;
        font-size: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 10px rgba(0, 123, 255, 0.3);
    }
    </style>
""", unsafe_allow_index=True)

# 3. محتوى الموقع الأساسي
st.title("🧮 مشروع الآلة الحاسبة الذكية")
st.write("---")

# خانات الإدخال
num1 = st.number_input("أدخل الرقم الأول:", value=0.0)
prosess = st.selectbox("اختر العملية الحسابية:", ["+", "-", "*", "/"])
num2 = st.number_input("أدخل الرقم الثاني:", value=0.0)

result = None
error_message = None

if st.button("احسب النتيجة"):
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

    st.write("---")
    if error_message:
        st.error(error_message)
    elif result is not None:
        # عرض النتيجة بشكل منسق ومميز
        st.balloons() # تأثير بالونات احتفالية عند النجاح!
        st.success(f"النتيجة النهائية هي: {result}")
