import streamlit as st

st.set_page_config(
    page_title="المحاضرة الأولى | تطبيقات التعلم العميق",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] { direction: rtl; text-align: right; }
.block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
.main-title {font-size: 2.2rem; font-weight: 800; margin-bottom: .3rem;}
.sub-title {font-size: 1.05rem; opacity: .8; margin-bottom: 1.2rem;}
.box {border:1px solid rgba(128,128,128,.25); border-radius:14px; padding:16px; margin:8px 0 14px 0;}
.small {font-size:.92rem; opacity:.85;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">المحاضرة الأولى: مقدمة في التعلم العميق وتطبيقاته في إدارة الموارد البشرية</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Introduction to Deep Learning and Its Applications in Human Resource Management</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("المقياس")
    st.write("تطبيقات التعلم العميق")
    st.write("الفئة المستهدفة: طلبة إدارة الموارد البشرية")
    st.divider()
    section = st.radio("الانتقال إلى:", [
        "الأهداف", "AI وML وDL", "الفرق بين ML وDL", "لماذا انتشر DL؟",
        "تطبيقات HR", "مثال Attrition", "القيود والأخلاقيات", "نشاط", "اختبار قصير", "المراجع"
    ])

if section == "الأهداف":
    st.header("أهداف المحاضرة")
    st.markdown("""
- تعريف الذكاء الاصطناعي **Artificial Intelligence (AI)**.
- تعريف التعلم الآلي **Machine Learning (ML)**.
- تعريف التعلم العميق **Deep Learning (DL)**.
- توضيح العلاقة بين AI وML وDL.
- التمييز بين ML التقليدي وDL.
- تفسير أسباب انتشار DL.
- تحديد أهم تطبيقاته في إدارة الموارد البشرية.
- التعرف على القيود المنهجية والأخلاقية الأساسية.
""")
    st.info("سؤال تمهيدي: هل يمكن للحاسوب أن يتعلم من بيانات الموظفين ويتوقع أي موظف قد يغادر المؤسسة؟")

elif section == "AI وML وDL":
    st.header("من الذكاء الاصطناعي إلى التعلم العميق")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.subheader("Artificial Intelligence")
        st.write("المجال الأشمل لأتمتة مهام تتطلب عادة قدرات بشرية مثل اتخاذ القرار وفهم اللغة والتعرف على الأنماط.")
    with c2:
        st.subheader("Machine Learning")
        st.write("فرع من AI يسمح للنظام بتعلم العلاقات والأنماط من البيانات بدلاً من الاعتماد فقط على قواعد مكتوبة مسبقًا.")
    with c3:
        st.subheader("Deep Learning")
        st.write("فرع من ML يعتمد أساسًا على شبكات عصبية متعددة الطبقات لتعلم تمثيلات معقدة للبيانات.")
    st.success("Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence")
    st.markdown("**المسار المبسط:** Data → Learning Algorithm → Model → Prediction")

elif section == "الفرق بين ML وDL":
    st.header("مقارنة مبسطة")
    st.table({
        "الجانب":["استخراج الخصائص","حجم البيانات","القدرة الحاسوبية","بنية النموذج","التفسير","ملاءمة بيانات HR الصغيرة"],
        "Machine Learning":["تدخل أكبر غالبًا","يمكن أن يعمل ببيانات محدودة نسبيًا","أقل غالبًا","أبسط نسبيًا","أسهل في كثير من النماذج","غالبًا مناسب"],
        "Deep Learning":["يتعلم كثيرًا منها تلقائيًا","يستفيد عادةً من بيانات كبيرة","أعلى غالبًا","شبكات متعددة الطبقات","قد يكون أصعب","ليس دائمًا الخيار الأفضل"]
    })
    st.warning("Deep Learning ليس أفضل تلقائيًا. اختيار النموذج يعتمد على طبيعة المشكلة والبيانات.")

elif section == "لماذا انتشر DL؟":
    st.header("العوامل الرئيسة وراء انتشار التعلم العميق")
    st.markdown("""
1. **Big Data:** زيادة حجم البيانات المتاحة.
2. **Computing Power:** تطور القدرة الحاسوبية، خصوصًا GPU.
3. **Better Algorithms:** تحسن طرق التدريب والتحسين.
4. **Software Libraries:** تطور مكتبات مثل TensorFlow وKeras.
""")
    st.subheader("مجالات الاستخدام")
    st.write("Computer Vision — NLP — Speech Recognition — Time Series Forecasting — Classification — Prediction")

elif section == "تطبيقات HR":
    st.header("تطبيقات AI/ML/DL في إدارة الموارد البشرية")
    st.table({
        "مجال HR":["Recruitment","Selection","Employee Attrition","Performance Management","Training","Engagement","Workforce Planning","Employee Feedback","Retention"],
        "مثال تطبيقي":["فرز وتحليل بيانات المتقدمين","دعم تصنيف المرشحين","التنبؤ باحتمال المغادرة","تحليل وتوقع الأداء","اقتراح احتياجات التدريب","تحليل الرضا والاندماج","التنبؤ بالاحتياجات المستقبلية","تحليل النصوص والمشاعر","تحليل عوامل الاحتفاظ"]
    })

elif section == "مثال Attrition":
    st.header("مثال تطبيقي: Employee Attrition Prediction")
    st.write("نفترض أن لدينا بيانات تاريخية للموظفين تتضمن:")
    st.code("Age | MonthlyIncome | YearsAtCompany | JobSatisfaction | Overtime | TrainingTimesLastYear | Attrition")
    st.write("إذا كانت قيمة Attrition هي Yes/No فإن المسألة **Classification Problem**.")
    st.info("هذا المثال سيستمر معنا في المحاضرات القادمة حتى نبني نموذجًا فعليًا باستخدام Keras.")

elif section == "القيود والأخلاقيات":
    st.header("قيود مهمة في سياق الموارد البشرية")
    st.markdown("""
- **Small Data:** قواعد بيانات HR قد تكون صغيرة مقارنة بمجالات أخرى.
- **Data Quality:** ضعف الجودة يؤدي إلى ضعف النتائج.
- **Bias:** البيانات المتحيزة قد تنتج قرارات متحيزة.
- **Fairness:** قرارات التوظيف والترقية والأجور تمس الأفراد مباشرة.
- **Explainability:** يجب أن تكون القرارات قابلة للتفسير والتبرير قدر الإمكان.
""")
    st.success("الهدف هو دعم القرار البشري (Decision Support)، وليس إلغاء الحكم الإداري.")

elif section == "نشاط":
    st.header("نشاط صفي")
    items = [
        ("هل سيغادر الموظف المؤسسة خلال السنة القادمة؟", "Classification"),
        ("كم سيكون تقييم الأداء المتوقع؟", "Regression / Prediction"),
        ("هل تعليق الموظف إيجابي أم سلبي؟", "Text Classification / Sentiment Analysis"),
        ("كم موظفًا ستحتاج المؤسسة السنة القادمة؟", "Forecasting"),
        ("ما الموظفون الأكثر تشابهًا في خصائصهم؟", "Clustering")
    ]
    for i,(q,a) in enumerate(items,1):
        with st.expander(f"{i}. {q}"):
            st.write(f"**الإجابة:** {a}")

elif section == "اختبار قصير":
    st.header("اختبار قصير")
    score = 0
    q1 = st.radio("1) أي مفهوم هو الأشمل؟", ["Deep Learning","Machine Learning","Artificial Intelligence"], index=None)
    q2 = st.radio("2) ما المقصود بكلمة Deep؟", ["التفكير الإنساني العميق","تعدد طبقات المعالجة في الشبكة","حجم الملف"], index=None)
    q3 = st.radio("3) التنبؤ بـ Leave/Stay يمثل:", ["Classification","Clustering","Image Generation"], index=None)
    q4 = st.radio("4) هل Deep Learning هو الأفضل دائمًا لبيانات HR؟", ["نعم","لا"], index=None)
    q5 = st.radio("5) إذا كانت بيانات التدريب متحيزة، فقد:", ["يختفي التحيز تلقائيًا","يعيد النموذج إنتاج التحيز","تزيد سرعة الحاسوب فقط"], index=None)
    if st.button("تصحيح الاختبار"):
        answers = [q1,q2,q3,q4,q5]
        correct = ["Artificial Intelligence","تعدد طبقات المعالجة في الشبكة","Classification","لا","يعيد النموذج إنتاج التحيز"]
        score = sum(a==b for a,b in zip(answers, correct))
        st.metric("النتيجة", f"{score}/5")
        if score >= 4: st.success("ممتاز. المفاهيم الأساسية واضحة.")
        elif score >= 3: st.info("جيد. راجع المقارنة بين ML وDL والقيود في HR.")
        else: st.warning("راجع أقسام AI وML وDL قبل الانتقال إلى المحاضرة الثانية.")

elif section == "المراجع":
    st.header("المراجع المعتمدة")
    st.markdown("""
- François Chollet, *Deep Learning with Python*.
- Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*.
- ميلاد وزان، *التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون*، ترجمة د. علاء طعيمة.
- ميلاد وزان، *التعلم العميق: المبادئ والمفاهيم والأساليب*، ترجمة د. علاء طعيمة.
- Marler & Boudreau (2017), *An Evidence-Based Review of HR Analytics*.
- Tambe, Cappelli & Yakubovich, *Artificial Intelligence in Human Resources Management: Challenges and a Path Forward*.
- Isson, Harriott & Fitz-enz, *People Analytics in the Era of Big Data*.
""")

st.divider()
st.caption("مقياس تطبيقات التعلم العميق — المحاضرة الأولى — موجه لطلبة إدارة الموارد البشرية")
