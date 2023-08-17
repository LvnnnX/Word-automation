from library import *
from process import *

def options():
    clear_background()
    placeholder = st.empty()
    with placeholder.container():
        st.markdown(f'<h1 style="text-align: center;">Options</h1>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="text-align: left;">Menu Pegawai</h3>', unsafe_allow_html=True)
        # col1, col2 = st.columns([1,20], gap='small')
        # show_pegawai_button = col1.checkbox('', key='tambah-pegawai-button', label_visibility='collapsed')
        # col2.write('Tampilkan Data Pegawai', key='show-pegawai')

        # if(show_pegawai_button):
        data_pegawai = get_dataframe('list-pegawai')
        data_pegawai['NIP'] = data_pegawai['NIP'].apply(lambda x:x.replace('\'',''))
        data_pegawai = data_pegawai.drop(columns=['Nama File'])
        data_pegawai = data_pegawai.sort_values(by=['Nama'], ascending=True)
        data_pegawai.reset_index(drop=True,inplace=True)
        data_pegawai.index+=1
        st.dataframe(data_pegawai, width=1000)