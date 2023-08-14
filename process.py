from library import *
PATH = Path(__file__).parent
ASSETS = PATH / "assets"

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

translate_ttd = {
    'Diana Hikmah, S.Tr' : ['Diana Hikmah', '199202132012102001'],
    'Kd.Diana Anggariati.SP' : ['Diana Anggariati', '196705231990032002'],
    'I Wayan Wirata, S.Tr' : ['I Wayan Wirata','196705231990032002'],
    'Ni Wayan Budhi Aggraeni, ST.' : ['Budhi Aggraeni','197804042008012032'],
    'Kadek Setiya Wati, S.Tr' : ['Kadek Setiya Wati', '198906032010122002'],
    'I Gusti Ayu Putu Putri Astiduari, S.Tr' : ['Putri Astiduari', '199308182013121001'],
    'I Wayan Gita Giriharta. S.Tr.Met' : ['Gita Giriharta', '199604012016011001'],
    'A.A.Putu Eka Putra Wirawan' : ['Eka Putra Wirawan', '198212232006041002'],
    'I Made SudarmaYadnya, S.Si' : ['SudarmaYadnya', '19810322 200701 1 013'],
    'Ni Putu Lia Cahyani' : ['Lia Cahyani', '198503012007012003'],
    'Putu Agus Dedy Permana, S. Tr' : ['Dedy Permana', '199308092013121001'],
    'Wulan Wandarana, S.Tr' : ['Wulan Wandarana', '199505142014112001'],
    'Luh Eka Arisanti, S.Si' : ['Eka Arisanti', '198909272010122001'],
}

user = list(sorted(translate_ttd.keys()))

form_status = {
    'form1' : False,
    'form2' : False,
    'form3' : False,
    'form4' : False,
    'form5' : False
}

all_shift = ['Pagi', 'Siang', 'Malam']

options = ['Baik', 'Rusak', 'Kosong']

def clear_background():
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

def get_docs(docs):
    docs = DocxTemplate(ASSETS / docs)
    return docs


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

def change_form_status(num_form:int, status:bool):
    global form_status
    form_status[f'form{num_form}'] = status

def get_jadwal_sekarang():
    tanggal_sekarang = datetime.now()
    jam_sekarang = datetime.now().strftime("%H:%M:%S")
    shift_sekarang = get_current_shift(jam_sekarang)
    return tanggal_sekarang, jam_sekarang, shift_sekarang


def make_table(num_rows:int, variables:list[int], context:dict, kwargs:dict):
        list_variables = []
        for value in list(kwargs.values())[variables[0]:variables[1]]:
            list_variables.append(value)
        for rows, status in enumerate(list_variables):
            if(status == 'Baik'):
                context[f't{num_rows}{rows+1}'] = '√'
                context[f't{num_rows+1}{rows+1}'] = ''
            elif(status == 'Rusak'):
                context[f't{num_rows}{rows+1}'] = ''
                context[f't{num_rows+1}{rows+1}'] = '√'
            else:
                context[f't{num_rows}{rows+1}'] = ''
                context[f't{num_rows+1}{rows+1}'] = ''
        return context


def change_docx(get_tanggal,**kwargs):
    template_docs = get_docs('data1.docx')
    context = {}

    #Tanggal
    tanggal = get_tanggal.strftime("%d %m %Y")
    tanggal = tanggal.split(' ')
    tanggal[1] = translate_bulan[tanggal[1]]
    tanggal = ' '.join(tanggal)
    context['datetime'] = tanggal

    #Hari
    context['date'] = kwargs['get_hari']

    #Jam Kerja
    context['hour'] = kwargs['get_jamkerja']

    #Shift
    context['shift'] = kwargs['get_shift']
    
    #Peralatan Umum Table 1
    context = make_table(num_rows=1, variables=[3,3+7], context=context, kwargs=kwargs)

    #Peralatan Operasional Table 1
    context = make_table(num_rows=3, variables=[10,10+6], context=context, kwargs=kwargs)

    #User1
    context['user1'] = kwargs['user1']

    #NIP user1
    context['user1nip'] = translate_ttd[kwargs['user1']][1]

    #TTD user1
    context['user1ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{translate_ttd[kwargs['user1']][0]}.jpg"))
    #Catatan
    context['notes1'] = kwargs['notes1']

    #Peralatan Umum Table 2
    context = make_table(num_rows=5, variables=[18,18+7], context=context, kwargs=kwargs)

    #Peralatan Operasional Table 2
    context = make_table(num_rows=7, variables=[25,25+6], context=context,kwargs=kwargs)

    #User2
    context['user2'] = kwargs['user2']

    #NIP user2
    context['user2nip'] = translate_ttd[kwargs['user2']][1]

    #TTD user2
    context['user2ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{translate_ttd[kwargs['user2']][0]}.jpg"))

    #Catatan
    context['notes2'] = kwargs['notes2']

    template_docs.render(context=context)
    return template_docs