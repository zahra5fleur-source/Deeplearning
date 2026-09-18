import streamlit as st
from pathlib import Path

st.set_page_config(page_title="تطبيقات التعلم العميق في HR", layout="wide", initial_sidebar_state="collapsed")
ROOT=Path(__file__).parent
ASSETS=ROOT/'assets'

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family:'Cairo',sans-serif;}
.stApp{background:#F7FAFC;color:#0F172A;direction:rtl;}
header[data-testid="stHeader"]{background:rgba(247,250,252,.92);}
.block-container{max-width:1180px;padding-top:1.2rem;padding-right:270px;padding-left:2rem;}
.toc{position:fixed;right:18px;top:88px;width:235px;max-height:82vh;overflow:auto;background:#fff;border:1px solid #DCE7F5;border-radius:18px;padding:14px 12px;box-shadow:0 10px 30px rgba(37,99,235,.08);z-index:999;direction:rtl}
.toc h3{color:#1D4ED8;font-size:20px;margin:0 0 10px 0}.toc a{display:block;text-decoration:none;color:#334155;font-size:15px;font-weight:600;padding:8px 10px;margin:5px 0;border-radius:10px}.toc a:hover{background:#EFF6FF;color:#1D4ED8}.toc .home{background:linear-gradient(90deg,#EFF6FF,#F5F3FF);color:#1D4ED8}
.hero{background:linear-gradient(120deg,#EFF6FF 0%,#F5F3FF 55%,#ECFEFF 100%);border:1px solid #DCE7F5;border-radius:24px;padding:28px 30px;margin-bottom:20px;box-shadow:0 10px 28px rgba(30,64,175,.08)}
.hero h1{font-size:34px;color:#173B8F;margin:0 0 8px 0}.hero p{font-size:18px;color:#475569;margin:0}
.section-title{font-size:27px;font-weight:800;color:#1D4ED8;margin-top:34px;margin-bottom:12px;border-right:6px solid #7C3AED;padding-right:12px}
.card{background:#fff;border:1px solid #E2E8F0;border-radius:18px;padding:18px 20px;margin:10px 0;box-shadow:0 7px 18px rgba(15,23,42,.05);font-size:18px;line-height:2}
.callout{background:#FFFBEB;border:1px solid #FDE68A;border-right:6px solid #F59E0B;border-radius:16px;padding:16px 18px;font-size:17px;line-height:1.9;margin:16px 0}
.obj-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.obj{background:#fff;border:1px solid #DBEAFE;border-radius:14px;padding:13px 15px;font-size:16px;color:#1E3A8A;font-weight:600}
.table-wrap{overflow-x:auto;background:#fff;border:1px solid #DCE7F5;border-radius:18px;box-shadow:0 7px 18px rgba(15,23,42,.05);margin:16px 0}.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:16px;direction:rtl}.tbl th{background:linear-gradient(90deg,#2563EB,#7C3AED);color:#fff;padding:13px 10px}.tbl td{padding:12px 10px;border-bottom:1px solid #E2E8F0;background:#fff}.tbl tr:nth-child(even) td{background:#F8FAFC}.tbl tr:hover td{background:#EFF6FF}.tbl th:first-child{border-top-right-radius:16px}.tbl th:last-child{border-top-left-radius:16px}
.codebox{direction:ltr;text-align:left;background:#0F172A;color:#E2E8F0;border-radius:16px;padding:18px;font-family:Consolas,monospace;font-size:14px;white-space:pre-wrap;overflow-x:auto}
.review{background:linear-gradient(120deg,#ECFEFF,#EFF6FF);border:1px solid #BAE6FD;border-radius:18px;padding:18px 20px;margin:18px 0}
.small{font-size:14px;color:#64748B}
@media(max-width:900px){.toc{position:relative;right:auto;top:auto;width:auto;max-height:none;margin-bottom:15px}.block-container{padding-right:1rem;padding-left:1rem}.obj-grid{grid-template-columns:1fr}.hero h1{font-size:28px}}
</style>
""",unsafe_allow_html=True)

# بيانات المحاضرات مضمّنة داخل app.py حتى تعمل النسخة حتى لو لم يُرفع مجلد content إلى GitHub.
LECTURES = [{'no': 2,
  'title': 'أساسيات التعلم الآلي: التصنيف والانحدار وتقييم النماذج',
  'subtitle': 'Machine Learning Foundations for HR',
  'visual': 'lecture02_ml_pipeline.png',
  'objectives': ['تمييز التعلم الخاضع للإشراف وغير الخاضع للإشراف.',
                 'التمييز بين التصنيف Classification والانحدار Regression.',
                 'فهم تقسيم البيانات إلى تدريب واختبار.',
                 'التعرف على مؤشرات التقييم الأساسية دون الدخول في رياضيات معقدة.',
                 'صياغة مشكلات الموارد البشرية بصيغة تحليلية مناسبة.'],
  'sections': [['1. من البيانات إلى المشكلة التحليلية',
                ['التعلم الآلي لا يبدأ بالخوارزمية، بل يبدأ بتحديد سؤال إداري واضح. في الموارد البشرية قد يكون السؤال: هل سيغادر الموظف؟ '
                 'ما مستوى الأداء المتوقع؟ ما المجموعات المتشابهة من الموظفين؟ بعد تحديد السؤال نحدد المتغير الهدف Target والمتغيرات '
                 'التفسيرية Features.',
                 'في التعلم الخاضع للإشراف Supervised Learning تكون لدينا أمثلة تاريخية تتضمن المدخلات والنتيجة الصحيحة. أما التعلم غير '
                 'الخاضع للإشراف Unsupervised Learning فيبحث عن أنماط أو مجموعات داخل البيانات دون متغير هدف محدد.']],
               ['2. التصنيف Classification',
                ['التصنيف يستخدم عندما تكون النتيجة فئة أو تسمية. مثال HR: Attrition = Yes/No، أو تصنيف المرشحين إلى فئات، أو تحديد ما إذا '
                 'كانت رسالة الموظف إيجابية أو سلبية. عندما تكون هناك فئتان فقط يسمى ذلك Binary Classification.',
                 'في مشكلة دوران الموظفين، المتغير الهدف ليس رقمًا مستمرًا بل فئة. لذلك نحتاج إلى مقاييس تقييم مثل Accuracy وPrecision '
                 'وRecall وF1-score، ولا يكفي الاعتماد على Accuracy وحده عندما تكون الفئات غير متوازنة.']],
               ['3. الانحدار Regression',
                ['الانحدار يستخدم عندما تكون النتيجة رقمًا مستمرًا، مثل توقع عدد أيام الغياب، أو تقدير تقييم أداء عددي، أو توقع مدة البقاء '
                 'في المؤسسة. تختلف دوال الخسارة ومقاييس التقييم هنا عن التصنيف.',
                 'من المقاييس الشائعة MAE وMSE وRMSE. كلما انخفض الخطأ كان التنبؤ أقرب للقيم الحقيقية، لكن يجب تفسير المقياس في سياق '
                 'الوحدة المستخدمة.']],
               ['4. بيانات التدريب والاختبار',
                ['تقسيم البيانات إلى Training Set وTest Set ضروري لتقييم قدرة النموذج على التعميم. الهدف ليس أن يحفظ النموذج البيانات '
                 'السابقة، بل أن يعمل جيدًا مع بيانات لم يرها أثناء التدريب.',
                 'عندما يؤدي النموذج بصورة ممتازة على التدريب وضعيفة على الاختبار فهذه علامة محتملة على Overfitting. أما Underfitting '
                 'فيحدث عندما يكون النموذج بسيطًا أكثر من اللازم ولا يلتقط النمط حتى في بيانات التدريب.']],
               ['5. تقييم النموذج في سياق HR',
                ['اختيار المقياس يجب أن يعكس تكلفة الخطأ الإداري. في مثال Attrition قد يكون فقدان موظف عالي القيمة أكثر تكلفة من توجيه '
                 'تدخل احتفاظ لموظف كان سيبقى أصلًا. لذلك يصبح Recall مهمًا عندما نريد التقاط أكبر عدد من الحالات المعرضة للمغادرة.',
                 'التقييم الجيد يجمع بين المقياس الكمي وفهم السياق الإداري والعدالة والتفسير. لا يوجد مقياس واحد يصلح لكل المشكلات.']]],
  'comparison': [['المهمة', 'نوع الهدف', 'مثال HR', 'مقياس شائع'],
                 ['Classification', 'فئة', 'غادر/لم يغادر', 'F1, Recall'],
                 ['Regression', 'رقم مستمر', 'أيام الغياب', 'MAE, RMSE'],
                 ['Clustering', 'لا يوجد هدف', 'شرائح موظفين', 'Silhouette/فحص نوعي']],
  'example': 'إذا كان لدينا 1000 موظف و150 فقط غادروا، فإن نموذجًا يتنبأ دائمًا "لن يغادر" سيحقق دقة 85% لكنه عديم الفائدة عمليًا. هنا '
             'نحتاج إلى Precision وRecall وF1 بدل الاكتفاء بالدقة.',
  'quiz': [['ما نوع مشكلة توقع مغادرة الموظف؟', ['Regression', 'Classification', 'Clustering'], 'Classification'],
           ['متى يحدث Overfitting؟',
            ['عندما يتعلم النموذج التدريب أكثر من اللازم ولا يعمم جيدًا', 'عندما لا نستخدم أي بيانات', 'عندما تكون كل القيم رقمية'],
            'عندما يتعلم النموذج التدريب أكثر من اللازم ولا يعمم جيدًا']],
  'review': ['اشرح الفرق بين Classification وRegression بمثال من HR.',
             'لماذا لا تكفي Accuracy دائمًا؟',
             'ما الفرق بين Training Set وTest Set؟',
             'اشرح Overfitting وUnderfitting.'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 3,
  'title': 'مقدمة إلى TensorFlow وKeras وبناء نموذج Sequential',
  'subtitle': 'TensorFlow, Keras & Sequential Models',
  'visual': 'lecture03_keras_pipeline.png',
  'objectives': ['التعرف على دور TensorFlow وKeras.',
                 'فهم مفهوم الطبقة Layer والنموذج Model.',
                 'بناء نموذج Sequential بسيط.',
                 'التعرف على compile وfit وevaluate وpredict.',
                 'قراءة model.summary() بصورة مبسطة.'],
  'sections': [['1. لماذا نستخدم Keras؟',
                ['Keras واجهة عالية المستوى لبناء نماذج التعلم العميق. وهي تقلل التفاصيل البرمجية المتكررة وتسمح للطالب بالتركيز على منطق '
                 'النموذج: ما المدخلات؟ ما الطبقات؟ ما دالة الخسارة؟ وما المقياس؟',
                 'وفق وثائق Keras 3، يعد Sequential مناسبًا عندما يكون النموذج عبارة عن تتابع خطي من الطبقات، بحيث لكل طبقة مدخل واحد '
                 'ومخرج واحد.']],
               ['2. مفهوم Layer وModel',
                ['الطبقة Layer تنفذ تحويلًا على البيانات. طبقة Dense تربط كل وحدة في الطبقة السابقة بكل وحدة في الطبقة التالية. النموذج '
                 'Model يجمع عدة طبقات في بنية واحدة قابلة للتدريب.',
                 'عند تحديد شكل المدخل Input Shape يصبح من الأسهل فهم عدد المعاملات وإظهار summary قبل التدريب.']],
               ['3. دورة حياة نموذج Keras',
                ['الخطوات الأساسية هي: إنشاء النموذج، إضافة الطبقات، compile، ثم fit، ثم evaluate وأخيرًا predict. في compile نحدد '
                 'optimizer وloss وmetrics.',
                 'fit يقوم بالتدريب عبر epochs. evaluate يقيس الأداء على بيانات منفصلة. predict ينتج توقعات لحالات جديدة.']],
               ['4. مثال HR مبسط',
                ['نفترض أن كل موظف يمثله 8 متغيرات رقمية/مشفرة، ونريد توقع Attrition. يمكن بناء نموذج Sequential بطبقة Dense مخفية وطبقة '
                 'إخراج واحدة مع Sigmoid.',
                 'الهدف هنا ليس حفظ الكود، بل فهم أن كل سطر يعبر عن قرار تصميمي: عدد الخصائص، عدد الوحدات، دالة التفعيل، نوع المخرج، ودالة '
                 'الخسارة.']],
               ['5. أخطاء شائعة للمبتدئين',
                ['استخدام عدد كبير من الطبقات دون مبرر، نسيان تجهيز البيانات، اختيار Loss غير مناسبة، تقييم النموذج على نفس بيانات '
                 'التدريب، والخلط بين احتمالية التنبؤ والفئة النهائية.',
                 'ينبغي دائمًا البدء بنموذج بسيط ثم زيادة التعقيد فقط عند الحاجة.']]],
  'comparison': [['الدالة', 'وظيفتها'],
                 ['compile()', 'تهيئة طريقة التعلم: loss + optimizer + metrics'],
                 ['fit()', 'تدريب النموذج'],
                 ['evaluate()', 'تقييم الأداء'],
                 ['predict()', 'إنتاج توقعات جديدة'],
                 ['summary()', 'عرض بنية النموذج والمعاملات']],
  'code': 'import keras\n'
          'from keras import layers\n'
          '\n'
          'model = keras.Sequential([\n'
          '    keras.Input(shape=(8,)),\n'
          "    layers.Dense(16, activation='relu'),\n"
          "    layers.Dense(1, activation='sigmoid')\n"
          '])\n'
          "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])",
  'example': 'في Attrition، طبقة الإخراج ذات وحدة واحدة مع Sigmoid تعطي قيمة بين 0 و1 يمكن تفسيرها كدرجة/احتمال للمغادرة قبل تحويلها إلى '
             'فئة وفق Threshold مناسب.',
  'quiz': [['متى يكون Sequential مناسبًا؟', ['لنموذج خطي من الطبقات', 'دائمًا لأي نموذج', 'فقط للصور'], 'لنموذج خطي من الطبقات'],
           ['ما وظيفة fit؟', ['التدريب', 'رسم البيانات', 'حذف الطبقات'], 'التدريب']],
  'review': ['ما الفرق بين Layer وModel؟', 'اذكر مراحل دورة حياة نموذج Keras.', 'ما وظيفة compile؟', 'لماذا نحدد Input Shape؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 4,
  'title': 'الشبكات العصبية أمامية التغذية وMLP',
  'subtitle': 'Feedforward Neural Networks & Multilayer Perceptron',
  'visual': 'lecture04_mlp.png',
  'objectives': ['فهم العصبون الاصطناعي بصورة مبسطة.',
                 'تمييز طبقة الإدخال والمخفية والإخراج.',
                 'فهم Forward Pass وBackpropagation على المستوى المفاهيمي.',
                 'ربط MLP ببيانات الموارد البشرية الجدولية.'],
  'sections': [['1. العصبون الاصطناعي',
                ['العصبون يستقبل مدخلات x، يضربها في أوزان w، يضيف Bias ثم يمرر الناتج عبر دالة تفعيل. الأوزان هي ما يتعلمه النموذج أثناء '
                 'التدريب.',
                 'يمكن التفكير في الوزن باعتباره درجة أهمية تتغير أثناء التعلم، لكن لا ينبغي تفسير كل وزن مباشرة على أنه أثر سببي.']],
               ['2. طبقات الشبكة',
                ['Input Layer تمثل خصائص الموظف. Hidden Layers تتعلم تمثيلات وسيطة. Output Layer تنتج النتيجة النهائية. في Feedforward '
                 'Network تتحرك المعلومات من المدخل إلى المخرج دون حلقات رجوع.',
                 'MLP هو شكل شائع من الشبكات الأمامية يستخدم Dense Layers.']],
               ['3. Forward Pass وBackpropagation',
                ['في Forward Pass تنتقل البيانات عبر الطبقات للحصول على Prediction. نحسب بعد ذلك Loss التي تقيس الفرق بين التوقع والحقيقة.',
                 'Backpropagation يحسب كيف ساهمت المعاملات في الخطأ، ثم يستخدم Optimizer هذه المعلومات لتحديث الأوزان.']],
               ['4. لماذا MLP مناسب لبيانات HR؟',
                ['بيانات HR غالبًا جدولية: راتب، أقدمية، رضا، تقييم، عمل إضافي، قسم. بعد ترميز المتغيرات الفئوية وقياس المتغيرات الرقمية '
                 'يمكن استخدام MLP للتصنيف أو الانحدار.',
                 'مع ذلك، لا يعني ذلك أن MLP سيكون دائمًا أفضل من النماذج التقليدية. ينبغي مقارنته بخط أساس Baseline.']],
               ['5. عدد الطبقات والعصبونات',
                ['زيادة العمق والسعة تزيد قدرة النموذج على تمثيل أنماط معقدة، لكنها قد تزيد Overfitting والتكلفة الحسابية.',
                 'القاعدة التعليمية: ابدأ صغيرًا، راقب منحنيات التدريب والتحقق، ثم عدّل البنية تدريجيًا.']]],
  'comparison': [['المكوّن', 'وظيفته'],
                 ['Input', 'استقبال الخصائص'],
                 ['Hidden Dense', 'تعلم علاقات غير خطية'],
                 ['Activation', 'إضافة اللاخطية'],
                 ['Output', 'إنتاج التنبؤ'],
                 ['Weights/Bias', 'معاملات يتم تعلمها']],
  'example': 'مثال: 12 متغيرًا للموظف → Dense(32, ReLU) → Dense(16, ReLU) → Dense(1, Sigmoid) لتصنيف Attrition. هذا مثال تعليمي وليس وصفة '
             'مثلى لكل مؤسسة.',
  'quiz': [['ما الذي يتعلمه النموذج أساسًا؟', ['الأوزان والانحيازات', 'أسماء الأعمدة', 'ألوان الواجهة'], 'الأوزان والانحيازات'],
           ['ما اتجاه المعلومات في Feedforward؟', ['من المدخل إلى المخرج', 'ذهابًا وإيابًا دائمًا', 'عشوائي'], 'من المدخل إلى المخرج']],
  'review': ['ارسم بنية MLP بسيطة واشرح طبقاتها.',
             'ما وظيفة Loss؟',
             'ما الفرق بين Forward Pass وBackpropagation؟',
             'لماذا لا نزيد عدد الطبقات بلا حدود؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 5,
  'title': 'تدريب الشبكات العصبية والتحسين: Gradient Descent وAdam',
  'subtitle': 'Optimization & Training Deep Networks',
  'visual': 'lecture05_optimization.png',
  'objectives': ['فهم معنى Loss وOptimizer.',
                 'التعرف على Gradient Descent وSGD وAdam.',
                 'فهم Learning Rate وEpoch وBatch Size.',
                 'التعرف على Early Stopping وDropout كمفاهيم مساعدة.'],
  'sections': [['1. ما الذي نحاول تحسينه؟',
                ['التدريب يبحث عن مجموعة أوزان تقلل Loss. الخسارة ليست هي نفسها Metric دائمًا؛ فهي الدالة التي توجه التعلم، بينما Metric '
                 'تستخدم غالبًا للتفسير والتقييم.',
                 'في التصنيف الثنائي تستخدم Binary Crossentropy كثيرًا، وفي الانحدار تستخدم MSE أو MAE بحسب طبيعة المشكلة.']],
               ['2. Gradient Descent',
                ['الانحدار المتدرج يعدل الأوزان في اتجاه يخفض الخسارة. الفكرة تشبه النزول على سطح حتى نصل إلى منطقة منخفضة.',
                 'SGD يستخدم عينات أو دفعات صغيرة بدل حساب التدرج على كامل البيانات في كل خطوة.']],
               ['3. Learning Rate',
                ['معدل التعلم يحدد حجم خطوة التحديث. إذا كان كبيرًا جدًا قد يتجاوز الحل، وإذا كان صغيرًا جدًا يصبح التعلم بطيئًا.',
                 'لا توجد قيمة مثالية عامة؛ الاختيار تجريبي ويعتمد على النموذج والبيانات.']],
               ['4. Adam',
                ['Adam Optimizer يجمع أفكارًا من التكيف مع حجم التدرجات والزخم، ولذلك يستخدم بكثرة كبداية عملية في نماذج عديدة. Keras يتيح '
                 'Adam مباشرة ضمن optimizers.',
                 'استخدام Adam لا يلغي الحاجة إلى مراقبة التدريب أو تجربة إعدادات أخرى.']],
               ['5. التحكم في Overfitting',
                ['Early Stopping يوقف التدريب عندما يتوقف تحسن Validation Loss. Dropout يعطل وحدات عشوائيًا أثناء التدريب لتقليل الاعتماد '
                 'الزائد على مسارات محددة.',
                 'أفضل ممارسة تعليمية هي مراقبة Training vs Validation بدل الاعتماد على رقم واحد في نهاية التدريب.']]],
  'comparison': [['المفهوم', 'المعنى'],
                 ['Epoch', 'مرور كامل على بيانات التدريب'],
                 ['Batch Size', 'عدد الأمثلة قبل تحديث الأوزان'],
                 ['Learning Rate', 'حجم خطوة التحديث'],
                 ['Loss', 'الخطأ الذي يوجه التعلم'],
                 ['Optimizer', 'آلية تحديث الأوزان']],
  'example': 'إذا انخفض Training Loss باستمرار بينما بدأ Validation Loss في الارتفاع، فهذه علامة شائعة على Overfitting؛ يمكن التفكير في '
             'Early Stopping أو تنظيم النموذج.',
  'quiz': [['ما وظيفة Optimizer؟', ['تحديث الأوزان', 'ترجمة النصوص', 'حذف البيانات'], 'تحديث الأوزان'],
           ['ما خطر Learning Rate كبير جدًا؟', ['عدم الاستقرار وتجاوز الحل', 'بطء شديد فقط', 'تحسين مضمون'], 'عدم الاستقرار وتجاوز الحل']],
  'review': ['اشرح Gradient Descent بلغة مبسطة.', 'ما الفرق بين Epoch وBatch؟', 'ما وظيفة Adam؟', 'كيف تساعد Early Stopping؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 6,
  'title': 'دوال التفعيل: Sigmoid وTanh وReLU وSoftmax',
  'subtitle': 'Activation Functions',
  'visual': 'lecture06_activations.png',
  'objectives': ['فهم لماذا نحتاج اللاخطية.',
                 'تمييز Sigmoid وTanh وReLU وSoftmax.',
                 'اختيار دالة إخراج مناسبة لنوع المسألة.',
                 'فهم العلاقة بين Activation وLoss.'],
  'sections': [['1. لماذا نحتاج Activation؟',
                ['لو كانت كل الطبقات تحويلات خطية فقط، فإن تكديسها يبقى في النهاية تحويلًا خطيًا. دوال التفعيل تضيف اللاخطية التي تسمح '
                 'للنموذج بتمثيل علاقات أكثر تعقيدًا.',
                 'اختيار Activation قرار تصميمي مرتبط بموقع الطبقة ونوع المخرج.']],
               ['2. ReLU',
                ['ReLU تعيد صفرًا للقيم السالبة وتبقي القيم الموجبة كما هي. تستخدم كثيرًا في Hidden Layers لبساطتها وفاعليتها العملية.',
                 'من مشكلاتها Dying ReLU عندما تتوقف بعض الوحدات عن التنشيط لفترات طويلة.']],
               ['3. Sigmoid',
                ['Sigmoid تحول القيمة إلى نطاق 0-1، ولذلك تناسب طبقة إخراج في Binary Classification.',
                 'لا يعني خروج 0.8 أن القرار النهائي دائمًا "نعم"؛ يعتمد ذلك على Threshold والسياق.']],
               ['4. Tanh وSoftmax',
                ['Tanh تنتج قيمًا بين -1 و1 وتاريخيًا استخدمت في شبكات متكررة. Softmax تحول مجموعة logits إلى توزيع احتمالي على عدة فئات.',
                 'في تصنيف عدة فئات حصرية مثل مستويات خطر منخفض/متوسط/مرتفع يمكن استخدام Softmax في طبقة الإخراج.']],
               ['5. كيف نختار؟',
                ['في Hidden Dense Layers: ReLU نقطة بداية شائعة. في Binary Output: Sigmoid. في Multi-class Output: Softmax. لكن التصميم '
                 'النهائي يجب أن يتوافق أيضًا مع Loss المناسبة.',
                 'لا نختار الدالة لأنها الأكثر شهرة، بل لأنها تتوافق مع بنية المشكلة.']]],
  'comparison': [['الدالة', 'المجال', 'استخدام شائع'],
                 ['ReLU', '0 إلى ∞', 'Hidden Layers'],
                 ['Sigmoid', '0 إلى 1', 'Binary Output'],
                 ['Tanh', '-1 إلى 1', 'RNN/تمثيلات محددة'],
                 ['Softmax', 'احتمالات مجموعها 1', 'Multi-class Output']],
  'example': 'لتوقع Attrition نعم/لا: Dense(1, activation="sigmoid"). لتصنيف الموظفين إلى 3 فئات خطر: Dense(3, activation="softmax").',
  'quiz': [['أي دالة مناسبة غالبًا لخروج Binary Classification؟', ['Sigmoid', 'Softmax فقط', 'ReLU'], 'Sigmoid'],
           ['ما الهدف الأساسي من Activation؟', ['إضافة اللاخطية', 'زيادة عدد الصفوف', 'تقسيم البيانات'], 'إضافة اللاخطية']],
  'review': ['لماذا لا تكفي التحويلات الخطية؟', 'قارن Sigmoid وSoftmax.', 'متى نستخدم ReLU؟', 'ما المقصود بـDying ReLU؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 7,
  'title': 'تطبيق متكامل: التنبؤ بدوران الموظفين باستخدام شبكة عصبية',
  'subtitle': 'Integrated HR Classification Case',
  'visual': 'lecture07_project_pipeline.png',
  'objectives': ['دمج ما سبق في مشروع واحد.',
                 'صياغة مشكلة Attrition بوضوح.',
                 'تنفيذ خطوات تجهيز البيانات والتدريب والتقييم.',
                 'تفسير النتائج بحذر وربطها بالقرار الإداري.'],
  'sections': [['1. تعريف المشكلة',
                ['الهدف هو بناء نموذج يصنف الموظفين إلى مغادر/غير مغادر بناءً على بيانات تاريخية. نحدد وحدة التحليل: الموظف. ونحدد لحظة '
                 'التنبؤ حتى نتجنب تسرب المعلومات من المستقبل.',
                 'يجب أن تكون المتغيرات المستخدمة متاحة قبل اتخاذ القرار المتوقع.']],
               ['2. تجهيز البيانات',
                ['نفحص القيم المفقودة، المتغيرات الفئوية، القيم الشاذة، التوازن بين الفئات، ونقوم بترميز Categoricals وScaling عند الحاجة.',
                 'يجب فصل Train/Test قبل أي تحويل يتعلم من البيانات حتى نتجنب Data Leakage.']],
               ['3. بناء Baseline ثم Neural Network',
                ['نبدأ بخط أساس بسيط مثل Logistic Regression أو شجرة قرار. ثم نبني MLP ونقارن النتائج.',
                 'الفائدة ليست إثبات أن Deep Learning أفضل، بل معرفة ما إذا كان التعقيد الإضافي يضيف قيمة.']],
               ['4. التقييم',
                ['نستخدم Confusion Matrix وPrecision وRecall وF1، ويمكن استخدام ROC-AUC. إذا كانت تكلفة فقدان موظف مرتفعة قد نهتم بـRecall '
                 'للحالات المعرضة للمغادرة.',
                 'ينبغي أيضًا فحص الأداء عبر مجموعات فرعية عندما توجد مخاطر عدالة أو تفاوت.']],
               ['5. من التنبؤ إلى القرار',
                ['النموذج لا يقرر وحده من يجب "الاحتفاظ به". هو يقدم إشارة Risk Score تساعد HR في استهداف مقابلات أو تدخلات احتفاظ أو فحص '
                 'أسباب تنظيمية.',
                 'لا ينبغي تفسير التنبؤ على أنه سبب للمغادرة؛ الارتباط التنبؤي لا يثبت السببية.']]],
  'comparison': [['المرحلة', 'سؤال تحقق'],
                 ['Problem', 'ما القرار الذي سيدعمه النموذج؟'],
                 ['Data', 'هل البيانات متاحة قبل لحظة التنبؤ؟'],
                 ['Model', 'هل لدينا Baseline؟'],
                 ['Evaluation', 'هل المقياس يناسب تكلفة الخطأ؟'],
                 ['Action', 'كيف سيستخدم HR النتيجة؟']],
  'example': 'إذا كان Recall للحالات المغادرة 0.78 فهذا يعني أن النموذج التقط 78% من المغادرين الفعليين في بيانات الاختبار، وليس أنه "دقيق '
             '78%" بشكل عام.',
  'quiz': [['لماذا نستخدم Baseline؟',
            ['لمعرفة قيمة التعقيد الإضافي', 'لزيادة عدد الأعمدة', 'لإلغاء الاختبار'],
            'لمعرفة قيمة التعقيد الإضافي'],
           ['هل التنبؤ يثبت السبب؟', ['لا', 'نعم دائمًا', 'فقط مع Keras'], 'لا']],
  'review': ['اشرح خطوات المشروع من السؤال إلى القرار.', 'ما معنى Data Leakage؟', 'لماذا نحتاج Baseline؟', 'كيف تفسر Recall في Attrition؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 8,
  'title': 'الشبكات العصبية الالتفافية CNN: المفهوم والبنية',
  'subtitle': 'Convolutional Neural Networks - Fundamentals',
  'visual': 'lecture08_cnn.png',
  'objectives': ['فهم فكرة Convolution وFilter.',
                 'فهم Feature Maps وPooling.',
                 'تمييز CNN عن Dense Network.',
                 'معرفة متى تكون CNN مفيدة في سياقات HR.'],
  'sections': [['1. لماذا CNN؟',
                ['Dense Networks تتعامل مع كل المدخلات بصورة عامة، بينما CNN تستفيد من البنية المحلية في الصور أو السلاسل. الفلتر الصغير '
                 'يمر على البيانات بحثًا عن أنماط محلية.',
                 'الميزة الأساسية هي مشاركة الأوزان Weight Sharing التي تقلل عدد المعاملات مقارنة بالربط الكامل.']],
               ['2. Convolution وFeature Maps',
                ['الفلتر Kernel يتعلم نمطًا صغيرًا، ويطبق عبر المدخل لينتج Feature Map. في الصور قد تتعلم الطبقات المبكرة الحواف ثم تنتقل '
                 'الطبقات الأعمق إلى أنماط أكثر تعقيدًا.',
                 'في بيانات 1D يمكن لـConv1D اكتشاف أنماط محلية عبر الزمن أو التسلسل.']],
               ['3. Pooling',
                ['Pooling يقلل الأبعاد مع الاحتفاظ بالمعلومات المهمة. Max Pooling يأخذ القيمة الأعلى ضمن نافذة صغيرة.',
                 'هذا يقلل العبء الحسابي ويزيد بعض الاستقرار، لكنه يفقد جزءًا من التفاصيل.']],
               ['4. CNN وبيانات HR',
                ['CNN ليست الخيار الأول للبيانات الجدولية التقليدية في HR. يمكن أن تكون مفيدة عند تحليل صور وثائق، أو إشارات زمنية، أو '
                 'نصوص بعد تمثيلها، لكن الاستخدام يجب أن يبرره نوع البيانات.',
                 'من الخطأ استخدام CNN فقط لأنها "متقدمة".']],
               ['5. بنية مبسطة',
                ['Input → Convolution → Activation → Pooling → Flatten/Global Pooling → Dense Output. عدد الفلاتر وحجم Kernel من '
                 'Hyperparameters.',
                 'في التطبيقات الحديثة قد توجد بنى أعمق، لكن هذا التسلسل يكفي لفهم الفكرة الأساسية.']]],
  'comparison': [['العنصر', 'الوظيفة'],
                 ['Kernel/Filter', 'اكتشاف نمط محلي'],
                 ['Feature Map', 'ناتج تطبيق الفلتر'],
                 ['Pooling', 'تقليل الأبعاد'],
                 ['Flatten', 'تحويل المخرجات لمتجه'],
                 ['Conv1D/Conv2D', 'سلاسل/صور']],
  'example': 'مثال HR محتمل: تحليل صور وثائق ممسوحة ضوئيًا لاكتشاف نوع المستند قبل تمريره إلى نظام أرشفة، مع مراعاة الخصوصية والأمان.',
  'quiz': [['ما وظيفة Filter في CNN؟', ['اكتشاف أنماط محلية', 'حفظ أسماء الموظفين', 'حساب الرواتب'], 'اكتشاف أنماط محلية'],
           ['ما دور Pooling؟', ['تقليل الأبعاد', 'زيادة عدد الفئات', 'ترجمة النص'], 'تقليل الأبعاد']],
  'review': ['اشرح Convolution بلغة بسيطة.', 'ما هي Feature Map؟', 'لماذا Weight Sharing مهم؟', 'هل CNN مناسبة تلقائيًا لكل بيانات HR؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 9,
  'title': 'تطبيقات CNN في البيانات غير المهيكلة والسلاسل',
  'subtitle': 'CNN Applications Beyond Images',
  'visual': 'lecture09_cnn_apps.png',
  'objectives': ['فهم امتداد CNN إلى Conv1D.',
                 'التعرف على أمثلة تطبيقية للصور والنصوص والسلاسل.',
                 'ربط اختيار CNN بشكل البيانات.',
                 'فهم مخاطر استخدام البيانات غير المهيكلة في HR.'],
  'sections': [['1. من الصور إلى السلاسل',
                ['CNN اشتهرت بالصور، لكن نفس فكرة الأنماط المحلية يمكن تطبيقها على بيانات 1D مثل الإشارات أو تسلسلات نصية ممثلة عدديًا.',
                 'Conv1D يمرر الفلتر على بعد واحد، ويستخدم أحيانًا كبديل سريع لنماذج متكررة في بعض مهام التسلسل.']],
               ['2. تحليل النصوص',
                ['بعد تحويل الكلمات أو الرموز إلى تمثيلات عددية، يمكن لـCNN التقاط عبارات محلية أو n-gram-like patterns.',
                 'في HR قد يستخدم ذلك لتحليل تعليقات الموظفين، لكن يجب الانتباه إلى اللغة والسياق والتحيز.']],
               ['3. الصور والوثائق',
                ['في أنظمة HR الرقمية قد توجد وثائق ممسوحة أو صور بطاقات أو نماذج. CNN يمكن أن تكون جزءًا من نظام Computer Vision للتصنيف '
                 'أو الاستخراج.',
                 'مع البيانات الشخصية يجب تحديد غرض واضح، وتقليل جمع البيانات، وحماية الوصول.']],
               ['4. CNN في السلاسل الزمنية',
                ['يمكن لـConv1D التقاط أنماط قصيرة المدى في سلاسل الغياب أو الأحمال التشغيلية. كما يمكن دمج CNN مع LSTM في بنى هجينة.',
                 'المراجع التطبيقية في السلاسل الزمنية توضح أن CNN قد تعمل كمستخرج خصائص قبل LSTM.']],
               ['5. متى نستخدمها؟',
                ['عندما تكون البنية المحلية في البيانات ذات معنى، وحين تتوفر كمية مناسبة من البيانات، وعندما تكون الفائدة أكبر من التكلفة '
                 'والتعقيد.',
                 'البدء بمشكلة واضحة وخط أساس يظل قاعدة أساسية.']]],
  'comparison': [['نوع البيانات', 'طبقة محتملة', 'مثال'],
                 ['صور', 'Conv2D', 'تصنيف وثائق'],
                 ['سلسلة زمنية', 'Conv1D', 'أنماط غياب قصيرة'],
                 ['نص ممثل عدديًا', 'Conv1D', 'تصنيف تعليقات'],
                 ['جدول HR', 'Dense/ML تقليدي', 'Attrition']],
  'example': 'نموذج CNN-LSTM يمكن أن يستخدم CNN لاستخراج أنماط محلية من سلسلة زمنية ثم LSTM لالتقاط الاعتماد الطويل، لكن لا يستخدم إلا إذا '
             'أثبتت المقارنة أنه يضيف قيمة.',
  'quiz': [['أي طبقة أقرب لسلسلة زمنية 1D؟', ['Conv1D', 'Conv2D فقط', 'Dense لا غير'], 'Conv1D'],
           ['ما أهم شرط قبل استخدام بيانات HR غير المهيكلة؟',
            ['الخصوصية والغرض الواضح', 'زيادة الألوان', 'إلغاء التقييم'],
            'الخصوصية والغرض الواضح']],
  'review': ['ما الفرق بين Conv1D وConv2D؟', 'اذكر تطبيقين لـCNN في HR.', 'ما فائدة CNN-LSTM؟', 'متى لا تكون CNN مناسبة؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 10,
  'title': 'الشبكات العصبية المتكررة RNN والبيانات التسلسلية',
  'subtitle': 'Recurrent Neural Networks',
  'visual': 'lecture10_rnn.png',
  'objectives': ['فهم معنى Sequence Data.',
                 'فهم الحالة المخفية Hidden State.',
                 'تمييز RNN عن MLP.',
                 'التعرف على مشكلة Vanishing Gradient.',
                 'ربط RNN بأمثلة HR زمنية.'],
  'sections': [['1. ما هي البيانات التسلسلية؟',
                ['في بعض المشكلات ترتيب الملاحظات مهم: غياب شهري، تقييمات أداء دورية، سلسلة أحداث الموظف، أو كلمات جملة.',
                 'MLP العادي يتعامل غالبًا مع متجه ثابت، بينما RNN صممت للاحتفاظ بمعلومة من خطوات سابقة عبر Hidden State.']],
               ['2. فكرة التكرار',
                ['في كل خطوة زمنية تأخذ RNN المدخل الحالي والحالة السابقة، وتنتج حالة جديدة ومخرجًا. نفس مجموعة الأوزان يعاد استخدامها عبر '
                 'الزمن.',
                 'هذا يجعلها مناسبة للتسلسلات ذات الأطوال المختلفة نسبيًا.']],
               ['3. Unrolling',
                ['للفهم نرسم RNN كأنها سلسلة من الخلايا المتكررة عبر الزمن، رغم أنها نفس الخلية والأوزان.',
                 'هذا التمثيل يوضح كيف تنتقل الذاكرة من t-1 إلى t ثم t+1.']],
               ['4. Vanishing/Exploding Gradients',
                ['عند تدريب RNN على تسلسلات طويلة قد تضعف التدرجات أو تتضخم، مما يصعب تعلم الاعتماد طويل المدى.',
                 'ظهرت LSTM وGRU جزئيًا لمعالجة هذه الصعوبة بصورة أكثر استقرارًا.']],
               ['5. مثال HR',
                ['إذا كانت لدينا سلسلة شهرية للغياب والإنتاجية والرضا، يمكن بناء نموذج يتعلم من الترتيب الزمني لتوقع خطر الغياب أو الأداء '
                 'في الشهر التالي.',
                 'يجب الحفاظ على ترتيب الزمن وعدم استخدام معلومات مستقبلية في التدريب.']]],
  'comparison': [['الخاصية', 'MLP', 'RNN'],
                 ['ترتيب الزمن', 'غير أساسي', 'أساسي'],
                 ['حالة داخلية', 'لا', 'نعم'],
                 ['استخدام شائع', 'بيانات جدولية', 'تسلسلات'],
                 ['تحدي', 'Overfitting', 'Vanishing Gradient + Overfitting']],
  'example': 'إذا استخدمنا بيانات أشهر يناير إلى يونيو للتنبؤ بيوليو، لا يجوز أن تدخل معلومات أغسطس في أي خطوة من تجهيز التدريب؛ هذا مثال '
             'على ضرورة تجنب leakage الزمني.',
  'quiz': [['ما الذي تمثله Hidden State؟', ['معلومة متراكمة عن التسلسل', 'لون الرسم', 'عدد الملفات'], 'معلومة متراكمة عن التسلسل'],
           ['لماذا ظهرت LSTM؟',
            ['لتحسين تعلم الاعتماد الطويل في RNN', 'لإنشاء جداول فقط', 'لإلغاء الزمن'],
            'لتحسين تعلم الاعتماد الطويل في RNN']],
  'review': ['ما الفرق بين MLP وRNN؟', 'اشرح Hidden State.', 'ما معنى Unrolling؟', 'لماذا Vanishing Gradient مهم؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.',
                 'Brownlee, J. (2018). Deep Learning for Time Series Forecasting: Predict the Future with MLPs, CNNs and LSTMs in '
                 'Python.']},
 {'no': 11,
  'title': 'شبكات الذاكرة الطويلة قصيرة المدى LSTM',
  'subtitle': 'Long Short-Term Memory Networks',
  'visual': 'lecture11_lstm.png',
  'objectives': ['فهم الهدف من LSTM.',
                 'التعرف على Cell State والبوابات بصورة مبسطة.',
                 'فهم Forget/Input/Output Gates.',
                 'استخدام LSTM في مسائل زمنية HR.'],
  'sections': [['1. لماذا LSTM؟',
                ['LSTM نوع من RNN صمم للتعامل بصورة أفضل مع الاعتماد طويل المدى. بدلاً من الاعتماد على تحديث بسيط للحالة، تستخدم مسار '
                 'ذاكرة وبوابات تتحكم في المعلومات.',
                 'الفكرة الأساسية ليست حفظ المعادلات، بل فهم أن النموذج يتعلم ماذا يحتفظ به وماذا ينسى.']],
               ['2. Cell State',
                ['Cell State يمثل مسار ذاكرة يمتد عبر الخطوات الزمنية. التعديلات عليه تنظمها البوابات.',
                 'هذا يساعد على نقل معلومات مهمة لفترات أطول مقارنة بـSimple RNN.']],
               ['3. البوابات',
                ['Forget Gate تتحكم فيما يحذف من الذاكرة. Input Gate تتحكم في المعلومات الجديدة التي تضاف. Output Gate تتحكم فيما يظهر '
                 'كحالة/مخرج.',
                 'هذه البوابات تتعلم من البيانات ولا يحددها الباحث يدويًا لكل حالة.']],
               ['4. شكل المدخل',
                ['في Keras، مدخل LSTM يكون عادة ثلاثي الأبعاد: samples × timesteps × features. هذه نقطة عملية مهمة عند تجهيز بيانات '
                 'السلاسل الزمنية.',
                 'يمكن استخدام return_sequences=True عندما نحتاج مخرجًا عند كل خطوة وليس فقط آخر مخرج.']],
               ['5. مثال HR',
                ['نستخدم آخر 12 شهرًا من الغياب والرضا والعمل الإضافي لتوقع الغياب في الشهر القادم أو خطر الانقطاع.',
                 'يجب مقارنة LSTM بخط أساس أبسط؛ تعقيد LSTM لا يضمن أداء أفضل خاصة مع عينات HR الصغيرة.']]],
  'comparison': [['البوابة', 'الدور المبسط'],
                 ['Forget', 'ما الذي ننساه؟'],
                 ['Input', 'ما الذي نضيفه؟'],
                 ['Cell State', 'ذاكرة ممتدة'],
                 ['Output', 'ما الذي نخرجه؟']],
  'example': 'صياغة المدخل: لكل موظف مصفوفة 12×4 تمثل 12 شهرًا و4 متغيرات زمنية. يصبح عدد الموظفين هو بعد samples.',
  'quiz': [['ما وظيفة Forget Gate؟',
            ['التحكم فيما ينسى من الذاكرة', 'تحديد لون الجدول', 'تغيير عدد الفئات'],
            'التحكم فيما ينسى من الذاكرة'],
           ['ما شكل مدخل LSTM غالبًا؟', ['3D: samples×timesteps×features', '1D فقط', 'صورة فقط'], '3D: samples×timesteps×features']],
  'review': ['لماذا LSTM أفضل من Simple RNN في بعض التسلسلات الطويلة؟',
             'اشرح Cell State.',
             'اذكر البوابات الثلاث.',
             'ما معنى samples×timesteps×features؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.',
                 'Brownlee, J. (2018). Deep Learning for Time Series Forecasting: Predict the Future with MLPs, CNNs and LSTMs in '
                 'Python.']},
 {'no': 12,
  'title': 'شبكات GRU ومقارنتها بـLSTM',
  'subtitle': 'Gated Recurrent Unit',
  'visual': 'lecture12_gru.png',
  'objectives': ['فهم البنية المبسطة لـGRU.', 'تمييز Reset وUpdate Gates.', 'مقارنة GRU وLSTM.', 'معرفة متى نجرب كل نموذج.'],
  'sections': [['1. ما هي GRU؟',
                ['GRU نوع من الشبكات المتكررة ذات البوابات، صممت لتقديم آلية ذاكرة أبسط من LSTM مع عدد أقل من المكونات.',
                 'تستخدم أساسًا Update Gate وReset Gate للتحكم في المعلومات القديمة والجديدة.']],
               ['2. Update Gate',
                ['تحدد مقدار الحالة السابقة الذي سيستمر ومقدار المعلومات الجديدة التي ستدخل في الحالة.',
                 'يمكن النظر إليها على أنها آلية موازنة بين الذاكرة القديمة والتحديث.']],
               ['3. Reset Gate',
                ['تتحكم في مدى تجاهل بعض المعلومات السابقة عند حساب التمثيل الجديد.',
                 'هذه البوابات تتعلم قيمها من البيانات أثناء التدريب.']],
               ['4. GRU أم LSTM؟',
                ['لا توجد قاعدة تقول إن أحدهما أفضل دائمًا. GRU أبسط وعدد معاملاته أقل عادة، وقد تتدرب أسرع. LSTM أكثر تفصيلًا في إدارة '
                 'الذاكرة.',
                 'الاختيار يتم بالتجربة المنضبطة على نفس تقسيم البيانات ومقاييس التقييم.']],
               ['5. مثال HR',
                ['في سلسلة شهرية لقياسات الاندماج والغياب، يمكن مقارنة GRU وLSTM من حيث F1 أو MAE وزمن التدريب والاستقرار.',
                 'إذا كان الفرق في الأداء طفيفًا، فقد تكون البنية الأبسط أكثر ملاءمة للتدريس أو النشر.']]],
  'comparison': [['الجانب', 'LSTM', 'GRU'],
                 ['البوابات الأساسية', 'Forget/Input/Output', 'Reset/Update'],
                 ['التعقيد', 'أعلى', 'أبسط'],
                 ['المعاملات', 'أكثر غالبًا', 'أقل غالبًا'],
                 ['الأفضل؟', 'يعتمد على البيانات', 'يعتمد على البيانات']],
  'example': 'المقارنة العادلة تعني تثبيت نفس Train/Test، نفس المتغيرات، نفس المقاييس، ثم مقارنة الأداء والزمن، وليس تدريب كل نموذج على '
             'بيانات مختلفة.',
  'quiz': [['كم بوابة رئيسية في الشرح المبسط لـGRU؟', ['2', '5', '0'], '2'],
           ['هل GRU أفضل دائمًا من LSTM؟', ['لا', 'نعم', 'فقط في HR'], 'لا']],
  'review': ['اشرح Reset وUpdate Gate.', 'قارن GRU وLSTM.', 'كيف تجري مقارنة عادلة؟', 'متى تفضل نموذجًا أبسط؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.',
                 'Brownlee, J. (2018). Deep Learning for Time Series Forecasting: Predict the Future with MLPs, CNNs and LSTMs in '
                 'Python.']},
 {'no': 13,
  'title': 'Google Colab والـGPU وتجهيز بيئة التجريب',
  'subtitle': 'Colab, GPU & Reproducible Experiments',
  'visual': 'lecture13_colab.png',
  'objectives': ['استخدام Google Colab لتشغيل نماذج Keras.',
                 'فهم الفرق العام بين CPU وGPU.',
                 'التعرف على Notebook وRuntime.',
                 'حفظ النتائج وإعادة التجربة بصورة منظمة.'],
  'sections': [['1. ما هو Colab؟',
                ['Google Colab بيئة Notebook تعمل في المتصفح وتسمح بتشغيل Python دون إعداد محلي مع إمكانية اختيار Runtime يدعم GPU حسب '
                 'التوفر والخطة.',
                 'الميزة التعليمية هي تقليل مشكلات التثبيت ومشاركة الدفاتر مع الطلبة.']],
               ['2. Notebook Cells',
                ['دفتر Colab يتكون من خلايا Code وخلايا Text/Markdown. تنظيم الدفتر إلى أقسام: تحميل البيانات، الاستكشاف، التجهيز، '
                 'النموذج، التقييم، الاستنتاجات يجعل المشروع قابلًا للمراجعة.',
                 'لا ينبغي وضع كامل المشروع في خلية واحدة.']],
               ['3. CPU وGPU',
                ['GPU يستطيع تنفيذ عدد كبير من العمليات المتوازية، وهو مفيد في نماذج الشبكات العصبية خاصة عندما تكون المصفوفات كبيرة.',
                 'في المشاريع الصغيرة قد لا يكون GPU أسرع دائمًا بسبب تكاليف نقل البيانات والإعداد.']],
               ['4. تفعيل GPU',
                ['في Colab يمكن اختيار Runtime ثم Change runtime type ثم GPU عندما يكون الخيار متاحًا. بعد ذلك يمكن فحص الأجهزة المتاحة من '
                 'داخل Python.',
                 'توفر GPU قد يتغير، لذلك يجب أن يكون الكود قادرًا على العمل أيضًا على CPU.']],
               ['5. قابلية إعادة الإنتاج',
                ['نسجل الإصدارات، البذور العشوائية، تقسيم البيانات، المعلمات، والنتائج. نحفظ الرسوم والجداول ونكتب استنتاجًا بعد كل تجربة.',
                 'في مشروع HR، يجب عدم رفع بيانات شخصية حساسة إلى خدمات سحابية دون تصريح وسياسة واضحة.']]],
  'comparison': [['العنصر', 'وظيفته'],
                 ['Notebook', 'تنظيم كود + شرح'],
                 ['Runtime', 'بيئة التنفيذ'],
                 ['GPU', 'تسريع عمليات متوازية'],
                 ['Drive/Files', 'حفظ/تحميل'],
                 ['Seed', 'تحسين قابلية إعادة النتائج']],
  'code': "import tensorflow as tf\nprint(tf.config.list_physical_devices('GPU'))\n",
  'example': 'يمكن للطالب إنشاء Notebook يبدأ بوصف مشكلة Attrition، ثم خلية لتحميل CSV، ثم تجهيز البيانات، ثم النموذج، ثم Confusion '
             'Matrix، ثم خلاصة إدارية.',
  'quiz': [['ما فائدة Notebook؟', ['دمج الكود والشرح والنتائج', 'زيادة الرواتب', 'إلغاء البيانات'], 'دمج الكود والشرح والنتائج'],
           ['هل GPU ضروري لكل تجربة؟', ['لا', 'نعم دائمًا', 'فقط للانحدار'], 'لا']],
  'review': ['اشرح Runtime في Colab.',
             'ما الفرق العام بين CPU وGPU؟',
             'كيف تنظم Notebook جيد؟',
             'ما الاعتبار الأخلاقي عند رفع بيانات HR للسحابة؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.',
                 'Google Colab documentation: GPU runtime and notebook workflow (accessed 2026).']},
 {'no': 14,
  'title': 'تصميم المشروع التطبيقي النهائي في إدارة الموارد البشرية',
  'subtitle': 'Capstone Project Design',
  'visual': 'lecture14_project.png',
  'objectives': ['صياغة سؤال مشروع قابل للتنفيذ.',
                 'اختيار Dataset ومتغير هدف مناسب.',
                 'تحديد Baseline ونموذج Deep Learning.',
                 'بناء خطة تقييم وتفسير.',
                 'إعداد مخرجات المشروع للتسليم.'],
  'sections': [['1. اختيار المشكلة',
                ['المشكلة الجيدة محددة، لها متغير هدف أو مخرج واضح، ولها قيمة إدارية. أمثلة: Attrition، الأداء، الغياب، Engagement Text '
                 'Classification، Workforce Forecasting.',
                 'نتجنب العناوين العامة مثل "استخدام الذكاء الاصطناعي في HR" دون سؤال تحليلي محدد.']],
               ['2. اختيار البيانات',
                ['يجب معرفة مصدر البيانات، حجمها، المتغيرات، القيم المفقودة، وتوازن الفئات. في المشاريع التعليمية يمكن استخدام Dataset '
                 'عامة منزوعة الهوية.',
                 'إذا كانت البيانات اصطناعية أو عامة يجب التصريح بذلك وعدم الادعاء أنها تمثل المؤسسة محليًا.']],
               ['3. خطة النمذجة',
                ['نحدد Baseline بسيط ثم نموذج الشبكة المناسب. البيانات الجدولية: MLP. التسلسل: RNN/LSTM/GRU. الصور: CNN.',
                 'لا نختار البنية لأن اسمها متقدم؛ يجب أن تتوافق مع شكل البيانات.']],
               ['4. خطة التقييم',
                ['نحدد Metric رئيسية ومقاييس مساعدة قبل التدريب. في التصنيف نستخدم Confusion Matrix وF1/Recall/Precision. في الانحدار '
                 'MAE/RMSE.',
                 'نضيف فحص Overfitting وربما مقارنة وقت التدريب وتعقيد النموذج.']],
               ['5. التفسير والتوصية',
                ['نميز بين Performance وDecision Value. نتيجة فنية جيدة لا تكفي إذا لم نفهم كيف يمكن استخدامها بصورة عادلة ومشروعة.',
                 'نختم بتوصية عملية محدودة بما تسمح به البيانات، مع ذكر القيود.']]],
  'comparison': [['جزء المشروع', 'المطلوب'],
                 ['Problem', 'سؤال واضح + قيمة HR'],
                 ['Data', 'وصف + مصدر + تجهيز'],
                 ['Baseline', 'نموذج بسيط للمقارنة'],
                 ['DL Model', 'مبرر حسب نوع البيانات'],
                 ['Evaluation', 'مقاييس مناسبة'],
                 ['Discussion', 'تفسير + قيود + أخلاقيات']],
  'example': 'عنوان جيد: "التنبؤ بدوران الموظفين باستخدام MLP: مقارنة مع Logistic Regression على بيانات عامة" لأنه يحدد الهدف والمنهج '
             'والمقارنة.',
  'quiz': [['ما أول خطوة في المشروع؟', ['تحديد المشكلة', 'اختيار اللون', 'تشغيل GPU'], 'تحديد المشكلة'],
           ['لماذا نحتاج Baseline؟', ['للمقارنة', 'لزيادة عدد الصفحات', 'لإلغاء الأخطاء'], 'للمقارنة']],
  'review': ['اقترح عنوان مشروع قابل للتنفيذ.',
             'ما العناصر التي يجب وصفها في Dataset؟',
             'كيف تختار Metric؟',
             'ما الذي يجعل التوصية مسؤولة؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']},
 {'no': 15,
  'title': 'عرض المشاريع وتقييم النماذج وتفسير النتائج بصورة مسؤولة',
  'subtitle': 'Project Presentation, Evaluation & Responsible Interpretation',
  'visual': 'lecture15_evaluation.png',
  'objectives': ['تقديم مشروع بصورة منظمة.',
                 'التمييز بين جودة النموذج وجودة العرض.',
                 'تفسير المقاييس والأخطاء.',
                 'مناقشة القيود والتحيز والعدالة.',
                 'تحويل النتائج إلى توصيات غير مبالغ فيها.'],
  'sections': [['1. بنية العرض',
                ['عرض المشروع يبدأ بالمشكلة والسياق، ثم البيانات، ثم المنهج، ثم النتائج، ثم التفسير والقيود، وأخيرًا التوصية.',
                 'لا يبدأ العرض بالكود، لأن الكود وسيلة وليس سؤال المشروع.']],
               ['2. تقييم جودة النموذج',
                ['نقيم مدى ملاءمة البيانات، صحة التقسيم، وجود Baseline، المقاييس، Overfitting، واستقرار النتائج.',
                 'رقم Accuracy مرتفع لا يكفي إذا كانت الفئات غير متوازنة أو إذا كان هناك Leakage.']],
               ['3. قراءة Confusion Matrix',
                ['True Positive وFalse Positive وFalse Negative وTrue Negative تساعدنا على فهم نوع الخطأ. في HR قد تختلف تكلفة كل نوع خطأ.',
                 'يجب شرح المقياس بلغة إدارية: من الأشخاص الذين أخطأنا في تصنيفهم؟ وما أثر ذلك؟']],
               ['4. القيود والأخلاقيات',
                ['نذكر محدودية العينة، جودة القياس، عدم التمثيل، احتمالات التحيز، وحساسية البيانات.',
                 'في القرارات عالية الأثر مثل التوظيف والترقية لا ينبغي تحويل Risk Score إلى قرار آلي دون رقابة بشرية وتقييم قانوني '
                 'وأخلاقي.']],
               ['5. التوصية النهائية',
                ['التوصية الجيدة مرتبطة بما أظهرته البيانات ولا تدعي السببية إذا كان المشروع تنبؤيًا فقط.',
                 'مثال: "يمكن استخدام النموذج كأداة فرز أولي لتحديد الحالات التي تحتاج مراجعة بشرية" أفضل من "النموذج يحدد من سيغادر بشكل '
                 'مؤكد".']]],
  'comparison': [['معيار التقييم', 'سؤال'],
                 ['Problem Framing', 'هل السؤال واضح ومفيد؟'],
                 ['Data', 'هل المصدر والتجهيز موثقان؟'],
                 ['Model', 'هل الاختيار مبرر؟'],
                 ['Metrics', 'هل تقيس ما يهم؟'],
                 ['Interpretation', 'هل التفسير صحيح وغير مبالغ؟'],
                 ['Ethics', 'هل نوقشت العدالة والخصوصية؟']],
  'example': 'في العرض النهائي، أظهر Confusion Matrix واحدة واضحة واشرح خطأين مهمين بدل عرض عشرة مخططات دون تفسير.',
  'quiz': [['ما الذي يجب أن يبدأ به العرض؟', ['المشكلة والسياق', 'الكود', 'المراجع فقط'], 'المشكلة والسياق'],
           ['هل Risk Score قرار نهائي؟', ['لا', 'نعم دائمًا', 'فقط إذا كان >0.5'], 'لا']],
  'review': ['ضع مخطط عرض من 6 شرائح لمشروعك.',
             'كيف تشرح False Negative في Attrition؟',
             'اذكر ثلاثة قيود يجب مناقشتها.',
             'ما الفرق بين Prediction وCausation؟'],
  'references': ['Chollet, F. (2018). Deep Learning with Python. Manning.',
                 'Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (2nd ed.). O’Reilly.',
                 'Wazan, M. التعلم العميق: المبادئ والمفاهيم والأساليب. ترجمة علاء طعيمة.',
                 'Wazan, M. (2022). التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون. ترجمة علاء طعيمة.',
                 'Marler, J. H., & Boudreau, J. W. (2017). An evidence-based review of HR Analytics. The International Journal of Human '
                 'Resource Management, 28(1), 3-26.',
                 'Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial Intelligence in Human Resources Management: Challenges and '
                 'a Path Forward. California Management Review, 61(4), 15-42.',
                 'Keras 3 Documentation (accessed 2026): Sequential model, Optimizers, Activations, Recurrent Layers.']}]
LECTURE_MAP = {int(d["no"]): d for d in LECTURES}
lecture_numbers = sorted(LECTURE_MAP)
if not lecture_numbers:
    st.error("لا توجد بيانات محاضرات في التطبيق.")
    st.stop()

try:
    raw = st.query_params.get("lecture", str(lecture_numbers[0]))
    if isinstance(raw, list):
        raw = raw[0] if raw else str(lecture_numbers[0])
    current_no = int(raw)
except Exception:
    current_no = lecture_numbers[0]
if current_no not in LECTURE_MAP:
    current_no = lecture_numbers[0]
D = LECTURE_MAP[current_no]

st.markdown("""
<style>
.course-nav{position:fixed;right:16px;top:74px;width:255px;max-height:88vh;overflow-y:auto;background:#FFFFFF;
 border:1px solid #DCE7F5;border-radius:20px;padding:14px 12px;box-shadow:0 12px 34px rgba(37,99,235,.10);z-index:1000;direction:rtl}
.course-nav .nav-title{font-size:19px;font-weight:800;color:#173B8F;margin:2px 4px 10px}
.course-nav .lecture-link{display:block;text-decoration:none;color:#334155;background:#F8FAFC;border:1px solid #E7EEF8;
 padding:9px 10px;margin:6px 0;border-radius:11px;font-size:14px;font-weight:650;line-height:1.45}
.course-nav .lecture-link:hover{background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE}
.course-nav .lecture-link.active{background:linear-gradient(90deg,#E0F2FE,#EEF2FF);color:#1D4ED8;border-color:#93C5FD;font-weight:800}
.course-nav .divider{height:1px;background:#E2E8F0;margin:12px 0}
.course-nav .sec-link{display:block;text-decoration:none;color:#64748B;padding:6px 9px;margin:2px 0;border-radius:8px;font-size:13px}
.course-nav .sec-link:hover{background:#F1F5F9;color:#1D4ED8}
.course-nav .smallnav{font-size:12px;color:#94A3B8;margin:4px 4px 8px}
.nav-buttons{display:flex;gap:10px;justify-content:space-between;margin:28px 0 8px}
.nav-btn{display:inline-block;text-decoration:none;background:#fff;border:1px solid #BFDBFE;color:#1D4ED8;border-radius:12px;padding:10px 14px;font-weight:700}
.nav-btn:hover{background:#EFF6FF}
.quick-label{font-weight:800;color:#173B8F;margin-top:3px}
@media(max-width:900px){.course-nav{position:relative;right:auto;top:auto;width:auto;max-height:none;margin-bottom:14px}.block-container{padding-right:1rem;padding-left:1rem}}
</style>
""", unsafe_allow_html=True)

lecture_links=[]
for n in lecture_numbers:
    cls='lecture-link active' if n==current_no else 'lecture-link'
    short=LECTURE_MAP[n]['title']
    if len(short)>52:
        short=short[:50]+'…'
    lecture_links.append(f'<a class="{cls}" href="?lecture={n}" target="_self"><b>المحاضرة {n}</b><br>{short}</a>')
section_links=''.join([f'<a class="sec-link" href="#sec{i+1}">{title}</a>' for i,(title,_) in enumerate(D['sections'])])
nav_html=(
    '<div class="course-nav">'
    '<div class="nav-title">📚 محاضرات المقياس</div>'
    '<div class="smallnav">اختر أي محاضرة للانتقال إليها مباشرة</div>'
    + ''.join(lecture_links) +
    '<div class="divider"></div>'
    f'<div class="nav-title">📑 فهرس المحاضرة {current_no}</div>'
    '<a class="sec-link" href="#top">بداية المحاضرة</a>'
    '<a class="sec-link" href="#objectives">الأهداف</a>'
    + section_links +
    '<a class="sec-link" href="#compare">المقارنة والتلخيص</a>'
    '<a class="sec-link" href="#quiz">الاختبار القصير</a>'
    '<a class="sec-link" href="#review">أسئلة المراجعة</a>'
    '<a class="sec-link" href="#refs">المراجع</a>'
    '</div>'
)
st.markdown(nav_html, unsafe_allow_html=True)

st.markdown('<div class="quick-label">الانتقال السريع بين المحاضرات</div>', unsafe_allow_html=True)
selected_no = st.selectbox(
    "الانتقال السريع بين المحاضرات",
    lecture_numbers,
    format_func=lambda n: f"المحاضرة {n} — {LECTURE_MAP[n]['title']}",
    index=lecture_numbers.index(current_no),
    label_visibility="collapsed",
    key="lecture_selector",
)
if int(selected_no) != current_no:
    st.query_params["lecture"] = str(int(selected_no))
    st.rerun()

st.markdown(f'<div id="top" class="hero"><h1>المحاضرة {D["no"]}: {D["title"]}</h1><p>{D["subtitle"]}</p></div>',unsafe_allow_html=True)

st.markdown('<div id="objectives" class="section-title">أهداف المحاضرة</div>',unsafe_allow_html=True)
objs=''.join([f'<div class="obj">🎯 {x}</div>' for x in D['objectives']])
st.markdown(f'<div class="obj-grid">{objs}</div>',unsafe_allow_html=True)

img=ASSETS/D['visual']
if img.exists():
    st.image(str(img),use_container_width=True)

for i,(title,paras) in enumerate(D['sections']):
    st.markdown(f'<div id="sec{i+1}" class="section-title">{title}</div>',unsafe_allow_html=True)
    for p in paras:
        st.markdown(f'<div class="card">{p}</div>',unsafe_allow_html=True)

if D.get('comparison'):
    st.markdown('<div id="compare" class="section-title">مقارنة وتلخيص بصري</div>',unsafe_allow_html=True)
    rows=D['comparison']
    hdr=''.join(f'<th>{x}</th>' for x in rows[0])
    body=''.join('<tr>'+''.join(f'<td>{x}</td>' for x in r)+'</tr>' for r in rows[1:])
    st.markdown(f'<div class="table-wrap"><table class="tbl"><thead><tr>{hdr}</tr></thead><tbody>{body}</tbody></table></div>',unsafe_allow_html=True)

if D.get('code'):
    st.markdown('<div class="section-title">مثال برمجي مبسط</div>',unsafe_allow_html=True)
    st.code(D['code'], language='python')

st.markdown('<div class="section-title">مثال تطبيقي من الموارد البشرية</div>',unsafe_allow_html=True)
st.markdown(f'<div class="callout">💡 {D["example"]}</div>',unsafe_allow_html=True)

st.markdown('<div id="quiz" class="section-title">اختبار قصير</div>',unsafe_allow_html=True)
score=0
for j,(q,opts,ans) in enumerate(D['quiz']):
    v=st.radio(q,opts,key=f"q{D['no']}_{j}",index=None)
    if v is not None:
        if v==ans:
            st.success('إجابة صحيحة')
            score+=1
        else:
            st.error(f'الإجابة الصحيحة: {ans}')
st.caption(f"النتيجة الحالية: {score}/{len(D['quiz'])}")

st.markdown('<div id="review" class="section-title">أسئلة للمراجعة والتثبيت</div>',unsafe_allow_html=True)
qs=''.join([f'<li>{q}</li>' for q in D['review']])
st.markdown(f'<div class="review"><ol>{qs}</ol></div>',unsafe_allow_html=True)

st.markdown('<div id="refs" class="section-title">المراجع الأساسية</div>',unsafe_allow_html=True)
for r in D['references']:
    st.markdown(f'<div class="small">• {r}</div>',unsafe_allow_html=True)

idx=lecture_numbers.index(current_no)
prev_html = f'<a class="nav-btn" href="?lecture={lecture_numbers[idx-1]}" target="_self">→ المحاضرة السابقة</a>' if idx>0 else '<span></span>'
next_html = f'<a class="nav-btn" href="?lecture={lecture_numbers[idx+1]}" target="_self">المحاضرة التالية ←</a>' if idx < len(lecture_numbers)-1 else '<span></span>'
st.markdown(f'<div class="nav-buttons">{prev_html}{next_html}</div>', unsafe_allow_html=True)
