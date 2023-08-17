from library import *
from process import *

def show_hapus_menu():
    clear_background()
    df = get_dataframe('list-pegawai')
    df['NIP'] = df['NIP'].apply(lambda x: x.replace('\'',''))
    _listnama = sorted(df['Nama'].tolist())
    with st.form(key='edit-pegawai-selectionform',clear_on_submit=False):
        st.markdown("<h1 style='text-align:center;padding-bottom:0px;'>Pilih Pegawai untuk di Edit</h1>",unsafe_allow_html=True)
        _namapegawai = st.selectbox(label='Nama Pegawai',options=_listnama,key='nama-pegawai')
        st.form_submit_button('Pilih')
        
    with st.form(key='edit-pegawai-form',clear_on_submit=False):
        st.markdown("<h1 style='text-align:center;padding-bottom:10px;'>Data Pegawai</h1>",unsafe_allow_html=True)
        try:
            ttd_nama = _namapegawai.split(',')[0]
        except:
            ttd_nama = _namapegawai
        col1,col2 = st.columns(2, gap='medium')
        
        _namaedited = col1.text_input(label='Nama Pegawai',key='nama-edited',value=_namapegawai, disabled=True)
        
        _nippegawai = col2.text_input(label='NIP Pegawai',key='nip-pegawai',value=df[df['Nama']==_namapegawai]['NIP'].values[0], disabled=True)
        
        button = st.form_submit_button('Hapus')
    
    if(button):
        index = df[df['Nama']==_namapegawai].index
        df = df.drop(index)
        df.reset_index(drop=True,inplace=True)
        df.index+=1
        df['NIP'] = df['NIP'].apply(lambda x: '\'' + str(x))
        df.to_excel(PATH / 'list-pegawai.xlsx')
        st.success(f'Data berhasil di hapus!')
        st.experimental_rerun()