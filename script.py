import streamlit as st
import pandas as pd
import ast

# Set up Streamlit page config
st.set_page_config(page_title="LALR Parsing Table Generator", layout="wide")

# Custom CSS for better styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .main {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            text-align: center; 
            font-size: 2.5em; 
            font-weight: bold; 
            color: #ff9800;
        }
        .subtitle {
            text-align: center; 
            font-size: 1.2em; 
            color: #bdbdbd;
        }
        .box {
            background: #292929;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 152, 0, 0.5);
        }
        .stButton>button {
            background-color: #ff9800;
            color: white;
            font-size: 16px;
            border-radius: 5px;
        }
        .stDataFrame {
            background: #333333;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ========== Introduction ==========
st.markdown("<div class='title'>LALR Parsing Table Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload your grammar files to generate a LALR parsing table</div>", unsafe_allow_html=True)
st.write("---")

# Description Section
st.markdown("""
    ## What is LALR Parsing?
    LALR (Look-Ahead LR) parsing is used in compiler design to generate parsing tables.
    This tool allows you to upload transition and CLR state files to generate a LALR parsing table.
    
    **How to Use:**
    1. Upload the Transition and CLR States text files.
    2. If parsing is successful, the table will be displayed.
    3. If the result is `-1`, it indicates an issue in parsing.
    4. Download the parsing table as a CSV file if needed.
""")
st.write("---")

# ========== File Upload Section ==========
col1, col2 = st.columns([1, 2])

# Left: File Upload
with col1:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("📂 Upload Files")
    trans_file = st.file_uploader("Upload Transitions File", type=["txt"])
    clr_file = st.file_uploader("Upload CLR States File", type=["txt"])
    st.markdown("</div>", unsafe_allow_html=True)

# Function to load transition table
def load_transitions(file):
    transitions = {}
    for line in file:
        state, trans = line.strip().split("|")
        transitions[int(state)] = ast.literal_eval(trans)
    return transitions

# Function to load CLR states
def load_clr_states(file):
    clr_states = []
    for line in file:
        state, items, lookaheads = line.strip().split("|")
        items = ast.literal_eval(items)
        lookaheads = ast.literal_eval(lookaheads)
        clr_states.append((int(state), items, lookaheads))
    return clr_states

# Process files if uploaded
if trans_file and clr_file:
    transitions = load_transitions(trans_file)
    clr_states = load_clr_states(clr_file)
    st.success("Files successfully uploaded and processed!")
else:
    transitions = None
    clr_states = None

# Right: Parsing Table Display
if transitions and clr_states:
    with col2:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.subheader("🔄 LALR Parsing Table")
        df_transitions = pd.DataFrame([{**{"State": k}, **v} for k, v in transitions.items()])
        st.dataframe(df_transitions)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")

    # Expandable Sections for CLR States
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("📝 CLR States")
    for state, items, lookaheads in clr_states:
        with st.expander(f"State {state}"):
            for rule, lookahead in zip(items, lookaheads):
                st.markdown(f"- `{rule}` **Lookahead:** `{lookahead}`")
    st.markdown("</div>", unsafe_allow_html=True)

    # Download Button
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.download_button(
        label="📥 Download Parsing Table as CSV",
        data=df_transitions.to_csv(index=False).encode('utf-8'),
        file_name="LALR_parsing_table.csv",
        mime="text/csv"
    )
    st.markdown("</div>", unsafe_allow_html=True)
