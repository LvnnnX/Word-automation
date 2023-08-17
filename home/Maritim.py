from process import *

def start_maritim():
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
        
        selatbali = st.text_area(label='Dari interpretasi citra HF Radar Maritim, menunjukkan bahwa arus permukaan Selat Bali ', value='', key='selatbali')
        
        selatlombok = st.text_area(label='Arus laut pada Selat Lombok ', value='', key='selatlombok')
        
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Gambar HF Radar Maritim<h3>", unsafe_allow_html=True)
        
        _jam1 = get_jamkerja.split('-')[0] + 'WITA'
        _jam2 = int(_jam1[0:2]) + 3
        if(_jam2>=24): _jam2 %= 24
        _jam3 = _jam2 + 3
        if(_jam3>=24):_jam3 %= 24
        _jam2 = f'{_jam2:02.0f}' + '.00 WITA'
        _jam3 = f'{_jam3:02.0f}' + '.00 WITA'

        
        col1, col2 = st.columns(2, gap='small')
        sb1 = col1.file_uploader(f'Selat Bali pukul {_jam1}', type=['png','jpg','jpeg'], key='selatbali1', accept_multiple_files=False)
        
        sl1 = col2.file_uploader(f'Selat Lombok pukul {_jam1}', type=['png','jpg','jpeg'], key='selatlombok1', accept_multiple_files=False)
        
        sb2 = col1.file_uploader(f'Selat Bali pukul {_jam2}', type=['png','jpg','jpeg'], key='selatbali2', accept_multiple_files=False)
        
        sl2 = col2.file_uploader(f'Selat Lombok pukul {_jam2}', type=['png','jpg','jpeg'], key='selatlombok2', accept_multiple_files=False)
        
        sb3 = col1.file_uploader(f'Selat Bali pukul {_jam3}', type=['png','jpg','jpeg'], key='selatbali3', accept_multiple_files=False)
        
        sl3 = col2.file_uploader(f'Selat Lombok pukul {_jam3}', type=['png','jpg','jpeg'], key='selatlombok3', accept_multiple_files=False)       
        
        st.markdown("<p style='font-size:10px'>*Gambar wajib diisi agar file dapat di Download</p>", unsafe_allow_html=True)
        
        user = st.selectbox('Dibuat Oleh', options=user, key='user')
        
        button = st.form_submit_button(label='Submit')
    if(button):
        try:
            template_docs = get_docs('template-maritim.docx')
            context = {}
            
            #Tanggal
            context['date'] = change_tanggal(get_tanggal)
            
            #Shift
            context['shift'] = get_jamkerja
            
            #Selatbali
            context['selatbali'] = selatbali
            
            #Selatlombok
            context['selatlombok'] = selatlombok
            
            #images
            context['sb1'] = InlineImage(template_docs, sb1, width=Mm(54),height=Mm(31))
            context['sl1'] = InlineImage(template_docs, sl1, width=Mm(54),height=Mm(31))
            context['sb2'] = InlineImage(template_docs, sb2, width=Mm(54),height=Mm(31))
            context['sl2'] = InlineImage(template_docs, sl2, width=Mm(54),height=Mm(31))
            context['sb3'] = InlineImage(template_docs, sb3, width=Mm(54),height=Mm(31))
            context['sl3'] = InlineImage(template_docs, sl3, width=Mm(54),height=Mm(31))
            
            #User
            
            context['user'] = user
            
            context['user_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f'{find_filename(user_file[user.index(user)])}'))
            
            context['user_nip'] = user_nip[user.index(user)].replace('\'','')
            
            template_docs.render(context=context)
            st.success('Data tersimpan, silahkan download file')
            
            bio = io.BytesIO()
            template_docs.save(bio)
            st.download_button(
                    label="Download file",
                    data=bio.getvalue(),
                    file_name=f'Maritim-{get_tanggal.strftime("%Y%m%d")}-{get_shift[0].upper()}.docx',
                    mime='docx'
                )
            
        except:
            st.error('Lengkapi data terlebih dahulu!')