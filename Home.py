from library import *
from process import *

if __name__ == '__main__':
    clear_background()
    with st.form(key='data-form', clear_on_submit=False):
        # TODO 1 : Waktu pelaksanaan
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
    

    with st.form(key='data-form2', clear_on_submit=False):
        # TODO 2 : Data tabel 1
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Kondisi Peralatan Pendukung Operasional<h3>", unsafe_allow_html=True)
        col3, col4 = st.columns(2, gap='large')

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

        user1 = st.selectbox('Dibuat oleh', options=user, key='User', help='Siapa yang sedang bertugas?')

        notes1 = st.text_area('Catatan dan informasi penting', key='Catatan', help='Tuliskan catatan dan informasi penting disini', value='')
        
        # TODO 3 : Data tabel 2
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
        komputer_kerja3wfh_status = col3.radio('Komputer Kerja 3 (WFH)', options=options, key='Komputer-kerja3wfh-status', help='Bagaimakah kondisi komputer kerja 3 (WFH)?', horizontal=True, index=2)

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

        user2 = st.selectbox('Dibuat oleh', options=user, key='User2', help='Siapa yang sedang bertugas?')

        notes2 = st.text_area('Catatan dan informasi penting', key='Catatan2', help='Tuliskan catatan dan informasi penting disini', value='')
        
        form2_submitbutton = st.form_submit_button(label='Check')
        st.markdown("<p style='font-size:10px'>*Klik tombol 'Check' untuk menyimpan perubahan</p>", unsafe_allow_html=True)

    if form2_submitbutton:
        st.markdown("<h3 style='text-align:center;font-weight:bold;'>Previews<h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap='large')
        
        col1.text_input("Pembuat pertama", value=user1, disabled=True)
        col1.text_area("Catatan", value=notes1, disabled=True)
        
        col2.text_input("Pembuat kedua", value=user2, disabled=True)
        col2.text_area("Catatan", value=notes2, disabled=True)
        
        # if(len(notes2) != 0):
        #     st.success(f'Berhasil mengubah nama pembuat menjadi **:blue[{user2}]** dengan catatan {notes2[0:32]} {"..." if len(notes2) > 32 else ""}')
        # else:
        #     st.success(f'Berhasil mengubah nama pembuat menjadi **:blue[{user2}]** tanpa catatan')

    try:
        docs = change_docx(get_tanggal=get_tanggal,                         
                           get_hari=get_hari,                         
                           get_shift=get_shift,                         get_jamkerja=get_jamkerja,                         telepon_status=telepon_status,                         handphone_status=handphone_status,                         kamera_status=kamera_status,                         video_kamera_status=video_kamera_status,                            laptop_pj1_status=laptop_pj1_status,                            laptop_pj2_status=laptop_pj2_status,                            widescreen_status=widescreen_status,                            komputer_meteo_status=komputer_meteo_status,        synergie1_status=synergie1_status,  
                           synergie2_status=synergie2_status,  
                           synergie3_status=synergie3_status,  
                           server_dmas_status=server_dmas_status,  server_produk_status=server_produk_status,  
                           user1=user1,    
                           notes1=notes1,  
                           komputer_kerja1_status=komputer_kerja1_status,
                           komputer_kerja2_status=komputer_kerja2_status,
                           client_radar1_status=client_radar1_status,
                           client_radar2_status=client_radar2_status,
                           komputer_kerja3fct_status=komputer_kerja3fct_status,
                           komputer_kerja3ndf_status=komputer_kerja3ndf_status,
                           komputer_kerja3wfh_status=komputer_kerja3wfh_status,
                           komputer_kerja6_status=komputer_kerja6_status,
                           komputer_kerja7_status=komputer_kerja7_status,
                           visumet_status=visumet_status,
                           display_info_pelabuhan_status=display_info_pelabuhan_status,
                           printer1_status=printer1_status,
                           printer2_status=printer2_status,
                           user2=user2,
                           notes2=notes2) 
        
        bio = io.BytesIO()
        docs.save(bio)
        st.download_button(
            label="Download file",
            data=bio.getvalue(),
            file_name=f'CekAlat-{get_tanggal.strftime("%Y%m%d")}-{get_shift[0].upper()}.docx',
            mime='docx'
        )
    except FileNotFoundError:
        st.error('Ada file TTD yang tidak ditemukan!')

   
        
