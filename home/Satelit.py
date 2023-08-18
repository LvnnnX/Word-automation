from process import *

def start_satelit():
    clear_background()
    with st.form(key='shift-form', clear_on_submit=False):
        user,user_file,user_nip = get_pegawai()
        
        tanggal_sekarang, jam_sekarang, shift_sekarang = get_jadwal_sekarang()

        st.markdown(f"<h3 style='text-align:center;font-weight:bold;'>Waktu Pelaksanaan<h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap='large')

        get_tanggal = col1.date_input(label='Tanggal',key="Tanggal-full", help='Tanggal hari ini adalah tanggal berapa?', value=tanggal_sekarang)

        get_hari = col2.text_input("Hari (otomatis terganti)", value=translate_hari[get_tanggal.strftime("%A")], key='Hari-sekarang', help='Hari ini adalah hari apa?', disabled=True)

        get_shift = col1.selectbox("Shift", options=all_shift, key='Shift-sekarang', help='Shift apa yang sedang berjalan?', index=all_shift.index(shift_sekarang))

        get_jamkerja = col2.text_input("Jam Kerja (otomatis terganti)", value=translate_shift[get_shift], key='Jam-kerja', help="Jam kerja yang sedang berjalan", disabled=True)

        form1_submitbutton = st.form_submit_button(label='Check')
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk mengubah Hari dan Jam Kerja</p>", unsafe_allow_html=True)
    if form1_submitbutton:
        st.success(f'Berhasil mengubah Hari dan Shift menjadi **:blue[{get_hari} {get_shift.lower()}]**')
        
    with st.form(key='maritim-form', clear_on_submit=False):
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Penginderaan Jarak Jauh<h3>", unsafe_allow_html=True)
        
        
        
        awan = st.text_area(label='Dari interpretasi citra satelit cuaca Himawari-8, menunjukkan bahwa awan yang terbentuk di wilayah Bali adalah ', value='', key='awan')
        
        col1,col2,col3 = st.columns([2,1,2], gap='small')        
        suhu1 = col1.text_input(label='Suhu puncak awan teramati berkisar antara', value='', key='selatlombok')
        col2.text_input(label='',value='hingga',label_visibility='hidden',disabled=True)
        suhu2 = col3.text_input(label='',value='',label_visibility='hidden',disabled=False)
        
        col1.markdown("<p style='font-size:10px'>Contoh pengisian : +60</p>", unsafe_allow_html=True)
        col3.markdown("<p style='font-size:10px'>Contoh pengisian : -60</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Gambar HF Radar Maritim<h3>", unsafe_allow_html=True)
        
        _jam1 = get_jamkerja.split('-')[0] + 'WITA'
        _jam2 = int(_jam1[0:2]) + 3
        if(_jam2>=24): _jam2 %= 24
        _jam3 = _jam2 + 3
        if(_jam3>=24):_jam3 %= 24
        _jam2 = f'{_jam2:02.0f}' + '.00 WITA'
        _jam3 = f'{_jam3:02.0f}' + '.00 WITA'
        
        col1, col2 = st.columns(2, gap='small')
        cs1 = col1.file_uploader(f'Selat Bali pukul {_jam1}', type=['png','jpg','jpeg'], key='selatbali1', accept_multiple_files=False)
        
        cl1 = col2.file_uploader(f'Selat Lombok pukul {_jam1}', type=['png','jpg','jpeg'], key='selatlombok1', accept_multiple_files=False)
        
        col1, col2 = st.columns(2, gap='small')
        cs2 = col1.file_uploader(f'Selat Bali pukul {_jam2}', type=['png','jpg','jpeg'], key='selatbali2', accept_multiple_files=False)
        
        cl2 = col2.file_uploader(f'Selat Lombok pukul {_jam2}', type=['png','jpg','jpeg'], key='selatlombok2', accept_multiple_files=False)
        
        col1, col2 = st.columns(2, gap='small')
        cs3 = col1.file_uploader(f'Selat Bali pukul {_jam3}', type=['png','jpg','jpeg'], key='selatbali3', accept_multiple_files=False)
        
        cl3 = col2.file_uploader(f'Selat Lombok pukul {_jam3}', type=['png','jpg','jpeg'], key='selatlombok3', accept_multiple_files=False)
        
        st.markdown("<p style='font-size:10px'>*Gambar wajib diisi agar file dapat di Download</p>", unsafe_allow_html=True)
        
        user1 = st.selectbox(label='Dibuah Oleh', options=user, key='user1')
        
        button = st.form_submit_button('Submit')
        
    if(button):
        try:
            template_docs = get_docs('template-satelit.docx')
            context = {}
            
            #Tanggal
            context['date'] = change_tanggal(get_tanggal)
            
            #Shift
            context['shift'] = get_jamkerja
            
            #Awan
            context['awan'] = awan
            
            #suhu
            context['suhu1'] = suhu1
            context['suhu2'] = suhu2
            
            context['cs1'] = InlineImage(template_docs, cs1, width=Mm(52.7),height=Mm(44.2))
            context['cl1'] = InlineImage(template_docs, cl1, width=Mm(52.7),height=Mm(44.2))
            context['cs2'] = InlineImage(template_docs, cs2, width=Mm(52.7),height=Mm(44.2))
            context['cl2'] = InlineImage(template_docs, cl2, width=Mm(52.7),height=Mm(44.2))
            context['cs3'] = InlineImage(template_docs, cs3, width=Mm(52.7),height=Mm(44.2))
            context['cl3'] = InlineImage(template_docs, cl3, width=Mm(52.7),height=Mm(44.2))
            
            context['jm1'] = _jam1
            context['jm2'] = _jam2
            context['jm3'] = _jam3
            
            #User
            context['user'] = user1
            
            context['user_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f'{find_filename(user_file[user.index(user1)])}'))
                
            context['user_nip'] = user_nip[user.index(user1)].replace('\'','')
            
            template_docs.render(context=context)
            st.success('Data tersimpan, silahkan download file')
            
            bio = io.BytesIO()
            template_docs.save(bio)
            st.download_button(
                    label="Download file",
                    data=bio.getvalue(),
                    file_name=f'Satelit-{get_tanggal.strftime("%Y%m%d")}-{get_shift[0].upper()}.docx',
                    mime='docx'
                )
            
        except:
            st.error('Lengkapi data terlebih dahulu!')