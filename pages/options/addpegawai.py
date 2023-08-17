from library import *
from process import *

def show_pegawai_form(num_pegawai:int=0):
    st.markdown("""---""")
    list_nama,list_nip,list_files = ['' for _ in range(num_pegawai)],['' for _ in range(num_pegawai)],['' for _ in range(num_pegawai)]
    for pegawai in range(num_pegawai):
        col1,col2 = st.columns([2,1.47],gap='small')
        
        list_nama[pegawai] = col1.text_input(f'Nama Pegawai {pegawai+1}', key=f'nama-pegawai-{pegawai}')
        
        list_nip[pegawai] = col1.text_input(f'NIP Pegawai {pegawai+1}', key=f'nip-pegawai-{pegawai}')
        
        list_files[pegawai] = col2.file_uploader(f'TTD Pegawai {pegawai+1}', key=f'foto-pegawai-{pegawai}', type=['jpg','png','jpeg'], accept_multiple_files=False)
        
        if(list_files[pegawai]==None): list_files[pegawai] = ''
        st.markdown("""---""")
        
    return list_nama, list_nip, list_files



def show_pegawai_menu():
    clear_background()
    num_pegawai = st.number_input('Jumlah pegawai yang ingin ditambahkan',key='jumlah-pegawai',min_value=1,value=1,max_value=10)
    list_nama, list_nip, list_files = [],[],[]
    with st.form(key='tambah-pegawai-form',clear_on_submit=True):
        st.markdown("<h1 style='text-align:center;padding-bottom:0px;'>Form Tambah Pegawai</h1>",unsafe_allow_html=True)
        list_nama, list_nip, list_files = show_pegawai_form(num_pegawai=num_pegawai)
        button = st.form_submit_button('Tambah')
    if button:
        if('' not in tuple(list_nama + list_nip + list_files)):
            if(max:=len(list_nama) > 0):
                df = get_dataframe('list-pegawai')
                df.to_excel(PATH / 'list-pegawai-backup.xlsx')
                count=0
                for nama,nip,file in zip(list_nama,list_nip,list_files):
                    nip = '\'' + str(nip.replace(' ', ''))
                    try:
                        _gelar = str(nama.split(',')[1])
                        nama_lengkap = nama +', '+_gelar
                    except:
                        nama_lengkap = nama
                    df = df.append({'Nama':nama_lengkap,'NIP':nip,'Nama File':nama},ignore_index=True)
                    save_image(file, nama)
                    count+=1
                df.to_excel(PATH / 'list-pegawai.xlsx')
            st.success('Data berhasil ditambahkan')
            st.experimental_rerun()     
        else:
            st.error(f'Lengkapi data terlebih dahulu!')
    # st.write(list_nama, list_nip, list_files)