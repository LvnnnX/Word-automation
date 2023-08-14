from library import *
import process
import UI

translate_hari = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu',
    'Sunday': 'Minggu'
}

translate_shift = {
    'Pagi' : '08.00 - 14.00 WITA',
    'Siang' : '14.00 - 20.30 WITA',
    'Malam' : '20.30 - 08.00 WITA'
}

user = [
    'Diana Hikmah, S.Tr',
    'Kd.Diana Anggariati.SP',
    'I Wayan Wirata, S.Tr',
    'Ni Wayan Budhi Aggraeni, ST.',
    'Kadek Setiya Wati, S.Tr',
    'I Gusti Ayu Putu Putri Astiduari, S.Tr',
]

translate_bulan = {
    '01' : 'Januari',
    '02' : 'Februari',
    '03' : 'Maret',
    '04' : 'April',
    '05' : 'Mei',
    '06' : 'Juni',
    '07' : 'Juli',
    '08' : 'Agustus',
    '09' : 'September',
    '10' : 'Oktober',
    '11' : 'November',
    '12' : 'Desember'
}

st.markdown(
    """
<style>
[data-testid^="stAppViewContainer"]{
    background-color=black;

}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
[data-testid^="stFormSubmitButton"] > button:first-child {
    background-color: transparent;
    text-align: center;
    margin: 10;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
[data-testid^="stFormSubmitButton"]:hover > button:first-child {
    border-color: green;
}

[class^="st-b"]  {
    color: white;
}
[data-testid^="stMarkdownContainer"]{
    background-color: transparent;
    size: 20px;
    color: white;
    weight: bold;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

[class^="main css-k1vhr4 egzxvld3"]{
    background-color:#0e1117;
}

</style>
""",
    unsafe_allow_html=True,
)

all_shift = ['Pagi', 'Siang', 'Malam']

def get_current_shift(jam_sekarang, shifts=translate_shift):
    shift_pagistart = translate_shift['Pagi'].split('-')[0].replace('.',':') + ':00'
    shift_siangstart = translate_shift['Siang'].split('-')[0].replace('.',':') + ':00'
    shift_malamstart = translate_shift['Malam'].split('-')[0].replace('.',':') + ':00'
    if(jam_sekarang >= shift_pagistart and jam_sekarang <= shift_siangstart):
        return 'Pagi'
    elif(jam_sekarang >= shift_siangstart and jam_sekarang <= shift_malamstart):
        return 'Siang'
    else:
        return 'Malam'

form_status = {
    'form1' : False,
    'form2' : False,
    'form3' : False,
    'form4' : False,
    'form5' : False
}

def change_form_status(num_form:int, status:bool):
    global form_status
    form_status[f'form{num_form}'] = status



