import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import math

st.set_page_config(
    page_title="المحاضرة الأولى | تطبيقات التعلم العميق",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================
# لوحة الألوان — Academic AI Light
# ==============================
BG = "#F4F8FE"
BG2 = "#EEF4FD"
CYAN = "#06B6D4"
BLUE = "#2563EB"
PURPLE = "#7C3AED"
PINK = "#DB2777"
YELLOW = "#D97706"
GREEN = "#059669"
WHITE = "#14213D"
MUTED = "#53667D"
CARD = "#FFFFFF"

# ==============================
# CSS عام + RTL + Academic AI Light
# ==============================
st.markdown(
    f"""
    <style>
    html {{ scroll-behavior: smooth; }}
    html, body, [data-testid="stAppViewContainer"] {{
        direction: rtl; text-align: right;
        font-family: "Segoe UI", Tahoma, Arial, sans-serif;
        color: {WHITE};
    }}
    [data-testid="stAppViewContainer"] {{
        background:
          radial-gradient(circle at 10% 7%, rgba(6,182,212,.08), transparent 23%),
          radial-gradient(circle at 88% 8%, rgba(124,58,237,.07), transparent 25%),
          linear-gradient(180deg, #FBFDFF 0%, {BG} 38%, #F7FAFE 100%);
    }}
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display:none !important; }}
    .block-container {{ max-width: 1500px; padding: 1.4rem 320px 4rem 2rem !important; }}
    p, li, div, label {{ line-height: 1.95; }}
    p, li {{ font-size: 18px; }}
    code, pre {{ direction:ltr !important; text-align:left !important; }}

    /* فهرس ثابت على اليمين */
    .right-toc {{
        position:fixed; right:18px; top:64px; width:270px; max-height:calc(100vh - 82px);
        overflow-y:auto; z-index:999; direction:rtl; text-align:right;
        background:rgba(255,255,255,.96); backdrop-filter: blur(12px);
        border:1px solid #D9E5F3; border-radius:22px; padding:18px 14px;
        box-shadow:0 18px 45px rgba(30,64,175,.10);
    }}
    .right-toc::-webkit-scrollbar {{ width:6px; }}
    .right-toc::-webkit-scrollbar-thumb {{ background:#C7D8EE; border-radius:99px; }}
    .toc-title {{ color:{BLUE}; font-size:21px; font-weight:950; margin:0 0 .25rem; }}
    .toc-subtitle {{ color:{MUTED}; font-size:14px; line-height:1.7; margin-bottom:.75rem; }}
    .toc-nav {{ display:flex; flex-direction:column; gap:.38rem; }}
    .toc-nav a {{
        display:block; text-decoration:none !important; color:#233A59 !important; background:#F7FAFE;
        border:1px solid #E0E9F4; border-right:4px solid transparent; border-radius:12px;
        padding:.58rem .68rem; font-weight:800; font-size:16px; line-height:1.5; transition:.18s ease;
    }}
    .toc-nav a:hover {{ background:#EAF4FF; border-color:#BBD9FA; border-right-color:{BLUE}; transform:translateX(-2px); color:{BLUE} !important; }}
    .toc-tip {{ margin-top:12px; padding:12px; border-radius:14px; background:linear-gradient(135deg,#EFF8FF,#F4F0FF); color:#415875; font-size:14px; border:1px solid #DDEAF7; }}

    /* Hero مريح للمدرج */
    .hero {{
        position:relative; overflow:hidden; padding:2.1rem 2rem; border-radius:28px;
        background:linear-gradient(115deg,#FFFFFF 0%,#F0F8FF 48%,#F6F0FF 100%);
        border:1px solid #D9E7F5; box-shadow:0 18px 55px rgba(37,99,235,.10); margin-bottom:1.35rem;
    }}
    .hero:after {{ content:""; position:absolute; left:-80px; top:-90px; width:250px; height:250px; border-radius:50%; background:radial-gradient(circle,rgba(6,182,212,.17),transparent 66%); }}
    .hero-inner {{ position:relative; z-index:2; }}
    .hero-kicker {{ display:inline-flex; gap:.45rem; align-items:center; padding:.42rem .9rem; border-radius:999px; background:#E9F7FB; border:1px solid #BFEAF2; color:#087D93; font-weight:900; font-size:16px; margin-bottom:.85rem; }}
    .hero-title {{ font-size:clamp(2.1rem,3.8vw,3.35rem); line-height:1.42; font-weight:950; margin:0; color:#143D8C; }}
    .hero-subtitle {{ color:#415C7E; font-size:18px; margin-top:.7rem; }}
    .hero-meta {{ display:flex; flex-wrap:wrap; gap:.6rem; margin-top:1rem; }}
    .pill {{ padding:.45rem .78rem; border-radius:999px; background:#FFFFFF; border:1px solid #D9E5F3; font-size:15px; color:#334D6E; font-weight:700; box-shadow:0 5px 15px rgba(15,23,42,.04); }}

    /* عناوين الأقسام */
    .section-heading {{ display:flex; align-items:center; gap:.8rem; margin:.35rem 0 1rem; padding-bottom:.75rem; border-bottom:2px solid #E6EEF7; }}
    .section-icon {{ width:52px; height:52px; display:grid; place-items:center; border-radius:16px; background:linear-gradient(135deg,#E6F7FB,#EEE9FF); border:1px solid #D4E5F2; font-size:1.45rem; box-shadow:0 8px 20px rgba(37,99,235,.06); }}
    .section-title {{ color:#174AA6; font-size:30px; font-weight:950; }}
    .section-note {{ color:{MUTED}; font-size:16px; }}

    /* بطاقات */
    .ai-card {{ height:100%; padding:1.25rem 1.2rem; border-radius:20px; background:#FFFFFF; border:1px solid #DFE9F4; box-shadow:0 12px 28px rgba(30,64,175,.07); transition:transform .22s ease, box-shadow .22s ease; }}
    .ai-card:hover {{ transform:translateY(-3px); box-shadow:0 17px 35px rgba(30,64,175,.12); }}
    .ai-card.cyan {{ border-top:4px solid {CYAN}; }} .ai-card.blue {{ border-top:4px solid {BLUE}; }} .ai-card.purple {{ border-top:4px solid {PURPLE}; }}
    .ai-card.pink {{ border-top:4px solid {PINK}; }} .ai-card.yellow {{ border-top:4px solid #F59E0B; }} .ai-card.green {{ border-top:4px solid {GREEN}; }}
    .card-label {{ font-size:14px; font-weight:850; color:#718198; margin-bottom:.2rem; }}
    .card-title {{ font-size:21px; font-weight:950; color:#087D93; margin-bottom:.45rem; }}
    .card-title.blue {{ color:{BLUE}; }} .card-title.purple {{ color:{PURPLE}; }} .card-title.pink {{ color:{PINK}; }} .card-title.yellow {{ color:#B76700; }} .card-title.green {{ color:{GREEN}; }}
    .card-text {{ color:#40546D; font-size:17px; }}

    /* Callouts */
    .callout {{ padding:1.05rem 1.15rem; border-radius:17px; margin:.85rem 0 1rem; background:#F1FAFC; border-right:5px solid {CYAN}; border-top:1px solid #DCEEF2; border-bottom:1px solid #DCEEF2; }}
    .callout.question {{ border-right-color:#F59E0B; background:#FFF9E9; border-color:#F7E7B4; }}
    .callout.warning {{ border-right-color:{PINK}; background:#FFF2F7; border-color:#F4DCE8; }}
    .callout.success {{ border-right-color:{GREEN}; background:#EEFBF6; border-color:#D3F0E4; }}
    .callout-title {{ color:#9A5D00; font-weight:950; font-size:18px; margin-bottom:.22rem; }}
    .callout-text {{ color:#263E5A; font-size:18px; }}

    /* جداول للعرض في المدرج */
    .fancy-table-wrap {{ overflow-x:auto; border-radius:18px; margin:1rem 0 1.25rem; border:1px solid #D8E5F2; box-shadow:0 12px 28px rgba(30,64,175,.07); background:#FFFFFF; }}
    table.fancy-table {{ width:100%; border-collapse:separate; border-spacing:0; min-width:720px; direction:rtl; }}
    .fancy-table thead th {{ padding:1rem .95rem; color:white; font-weight:950; font-size:18px; text-align:right; background:linear-gradient(100deg,#1D4ED8,#2563EB 45%,#6D4DDC); border-bottom:1px solid rgba(255,255,255,.22); }}
    .fancy-table tbody td {{ padding:.95rem .95rem; color:#2E435E; font-size:17px; border-bottom:1px solid #E7EEF6; background:#FFFFFF; }}
    .fancy-table tbody tr:nth-child(even) td {{ background:#F7FAFE; }}
    .fancy-table tbody tr:hover td {{ background:#ECF6FF; color:#183A66; }}
    .fancy-table tbody tr:last-child td {{ border-bottom:none; }}
    .table-badge {{ display:inline-block; padding:.28rem .62rem; border-radius:999px; background:#E7F7FB; color:#087D93; border:1px solid #BFE6EE; font-weight:900; font-size:15px; }}

    /* Flow حديث */
    .flow {{ display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:.64rem; margin:1rem 0; }}
    .flow-node {{ padding:.75rem 1.05rem; border-radius:14px; font-weight:900; font-size:17px; color:#1E3A5F; background:linear-gradient(135deg,#F3FAFF,#F6F2FF); border:1px solid #D5E4F3; box-shadow:0 8px 20px rgba(30,64,175,.06); }}
    .flow-arrow {{ color:{PURPLE}; font-size:1.45rem; font-weight:950; }}

    .mini-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:.72rem; margin:.9rem 0; }}
    .mini-chip {{ padding:1rem .85rem; border-radius:15px; text-align:center; background:#FFFFFF; border:1px solid #DCE6F1; color:#28445F; font-weight:850; font-size:16px; box-shadow:0 7px 18px rgba(30,64,175,.05); }}
    .mini-chip:hover {{ transform:translateY(-2px); border-color:#C9BDF5; background:#FAF8FF; }}

    .formula-box {{ text-align:center; direction:ltr; font-size:22px; font-weight:950; padding:1rem; border-radius:17px; background:linear-gradient(90deg,#EAF8FC,#EEF4FF,#F4EEFF); border:1px solid #D3E3F3; color:#5B35B5; margin:.95rem 0; }}
    .scroll-anchor {{ scroll-margin-top:1.2rem; height:1px; width:1px; }}
    .section-separator {{ height:1px; margin:2.3rem 0 1.7rem; background:linear-gradient(90deg,transparent,#D5E4F2,#DCCEF5,transparent); }}

    div.stButton > button {{ width:100%; border-radius:14px; border:1px solid #BFD3EE; background:linear-gradient(90deg,#EAF6FF,#F3EEFF); color:#194688; font-weight:950; font-size:17px; padding:.7rem 1rem; }}
    div.stButton > button:hover {{ border-color:#8DB8E9; box-shadow:0 8px 22px rgba(37,99,235,.10); }}
    [data-testid="stExpander"] {{ background:#FFFFFF; border:1px solid #DDE7F1; border-radius:14px; box-shadow:0 7px 18px rgba(30,64,175,.04); }}
    [data-testid="stMetric"] {{ background:#FFFFFF; border:1px solid #DDE7F1; border-radius:16px; padding:.9rem; }}
    h1,h2,h3,h4 {{ color:#174AA6; }}
    .footer {{ margin-top:2rem; padding:1.1rem; text-align:center; color:{MUTED}; border-top:1px solid #DDE7F1; font-size:15px; }}

    @media(max-width:1050px) {{
      .right-toc {{ display:none; }}
      .block-container {{ padding:1rem 1rem 4rem !important; max-width:100%; }}
    }}
    @media(max-width:760px) {{
      .hero {{ padding:1.45rem 1rem; border-radius:22px; }} .hero-title {{ font-size:2rem; }}
      .section-title {{ font-size:25px; }} p,li {{ font-size:17px; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================
# دوال مساعدة
# ==============================
def section_header(icon: str, title: str, note: str = ""):
    st.markdown(
        f"""
        <div class="section-heading">
          <div class="section-icon">{icon}</div>
          <div>
            <div class="section-title">{title}</div>
            <div class="section-note">{note}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card(title: str, text: str, color: str = "cyan", label: str = ""):
    title_class = "card-title" if color == "cyan" else f"card-title {color}"
    return f"""
    <div class="ai-card {color}">
      {f'<div class="card-label">{label}</div>' if label else ''}
      <div class="{title_class}">{title}</div>
      <div class="card-text">{text}</div>
    </div>
    """


def fancy_table(headers, rows, badge_col=None):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = []
    for row in rows:
        cells = []
        for idx, cell in enumerate(row):
            if badge_col is not None and idx == badge_col:
                cells.append(f'<td><span class="table-badge">{cell}</span></td>')
            else:
                cells.append(f"<td>{cell}</td>")
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    html = f"""
    <div class="fancy-table-wrap">
      <table class="fancy-table">
        <thead><tr>{head}</tr></thead>
        <tbody>{''.join(body_rows)}</tbody>
      </table>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def animated_ai_ml_dl():
    components.html(
        f"""
        <html dir="rtl"><head><meta charset="utf-8"><style>
        body{{margin:0;background:transparent;font-family:Tahoma,Arial,sans-serif;color:#14213D;overflow:hidden}}
        .wrap{{height:455px;display:flex;align-items:center;justify-content:center;position:relative;background:linear-gradient(135deg,#FFFFFF,#F6FAFF);border:1px solid #DDE8F3;border-radius:22px;}}
        .halo{{position:absolute;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(6,182,212,.10),transparent 66%);filter:blur(8px);animation:glow 3.6s ease-in-out infinite}}
        @keyframes glow{{0%,100%{{transform:scale(.98);opacity:.65}}50%{{transform:scale(1.06);opacity:1}}}}
        .ring{{position:absolute;border-radius:50%;display:flex;align-items:flex-start;justify-content:center;box-shadow:0 0 28px rgba(30,64,175,.08) inset,0 10px 30px rgba(30,64,175,.05);transition:.25s ease;}}
        .ring:hover{{transform:scale(1.03)}}
        .ai{{width:380px;height:380px;border:2px solid rgba(6,182,212,.65);background:radial-gradient(circle at 30% 25%,rgba(6,182,212,.18),rgba(6,182,212,.06) 45%,rgba(255,255,255,.65) 76%);animation:float1 5s ease-in-out infinite}}
        .ml{{width:270px;height:270px;border:2px solid rgba(124,58,237,.62);background:radial-gradient(circle at 35% 28%,rgba(124,58,237,.16),rgba(124,58,237,.05) 46%,rgba(255,255,255,.72) 76%);top:100px;animation:float2 5s ease-in-out infinite}}
        .dl{{width:160px;height:160px;border:2px solid rgba(219,39,119,.60);background:radial-gradient(circle at 32% 25%,rgba(219,39,119,.16),rgba(219,39,119,.05) 48%,rgba(255,255,255,.75) 76%);top:155px;animation:float3 4.5s ease-in-out infinite}}
        @keyframes float1{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
        @keyframes float2{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(5px)}}}}
        @keyframes float3{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
        .label{{margin-top:26px;text-align:center;font-weight:900;text-shadow:0 0 16px rgba(255,255,255,.12)}}
        .ai .label{{color:#087D93;font-size:25px}} .ml .label{{color:#6336C6;font-size:23px}} .dl .label{{color:#B51E67;font-size:21px;margin-top:48px}}
        .small{{display:block;color:#5B6E84;font-size:14px;font-weight:700;margin-top:4px}}
        .hint{{position:absolute;bottom:10px;color:#53667D;font-size:14px;background:#F7FAFE;border:1px solid #DDE7F1;padding:8px 12px;border-radius:12px}}
        </style></head><body>
        <div class="wrap">
          <div class="halo"></div>
          <div class="ring ai"><div class="label">Artificial Intelligence<span class="small">المجال الأشمل</span></div></div>
          <div class="ring ml"><div class="label">Machine Learning<span class="small">يتعلم من البيانات</span></div></div>
          <div class="ring dl"><div class="label">Deep Learning<span class="small">شبكات عصبية متعددة الطبقات</span></div></div>
          <div class="hint">مرّر المؤشر فوق الدوائر ولاحظ أن DL داخل ML وML داخل AI</div>
        </div>
        </body></html>
        """,
        height=480,
        scrolling=False,
    )


def neural_network_3d():
    # بنية بسيطة: 4 طبقات، لإظهار معنى العمق بصريًا
    layer_sizes = [5, 7, 6, 2]
    x_positions = [0, 1.4, 2.8, 4.2]
    layer_names = ["Input", "Hidden 1", "Hidden 2", "Output"]
    layer_colors = [CYAN, BLUE, PURPLE, PINK]

    node_xyz = []
    layer_nodes = []
    for li, (size, x) in enumerate(zip(layer_sizes, x_positions)):
        nodes = []
        for i in range(size):
            angle = 2 * math.pi * i / size
            y = 1.25 * math.cos(angle)
            z = 1.25 * math.sin(angle)
            nodes.append((x, y, z))
            node_xyz.append((x, y, z, li, i))
        layer_nodes.append(nodes)

    fig = go.Figure()
    # edges
    for li in range(len(layer_nodes)-1):
        for a in layer_nodes[li]:
            for b in layer_nodes[li+1]:
                fig.add_trace(go.Scatter3d(
                    x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]],
                    mode="lines", line=dict(color="rgba(84,108,150,.22)", width=2),
                    hoverinfo="skip", showlegend=False
                ))
    # nodes by layer
    for li, nodes in enumerate(layer_nodes):
        fig.add_trace(go.Scatter3d(
            x=[n[0] for n in nodes], y=[n[1] for n in nodes], z=[n[2] for n in nodes],
            mode="markers+text",
            text=[layer_names[li] if i == 0 else "" for i in range(len(nodes))],
            textposition="top center",
            marker=dict(size=9, color=layer_colors[li], opacity=.96, line=dict(color="#FFFFFF", width=.7)),
            hovertemplate=f"{layer_names[li]}<extra></extra>",
            name=layer_names[li]
        ))
    fig.update_layout(
        height=430,
        margin=dict(l=0,r=0,t=25,b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=WHITE, family="Tahoma"),
        showlegend=False,
        scene=dict(
            bgcolor="rgba(0,0,0,0)",
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            camera=dict(eye=dict(x=1.6,y=1.45,z=.9)),
        ),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False, "scrollZoom": True})


# ==============================
# HERO
# ==============================
st.markdown('<div id="top"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="hero"><div class="hero-inner">
      <div class="hero-kicker">🧠 المقياس: تطبيقات التعلم العميق</div>
      <div class="hero-title">المحاضرة الأولى: مقدمة في التعلم العميق وتطبيقاته في إدارة الموارد البشرية</div>
      <div class="hero-subtitle">Introduction to Deep Learning and Its Applications in Human Resource Management</div>
      <div class="hero-meta">
        <span class="pill">🎓 طلبة إدارة الموارد البشرية</span>
        <span class="pill">⏱️ الأسبوع 01</span>
        <span class="pill">✨ تصميم تفاعلي + أمثلة HR</span>
      </div>
    </div></div>
    """,
    unsafe_allow_html=True,
)

# ==============================
# الفهرس الثابت على اليمين
# ==============================
st.markdown(
    """
    <aside class="right-toc">
      <div class="toc-title">🧭 فهرس المحاضرة</div>
      <div class="toc-subtitle">اقرأ من الأعلى إلى الأسفل، أو انتقل مباشرة إلى أي جزء.</div>
      <div class="toc-nav">
        <a href="#goals">🎯 أهداف المحاضرة</a>
        <a href="#concepts">🧠 AI وML وDL</a>
        <a href="#deep-visual">🧬 ماذا تعني Deep؟</a>
        <a href="#comparison">⚖️ مقارنة ML وDL</a>
        <a href="#growth">⚡ لماذا انتشر DL؟</a>
        <a href="#hr-apps">👥 تطبيقات HR</a>
        <a href="#attrition">📊 مثال Attrition</a>
        <a href="#ethics">🛡️ القيود والأخلاقيات</a>
        <a href="#activity">🧩 نشاط</a>
        <a href="#quiz">🏆 اختبار قصير</a>
        <a href="#references">📚 المراجع</a>
      </div>
      <div class="toc-tip">💡 استخدم الفهرس أثناء العرض، والقراءة تظل متتابعة في الصفحة نفسها.</div>
    </aside>
    """,
    unsafe_allow_html=True,
)

# ==============================
# 1) الأهداف
# ==============================
st.markdown('<div id="goals" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("🎯", "أهداف المحاضرة", "نبدأ بجذب الانتباه ثم نبني المفاهيم تدريجيًا")
st.markdown("""
<div class="callout question"><div class="callout-title">سؤال افتتاحي</div>
<div class="callout-text">هل يمكن لنظام ذكي أن يتعلم من بيانات الموظفين ويتوقع من قد يغادر المؤسسة؟ وما البيانات التي يمكن أن تساعده؟</div></div>
""", unsafe_allow_html=True)

cols = st.columns(2)
goals = [
    ("01","تعريف AI وML وDL","تمييز المفاهيم الثلاثة دون خلط بينها."),
    ("02","فهم العلاقة بينها","DL جزء من ML، وML جزء من AI."),
    ("03","مقارنة ML وDL","البيانات، استخراج الخصائص، الحوسبة، التفسير."),
    ("04","ربط التقنية بـHR","التوظيف، الأداء، الدوران الوظيفي، التخطيط."),
    ("05","الوعي بالقيود","التحيز، العدالة، صغر البيانات وقابلية التفسير."),
    ("06","تحويل مشكلة HR إلى مشكلة بيانات","Classification وRegression وForecasting وText Analysis."),
]
for i,(n,t,x) in enumerate(goals):
    with cols[i%2]:
        st.markdown(card(t,x,"cyan" if i%2==0 else "purple",f"الهدف {n}"),unsafe_allow_html=True)

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 2) AI ML DL
# ==============================
st.markdown('<div id="concepts" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("🧠", "من الذكاء الاصطناعي إلى التعلم العميق", "الشكل أولًا، ثم التعريف")

animated_ai_ml_dl()

c1,c2,c3 = st.columns(3)
with c1:
    st.markdown(card("Artificial Intelligence", "الإطار الأوسع لأتمتة مهام تتطلب عادة قدرات بشرية مثل الفهم واتخاذ القرار والتعرف على الأنماط.", "cyan", "AI | الذكاء الاصطناعي"), unsafe_allow_html=True)
with c2:
    st.markdown(card("Machine Learning", "فرع من AI يتعلم العلاقات من البيانات بدل الاعتماد فقط على قواعد يكتبها المبرمج.", "purple", "ML | التعلم الآلي"), unsafe_allow_html=True)
with c3:
    st.markdown(card("Deep Learning", "فرع من ML يعتمد على شبكات عصبية متعددة الطبقات لتعلم تمثيلات معقدة للبيانات.", "pink", "DL | التعلم العميق"), unsafe_allow_html=True)

st.markdown('<div class="formula-box">Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence</div>', unsafe_allow_html=True)

st.markdown("""
<div class="flow">
  <div class="flow-node">بيانات Data</div><div class="flow-arrow">←</div>
  <div class="flow-node">خوارزمية تعلم</div><div class="flow-arrow">←</div>
  <div class="flow-node">نموذج Model</div><div class="flow-arrow">←</div>
  <div class="flow-node">تنبؤ Prediction</div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 المصدر الأكاديمي لهذا القسم"):
    st.write("François Chollet, *Deep Learning with Python*, Chapter 1.")
    st.write("ميلاد وزان، *التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون*، الفصل الأول.")

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 3) ما معنى Deep؟ + 3D
# ==============================
st.markdown('<div id="deep-visual" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("🧬", "كيف نفهم كلمة Deep؟", "هنا يصبح استخدام 3D مفيدًا لأنه يوضح تتابع الطبقات بصريًا")

left,right = st.columns([.92,1.08])
with left:
    st.markdown(card("ليست «تفكيرًا عميقًا»", "كلمة Deep تشير أساسًا إلى تعدد مستويات/طبقات التمثيل داخل الشبكة العصبية، وليس إلى فهم بشري عميق.", "yellow", "الفكرة الصحيحة"), unsafe_allow_html=True)
    st.markdown("""
    <div class="callout"><div class="callout-title">اقرأ الرسم من اليسار إلى اليمين</div>
    <div class="callout-text">Input Layer ← Hidden Layers ← Output Layer. حرّك الشكل ثلاثي الأبعاد بالماوس ولاحظ كيف تمر المعلومات عبر طبقات متعددة.</div></div>
    """, unsafe_allow_html=True)
    fancy_table(
        ["الطبقة","وظيفتها المبسطة"],
        [
            ("Input Layer","تستقبل بيانات الموظف."),
            ("Hidden Layer 1","تتعلم أنماطًا أولية."),
            ("Hidden Layer 2","تتعلم علاقات أكثر تركيبًا."),
            ("Output Layer","تعطي النتيجة النهائية مثل Stay / Leave."),
        ],
        badge_col=0,
    )
with right:
    neural_network_3d()

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 4) المقارنة
# ==============================
st.markdown('<div id="comparison" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("⚖️", "Machine Learning أم Deep Learning؟", "الجدول مصمم للقراءة السريعة والمقارنة البصرية")

fancy_table(
    ["الجانب","Machine Learning","Deep Learning"],
    [
        ("استخراج الخصائص","يحتاج غالبًا إلى تدخل أكبر من الباحث","يتعلم كثيرًا منها تلقائيًا"),
        ("حجم البيانات","يمكن أن يعمل جيدًا ببيانات محدودة نسبيًا","يستفيد غالبًا من بيانات أكبر"),
        ("القدرة الحاسوبية","أقل غالبًا","أعلى غالبًا"),
        ("بنية النموذج","أبسط نسبيًا","شبكات عصبية متعددة الطبقات"),
        ("التفسير","أسهل في كثير من النماذج","قد يكون أصعب"),
        ("بيانات HR الصغيرة","غالبًا مناسب","ليس دائمًا الخيار الأفضل"),
    ]
)

st.markdown("""
<div class="callout warning"><div class="callout-title">قاعدة المقياس</div>
<div class="callout-text">نختار النموذج وفق المشكلة والبيانات، لا وفق درجة تعقيده أو شهرته.</div></div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 5) لماذا انتشر DL
# ==============================
st.markdown('<div id="growth" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("⚡", "لماذا انتشر التعلم العميق؟", "ثلاثة محركات رئيسة وراء صعوده")

c1,c2,c3 = st.columns(3)
with c1: st.markdown(card("Big Data","تزايد حجم البيانات وتنوعها: نصوص، صور، سجلات رقمية، معاملات وغيرها.","cyan","01 | البيانات"),unsafe_allow_html=True)
with c2: st.markdown(card("Computing Power","تطور القدرة الحاسوبية، خصوصًا GPU، جعل تدريب الشبكات الكبيرة أسرع.","blue","02 | الحوسبة"),unsafe_allow_html=True)
with c3: st.markdown(card("Better Algorithms","تحسن خوارزميات التدريب والتحسين ودوال التنشيط وبنى الشبكات.","pink","03 | الخوارزميات"),unsafe_allow_html=True)

st.markdown("### ✨ أين نرى Deep Learning؟")
st.markdown(f"""
<div class="mini-grid">
  <div class="mini-chip">👁️ Computer Vision</div>
  <div class="mini-chip">📝 Natural Language Processing</div>
  <div class="mini-chip">🎙️ Speech Recognition</div>
  <div class="mini-chip">📈 Time Series</div>
  <div class="mini-chip">🏷️ Classification</div>
  <div class="mini-chip">🔮 Prediction</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 6) تطبيقات HR
# ==============================
st.markdown('<div id="hr-apps" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("👥", "تطبيقات AI / ML / DL في إدارة الموارد البشرية", "نحوّل التقنية إلى مواقف قريبة من تخصص الطالب")

apps = [
    ("🧲 Recruitment","تحليل بيانات المتقدمين ودعم الفرز الأولي.","cyan"),
    ("🎯 Selection","دعم تصنيف المرشحين وفق خصائص محددة.","purple"),
    ("🚪 Attrition","التنبؤ باحتمال مغادرة الموظف.","pink"),
    ("📊 Performance","تحليل وتوقع مؤشرات الأداء.","yellow"),
    ("🎓 Training","تحديد احتياجات التدريب واقتراح مسارات تعلم.","green"),
    ("🤝 Engagement","تحليل الرضا والاندماج الوظيفي.","cyan"),
    ("🗓️ Workforce Planning","التنبؤ بالاحتياجات المستقبلية من العمالة.","blue"),
    ("💬 Employee Feedback","تحليل النصوص ومشاعر الموظفين.","purple"),
    ("🧩 Retention","تحليل العوامل المرتبطة بالاحتفاظ بالموظفين.","green"),
]
for start in range(0,len(apps),3):
    cols = st.columns(3)
    for j,item in enumerate(apps[start:start+3]):
        with cols[j]:
            st.markdown(card(item[0],item[1],item[2]),unsafe_allow_html=True)

with st.expander("📚 People Analytics: كيف ننظر للمجال؟"):
    st.write("People Analytics يشمل تخطيط القوى العاملة، الاستقطاب، التوظيف، Onboarding، الأداء، Employee Churn والاحتفاظ بالموظفين.")
    st.write("المصدر: Isson, Harriott & Fitz-enz, *People Analytics in the Era of Big Data*.")

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 7) Attrition
# ==============================
st.markdown('<div id="attrition" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("📊", "مثالنا المستمر: Employee Attrition Prediction", "نستخدم المثال نفسه عبر عدة محاضرات حتى يصل الطالب إلى نموذج Keras")

st.markdown("""
<div class="callout"><div class="callout-title">المشكلة</div>
<div class="callout-text">نريد استخدام بيانات الموظفين السابقة لتحديد ما إذا كان الموظف سيبقى في المؤسسة أم سيغادرها.</div></div>
""", unsafe_allow_html=True)

fancy_table(
    ["المتغير","المعنى","مثال"],
    [
        ("Age","العمر","32"),
        ("MonthlyIncome","الدخل الشهري","55,000"),
        ("YearsAtCompany","سنوات العمل بالمؤسسة","3"),
        ("JobSatisfaction","الرضا الوظيفي","2/4"),
        ("Overtime","العمل الإضافي","Yes"),
        ("Attrition","هل غادر الموظف؟","Yes / No"),
    ],
    badge_col=0,
)

st.markdown("""
<div class="flow">
  <div class="flow-node">بيانات الموظفين</div><div class="flow-arrow">←</div>
  <div class="flow-node">تعلم الأنماط</div><div class="flow-arrow">←</div>
  <div class="flow-node">احتمال المغادرة</div><div class="flow-arrow">←</div>
  <div class="flow-node">دعم القرار</div>
</div>
""", unsafe_allow_html=True)

c1,c2 = st.columns(2)
with c1: st.markdown(card("لماذا Classification؟","لأن المخرج النهائي فئة: Stay أو Leave.","purple","نوع المشكلة"),unsafe_allow_html=True)
with c2: st.markdown(card("لماذا لا نبرمج قاعدة ثابتة؟","لأن العلاقات بين الرضا والراتب والأقدمية والعمل الإضافي قد تكون متداخلة ومعقدة.","yellow","الفكرة التعليمية"),unsafe_allow_html=True)

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 8) القيود والأخلاقيات
# ==============================
st.markdown('<div id="ethics" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("🛡️", "القيود والأخلاقيات في تطبيق AI على الموظفين", "الدقة وحدها ليست كافية عندما يتعلق القرار بأشخاص")

c1,c2,c3 = st.columns(3)
with c1: st.markdown(card("Small Data","قواعد بيانات HR قد تكون صغيرة مقارنة بمجالات أخرى.","cyan","البيانات"),unsafe_allow_html=True)
with c2: st.markdown(card("Bias & Fairness","قد يعيد النموذج إنتاج تحيزات موجودة أصلًا في البيانات.","pink","العدالة"),unsafe_allow_html=True)
with c3: st.markdown(card("Explainability","قرارات التوظيف والترقية والتقييم يجب أن تكون قابلة للتفسير والتبرير.","yellow","التفسير"),unsafe_allow_html=True)

st.markdown("""
<div class="callout success"><div class="callout-title">المبدأ الذي سنعتمده</div>
<div class="callout-text">الهدف هو دعم القرار البشري (Decision Support)، وليس استبدال مسؤول الموارد البشرية.</div></div>
""", unsafe_allow_html=True)

with st.expander("📚 ما الذي تقوله الأدبيات؟"):
    st.write("Tambe, Cappelli & Yakubovich يبرزون تحديات منها تعقيد الظواهر البشرية، صغر مجموعات البيانات، العدالة والقيود القانونية، وردود فعل الموظفين تجاه القرارات الخوارزمية.")
    st.write("Marler & Boudreau يناقشان HR Analytics كمدخل لاتخاذ قرار قائم على البيانات، مع الإشارة إلى محدودية الأدلة الأكاديمية مقارنة بالاهتمام التطبيقي.")

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 9) النشاط
# ==============================
st.markdown('<div id="activity" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("🧩", "نشاط تفاعلي: حوّل مشكلة HR إلى مشكلة بيانات", "التفاعل هنا جزء من التصميم، لا مجرد زخرفة")

items = [
    ("هل سيغادر الموظف المؤسسة خلال السنة القادمة؟","Classification","النتيجة فئة: Stay / Leave."),
    ("كم سيكون تقييم الأداء المتوقع؟","Regression / Prediction","المطلوب قيمة عددية متوقعة."),
    ("هل تعليق الموظف إيجابي أم سلبي؟","Text Classification / Sentiment Analysis","المدخل نص والهدف تصنيف المشاعر."),
    ("كم موظفًا ستحتاج المؤسسة السنة القادمة؟","Forecasting","المطلوب توقع قيمة مستقبلية عبر الزمن."),
    ("ما الموظفون الأكثر تشابهًا في خصائصهم؟","Clustering","نبحث عن مجموعات متشابهة دون فئات مسبقة."),
]
for i,(q,a,why) in enumerate(items,1):
    with st.expander(f"{i}. {q}"):
        st.success(f"الإجابة: {a}")
        st.caption(why)

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 10) Quiz
# ==============================
st.markdown('<div id="quiz" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("🏆", "اختبر فهمك", "اختبار قصير قبل الانتقال إلى المحاضرة الثانية")

q1 = st.radio("1) أي مفهوم هو الأشمل؟", ["Deep Learning","Machine Learning","Artificial Intelligence"], index=None)
q2 = st.radio("2) ما المقصود بكلمة Deep في Deep Learning؟", ["التفكير الإنساني العميق","تعدد طبقات المعالجة في الشبكة","حجم ملف البيانات"], index=None)
q3 = st.radio("3) التنبؤ بـ Leave / Stay يمثل:", ["Classification","Clustering","Image Generation"], index=None)
q4 = st.radio("4) هل Deep Learning هو الأفضل دائمًا لبيانات HR؟", ["نعم","لا"], index=None)
q5 = st.radio("5) إذا كانت بيانات التدريب متحيزة، فقد:", ["يختفي التحيز تلقائيًا","يعيد النموذج إنتاج التحيز","تزيد سرعة الحاسوب فقط"], index=None)

if st.button("✨ صحّح إجاباتي"):
    answers = [q1,q2,q3,q4,q5]
    correct = ["Artificial Intelligence","تعدد طبقات المعالجة في الشبكة","Classification","لا","يعيد النموذج إنتاج التحيز"]
    if any(a is None for a in answers):
        st.warning("أجب عن جميع الأسئلة أولًا ثم اضغط على التصحيح.")
    else:
        score = sum(a==b for a,b in zip(answers,correct))
        st.metric("النتيجة", f"{score}/5")
        if score == 5:
            st.balloons(); st.success("ممتاز جدًا! يمكنك الانتقال بثقة إلى المحاضرة الثانية 🚀")
        elif score >= 4:
            st.success("ممتاز. المفاهيم الأساسية واضحة جدًا.")
        elif score >= 3:
            st.info("جيد. راجع المقارنة بين ML وDL والقيود في HR.")
        else:
            st.warning("راجع أقسام AI وML وDL قبل الانتقال إلى المحاضرة الثانية.")

st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

# ==============================
# 11) المراجع
# ==============================
st.markdown('<div id="references" class="scroll-anchor"></div>', unsafe_allow_html=True)
section_header("📚", "المراجع المعتمدة", "المحتوى مبني على المراجع المتاحة للمقياس")
refs = [
    "François Chollet, Deep Learning with Python.",
    "Aurélien Géron, Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.",
    "ميلاد وزان، التعلم العميق: من الأساسيات حتى بناء شبكة عصبية عميقة بلغة البايثون، ترجمة د. علاء طعيمة.",
    "ميلاد وزان، التعلم العميق: المبادئ والمفاهيم والأساليب، ترجمة د. علاء طعيمة.",
    "Marler & Boudreau (2017), An Evidence-Based Review of HR Analytics.",
    "Tambe, Cappelli & Yakubovich, Artificial Intelligence in Human Resources Management: Challenges and a Path Forward.",
    "Isson, Harriott & Fitz-enz, People Analytics in the Era of Big Data.",
]
for i,ref in enumerate(refs,1):
    st.markdown(f"**{i}.** {ref}")

st.markdown("""
<div class="footer">
  مقياس تطبيقات التعلم العميق — المحاضرة الأولى<br>
  <span style="color:#29E7F2;font-weight:900">تعلّم الفكرة ➜ شاهدها بصريًا ➜ جرّب ➜ ناقش ➜ طبّق</span>
</div>
""", unsafe_allow_html=True)
