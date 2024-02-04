import moviepy.editor as mp 
#Edição de vídeo: corte, concatenações, inserções de títulos, composição de vídeo

path = str(input('Digite o caminho do arquivo de video: \n'))
#Usa a função VideoFileClip para carregar o arquivo de vídeo no caminho fornecido
videoclip = mp.VideoFileClip(path)
#Acessa a parte de áudio do objeto videoclip usando o atributo audio
audioclip = videoclip.audio
#Usa o método write_audiofile do objeto audioclip para salvar o áudio como um arquivo MP3
audioclip.write_audiofile('audio.mp3')
