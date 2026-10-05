import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import pathlib

st.set_page_config(page_title="StatsLogic.lk", page_icon="📊", layout="wide")

if 'lang' not in st.session_state:
    st.session_state.lang = 'en'
if 'entered' not in st.session_state:
    st.session_state.entered = False
if 'tutor' not in st.session_state:
    st.session_state.tutor = {}

st.markdown("""
<style>
.main-title {font-size: 70px; font-weight: 900; text-align:center; background: linear-gradient(90deg, #00F5FF, #7B68EE, #FF6B9D, #FFD700); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: float 3s ease-in-out infinite;}
@keyframes float {0%{transform:translateY(0)}50%{transform:translateY(-12px)}100%{transform:translateY(0)}}
.owner-card {background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color:white; padding:30px; border-radius:24px; text-align:center; box-shadow: 0 15px 50px rgba(123,104,238,0.4); border:1px solid rgba(255,255,255,0.15);}
.owner-name {font-size:32px; font-weight:800; color:#FFD700;}
.badge {display:inline-block; background:rgba(255,255,255,0.1); padding:8px 16px; border-radius:30px; margin:5px; font-size:12px; border:1px solid rgba(255,255,255,0.2);}
</style>
""", unsafe_allow_html=True)

# --- FIXED TRANSLATION WITH L4 ---
T = {
'en': {'btn_en':'In English','btn_si':'සිංහලෙන්','enter':'Enter to StatsLogic.lk','home':'🏠 Home','ln':'📚 Logic Notes','sn':'📊 Statistics Notes','l1':'📊 Lesson 01: Mean, Median, Mode','l2':'📊 Lesson 02: Standard Deviation','l3':'📊 Lesson 03: Probability','l4':'📊 Lesson 04: Mode (Advanced)','14':'📊 Lesson 04: Mode (Advanced)','concept':'Concept','formula':'Formula','note':'Note','graph':'Graph','quiz':'Quiz','ai':'AI Tutor','ask':'Ask your doubt...'},
'si': {'btn_en':'In English','btn_si':'සිංහලෙන්','enter':'StatsLogic.lk ඇතුලට','home':'🏠 Home','ln':'📚 Logic Notes','sn':'📊 Statistics Notes','l1':'📊 Lesson 01: Mean, Median, Mode','l2':'📊 Lesson 02: Standard Deviation','l3':'📊 Lesson 03: Probability','l4':'📊 Lesson 04: බහුලම අගය (Advanced)','14':'📊 Lesson 04: බහුලම අගය','concept':'සංකල්පය','formula':'සූත්‍රය','note':'සටහන','graph':'ප්‍රස්තාරය','quiz':'ප්‍රශ්නාවලිය','ai':'AI ගුරුවරයා','ask':'ප්‍රශ්නයක් අහන්න...'}
}

def tr(k):
    try: return T[st.session_state.lang][k]
    except: return k.replace("_"," ").title()

