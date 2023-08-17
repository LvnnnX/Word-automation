from process import *
import CekAlat
import EvaluasiCuacaMaritim
import EvaluasiPub
import Internet
import Maritim

if __name__ == '__main__':
    with st.sidebar:
        selected = option_menu(
            menu_title= None,
            options=['Cek Alat','Evaluasi Cuaca Maritim','Evaluasi Kondisi Cuaca','Internet','Maritim'],
            icons=['house-gear','cloud-fog2','clouds','wifi','water'],
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
   
        