if __name__ == '__main__':
    with st.form(key='data-form', clear_on_submit=False):
        # TODO 1 : Waktu pelaksanaan
        # st.write('### Waktu Pelaksanaan')
        tanggal_sekarang = datetime.now()
        jam_sekarang = datetime.now().strftime("%H:%M:%S")
        shift_sekarang = get_current_shift(jam_sekarang)

        st.markdown(f"<h3 style='text-align:center;font-weight:bold;'>Waktu Pelaksanaan<h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap='large')
        

        # col1.markdown("<p style='padding-bottom:-10px;font-weight:bold;padding-left:5px;'>Tanggal<p>", unsafe_allow_html=True)

        get_tanggal = col1.date_input(label='Tanggal',key="Tanggal-full", help='Tanggal hari ini adalah tanggal berapa?', value=tanggal_sekarang)

        get_hari = col2.text_input("Hari (otomatis terganti)", value=translate_hari[get_tanggal.strftime("%A")], key='Hari-sekarang', help='Hari ini adalah hari apa?', disabled=True)

        get_shift = col1.selectbox("Shift", options=all_shift, key='Shift-sekarang', help='Shift apa yang sedang berjalan?', index=all_shift.index(shift_sekarang))

        get_jamkerja = col2.text_input("Jam Kerja (otomatis terganti)", value=translate_shift[get_shift], key='Jam-kerja', help="Jam kerja yang sedang berjalan", disabled=True)

        form1_submitbutton = st.form_submit_button(label='Check', on_click=change_form_status(1, True))
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk mengubah Hari dan Jam Kerja</p>", unsafe_allow_html=True)
    if form_status['form1']:
        st.success(f'Berhasil mengubah Hari dan Shift menjadi {get_hari} {get_shift.lower()}')
    

    with st.form(key='data-form2', clear_on_submit=False):
        # TODO 2 : Data tabel
        # st.write('### Kondisi Peralatan Pendukung Operasional')
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Kondisi Peralatan Pendukung Operasional<h3>", unsafe_allow_html=True)
        col3, col4 = st.columns(2, gap='large')

        options = ['Baik', 'Rusak']
        #kondisi telepon
        telepon_status = col3.radio('Telepon', options=options, key='Telepon-status', help='Bagaimakah kondisi telepon?', horizontal=True)

        #kondisi handphone
        handphone_status = col3.radio('Handphone Operasional', options=options, key='Handphone-status', help='Bagaimakah kondisi handphone operasional?', horizontal=True)

        #kondisi Kamera DSLR
        kamera_status = col3.radio('Kamera DSLR', options=options, key='Kamera-status', help='Bagaimakah kondisi kamera DSLR?', horizontal=True)

        #kondisi Video Kamera
        video_kamera_status = col3.radio('Video Kamera', options=options, key='Video-kamera-status', help='Bagaimakah kondisi video kamera?', horizontal=True)

        #kondisi Laptop P.Jasa 1
        laptop_pj1_status = col3.radio('Laptop P.Jasa 1', options=options, key='Laptop-pj1-status', help='Bagaimakah kondisi laptop P.Jasa 1?', horizontal=True)

        #kondisi Laptop P.Jasa 2
        laptop_pj2_status = col3.radio('Laptop P.Jasa 2', options=options, key='Laptop-pj2-status', help='Bagaimakah kondisi laptop P.Jasa 2?', horizontal=True)

        #kondisi Wide Screen
        widescreen_status = col3.radio('Wide Screen', options=options, key='Widescreen-status', help='Bagaimakah kondisi wide screen?', horizontal=True)

        #kondisi Komputer Meteo Factory (1 set)
        komputer_meteo_status = col4.radio('Komputer Meteo Factory (1 set)', options=options, key='Komputer-meteo-status', help='Bagaimakah kondisi komputer meteo factory?', horizontal=True)

        #kondisi Synergie 1
        synergie1_status = col4.radio('Synergie 1', options=options, key='Synergie1-status', help='Bagaimakah kondisi synergie 1?', horizontal=True)

        #kondisi Synergie 2
        synergie2_status = col4.radio('Synergie 2', options=options, key='Synergie2-status', help='Bagaimakah kondisi synergie 2?', horizontal=True)

        #kondisi Synergie 3
        synergie3_status = col4.radio('Synergie 3', options=options, key='Synergie3-status', help='Bagaimakah kondisi synergie 3?', horizontal=True)

        #kondisi Server DMAS
        server_dmas_status = col4.radio('Server DMAS', options=options, key='Server-dmas-status', help='Bagaimakah kondisi server DMAS?', horizontal=True)

        #kondisi Server Produk Forecast*
        server_produk_status = col4.radio('Server Produk Forecast', options=options, key='Server-produk-status', help='Bagaimakah kondisi server produk forecast?', horizontal=True)

        form2_submitbutton = st.form_submit_button(label='Check', on_click=change_form_status(2, True))
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk mengubah kondisi peralatan pendukung operasional</p>", unsafe_allow_html=True)
    if form_status['form2']:
        st.success('Berhasil mengubah kondisi peralatan pendukung operasional')

    with st.form(key='data-form3', clear_on_submit=False):
        user1 = st.selectbox('Dibuat oleh', options=user, key='User', help='Siapa yang sedang bertugas?')

        notes1 = st.text_area('Catatan dan informasi penting', key='Catatan', help='Tuliskan catatan dan informasi penting disini', value='')
        
        form3_submitbutton = st.form_submit_button(label='Check', on_click=change_form_status(3, True))
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk mengubah nama pembuat</p>", unsafe_allow_html=True)
    if form_status['form3']:
        if(len(notes1) != 0):
            st.success(f'Berhasil mengubah nama pembuat menjadi {user1} dengan catatan {notes1[0:32]} {"..." if len(notes1) > 32 else ""}')
        else:
            st.success(f'Berhasil mengubah nama pembuat menjadi {user1} tanpa catatan')

    with st.form(key='data-form4', clear_on_submit=False):
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Kondisi Peralatan Operasional<h3>", unsafe_allow_html=True)
        col3, col4 = st.columns(2, gap='large')

        #kondisi Komputer Kerja 1
        komputer_kerja1_status = col3.radio('Komputer Kerja 1', options=options, key='Komputer-kerja1-status', help='Bagaimakah kondisi komputer kerja 1?', horizontal=True)

        #kondisi Komputer Kerja 2
        komputer_kerja2_status = col3.radio('Komputer Kerja 2', options=options, key='Komputer-kerja2-status', help='Bagaimakah kondisi komputer kerja 2?', horizontal=True)

        #kondisi Client Radar 1
        client_radar1_status = col3.radio('Client Radar 1', options=options, key='Client-radar1-status', help='Bagaimakah kondisi client radar 1?', horizontal=True)

        #kondisi Client Radar 2
        client_radar2_status = col3.radio('Client Radar 2', options=options, key='Client-radar2-status', help='Bagaimakah kondisi client radar 2?', horizontal=True)

        #kondisi Komputer Kerja 3 (FCT)
        komputer_kerja3fct_status = col3.radio('Komputer Kerja 3 (FCT)', options=options, key='Komputer-kerja3-status', help='Bagaimakah kondisi komputer kerja 3 (FCT)?', horizontal=True)

        #kondisi Komputer Kerja 3 (NDF)
        komputer_kerja3ndf_status = col3.radio('Komputer Kerja 3 (NDF)', options=options, key='Komputer-kerja3ndf-status', help='Bagaimakah kondisi komputer kerja 3 (NDF)?', horizontal=True)

        #kondisi Komputer Kerja 3 (WFH)
        komputer_kerja3wfh_status = col3.radio('Komputer Kerja 3 (WFH)', options=options, key='Komputer-kerja3wfh-status', help='Bagaimakah kondisi komputer kerja 3 (WFH)?', horizontal=True)

        #kondisi Komputer kerja 6
        komputer_kerja6_status = col4.radio('Komputer Kerja 6', options=options, key='Komputer-kerja6-status', help='Bagaimakah kondisi komputer kerja 6?', horizontal=True)

        #kondisi Komputer kerja 7
        komputer_kerja7_status = col4.radio('Komputer Kerja 7', options=options, key='Komputer-kerja7-status', help='Bagaimakah kondisi komputer kerja 7?', horizontal=True)

        #kondisi Visumet
        visumet_status = col4.radio('Visumet', options=options, key='Visumet-status', help='Bagaimakah kondisi visumet?', horizontal=True)

        #kondisi Display Info Pelabuhan
        display_info_pelabuhan_status = col4.radio('Display Info Pelabuhan', options=options, key='Display-info-pelabuhan-status', help='Bagaimakah kondisi display info pelabuhan?', horizontal=True)

        #kondisi Printer 1 (Epson L4150)
        printer1_status = col4.radio('Printer 1 (Epson L4150)', options=options, key='Printer1-status', help='Bagaimakah kondisi printer 1 (Epson L4150)?', horizontal=True)

        #kondisi Printer 2 (HP M402dn)
        printer2_status = col4.radio('Printer 2 (HP M402dn)', options=options, key='Printer2-status', help='Bagaimakah kondisi printer 2 (HP M402dn)?', horizontal=True)

        form4_submitbutton = st.form_submit_button(label='Check', on_click=change_form_status(4, True))
    if form_status['form4']:
        st.success('Berhasil mengubah kondisi peralatan operasional')
        
    with st.form(key='data-form5', clear_on_submit=False):
        user2 = st.selectbox('Dibuat oleh', options=user, key='User2', help='Siapa yang sedang bertugas?')

        notes2 = st.text_area('Catatan dan informasi penting', key='Catatan2', help='Tuliskan catatan dan informasi penting disini', value='')
        
        form5_submitbutton = st.form_submit_button(label='Check', on_click=change_form_status(5, True))
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk mengubah nama pembuat</p>", unsafe_allow_html=True)
    if form_status['form5']:
        if(len(notes2) != 0):
            st.success(f'Berhasil mengubah nama pembuat menjadi {user2} dengan catatan {notes2[0:32]} {"..." if len(notes2) > 32 else ""}')
        else:
            st.success(f'Berhasil mengubah nama pembuat menjadi {user2} tanpa catatan')

    template_docs = process.get_docs('data1.docx')
    context = {}

    #Tanggal
    tanggal = get_tanggal.strftime("%d %m %Y")
    tanggal = tanggal.split(' ')
    tanggal[1] = translate_bulan[tanggal[1]]
    tanggal = ' '.join(tanggal)
    context['datetime'] = tanggal

    #Hari
    context['date'] = get_hari

    #Jam Kerja
    context['hour'] = get_jamkerja

    #Shift
    context['shift'] = get_shift

    #Table1
    def make_table(num_rows:int, variables:list[str], context:dict):
        for rows, status in enumerate(variables):
            if(status == 'Baik'):
                context[f't{num_rows}{rows+1}'] = '√'
                context[f't{num_rows+1}{rows+1}'] = ''
            else:
                context[f't{num_rows}{rows+1}'] = ''
                context[f't{num_rows+1}{rows+1}'] = '√'
        return context
    
    #Peralatan Umum Table 1
    context = make_table(num_rows=1, variables=[telepon_status, handphone_status, kamera_status, video_kamera_status, laptop_pj1_status, laptop_pj2_status, widescreen_status], context=context)

    #Peralatan Operasional Table 1
    context = make_table(num_rows=3, variables=[komputer_meteo_status, synergie1_status, synergie2_status, synergie3_status, server_dmas_status, server_produk_status], context=context)

    #User1
    context['user1'] = user1

    #NIP user1
    context['user1nip'] = 'default'

    #TTD user1
    context['user1ttd'] = 'default'

    #Catatan
    context['notes1'] = ''

    #Peralatan Umum Table 2
    context = make_table(num_rows=5, variables=[komputer_kerja1_status, komputer_kerja2_status, client_radar1_status, client_radar2_status, komputer_kerja3fct_status, komputer_kerja3ndf_status, komputer_kerja3wfh_status], context=context)

    #Peralatan Operasional Table 2
    context = make_table(num_rows=7, variables=[komputer_kerja6_status, komputer_kerja7_status, visumet_status, display_info_pelabuhan_status, printer1_status, printer2_status], context=context)

    #User2
    context['user2'] = user2

    #NIP user2
    context['user2nip'] = 'default'

    #TTD user2
    context['user2ttd'] = 'default'

    #Catatan
    context['notes2'] = ''

    template_docs.render(context=context)

    bio = io.BytesIO()
    template_docs.save(bio)
    st.download_button(
        label="Download file",
        data=bio.getvalue(),
        file_name=f'CekAlat-{get_tanggal.strftime("%Y%m%d")}.docx',
        mime='docx'
    )

        
