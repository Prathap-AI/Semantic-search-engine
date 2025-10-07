import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LangChain Tutorial: Document Loaders, Embeddings, and Vector Stores",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        color: #1f77b4;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .nav-button {
        background-color: #1f77b4;
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        margin: 0.5rem;
        width: 100%;
        text-align: center;
    }
    .nav-button:hover {
        background-color: #155a8a;
    }
    .footer {
        background-color: #f1f1f1;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-header">LangChain Tutorial</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Document Loaders, Embeddings, and Vector Stores for Retrieval-Augmented Generation (RAG)</div>', unsafe_allow_html=True)

# Overview Section
st.markdown('<div class="section-header">Overview</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="card">
        <h3>What You'll Learn</h3>
        <p>This tutorial covers the essential components for building semantic search engines and RAG applications using LangChain:</p>
        <ul>
            <li><strong>Document Loaders</strong>: Extract and load data from various sources (PDFs, websites, databases)</li>
            <li><strong>Embeddings</strong>: Convert text into numerical vectors that capture semantic meaning</li>
            <li><strong>Vector Stores</strong>: Efficiently store and retrieve embedded documents</li>
            <li><strong>RAG Applications</strong>: Combine retrieval with generation for accurate, context-aware responses</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Why This Matters</h3>
        <p>These technologies are crucial for:</p>
        <ul>
            <li>Overcoming LLM context window limitations</li>
            <li>Providing up-to-date information beyond training data</li>
            <li>Building domain-specific AI applications</li>
            <li>Improving response accuracy with relevant context</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Navigation Section
st.markdown('<div class="section-header">Tutorial Navigation</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📄 Document Loaders", key="loaders"):
        st.session_state.current_section = "Document Loaders"
        st.info("Navigating to Document Loaders section...")

with col2:
    if st.button("🔤 Embeddings", key="embeddings"):
        st.session_state.current_section = "Embeddings"
        st.info("Navigating to Embeddings section...")

with col3:
    if st.button("🗄️ Vector Stores", key="vector_stores"):
        st.session_state.current_section = "Vector Stores"
        st.info("Navigating to Vector Stores section...")

with col4:
    if st.button("🤖 RAG Example", key="rag"):
        st.session_state.current_section = "RAG Example"
        st.info("Navigating to RAG Example section...")

# Key Concepts Section
st.markdown('<div class="section-header">Key Concepts</div>', unsafe_allow_html=True)

concept_col1, concept_col2, concept_col3 = st.columns(3)

with concept_col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>📄 Document Loaders</h3>
        <p>LangChain provides specialized loaders for hundreds of data sources including PDFs, websites, databases, and more. These convert raw data into standardized Document objects with metadata.</p>
    </div>
    """, unsafe_allow_html=True)

with concept_col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>🔤 Embeddings</h3>
        <p>Embedding models convert text into dense vector representations where semantically similar texts are geometrically close. This enables semantic search beyond keyword matching.</p>
    </div>
    """, unsafe_allow_html=True)

with concept_col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>🗄️ Vector Stores</h3>
        <p>Vector databases efficiently store and retrieve embedded documents using similarity search. Popular options include Chroma, Pinecone, and FAISS.</p>
    </div>
    """, unsafe_allow_html=True)

# RAG Workflow Visualization
st.markdown('<div class="section-header">RAG Workflow</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 10px; color: white; margin: 1rem 0;">
    <h3 style="color: white;">Retrieval-Augmented Generation Pipeline</h3>
    <p><strong>Document Loading → Text Splitting → Embedding → Vector Storage → Query Processing → Context Retrieval → LLM Generation</strong></p>
</div>
""", unsafe_allow_html=True)

# Prerequisites Section
st.markdown('<div class="section-header">Prerequisites</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <ul>
        <li>Basic Python programming knowledge</li>
        <li>Familiarity with machine learning concepts</li>
        <li>Python 3.8+ installed on your system</li>
        <li>Basic understanding of LLMs and their applications</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3>Additional Resources</h3>
    <p>
        <a href="https://python.langchain.com/docs/get_started/introduction" target="_blank">LangChain Documentation</a> • 
        <a href="https://python.langchain.com/docs/use_cases/question_answering/" target="_blank">RAG Tutorial</a> • 
        <a href="https://huggingface.co/" target="_blank">Hugging Face</a>
    </p>
    <p><strong>Created for educational purposes</strong> - This tutorial demonstrates core concepts for building semantic search and RAG applications.</p>
    <p>For questions or feedback, please contact: tutorial@example.com</p>
    <p style="margin-top: 1rem; font-size: 0.8rem; color: #666;">
        © 2024 LangChain Tutorial. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = "Home"