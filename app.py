import streamlit as st

def main():
    st.set_page_config(
        page_title="Prediksi Harga Altcoin dengan SVR dan Firefly Optimization",
        page_icon="👋",
        layout="centered"
    )
    st.header("INTEGRASI SUPPORT VECTOR REGRESSION DAN FIREFLY OPTIMIZATION DALAM PERANCANGAN SISTEM PREDIKSI HARGA ALTCOIN BERBASIS STREAMLIT")
    st.subheader("Informatika - UPN VETERAN JATIM")
    
    st.markdown("---")
    
    st.write("### 📋 Penjelasan Singkat")
    with st.container():
        st.markdown("""
        Aplikasi ini mengimplementasikan integrasi metode **Support Vector Regression (SVR)** dengan **Firefly Optimization** 
        untuk prediksi harga cryptocurrency dengan karakteristik sebagai berikut:
        
        1. **Sumber Data**: Yahoo Finance
        2. **Dataset**: Ethereum, Solana, dan Litecoin
        3. **Periode Data**: 24 Desember 2020 – 1 Februari 2025
        4. **Metode**: Firefly Optimization dan Support Vector Regression (SVR)
        5. **Fitur**: Close, High, Low, Open, dan Volume
        6. **Target Prediksi**: Harga Close (USD) hari selanjutnya
        7. **Cakupan Analisis**: Dilakukan tanpa mempertimbangkan pengaruh tren pasar eksternal
        """)
    
    st.write("### 👨‍🎓 Mahasiswa")
    st.write("**Nama:** Alief Indy Millani")
    st.write("**NIM:** 2008010013")
    
    st.write("### 👨‍🏫 Tim Pembimbing")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Pembimbing 1:**")
        st.write("Dr.Eng.Ir. Dwi Arman Prasetya, ST., MT., IPU., ASEAN Eng.")
        
        st.write("**Pembimbing 3:**")
        st.write("Dr. Ir. Kartini, S.Kom., MT.")
    
    with col2:
        st.write("**Pembimbing 2:**")
        st.write("Eka Prakarsa Mandyartha, S.T., M.Kom.")
        
        st.write("**Pembimbing 4:**")
        st.write("Firza Prima Aditiawan, S.Kom., MTI.")
    
    st.markdown("---")
    st.caption("© 2024 - Alief Indy Millani")

if __name__ == "__main__":
    main()