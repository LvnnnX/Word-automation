from process import *

def start_website():
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
        
    with st.form(key='website-form', clear_on_submit=False):
        st.markdown("<h3 style='text-align:center;font-weight:bold;padding-bottom:0px;'>Penyajian data melalui Website<h3>", unsafe_allow_html=True)
        
        publik = st.file_uploader('Gambar Prakiraan Cuaca Publik', type=['png','jpg','jpeg'], key='prakiraan-cuaca-publik', accept_multiple_files=False)
        
        user1 = st.selectbox('Dibuat Oleh', options=user, key='user1')
        
        st.markdown('---')
        
        maritim = st.file_uploader('Gambar Prakiraan Cuaca Maritim', type=['png','jpg','jpeg'], key='prakiraan-cuaca-maritim', accept_multiple_files=False)
        
        user2 = st.selectbox('Dibuat Oleh', options=user, key='user2')
        
        button = st.form_submit_button(label='Submit')
        
    if(button):
        try:
            template_docs = get_docs('template-website.docx')
            context = {}
            
            #Tanggal
            context['date'] = change_tanggal(get_tanggal)
            
            #Publik
            context['publik_img'] = InlineImage(template_docs, publik, height=Mm(150), width=Mm(137.4))
            
            #User1
            context['user1'] = user1
            context['user1_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_file[user.index(user1)])}"))
            context['user1_nip'] = user_nip[user.index(user1)].replace('\'','')
            
            #Maritim
            context['maritim_img'] = InlineImage(template_docs, maritim, height=Mm(150), width=Mm(137.4))
            
            #User2
            context['user2'] = user2
            context['user2_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_file[user.index(user2)])}"))
            context['user2_nip'] = user_nip[user.index(user2)].replace('\'','')
            
            template_docs.render(context=context)
            st.success('Data tersimpan, silahkan download file')
            
            bio = io.BytesIO()
            template_docs.save(bio)
            st.download_button(
                    label="Download file",
                    data=bio.getvalue(),
                    file_name=f'Website-{get_tanggal.strftime("%Y%m%d")}-{get_shift[0].upper()}.docx',
                    mime='docx'
                )
        
        except:
            st.error('Lengkapi data terlebih dahulu!')