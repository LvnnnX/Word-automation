from library import *
PATH = Path(__file__).parent
ASSETS = PATH / "assets"
DOCS = ASSETS / "word"
TTD = ASSETS / "ttd"

with open(PATH / 'list-hari.txt', 'r') as f:
    lshr = f.read()
translate_hari = json.loads(lshr)

with open(PATH / 'list-shift-full.txt', 'r') as f:
    lsshf = f.read()
translate_shift = json.loads(lsshf)

with open(PATH / 'list-bulan.txt', 'r') as f:
    lsbln = f.read()    
translate_bulan = json.loads(lsbln)

all_shift = ['Pagi', 'Siang', 'Malam', 'Tengah Malam']

options = ['Baik', 'Rusak', 'Kosong']

def get_media():
    with open(PATH / 'list-media-radio.json','r') as f:
        data = json.load(f)
        list_media = data['Media']
        all = []
        for media in list_media:
            all.append(media['name'])
    return all

def get_pegawai():
    list_pegawai = pd.read_excel('list-pegawai.xlsx')
    list_pegawai = list_pegawai.sort_values(by=['Nama'], ascending=True)
    list_pegawai = list_pegawai.to_dict()

    user = tuple(list_pegawai['Nama'].values())
    user_filename = tuple(list_pegawai['Nama File'].values())
    user_nip = tuple(list_pegawai['NIP'].values())
    return user, user_filename, user_nip

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

def popup_clear_background():
    st.markdown(
    """
<style>
div[data-modal-container='true'][key='Demo key'] > div:first-child > div:first-child{
    background-color:#0e1117;
}
</style>
""", unsafe_allow_html=True)

def get_docs(docs):
    docs = DocxTemplate(DOCS / docs)
    return docs


def find_filename(name):
    try:
        named = glob.glob(f'{TTD}/{name}.*')
        return named[0]
    except:
        return ValueError

def get_image(location):
    image = Image.open(os.path.join(location))
    return image

def get_dataframe(nama_dataframe:str):
    df = pd.read_excel(PATH / f'{nama_dataframe}.xlsx', index_col=0)
    df.index +=1 
    return df

def save_image(file_uploaded, name):
    if file_uploaded is not '':
        file_uploaded.name = name + '.' + file_uploaded.name.split('.')[-1]
        with open(os.path.join(ASSETS,file_uploaded.name),"wb") as f:
            f.write(file_uploaded.getbuffer())

def get_current_shift(jam_sekarang, shifts=translate_shift):
    jam_sekarang = jam_sekarang.strftime("%H:%M:%S")
    shift_pagistart = translate_shift['Pagi'].split('-')[0].replace('.',':') + ':00'
    shift_siangstart = translate_shift['Siang'].split('-')[0].replace('.',':') + ':00'
    shift_malamstart = translate_shift['Malam'].split('-')[0].replace('.',':') + ':00'
    if(jam_sekarang >= shift_pagistart and jam_sekarang <= shift_siangstart):
        return 'Pagi'
    elif(jam_sekarang >= shift_siangstart and jam_sekarang <= shift_malamstart):
        return 'Siang'
    else:
        return 'Malam'

def get_jadwal_sekarang():
    #Jam ditambah 8 karena GMT+8
    tanggal_sekarang = datetime.now()
    jam_sekarang = datetime.now().strftime("%H:%M:%S")
    #jam_sekarang ditambah 8
    jam_sekarang = datetime.strptime(jam_sekarang, "%H:%M:%S") + timedelta(hours=8)
    shift_sekarang = get_current_shift(jam_sekarang)
    return tanggal_sekarang, jam_sekarang, shift_sekarang

def change_tanggal(tanggal):
    tanggal = tanggal.strftime("%d %m %Y")
    tanggal = tanggal.split(' ')
    tanggal[1] = translate_bulan[tanggal[1]]
    tanggal = ' '.join(tanggal)
    return tanggal

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


def cek_alat(get_tanggal,**kwargs):
    template_docs = get_docs('template-cekalat.docx')
    user, user_filename, user_nip = get_pegawai()
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
    context['user1nip'] = user_nip[user.index(kwargs['user1'])].replace('\'','')

    #TTD user1
    context['user1ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_filename[user.index(kwargs['user1'])])}"))
    #Catatan
    context['notes1'] = kwargs['notes1']

    #Peralatan Umum Table 2
    context = make_table(num_rows=5, variables=[18,18+7], context=context, kwargs=kwargs)

    #Peralatan Operasional Table 2
    context = make_table(num_rows=7, variables=[25,25+6], context=context,kwargs=kwargs)

    #User2
    context['user2'] = kwargs['user2']

    #NIP user2
    context['user2nip'] = user_nip[user.index(kwargs['user2'])].replace('\'','')

    #TTD user2
    context['user2ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_filename[user.index(kwargs['user2'])])}"))

    #Catatan
    context['notes2'] = kwargs['notes2']

    template_docs.render(context=context)
    return template_docs

def evaluasi_cuaca_maritim(tanggal1,tanggal2,**kwargs):
    template_docs = get_docs('template-evaluasimaritim.docx')
    user, user_filename, user_nip = get_pegawai()
    context = {}
    
    #Tanggal
    context['datetime1'] = change_tanggal(tanggal1)
    
    #Jam1
    context['jam'] = str(kwargs['jam'])[0:5].replace(':','.')
    
    #Tanggal2
    context['datetime2'] = change_tanggal(tanggal2)
    
    #Jam2
    context['jam2'] = str(kwargs['jam2'])[0:5].replace(':','.')
    
    #Dasar pertimbangan
    context['dasar_pertimbangan1'] = kwargs['dasar_pertimbangan1']
    context['text_rendah'] = kwargs['text_rendah']
    context['text_sedang'] = kwargs['text_sedang']
    context['text_tinggi'] = kwargs['text_tinggi']
    context['text_sangattinggi'] = kwargs['text_sangattinggi']
    context['dasar_pertimbangan2'] = kwargs['dasar_pertimbangan2']
    context['image1'] = InlineImage(template_docs, kwargs['image_1'], width=Mm(75), height=Mm(80))
    context['image2'] = InlineImage(template_docs, kwargs['image_2'], width=Mm(75), height=Mm(80))
    
    #Kesimpulan
    context['kesimpulan'] = kwargs['kesimpulan']
    
    #User
    context['user1_ttd'] = InlineImage(template_docs, os.path.join(ASSETS, f"{find_filename(user_filename[user.index(kwargs['user1'])])}"))
    
    context['user1'] = kwargs['user1']
    
    context['user1_nip'] = user_nip[user.index(kwargs['user1'])].replace('\'','')
    
    template_docs.render(context=context)
    return template_docs