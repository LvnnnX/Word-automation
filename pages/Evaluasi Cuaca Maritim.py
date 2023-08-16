from library import *
from process import *

clear_background()
with st.form(key='data-form', clear_on_submit=False):
    # TODO 1 : Waktu pelaksanaan
    tanggal_sekarang, jam_sekarang, shift_sekarang = get_jadwal_sekarang()
    tanggal_besok = tanggal_sekarang + timedelta(days=1)

    st.markdown(f"<h3 style='text-align:center;font-weight:bold;'>Evaluasi Cuaca Maritim<h3>", unsafe_allow_html=True)

    col1,col2,col3,col4,col5 = st.columns(5, gap='small')
    get_tanggal1 = col1.date_input('Tanggal', value=tanggal_sekarang, key='tanggal-awal')
    
    get_jam1 = col2.time_input('Pukul', value=jam_sekarang, key='jam-awal')
    
    col3.text_input('',value='sampai',key='sampai',disabled=True)
    
    get_tanggal2 = col4.date_input('Tanggal', value=tanggal_besok, key='tanggal-akhir')
    
    get_jam2 = col5.time_input('Pukul', value=jam_sekarang, key='jam-akhir')
    
    
    st.write('')
    st.markdown("<p style='text-align:left;font-weight:bold;'>Dasar pertimbangan</p>", unsafe_allow_html=True)
    dasar_pertimbangan1 = st.text_area('Deskripsi', value='', key='cuaca')
    
    col1,col2 = st.columns([1,2], gap='small')
    col1.text_input('',label_visibility='hidden',value='0.5 - 1.25 Meter (Rendah)',disabled=True)
    text_rendah = col2.text_input('',value='',key='text-rendah', label_visibility='hidden')
    
    col1.text_input('',label_visibility='hidden',value='1.25 - 2.5 Meter (Sedang)',disabled=True)
    text_sedang = col2.text_input('',value='',key='text-sedang', label_visibility='hidden')
    
    col1.text_input('',label_visibility='hidden',value='2.5 - 4 Meter (Tinggi)',disabled=True)
    text_tinggi = col2.text_input('',value='',key='text-tinggi', label_visibility='hidden')
    
    col1.text_input('',label_visibility='hidden',value='4 - 6 Meter (Sangat Tinggi)',disabled=True)
    text_sangattinggi = col2.text_input('',value='',key='text-sangattinggi', label_visibility='hidden')

    form1_submitbutton = st.form_submit_button(label='Check')
    st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk mengubah Hari dan Jam Kerja</p>", unsafe_allow_html=True)

if form1_submitbutton:
    st.success(f'Berhasil mengubah Hari dan Shift menjadi **:blue[{get_hari} {get_shift.lower()}]**')