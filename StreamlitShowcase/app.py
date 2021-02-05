import streamlit as st


#Título
st.title("Página Streamlit Alterada")

#Header/Subheader
st.header("Isso é um header")
st.subheader("Isso é um subheader")

#Texto
st.text("Oi Steamlit")

#Markdown
st.markdown("### Isso é um *** markdown ***")

#Texto/Texto Colorido
st.success("Sucesso!")

st.info("Informação!")

st.warning("Isso é um aviso!")

st.error("Isso é um erro!")

st.exception("NameError('nome não definido')")

#Ajuda sobre python
st.markdown("## Informações sobre range ##")
st.help(range)

#Escrevendo Texto
st.write("Texto usando *** write ***")

st.write(range(10))

#Imagens
from PIL import Image
img = Image.open("cat.jpg")
st.image(img,width=500,caption="bichano")

#Video
vid_file = open("video.mp4", "rb")
#vid_bytes = vid_file.read()
st.video(vid_file)

#Audio
audio_file = open("audio.mp3","rb").read()
st.audio(audio_file,format='audio/mp3')

#Widget/Checkbox
if st.checkbox("Mostrando/Escondendo"):
    st.text("Mostrando ou Escondendo Widget")
    
#Radio Buttons
status = st.radio("Você apertou em algum botão?", ("Sim", "Não"))

if status == 'Sim':
    st.success("De fato!")
else:
    st.warning("Mentira")
    

#SelectBox
comida = st.selectbox("Qual a sua comida favorita a seguir?", ["Pizza", "Hamburguer", "Macarrão", "Pipoca"])
st.write("Sua comida favorita que está na lista é", comida)

#MultiSelect
location = st.multiselect("Onde você trabalha?", ("New York", "London", "Berlim"))
st.write("Você escolheu", len(location), "lugares")

#Slider
age = st.slider("Qual a sua idade?", 1,100)

#Botões
st.button("Botão Simples")
if st.button("Sobre"):
    st.text("Sim, sobre")
    
#Text Input
primeironome = st.text_input("Coloque seu primeiro nome.", "Escreva Aqui...")
if st.button("Aplicar"):
    resultado = primeironome.title()
    st.success(resultado)
    
#Area De texto
mensagem = st.text_area("Coloque sua mensagem.", "Escreva Aqui...")
if st.button("Mandar"):
    resultado = mensagem.title()
    st.success(resultado)
    
#Date input
import datetime
today = st.date_input("Hoje é", datetime.datetime.now())

#Time
hora = st.time_input("Agora são", datetime.time())

#Displaying JSON
st.text("Display JSON")
st.json({'name':"Miguel", 'gênero':"Masculino",})

#Display RAW Code
st.text("Display RAW Code")