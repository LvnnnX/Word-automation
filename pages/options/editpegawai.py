from library import *
from process import *

def find_filename(name):
    name = glob.glob(f'{ASSETS}/{name}.*')
    return name[0]

def show_edit_menu():
    clear_background()
    df = get_dataframe('list-pegawai')
    df['NIP'] = df['NIP'].apply(lambda x: x.replace('\'',''))
    _listnama = sorted(df['Nama'].tolist())
    with st.form(key='edit-pegawai-selectionform',clear_on_submit=False):
        st.markdown("<h1 style='text-align:center;padding-bottom:0px;'>Pilih Pegawai untuk di Edit</h1>",unsafe_allow_html=True)
        _namapegawai = st.selectbox(label='Nama Pegawai',options=_listnama,key='nama-pegawai')
        st.form_submit_button('Pilih')
        
    error = False
    with st.form(key='edit-pegawai-form',clear_on_submit=False):
        st.markdown("<h1 style='text-align:center;padding-bottom:10px;'>Form Edit Pegawai</h1>",unsafe_allow_html=True)
        try:
            ttd_nama = _namapegawai.split(',')[0]
        except:
            ttd_nama = _namapegawai
        col1,col2 = st.columns(2, gap='medium')
        _namaedited = col1.text_input(label='Nama Pegawai',key='nama-edited',value=_namapegawai)
        
        _nippegawai = col2.text_input(label='NIP Pegawai',key='nip-pegawai',value=str(df[df['Nama']==_namapegawai]['NIP'].values[0]))
        try:
            ttd_image = get_image(get_filename_for_show(ttd_nama))
            # st.write(ttd_image)
            col1.write('TTD Pegawai')
            
            col1.image(ttd_image,width=150)
            
            _ttdedit = col2.file_uploader(label='Upload TTD Pegawai',key='ttd-pegawai',type=['jpg','png','jpeg'],accept_multiple_files=False)
            
        except ValueError as e:
            st.write(e)
            error = True
            # st.error(f'TTD Tidak ditemukan!')
        
        button2 = st.form_submit_button('Simpan')

    if(button2):
        if(_namapegawai!=_namaedited):
            df = df.replace(_namapegawai,_namaedited)
        if(df[df['Nama']==_namapegawai]['NIP'].values!=_nippegawai):
            df = df.replace(df[df['Nama']==_namapegawai]['NIP'].values,str(_nippegawai))
        if(not error):
            if(_ttdedit is not None):
                nama_file2 =_namaedited.split(',')[0]
                nama_file2 = ' '.join([x.capitalize() for x in nama_file2.split(' ')])
                
                nama_file1 = _namapegawai.split(',')[0]
                nama_file1 = ' '.join([x.capitalize() for x in nama_file1.split(' ')])
                
                df.replace(nama_file1,str(nama_file2))
                save_image(_ttdedit, nama_file2)
        
        df['NIP'] = df['NIP'].apply(lambda x: '\'' + str(x))
        df.to_excel(PATH / 'list-pegawai.xlsx')
        st.success(f'Data berhasil di edit!')
        st.experimental_rerun()