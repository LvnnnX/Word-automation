from process import *

def start_internet():
    clear_background()
    with st.form(key='internet-shift-form',clear_on_submit=False):
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
        
    with st.form(key='internet-form', clear_on_submit=False):
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Prakiraan Cuaca Publik<h3>", unsafe_allow_html=True)
        publik1 = st.file_uploader('Penyebaran data internet (Email)', type=['png','jpg','jpeg'], key='penyebaran-data-inet1', accept_multiple_files=False)
        
        col1, col2 = st.columns(2, gap='small')
        
        publik2 = col1.file_uploader('Penyebaran data internet (Media Sosial telegram)', type=['png','jpg','jpeg'], key='penyebaran-data-inet2', accept_multiple_files=False)
        
        publik3 = col2.file_uploader('Penyebaran data internet (Media Sosial instagram)', type=['png','jpg','jpeg'], key='penyebaran-data-inet3', accept_multiple_files=False)
        
        user1 = st.selectbox('Dibuat Oleh', options=user, key='user1')
        
        st.markdown('---')
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Prakiraan Cuaca Maritim<h3>", unsafe_allow_html=True)
        
        maritim1 = st.file_uploader('Penyebaran data internet (Email)', type=['png','jpg','jpeg'], key='penyebaran-data-inet4', accept_multiple_files=False)
        
        col1, col2 = st.columns(2, gap='small')
        
        maritim2 = col1.file_uploader('Penyebaran data internet (Media Sosial telegram)', type=['png','jpg','jpeg'], key='penyebaran-data-inet5', accept_multiple_files=False)
        
        maritim3 = col2.file_uploader('Penyebaran data internet (Media Sosial instagram)', type=['png','jpg','jpeg'], key='penyebaran-data-inet6', accept_multiple_files=False)
        
        user2 = st.selectbox('Dibuat Oleh', options=user, key='user2')
        
        button1 = st.form_submit_button(label='Submit')
    
    if(button1):
        template_docs = get_docs('template-internet.docx')
        context = {}
        
        #Tanggal
        context['date'] = change_tanggal(get_tanggal)
        
        #Publik
        context['publik1'] = InlineImage(template_docs, publik1, width=Mm(161), height=Mm(83.5))
        
        context['publik2'] = InlineImage(template_docs, publik2, width=Mm(81.2), height=Mm(52.8))
        
        context['publik3'] = InlineImage(template_docs, publik3, width=Mm(81.2), height=Mm(52.8))
        
        #User1
        context['user1'] = user1
        
        context['user1_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_file[user.index(user1)])}"))
        
        context['user1_nip'] = user_nip[user.index(user1)].replace('\'','')
                
        #Maritim
        
        context['maritim1'] = InlineImage(template_docs, maritim1, width=Mm(161), height=Mm(83.5))
        
        context['maritim2'] = InlineImage(template_docs, maritim2, width=Mm(81.2), height=Mm(52.8))
        
        context['maritim3'] = InlineImage(template_docs, maritim3, width=Mm(81.2), height=Mm(52.8))
        
        #User2
        context['user2'] = user2
        
        context['user2_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_file[user.index(user2)])}"))
        
        context['user2_nip'] = user_nip[user.index(user2)].replace('\'','')
        
        template_docs.render(context=context)
        
        bio = io.BytesIO()
        template_docs.save(bio)
        st.download_button(
                label="Download file",
                data=bio.getvalue(),
                file_name=f'Internet-{get_tanggal.strftime("%Y%m%d")}-{get_shift[0].upper()}.docx',
                mime='docx'
            )