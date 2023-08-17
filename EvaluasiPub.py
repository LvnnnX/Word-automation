from process import *

def start_evaluasi_pub():
    clear_background()
    with st.form(key='data-form', clear_on_submit=False):
        user,user_file,user_nip = get_pegawai()
        
        tanggal_sekarang, jam_sekarang, shift_sekarang = get_jadwal_sekarang()
        tanggal_besok = tanggal_sekarang + timedelta(days=1)
        
        st.markdown(f"<h3 style='text-align:center;font-weight:bold;'>Evaluasi Kondisi Cuaca Wilayah Bali<h3>", unsafe_allow_html=True)
        
        col1,col2,col3,col4,col5 = st.columns(5, gap='small')
        get_tanggal1 = col1.date_input('Tanggal', value=tanggal_sekarang, key='tanggal-awal')
        
        get_jam1 = col2.time_input('Pukul', value=jam_sekarang, key='jam-awal')
        
        col3.text_input('',value='Hingga',key='hingga',disabled=True)
        
        get_tanggal2 = col4.date_input('Tanggal', value=tanggal_besok, key='tanggal-akhir')
        
        get_jam2 = col5.time_input('Pukul', value=jam_sekarang, key='jam-akhir')
        
        st.write('')
        st.markdown("<p style='text-align:left;font-weight:bold;'>Dasar pertimbangan</p>", unsafe_allow_html=True)
        
        col1,col2 = st.columns([1,1],gap='small')
        
        analisa_isobar = col1.text_area('Dari analisa isobar', value='', key='isobar')
        
        isobar_img = col2.file_uploader('', type=['png','jpg','jpeg'], key='isobar-img', accept_multiple_files=False,label_visibility='visible')
        
        col1,col2,col3,col4 = st.columns(4)
        isobar_jam = col1.time_input('Waktu pengambilan gambar Isobar', value=jam_sekarang, key='isobar-jam')
        
        isobar_tgl = col2.date_input('Tanggal pengambilan gambar Isobar', value=tanggal_sekarang, key='isobar-tgl')
        
        col1,col2 = st.columns([1,1],gap='small')
        analisis_streamline = col1.text_area('Dari analisis streamline', value='', key='streamline')
        
        streamline_img = col2.file_uploader('', type=['png','jpg','jpeg'], key='streamline-img', accept_multiple_files=False,label_visibility='visible')
        
        col1,col2,col3,col4 = st.columns(4)
        streamline_jam = col1.time_input('Waktu pengambilan gambar Streamline', value=jam_sekarang, key='streamline-jam')
        
        streamline_date = col2.date_input('Tanggal pengambilan gambar Streamline', value=tanggal_sekarang, key='Streamline-tgl')
        
        col1,col2 = st.columns([1,1],gap='small')
        radar_cuaca = col1.text_area('Dari interpretasi citra radar cuaca ', value='', key='radar')
        
        radar_img = col2.file_uploader('', type=['png','jpg','jpeg'], key='radar-img', accept_multiple_files=False,label_visibility='visible')
        
        col1,col2,col3,col4 = st.columns(4)
        Radar_jam = col1.time_input('Waktu pengambilan gambar Radar', value=jam_sekarang, key='Radar-jam')
        
        Radar_tgl = col2.date_input('Tanggal pengambilan gambar Radar', value=tanggal_sekarang, key='Radar-tgl')
        
        col1,col2 = st.columns([1,1],gap='small')
        satelit = col1.text_area('Dari interpretasi citra satelit Himawari', value='', key='satelit')
        
        satelit_img = col2.file_uploader('', type=['png','jpg','jpeg'], key='satelit-img', accept_multiple_files=False,label_visibility='visible')
        
        col1,col2,col3,col4 = st.columns(4)
        Satelit_jam = col1.time_input('Waktu pengambilan gambar Satelit', value=jam_sekarang, key='Satelit-jam')
        
        Satelit_tgl = col2.date_input('Tanggal pengambilan gambar Satelit', value=tanggal_sekarang, key='Satelit-tgl')
        
        khusus = st.text_area('Cuaca Khusus', value='', key='khusus')
        
        st.write('')
        st.markdown("<p style='text-align:left;font-weight:bold;'>Kesimpulan</p>", unsafe_allow_html=True)
        
        kesimpulan = st.text_area('', value='', key='kesimpulan',label_visibility='collapsed')
        
        user1 = st.selectbox(options=user,label='Dibuat oleh')
        
        button = st.form_submit_button(label='Check')
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk menyimpan perubahan</p>", unsafe_allow_html=True)
        
    if button:
        template_docs = get_docs('template-evaluasipub.docx')
        context = {}
        
        #Tanggal
        context['date1'] = change_tanggal(get_tanggal1)
        
        #Jam1
        context['jam1'] = str(get_jam1)[0:5].replace(':','.')
        
        #Tanggal2
        context['date2'] = change_tanggal(get_tanggal2)
        
        #Jam2
        context['jam2'] = str(get_jam2)[0:5].replace(':','.')
        
        #Dasar pertimbangan
        context['analisa_isobar'] = analisa_isobar
        context['analisis_streamline'] = analisis_streamline
        context['radar_cuaca'] = radar_cuaca
        context['satelit_himawari'] = satelit
        context['khusus'] = khusus
        
        #Images
        context['isobar_img'] = InlineImage(template_docs, isobar_img, height=Mm(40), width=Mm(76))
        context['streamline_img'] = InlineImage(template_docs, streamline_img, height=Mm(40), width=Mm(76))
        context['radar_img'] = InlineImage(template_docs, radar_img, height=Mm(40), width=Mm(76))
        context['satelit_img'] = InlineImage(template_docs, satelit_img, height=Mm(40), width=Mm(76))
        
        #Images Keterangan
        context['isobar_jam'] = str(isobar_jam)[0:5].replace(':','.')
        context['isobar_date'] = change_tanggal(isobar_tgl)
        context['str_jam'] = str(streamline_jam)[0:5].replace(':','.')
        context['str_date'] = change_tanggal(streamline_date)
        context['rdr_jam'] = str(Radar_jam)[0:5].replace(':','.')
        context['rdr_date'] = change_tanggal(Radar_tgl)
        context['stlt_jam'] = str(Satelit_jam)[0:5].replace(':','.')
        context['stlt_date'] = change_tanggal(Satelit_tgl)
            
        #Kesimpulan
        context['kesimpulan'] = kesimpulan
        
        #User
        context['user_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{user_file[user.index(user1)]}.jpg"))
    
        context['user'] = user1
        
        context['user_nip'] = user_nip[user.index(user1)].replace('\'','')
        
        template_docs.render(context=context)

        bio = io.BytesIO()
        template_docs.save(bio)
        st.download_button(
                label="Download file",
                data=bio.getvalue(),
                file_name=f'EvaluasiPub-{get_tanggal1.strftime("%Y%m%d")}.docx',
                mime='docx'
            )