if not st.session_state.entered:
    st.markdown('<div class="main-title">StatsLogic.lk</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:monospace; color:#666;'>while(!understand){ learn(); code(); solve(); }<br>CS + Statistics + Logic = One Platform</p>", unsafe_allow_html=True)
    st.write("")
    col1,col2,col3 = st.columns([0.2,2.5,0.2])
    with col2:
        st.markdown("""<div class="owner-card"><div style="font-size:11px; letter-spacing:4px; color:#00F5FF;">OPEN UNIVERSITY OF SRI LANKA</div><div class="owner-name">Dilshi Rathnayaka</div><div style="font-size:13px; color:#bbb;">B.Sc. Natural Sciences (Undergraduate)</div><div style="margin-top:14px;"><span class="badge">💻 Major: Computer Science</span><span class="badge">📊 2nd Major: Applied Maths</span><span class="badge">🧮 Minor: Pure Maths</span></div><div style="margin-top:18px; font-size:13px;">💻 Code + 📊 Stats + 🧠 Logic = <b style="color:#FFD700;">StatsLogic.lk</b></div><div style="margin-top:8px; font-size:11px; opacity:0.6; font-family:monospace;">print("Making A/L Maths Simple ❤️")</div></div>""", unsafe_allow_html=True)
        st.write(""); st.write("")
        c1,c2,c3 = st.columns(3)
        with c1: st.markdown('<div style="text-align:center; background:#f8f9ff; padding:15px; border-radius:15px; border:1px solid #e0e0ff;">💻<br><b>CS Logic</b><br><small>Algorithms</small></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div style="text-align:center; background:#f0fff4; padding:15px; border-radius:15px; border:1px solid #c6f6d5;">📊<br><b>Statistics</b><br><small>Data Insights</small></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div style="text-align:center; background:#fff5f5; padding:15px; border-radius:15px; border:1px solid #fed7d7;">🧠<br><b>Pure Logic</b><br><small>Reasoning</small></div>', unsafe_allow_html=True)
        st.write("")
        if st.button(tr('enter'), use_container_width=True, type="primary", key="enter_btn"):
            st.session_state.entered=True
            st.rerun()
    st.stop()

c1,c2,c3,c4 = st.columns([4,1,1,1])
with c1: st.markdown("### 📊 **StatsLogic.lk** | Dilshi Rathnayaka - OUSL")
with c3:
    if st.button(T[st.session_state.lang]['btn_en'], key="lang_en"): st.session_state.lang='en'; st.rerun()
with c4:
    if st.button(T[st.session_state.lang]['btn_si'], key="lang_si"): st.session_state.lang='si'; st.rerun()
st.divider()

# FIXED PATH - CHECK ALL POSSIBLE LOCATIONS
def get_files():
    paths_to_check = ["Lessons/Statistics", "lessons/statistics", "Lessons", "lessons", "Notes/statistics", "notes/statistics"]
    all_files = []
    for p in paths_to_check:
        if pathlib.Path(p).exists():
            all_files.extend(list(pathlib.Path(p).glob("*.md")))
    return list(set(all_files))

def get_logic_files():
    paths_to_check = ["Lessons/Logic", "lessons/logic", "Notes/logic", "notes/logic"]
    all_files = []
    for p in paths_to_check:
        if pathlib.Path(p).exists():
            all_files.extend(list(pathlib.Path(p).glob("*.md")))
    return list(set(all_files))

logic_files = get_logic_files()
stat_files = get_files()

all_menu = [tr('home'), tr('ln'), tr('sn')]
all_menu.append("--- 🧠 LOGIC LESSONS ---")
for f in logic_files: all_menu.append(f"🧠 {f.stem}")
all_menu.append("--- 📊 STAT LESSONS ---")
all_menu.append(tr('l1')); all_menu.append(tr('l2')); all_menu.append(tr('l3')); all_menu.append(tr('l4'))
for f in stat_files:
    if f.stem not in ["Lesson 01","Lesson 02","Lesson 03","Lesson 04"]:
        all_menu.append(f"📊 {f.stem}")

menu = st.sidebar.radio("Navigate", all_menu)
st.sidebar.markdown("---")
if st.sidebar.button("🔙 Back to Cover Page", use_container_width=True, key="back_cover"):
    st.session_state.entered = False
    st.rerun()
st.sidebar.markdown("---\n**👩‍🏫 Dilshi Rathnayaka**\nB.Sc. Natural Sciences\n*Open University of Sri Lanka*\n💻 CS + 📊 Maths")

def ai_tutor(pid,en,si):
    st.markdown(f"#### {tr('ai')} - {pid}")
    ctx = si if st.session_state.lang=='si' else en
    if pid not in st.session_state.tutor: st.session_state.tutor[pid]=[]
    for u,a in st.session_state.tutor[pid]:
        with st.chat_message("user"): st.write(u)
        with st.chat_message("assistant"): st.write(a)
    q=st.chat_input(tr('ask'), key=f"chat_{pid}")
    if q:
        ans = f"{ctx}\n\n💡 Tip: Example එකකින් මතක තියාගන්න!" if st.session_state.lang=='si' else f"{ctx}\n\n💡 Tip: Learn with an example!"
        st.session_state.tutor[pid].append((q,ans))
        st.rerun()

if menu == tr('home'):
    if st.session_state.lang=='en':
        st.header("Welcome to StatsLogic.lk"); st.subheader("Learn A/L Statistics with CS Thinking"); st.write("I'm Dilshi from **Open University of Sri Lanka**. I combine Computer Science logic with Statistics to make everything super simple with graphs, bilingual notes & AI tutor for each part.")
    else:
        st.header("StatsLogic.lk වෙත සාදරයෙන් පිළිගනිමු"); st.subheader("CS තර්කනයත් එක්ක A/L සංඛ්‍යානය ඉගෙන ගමු"); st.write("මම දිල්ෂි, **ශ්‍රී ලංකා විවෘත විශ්වවිද්‍යාලයේ** B.Sc. Natural Sciences උපාධිධාරිනිය. CS logic එකයි Stats එකයි combine කරලා ප්‍රස්තාර, ද්විභාෂා සටහන් සහ හැම කොටසටම AI ගුරුවරයෙක් එක්ක උගන්වනවා.")
    c1,c2,c3 = st.columns(3)
    c1.metric("Lessons", "10+", "Full A/L"); c2.metric("AI Tutors", "30+", "Per Part"); c3.metric("Quizzes", "100+", "With Answers")
    st.info("👈 Sidebar එකෙන් Lesson එකක් තෝරන්න!")

elif menu == tr('l1'):
    st.header(tr('l1'))
    with st.container(border=True):
        st.subheader("🔹 Part 01: Mean (මධ්‍යමය)")
        c1,c2 = st.columns(2)
        with c1:
            st.markdown(f"**{tr('concept')}**"); st.write("Add all / divide by n. Outlier වලට අහු වෙනවා!" if st.session_state.lang=='si' else "Add all / divide by n. Sensitive to outliers!"); st.markdown(f"**{tr('formula')}**"); st.latex(r"\bar{x} = \frac{\sum x}{n}"); st.markdown(f"**{tr('note')}**"); st.success("📌 10,20,20,30,70 => Mean 30 but wrong! Use Median 20" if st.session_state.lang=='en' else "📌 10,20,20,30,70 => Mean 30 ඒත් වැරදියි! Median 20 ගන්න")
        with c2:
            st.markdown(f"**{tr('graph')}**"); fig,ax = plt.subplots(); data=[10,20,20,30,70]; ax.bar(range(len(data)),data, color=['#7B68EE']*4+['red']); ax.axhline(np.mean(data),color='red',ls='--',label='Mean 30'); ax.axhline(np.median(data),color='green',label='Median 20'); ax.legend(); st.pyplot(fig)
        ai_tutor("L1-P1","Mean = sum/n, fails with outlier","මධ්‍යමය = එකතුව/ගණන, Outlier තිබ්බොත් වැරදෙනවා")
    with st.container(border=True):
        st.subheader("🔸 Part 02: Median (මධ්‍යස්ථය)")
        c1,c2 = st.columns(2)
        with c1: st.write("Sort කරලා මැද එක. Outlier වලට අසුවෙන්නේ නෑ! ⭐" if st.session_state.lang=='si' else "Sort and take middle. NOT affected by outliers! ⭐"); st.latex(r"\text{Median = Middle after sorting}"); st.info("A/L වල Outlier තියෙනවා නම් හැමදාම Median ගන්න!")
        with c2: fig,ax = plt.subplots(); ax.boxplot([10,20,20,30,70], vert=False); st.pyplot(fig)
        ai_tutor("L1-P2","Median safe from outliers","මධ්‍යස්ථය Outlier වලින් ආරක්ෂිතයි")
    st.divider(); st.subheader(tr('quiz')); q=st.radio("10,20,20,30,70 Median?",["20","30","70"], key="quiz_l1_q1", index=None)
    if q:
        if q=="20": st.success("Correct! හරි! 🎉"); st.balloons()
        else: st.error("Wrong! Correct is 20")

elif menu == tr('l2'):
    st.header(tr('l2'))
    with st.container(border=True):
        st.subheader("🔹 Part 01: Standard Deviation"); c1,c2=st.columns(2)
        with c1: st.latex(r"\sigma = \sqrt{\frac{\sum (x-\bar{x})^2}{n}}"); st.success("Low SD = stable class, High SD = spread class!")
        with c2: fig,ax=plt.subplots(); ax.hist(np.random.normal(50,5,200),alpha=0.6,label='Low SD - Stable'); ax.hist(np.random.normal(50,15,200),alpha=0.6,label='High SD - Spread'); ax.legend(); st.pyplot(fig)
        ai_tutor("L2-P1","SD measures spread","SD මගින් විසිරීම මනිනවා")
    st.divider(); st.subheader(tr('quiz')); q2=st.radio("Low SD means?",["Data close to mean","Data spread"], key="quiz_l2_q1", index=None)
    if q2:
        if q2=="Data close to mean": st.success("Correct! 🎉"); st.balloons()
        else: st.error("Wrong! Low SD = close to mean")

elif menu == tr('l3'):
    st.header(tr('l3'))
    with st.container(border=True):
        st.subheader("🔹 Part 01: Probability Basics"); st.write("P(A) = Favourable / Total"); st.latex(r"P(A) = \frac{n(A)}{n(S)}"); st.info("Dice example: P(6) = 1/6"); ai_tutor("L3-P1","Probability = fav/total","සම්භාවිතාව = හිතකර/මුළු")

# ============ FIXED LESSON 04 ============
elif menu == tr('l4') or menu == tr('14') or "Lesson 04" in menu or "04" in menu:
    st.header(tr('l4'))
    with st.container(border=True):
        st.subheader("🔹 Part 01: Mode - The Most Frequent (බහුලම අගය)")
        from pathlib import Path
        possible_paths = [Path("Lessons/Statistics/Lesson 04.md"), Path("lessons/statistics/Lesson 04.md"), Path("Lessons/Statistics/lesson 04.md"), Path("Lesson 04.md")]
        found = False
        for p in possible_paths:
            if p.exists():
                st.markdown(p.read_text(encoding="utf-8"))
                found = True
                break
        if not found:
            st.markdown("""
            **Mode = Most frequent value**
            - Ungrouped: Count karala balanawa
            - Grouped: `Mode = L + (f1-f0)/(2*f1-f0-f2) * h`
            """)
        st.info("Grouped Mode = L + (f1-f0)/(2f1-f0-f2) * h")
        ai_tutor("L4-P1","Mode = most frequent value","බහුලම දත්ත අගය = Mode")

# --- AUTO LOGIC LESSONS ---
elif menu.startswith("🧠"):
    st.header(menu)
    lesson_name = menu.replace("🧠","").strip()
    from pathlib import Path
    for base in ["lessons/logic", "Lessons/Logic", "notes/logic", "Notes/logic"]:
        p = Path(f"{base}/{lesson_name}.md")
        if p.exists():
            st.markdown(p.read_text(encoding="utf-8"))
            break

# --- ALL STAT LESSONS AUTO ---
elif "Lesson" in menu and menu not in [tr('l1'), tr('l2'), tr('l3'), tr('l4')]:
    st.header(menu)
    from pathlib import Path
    import re
    m = re.search(r"Lesson\s*0*(\d+)", menu)
    num = m.group(1) if m else "04"
    folder = Path("Lessons/Statistics")
    if not folder.exists(): folder = Path("lessons/statistics")
    found = None
    for f in folder.glob("*.md"):
        if num in f.stem: found = f; break
    if found and found.exists(): st.markdown(found.read_text(encoding="utf-8"))
    else: st.info(f"File eka na: {folder}/Lesson {num}.md")

elif menu == tr('ln'):
    st.header("📚 Logic Notes")
    from pathlib import Path
    base = Path("notes") / "logic"
    if not base.exists(): base = Path("Notes") / "logic"
    files = list(base.rglob("*.pdf")) + list(base.rglob("*.jpg")) + list(base.rglob("*.jpeg")) + list(base.rglob("*.png")) + list(base.rglob("*.webp"))
    if not files: st.info("notes/logic folder ekata files danna!")
    else:
        for f in sorted(files):
            c1,c2 = st.columns([1,3])
            with c1:
                if f.suffix.lower() in ['.jpg','.jpeg','.png','.webp']: st.image(str(f), use_container_width=True)
            with c2:
                st.write(f"**{f.name}**")
                with open(f, "rb") as file: st.download_button(f"⬇️ Download", file, file_name=f.name, key=str(f))

elif menu == tr('sn'):
    st.header("📊 Statistics Notes")
    from pathlib import Path
    base = Path("notes") / "statistics"
    if not base.exists(): base = Path("Notes") / "statistics"
    if not base.exists(): base = Path("Notes") / "logic"
    files = list(base.rglob("*.pdf")) + list(base.rglob("*.jpg")) + list(base.rglob("*.jpeg")) + list(base.rglob("*.png")) + list(base.rglob("*.webp"))
    if not files: st.info("notes/statistics folder ekata files danna! Dan thiyenne logic images tika pennanawa")
    else:
        for f in sorted(files):
            c1,c2 = st.columns([1,3])
            with c1:
                if f.suffix.lower() in ['.jpg','.jpeg','.png','.webp']: st.image(str(f), use_container_width=True)
            with c2:
                st.write(f"**{f.name}**")
                with open(f, "rb") as file: st.download_button(f"⬇️ Download", file, file_name=f.name, key=str(f))

