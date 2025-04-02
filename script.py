
import streamlit as st
import pandas as pd
import ast

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

# Streamlit UI
st.set_page_config(page_title="LALR Parsing Table Generator", layout="wide")
st.title("📖 LALR Parsing Table Generator")

# Bento Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📂 Upload Files")
    trans_file = st.file_uploader("Upload Transitions File", type=["txt"])
    clr_file = st.file_uploader("Upload CLR States File", type=["txt"])
    
    if trans_file and clr_file:
        transitions = load_transitions(trans_file)
        clr_states = load_clr_states(clr_file)
        st.success("Files successfully uploaded and processed!")
    else:
        transitions = None
        clr_states = None

if transitions and clr_states:
    with col2:
        st.header("🔄 Transition Table")
        df_transitions = pd.DataFrame([{**{"State": k}, **v} for k, v in transitions.items()])
        st.dataframe(df_transitions, hide_index=True)

    st.divider()
    
    st.header("📝 CLR States")
    for state, items, lookaheads in clr_states:
        with st.expander(f"State {state}"):
            for rule, lookahead in zip(items, lookaheads):
                st.markdown(f"- `{rule}` **Lookahead:** `{lookahead}`")

    # Download Option
    st.download_button(
        label="Download Parsing Table as CSV",
        data=df_transitions.to_csv(index=False).encode('utf-8'),
        file_name="LALR_parsing_table.csv",
        mime="text/csv"
    )
