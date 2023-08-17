from library import *
from process import *

def start_evaluasi_cuaca_maritim():
    clear_background()
    with st.form(key='data-form', clear_on_submit=False):
        user,_,_ = get_pegawai()
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
        dasar_pertimbangan1 = st.text_area('1.Tinggi dan Gelombang', value='', key='cuaca')
        
        col1,col2,col3 = st.columns([1,0.2,2], gap='small')
        col1.text_input('',label_visibility='collapsed',value='0.5 - 1.25 Meter (Rendah)',disabled=True)
        col2.text_input('',value='=',key='col2-1',disabled=True, label_visibility='collapsed') 
        col2.text_input('',value='=',key='col2-2',disabled=True, label_visibility='collapsed')
        col2.text_input('',value='=',key='col2-3',disabled=True, label_visibility='collapsed')
        col2.text_input('',value='=',key='col2-4',disabled=True, label_visibility='collapsed')
        
        text_rendah = col3.text_input('',value='',key='text-rendah', label_visibility='collapsed')
        
        col1.text_input('',label_visibility='collapsed',value='1.25 - 2.5 Meter (Sedang)',disabled=True)
        text_sedang = col3.text_input('',value='',key='text-sedang', label_visibility='collapsed')
        
        col1.text_input('',label_visibility='collapsed',value='2.5 - 4 Meter (Tinggi)',disabled=True)
        text_tinggi = col3.text_input('',value='',key='text-tinggi', label_visibility='collapsed')
        
        col1.text_input('',label_visibility='collapsed',value='4 - 6 Meter (Sangat Tinggi)',disabled=True)
        text_sangattinggi = col3.text_input('',value='',key='text-sangattinggi', label_visibility='collapsed')

        dasar_pertimbangan2 = st.text_area('2.Arah dan Kecepatan Angin')
        
        col1,col2 = st.columns(2, gap='medium')
        
        col1.markdown("<p style='font-size:14px;text-align:center'>Arah dan Kecepatan Angin</p>", unsafe_allow_html=True)
        col2.markdown("<p style='font-size:14px;text-align:center'>Tinggi Gelombang </p>", unsafe_allow_html=True)
        
        
        image_1 = col1.file_uploader('Arah dan Kecepatan Angin', type=['png','jpg','jpeg'], key='angin', accept_multiple_files=False,label_visibility='collapsed')
        image_2 = col2.file_uploader('Tinggi Gelombang Signifikan', type=['png','jpg','jpeg'], key='gelombang', accept_multiple_files=False,label_visibility='collapsed')
        col1.markdown("<p style='font-size:10px'>*Gambar wajib diisi agar file dapat di Download</p>", unsafe_allow_html=True)
        
        st.write('')
        st.markdown("<p style='text-align:left;font-weight:bold;'>Kesimpulan</p>", unsafe_allow_html=True)
        kesimpulan = st.text_area('',value='',key='kesimpulan',disabled=False,label_visibility='collapsed')
        
        user1 = st.selectbox(options=user,label='Dibuat oleh')
        
        form1_submitbutton = st.form_submit_button(label='Check')
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk menyimpan perubahan</p>", unsafe_allow_html=True)

    if form1_submitbutton:
        if(None in [image_1,image_2]):
            st.error('Mohon masukkan gambar')
        else:
            st.success(f'Berhasil mengupdate data')
        
    try:
        docs = evaluasi_cuaca_maritim(get_tanggal1,get_tanggal2,
                                    jam=get_jam1,
                                    jam2=get_jam2,
                                    dasar_pertimbangan1=dasar_pertimbangan1,
                                    dasar_pertimbangan2=dasar_pertimbangan2,
                                    text_rendah=text_rendah,
                                    text_sedang=text_sedang,
                                    text_tinggi=text_tinggi,
                                    text_sangattinggi=text_sangattinggi,
                                    image_1=image_1,
                                    image_2=image_2,
                                    kesimpulan=kesimpulan,
                                    user1=user1
                                        )
        bio = io.BytesIO()
        docs.save(bio)
        st.download_button(
            label="Download file",
            data=bio.getvalue(),
            file_name=f'EvaluasiMar-{get_tanggal1.strftime("%Y%m%d")}.docx',
            mime='docx'
        )
    except:
        pass
