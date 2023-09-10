from library import *
from process import *
import sys
sys.path.insert(0,'pages/options')
import addpegawai as agw
import showpegawai as sgw
import editpegawai as egw
import hapuspegawai as hgw

if __name__ == '__main__':
    header()
    with st.sidebar:
        selected = option_menu(
            menu_title= None,
            options=['Pegawai','Add Pegawai','Edit Pegawai','Hapus Pegawai'],
            icons=['list-columns','person-add','person-fill-gear','person-dash-fill'],
            menu_icon='cast',
            default_index=0,
            orientation='vertical',
            
        )
    
if selected == 'Pegawai':
    sgw.options()
elif selected == 'Add Pegawai':
    agw.show_pegawai_menu()
elif selected == 'Edit Pegawai':
    egw.show_edit_menu()
elif selected == 'Hapus Pegawai':
    hgw.show_hapus_menu()
        
