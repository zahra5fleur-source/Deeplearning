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
# لوحة الألوان
# ==============================
BG = "#050816"
BG2 = "#0A1030"
CYAN = "#29E7F2"
BLUE = "#5B8CFF"
PURPLE = "#9B6BFF"
PINK = "#FF72C7"
YELLOW = "#FFD166"
GREEN = "#58E6A9"
WHITE = "#F8FAFF"
MUTED = "#C8D0EE"
CARD = "rgba(255,255,255,.055)"

# ==============================
# CSS عام + RTL + تصميم عصري
# ==============================
st.markdown(
    f"""
    <style>
    html {{ scroll-behavior: smooth; }}
    html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {{
        direction: rtl;
        text-align: right;
        font-family: Tahoma, "Segoe UI", Arial, sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{
        flex-direction: row-reverse !important;
        background:
          radial-gradient(circle at 8% 10%, rgba(41,231,242,.14), transparent 26%),
          radial-gradient(circle at 92% 6%, rgba(155,107,255,.20), transparent 29%),
          radial-gradient(circle at 76% 88%, rgba(255,114,199,.12), transparent 26%),
          linear-gradient(155deg, {BG} 0%, {BG2} 54%, #07091C 100%);
        color: {WHITE};
    }}
    .block-container {{ max-width: 1280px; padding-top: 1rem; padding-bottom: 4rem; }}
    p, li, div, label {{ line-height: 1.95; }}
    code, pre {{ direction:ltr !important; text-align:left !important; }}

    /* Sidebar على اليمين */
    [data-testid="stSidebar"] {{
        direction: rtl !important;
        text-align: right !important;
        background: linear-gradient(180deg, #090D28 0%, #12183B 100%);
        border-right: 1px solid rgba(41,231,242,.20) !important;
        border-left: none !important;
    }}
    [data-testid="stSidebar"] * {{ color:{WHITE}; }}

    /* Hero */
    .hero {{
        position: relative; overflow:hidden;
        padding: 2.3rem 2rem 2.1rem;
        border-radius: 30px;
        background: linear-gradient(130deg, rgba(41,231,242,.11), rgba(91,140,255,.08) 34%, rgba(155,107,255,.13) 65%, rgba(255,114,199,.10));
        border: 1px solid rgba(41,231,242,.25);
        box-shadow: 0 22px 75px rgba(0,0,0,.38), inset 0 1px 0 rgba(255,255,255,.08);
        margin-bottom: 1.3rem;
    }}
    .hero:before {{
        content:""; position:absolute; inset:-40%;
        background: conic-gradient(from 80deg, transparent, rgba(41,231,242,.05), transparent 28%, rgba(155,107,255,.07), transparent 60%, rgba(255,114,199,.05), transparent);
        animation: heroSpin 18s linear infinite;
    }}
    @keyframes heroSpin {{ to {{ transform: rotate(360deg); }} }}
    .hero-inner {{ position:relative; z-index:2; }}
    .hero-kicker {{
        display:inline-flex; gap:.4rem; align-items:center;
        padding:.38rem .86rem; border-radius:999px;
        background:rgba(41,231,242,.09); border:1px solid rgba(41,231,242,.36);
        color:{CYAN}; font-weight:900; font-size:.92rem; margin-bottom:.85rem;
    }}
    .hero-title {{
        font-size:clamp(2rem,4vw,3.25rem); line-height:1.42; font-weight:950; margin:0;
        background:linear-gradient(90deg,{CYAN},#B7C7FF 35%,#C9AAFF 62%,{PINK});
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }}
    .hero-subtitle {{ color:{MUTED}; font-size:1.05rem; margin-top:.7rem; }}
    .hero-meta {{ display:flex; flex-wrap:wrap; gap:.55rem; margin-top:1rem; }}
    .pill {{ padding:.38rem .72rem; border-radius:999px; background:rgba(255,255,255,.055); border:1px solid rgba(255,255,255,.10); font-size:.9rem; }}

    /* عناوين الأقسام */
    .section-heading {{
        display:flex; align-items:center; gap:.7rem; margin:.2rem 0 1rem;
        padding-bottom:.65rem; border-bottom:1px solid rgba(255,255,255,.085);
    }}
    .section-icon {{
        width:48px; height:48px; display:grid; place-items:center; border-radius:15px;
        background:linear-gradient(135deg, rgba(41,231,242,.17), rgba(155,107,255,.18));
        border:1px solid rgba(41,231,242,.24); font-size:1.35rem;
        box-shadow:0 8px 24px rgba(41,231,242,.06);
    }}
    .section-title {{ color:{PINK}; font-size:1.72rem; font-weight:950; }}
    .section-note {{ color:{MUTED}; font-size:.93rem; }}

    /* بطاقات */
    .ai-card {{
        height:100%; padding:1.2rem 1.15rem; border-radius:20px;
        background:linear-gradient(180deg, rgba(255,255,255,.065), rgba(255,255,255,.035));
        border:1px solid rgba(255,255,255,.095);
        box-shadow:inset 0 1px 0 rgba(255,255,255,.05), 0 14px 32px rgba(0,0,0,.18);
        transition:transform .22s ease, border-color .22s ease, box-shadow .22s ease;
    }}
    .ai-card:hover {{ transform:translateY(-4px); border-color:rgba(41,231,242,.30); box-shadow:0 18px 42px rgba(0,0,0,.26); }}
    .ai-card.cyan {{ border-top:3px solid {CYAN}; }}
    .ai-card.blue {{ border-top:3px solid {BLUE}; }}
    .ai-card.purple {{ border-top:3px solid {PURPLE}; }}
    .ai-card.pink {{ border-top:3px solid {PINK}; }}
    .ai-card.yellow {{ border-top:3px solid {YELLOW}; }}
    .ai-card.green {{ border-top:3px solid {GREEN}; }}
    .card-label {{ font-size:.82rem; font-weight:850; color:{MUTED}; margin-bottom:.18rem; }}
    .card-title {{ font-size:1.2rem; font-weight:950; color:{CYAN}; margin-bottom:.42rem; }}
    .card-title.blue {{ color:#9BB7FF; }} .card-title.purple {{ color:#C0A9FF; }}
    .card-title.pink {{ color:#FF9DD5; }} .card-title.yellow {{ color:{YELLOW}; }}
    .card-title.green {{ color:{GREEN}; }}
    .card-text {{ color:{MUTED}; font-size:.97rem; }}

    /* Callouts */
    .callout {{ padding:1rem 1.1rem; border-radius:17px; margin:.8rem 0 1rem; background:rgba(255,255,255,.043); border-right:5px solid {CYAN}; }}
    .callout.question {{ border-right-color:{YELLOW}; background:rgba(255,209,102,.052); }}
    .callout.warning {{ border-right-color:{PINK}; background:rgba(255,114,199,.052); }}
    .callout.success {{ border-right-color:{GREEN}; background:rgba(88,230,169,.052); }}
    .callout-title {{ color:{YELLOW}; font-weight:950; margin-bottom:.2rem; }}
    .callout-text {{ color:{WHITE}; }}

    /* جدول جذاب */
    .fancy-table-wrap {{
        overflow-x:auto; border-radius:20px; margin:1rem 0 1.2rem;
        border:1px solid rgba(91,140,255,.22);
        box-shadow:0 18px 38px rgba(0,0,0,.22);
        background:rgba(255,255,255,.028);
    }}
    table.fancy-table {{ width:100%; border-collapse:separate; border-spacing:0; min-width:720px; direction:rtl; }}
    .fancy-table thead th {{
        padding:1rem .9rem; color:white; font-weight:950; text-align:right;
        background:linear-gradient(100deg, rgba(41,231,242,.30), rgba(91,140,255,.24), rgba(155,107,255,.30));
        border-bottom:1px solid rgba(255,255,255,.13);
    }}
    .fancy-table tbody td {{ padding:.88rem .9rem; color:{MUTED}; border-bottom:1px solid rgba(255,255,255,.065); background:rgba(255,255,255,.024); }}
    .fancy-table tbody tr:nth-child(even) td {{ background:rgba(255,255,255,.042); }}
    .fancy-table tbody tr:hover td {{ background:rgba(41,231,242,.075); color:{WHITE}; }}
    .fancy-table tbody tr:last-child td {{ border-bottom:none; }}
    .table-badge {{ display:inline-block; padding:.2rem .55rem; border-radius:999px; background:rgba(41,231,242,.10); color:{CYAN}; border:1px solid rgba(41,231,242,.22); font-weight:850; font-size:.82rem; }}

    /* Flow حديث */
    .flow {{ display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:.58rem; margin:1rem 0; }}
    .flow-node {{
        position:relative; padding:.7rem 1rem; border-radius:14px; font-weight:900; color:{WHITE};
        background:linear-gradient(135deg, rgba(41,231,242,.09), rgba(155,107,255,.09));
        border:1px solid rgba(41,231,242,.24); box-shadow:0 10px 24px rgba(0,0,0,.14);
        animation:softPulse 3.4s ease-in-out infinite;
    }}
    .flow-node:nth-child(3) {{ animation-delay:.35s; }} .flow-node:nth-child(5) {{ animation-delay:.7s; }} .flow-node:nth-child(7) {{ animation-delay:1.05s; }}
    @keyframes softPulse {{ 0%,100%{{box-shadow:0 10px 24px rgba(0,0,0,.14)}} 50%{{box-shadow:0 10px 28px rgba(41,231,242,.12)}} }}
    .flow-arrow {{ color:{PINK}; font-size:1.3rem; font-weight:950; }}

    /* Mini chips */
    .mini-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:.72rem; margin:.85rem 0; }}
    .mini-chip {{ padding:.9rem .8rem; border-radius:15px; text-align:center; background:rgba(255,255,255,.043); border:1px solid rgba(255,255,255,.085); color:{WHITE}; font-weight:850; transition:.2s ease; }}
    .mini-chip:hover {{ transform:translateY(-3px); border-color:rgba(155,107,255,.38); background:rgba(155,107,255,.07); }}

    /* Formula */
    .formula-box {{ text-align:center; direction:ltr; font-size:1.24rem; font-weight:950; padding:1rem; border-radius:17px; background:linear-gradient(90deg,rgba(41,231,242,.08),rgba(91,140,255,.09),rgba(155,107,255,.11),rgba(255,114,199,.07)); border:1px solid rgba(155,107,255,.25); color:{YELLOW}; margin:.9rem 0; }}

    /* Sidebar TOC */
    .toc-title {{ color:{CYAN}; font-size:1.2rem; font-weight:950; margin:.2rem 0 .35rem; }}
    .toc-subtitle {{ color:{MUTED}; font-size:.88rem; margin-bottom:.8rem; }}
    .toc-nav {{ display:flex; flex-direction:column; gap:.38rem; margin:.4rem 0 1rem; }}
    .toc-nav a {{ display:block; text-decoration:none !important; color:{WHITE} !important; background:rgba(255,255,255,.043); border:1px solid rgba(255,255,255,.08); border-right:3px solid transparent; border-radius:12px; padding:.48rem .62rem; font-weight:800; line-height:1.55; transition:.18s ease; }}
    .toc-nav a:hover {{ background:rgba(41,231,242,.09); border-color:rgba(41,231,242,.32); border-right-color:{CYAN}; transform:translateX(-2px); }}

    .scroll-anchor {{ scroll-margin-top:1.2rem; height:1px; width:1px; }}
    .section-separator {{ height:1px; margin:2.2rem 0 1.65rem; background:linear-gradient(90deg,transparent,rgba(41,231,242,.34),rgba(155,107,255,.34),transparent); }}
    .back-top {{ text-align:left; margin:.7rem 0 0; }} .back-top a {{ color:{CYAN} !important; text-decoration:none !important; font-size:.88rem; font-weight:850; }}

    /* Streamlit widgets */
    div.stButton > button {{ width:100%; border-radius:14px; border:1px solid rgba(41,231,242,.35); background:linear-gradient(90deg,rgba(41,231,242,.20),rgba(155,107,255,.24)); color:white; font-weight:950; padding:.65rem 1rem; transition:.18s ease; }}
    div.stButton > button:hover {{ transform:translateY(-2px); box-shadow:0 8px 24px rgba(41,231,242,.14); }}
    [data-testid="stExpander"] {{ background:rgba(255,255,255,.035); border:1px solid rgba(255,255,255,.08); border-radius:14px; }}
    [data-testid="stMetric"] {{ background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.08); border-radius:16px; padding:.9rem; }}

    .footer {{ margin-top:2rem; padding:1.1rem; text-align:center; color:{MUTED}; border-top:1px solid rgba(255,255,255,.08); font-size:.9rem; }}

    @media(max-width:760px) {{
        [data-testid="stAppViewContainer"] {{ flex-direction:row !important; }}
        .hero {{ padding:1.45rem 1rem; border-radius:22px; }}
        .hero-title {{ font-size:2rem; }}
        .section-title {{ font-size:1.38rem; }}
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
        body{{margin:0;background:transparent;font-family:Tahoma,Arial,sans-serif;color:{WHITE};overflow:hidden}}
        .wrap{{height:470px;display:flex;align-items:center;justify-content:center;position:relative}}
        .halo{{position:absolute;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(41,231,242,.10),transparent 66%);filter:blur(8px);animation:glow 3.6s ease-in-out infinite}}
        @keyframes glow{{0%,100%{{transform:scale(.98);opacity:.65}}50%{{transform:scale(1.06);opacity:1}}}}
        .ring{{position:absolute;border-radius:50%;display:flex;align-items:flex-start;justify-content:center;box-shadow:0 0 38px rgba(0,0,0,.28) inset,0 0 34px rgba(41,231,242,.06);transition:.25s ease;}}
        .ring:hover{{transform:scale(1.03)}}
        .ai{{width:380px;height:380px;border:2px solid rgba(41,231,242,.65);background:radial-gradient(circle at 30% 25%,rgba(41,231,242,.20),rgba(41,231,242,.06) 40%,rgba(255,255,255,.01) 70%);animation:float1 5s ease-in-out infinite}}
        .ml{{width:270px;height:270px;border:2px solid rgba(155,107,255,.75);background:radial-gradient(circle at 35% 28%,rgba(155,107,255,.22),rgba(155,107,255,.07) 44%,rgba(255,255,255,.01) 72%);top:100px;animation:float2 5s ease-in-out infinite}}
        .dl{{width:160px;height:160px;border:2px solid rgba(255,114,199,.82);background:radial-gradient(circle at 32% 25%,rgba(255,114,199,.25),rgba(255,114,199,.08) 46%,rgba(255,255,255,.01) 72%);top:155px;animation:float3 4.5s ease-in-out infinite}}
        @keyframes float1{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
        @keyframes float2{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(5px)}}}}
        @keyframes float3{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
        .label{{margin-top:26px;text-align:center;font-weight:900;text-shadow:0 0 16px rgba(255,255,255,.12)}}
        .ai .label{{color:{CYAN};font-size:24px}} .ml .label{{color:#C5B2FF;font-size:22px}} .dl .label{{color:#FF9DD5;font-size:20px;margin-top:48px}}
        .small{{display:block;color:{MUTED};font-size:12px;font-weight:700;margin-top:4px}}
        .hint{{position:absolute;bottom:8px;color:{MUTED};font-size:13px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);padding:8px 12px;border-radius:12px}}
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
                    mode="lines", line=dict(color="rgba(180,195,255,.16)", width=2),
                    hoverinfo="skip", showlegend=False
                ))
    # nodes by layer
    for li, nodes in enumerate(layer_nodes):
        fig.add_trace(go.Scatter3d(
            x=[n[0] for n in nodes], y=[n[1] for n in nodes], z=[n[2] for n in nodes],
            mode="markers+text",
            text=[layer_names[li] if i == 0 else "" for i in range(len(nodes))],
            textposition="top center",
            marker=dict(size=8, color=layer_colors[li], opacity=.95, line=dict(color="white", width=.4)),
            hovertemplate=f"{layer_names[li]}<extra></extra>",
            name=layer_names[li]
        ))
    fig.update_layout(
        height=470,
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
# الفهرس
# ==============================
with st.sidebar:
    st.markdown(
        """
        <div class="toc-title">🧭 فهرس المحاضرة</div>
        <div class="toc-subtitle">القراءة متتابعة من الأعلى إلى الأسفل، ويمكن الانتقال مباشرة إلى أي جزء.</div>
        <div class="toc-nav">
          <a href="#goals" target="_self">🎯 أهداف المحاضرة</a>
          <a href="#concepts" target="_self">🧠 AI وML وDL</a>
          <a href="#deep-visual" target="_self">🧬 كيف نفهم كلمة Deep؟</a>
          <a href="#comparison" target="_self">⚖️ مقارنة ML وDL</a>
          <a href="#growth" target="_self">⚡ لماذا انتشر DL؟</a>
          <a href="#hr-apps" target="_self">👥 تطبيقات HR</a>
          <a href="#attrition" target="_self">📊 مثال Attrition</a>
          <a href="#ethics" target="_self">🛡️ القيود والأخلاقيات</a>
          <a href="#activity" target="_self">🧩 نشاط</a>
          <a href="#quiz" target="_self">🏆 اختبار قصير</a>
          <a href="#references" target="_self">📚 المراجع</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(card("فكرة الواجهة", "المعلومة تظهر داخل تصميم بصري؛ الحركة تستخدم فقط عندما تضيف معنى، والـ3D عندما يساعد على فهم البنية.", "green", "Learning by seeing"), unsafe_allow_html=True)

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
