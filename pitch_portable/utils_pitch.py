import streamlit as st


def header(title, subtitle=""):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"**{subtitle}**")


def footer():
    st.markdown("---")
    st.markdown("© Projet Rakuten – Pitch condensé")


def badge(label, value):
    st.markdown(
        f"""
        <div style='display:inline-block; padding:6px 12px; margin:4px;
                    background:#f0f0f0; border-radius:6px;'>
            <b>{label} :</b> {value}
        </div>
        """,
        unsafe_allow_html=True
    )


def insight_card(text):
    st.markdown(
        f"""
        <div style='padding:12px; background:#eef6ff; border-left:4px solid #1f77b4;
                    border-radius:4px; margin:10px 0;'>
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )
