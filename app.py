import streamlit as st
import pandas as pd
import ast
import networkx as nx
import matplotlib.pyplot as plt

def load_transitions(file):
    """Loads state transitions from the uploaded file."""
    transitions = {}
    try:
        content = file.getvalue().decode('utf-8')
        for line in content.splitlines():
            state, trans = line.strip().split("|")
            transitions[int(state)] = ast.literal_eval(trans)
        return transitions
    except Exception as e:
        st.error(f"Error loading transitions: {e}")
        return None

def load_clr_states(file):
    """Loads CLR states from the uploaded file."""
    clr_states = []
    try:
        content = file.getvalue().decode('utf-8')
        for line in content.splitlines():
            state, items, lookaheads = line.strip().split("|")
            items = ast.literal_eval(items)
            lookaheads = ast.literal_eval(lookaheads)
            clr_states.append((int(state), items, lookaheads))
        return clr_states
    except Exception as e:
        st.error(f"Error loading CLR states: {e}")
        return None

def main():
    st.set_page_config(page_title="LALR Parsing Table Generator", layout="wide")
    st.title("🔷 LALR Parsing Table Generator")
    st.markdown("Upload transition and CLR state files to generate a parsing table.")
    
    col1, col2 = st.columns(2)
    with col1:
        trans_file = st.file_uploader("Upload Transitions File", type=["txt"])
    with col2:
        clr_file = st.file_uploader("Upload CLR States File", type=["txt"])
    
    if st.button("🚀 Generate Table"):
        if trans_file and clr_file:
            transitions = load_transitions(trans_file)
            clr_states = load_clr_states(clr_file)
            
            if transitions and clr_states:
                st.success("✅ Files loaded successfully!")
                # Further processing logic goes here
            else:
                st.error("❌ Failed to process the files. Check formatting.")
        else:
            st.error("❌ Please upload both files.")
    
if __name__ == "__main__":
    main()
