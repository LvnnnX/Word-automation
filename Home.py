from process import *
import home.CekAlat as CekAlat
import home.EvaluasiCuacaMaritim as EvaluasiCuacaMaritim
import home.EvaluasiPub as EvaluasiPub
import home.Internet as Internet
import home.Maritim as Maritim
import home.Radar as Radar
import home.Radio as Radio
import home.Website as Website
import home.Satelit as Satelit

if __name__ == '__main__':
    header()
    with st.sidebar:

        selected = option_menu(
            menu_title= None,
            options=['Cek Alat','Evaluasi Cuaca Maritim','Evaluasi Kondisi Cuaca','Internet','Maritim','Radar','Satelit','Radio','Website'],
            icons=['house-gear','cloud-fog2','clouds','wifi','water','broadcast','globe-asia-australia','music-player','globe'],
            menu_icon='cast',
            default_index=0,
            orientation='vertical',
            )
    
if selected == 'Cek Alat':
    CekAlat.start_cek_alat()
elif selected == 'Evaluasi Cuaca Maritim':
    EvaluasiCuacaMaritim.start_evaluasi_cuaca_maritim()
elif selected == 'Evaluasi Kondisi Cuaca':
    EvaluasiPub.start_evaluasi_pub()
elif selected == 'Internet':
    Internet.start_internet()
elif selected == 'Maritim':
    Maritim.start_maritim()
elif selected == 'Radar':
    Radar.start_radar()
elif selected == 'Satelit':
    Satelit.start_satelit()
elif selected == 'Radio':
    Radio.start_radio()
elif selected == 'Website':
    Website.start_website()
    
   
        
