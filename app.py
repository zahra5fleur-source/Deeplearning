import streamlit as st, json, os
from pathlib import Path

st.set_page_config(page_title="تطبيقات التعلم العميق في HR", layout="wide", initial_sidebar_state="collapsed")
ROOT=Path(__file__).parent
CONTENT=ROOT/'content'; ASSETS=ROOT/'assets'

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

lectures=sorted(CONTENT.glob('lecture_*.json'))
items=[]
for p in lectures:
    d=json.load(open(p,encoding='utf-8')); items.append((d['no'],d['title'],p))
choice=st.selectbox('اختر المحاضرة',items,format_func=lambda x:f"المحاضرة {x[0]} - {x[1]}")
D=json.load(open(choice[2],encoding='utf-8'))

links=''.join([f'<a href="#sec{i+1}">{title}</a>' for i,(title,_) in enumerate(D['sections'])])
toc=f'<div class="toc"><h3>فهرس المحاضرة</h3><a class="home" href="#top">بداية المحاضرة</a><a href="#objectives">الأهداف</a>{links}<a href="#compare">جدول المقارنة</a><a href="#quiz">اختبار قصير</a><a href="#review">أسئلة المراجعة</a><a href="#refs">المراجع</a></div>'
st.markdown(toc,unsafe_allow_html=True)
st.markdown(f'<div id="top" class="hero"><h1>المحاضرة {D["no"]}: {D["title"]}</h1><p>{D["subtitle"]}</p></div>',unsafe_allow_html=True)

st.markdown('<div id="objectives" class="section-title">أهداف المحاضرة</div>',unsafe_allow_html=True)
objs=''.join([f'<div class="obj">🎯 {x}</div>' for x in D['objectives']])
st.markdown(f'<div class="obj-grid">{objs}</div>',unsafe_allow_html=True)

img=ASSETS/D['visual']
if img.exists(): st.image(str(img),use_container_width=True)

for i,(title,paras) in enumerate(D['sections']):
    st.markdown(f'<div id="sec{i+1}" class="section-title">{title}</div>',unsafe_allow_html=True)
    for p in paras: st.markdown(f'<div class="card">{p}</div>',unsafe_allow_html=True)

if D.get('comparison'):
    st.markdown('<div id="compare" class="section-title">مقارنة وتلخيص بصري</div>',unsafe_allow_html=True)
    rows=D['comparison']; hdr=''.join(f'<th>{x}</th>' for x in rows[0]); body=''.join('<tr>'+''.join(f'<td>{x}</td>' for x in r)+'</tr>' for r in rows[1:])
    st.markdown(f'<div class="table-wrap"><table class="tbl"><thead><tr>{hdr}</tr></thead><tbody>{body}</tbody></table></div>',unsafe_allow_html=True)

if D.get('code'):
    st.markdown('<div class="section-title">مثال برمجي مبسط</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="codebox">{D["code"]}</div>',unsafe_allow_html=True)

st.markdown('<div class="section-title">مثال تطبيقي من الموارد البشرية</div>',unsafe_allow_html=True)
st.markdown(f'<div class="callout">💡 {D["example"]}</div>',unsafe_allow_html=True)

st.markdown('<div id="quiz" class="section-title">اختبار قصير</div>',unsafe_allow_html=True)
score=0
for j,(q,opts,ans) in enumerate(D['quiz']):
    v=st.radio(q,opts,key=f"q{D['no']}_{j}",index=None)
    if v is not None:
        if v==ans: st.success('إجابة صحيحة'); score+=1
        else: st.error(f'الإجابة الصحيحة: {ans}')
st.caption(f"النتيجة الحالية: {score}/{len(D['quiz'])}")

st.markdown('<div id="review" class="section-title">أسئلة للمراجعة والتثبيت</div>',unsafe_allow_html=True)
qs=''.join([f'<li>{q}</li>' for q in D['review']])
st.markdown(f'<div class="review"><ol>{qs}</ol></div>',unsafe_allow_html=True)

st.markdown('<div id="refs" class="section-title">المراجع الأساسية</div>',unsafe_allow_html=True)
for r in D['references']: st.markdown(f'<div class="small">• {r}</div>',unsafe_allow_html=True)
