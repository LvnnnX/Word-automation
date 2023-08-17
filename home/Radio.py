from process import *

def start_radio():
    clear_background()
    list_media = get_media()
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
    
    with st.form(key='many-form',clear_on_submit=False):
        st.markdown("<h3 style='text-align:center;font-weight:bold;padding-bottom:0px;'>Berapa banyak Media yang telah dilayani?<h3>", unsafe_allow_html=True)
        num_media = st.number_input(label='Berapa banyak Media yang telah dilayani?', key='jumlah-media', min_value=1, value=3, max_value=5, label_visibility='collapsed')
        many_button = st.form_submit_button(label='OK')
        
        
    with st.form(key='radio-form',clear_on_submit=False):
        st.markdown("<h2 style='text-align:center;font-weight:bold;padding-bottom:0px;'>Narasi Live Radio RRI<h2>", unsafe_allow_html=True)
        all_media = ['' for _ in range(num_media)]
        all_jam = ['' for _ in range(num_media)]
        for x in range(num_media):
            col1, col2 = st.columns([2,1], gap='medium')
            all_media[x] = col1.selectbox(label=f'Media {x+1}', options=list_media, key=f'media-{x}', index=(x%len(list_media)))
            all_jam[x] = col2.time_input('Jam Layanan', key=f'jam-{x}',value=jam_sekarang)
            
            
        st.markdown("<h3 style='text-align:center;font-weight:bold;padding-bottom:0px;'>Narasi<h3>", unsafe_allow_html=True)
        
        judul = st.text_input('Judul Narasi', key='judul', value='Pagi > Cuaca Wilayah Bali')
        st.text_input(label='',value='Contoh Judul Narasi : Pagi > Cuaca Wilayah Bali', label_visibility='collapsed',disabled=True)
        
        isi = st.text_area(label='Isi Narasi', value='', key='isi')
        
        st.markdown("<p style='text-align:left;'><font color='red'>Waspada</font><p>", unsafe_allow_html=True)
        waspada = st.text_area(label='Waspada', value='', key='waspada',label_visibility='collapsed')
        
        user = st.selectbox('Dibuat Oleh', options=user, key='user')
        
        button = st.form_submit_button(label='Submit')
    
    if(button):
        try:
            template_docs =  get_docs('template-radio.docx')
            context = {}
            
            #Tanggal
            context['date'] = change_tanggal(get_tanggal)
            
            #Hari
            context['hari'] = get_hari
            
            #Jam Kerja
            context['jamkerja'] = get_jamkerja
            
            #Shift
            context['shift'] = get_shift
            
            #User
            context['user'] = user
            try:
                _user = user.split(',')[0]
            except:
                _user = user
            
            context['user_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_file[user.index(user)])}"))
            
            context['user_nip'] = user_nip[user.index(user)].replace('\'','')
            
            media = []
            for x in range(num_media):
                media.append({'place':all_media[x],'jam':all_jam[x].strftime("%H.%M"), 'user':_user})
            
            context['table'] = media
            
            #Judul
            context['judul'] = judul
            
            #isi
            context['isi'] = isi
            
            #waspada
            context['waspada'] = waspada
            
            template_docs.render(context=context)
            st.success('Data tersimpan, silahkan download file')
            
            bio = io.BytesIO()
            template_docs.save(bio)
            st.download_button(
                    label="Download file",
                    data=bio.getvalue(),
                    file_name=f'Radio-{get_tanggal.strftime("%Y%m%d")}-{get_shift[0].upper()}.docx',
                    mime='docx'
                )
        except:
            st.error('Lengkapi data terlebih dahulu!')