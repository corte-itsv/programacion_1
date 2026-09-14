class ArchivoAudio:
    def __init__(self, nombre, duracion_segundos):
        self.nombre = nombre
        self.duracion_segundos = duracion_segundos

    def reproducir(self):
        pass

    def info(self):
        pass


class MP3(ArchivoAudio):
    def __init__(self, nombre, duracion_segundos, bitrate_kbps):
        super().__init__(nombre, duracion_segundos)
        self.bitrate_kbps = bitrate_kbps

    def reproducir(self):
        print(f"Decodificando MP3 (bitrate {self.bitrate_kbps}kbps): {self.nombre}")

    def info(self):
        print(f"[MP3] {self.nombre} - {self.duracion_segundos}s - {self.bitrate_kbps}kbps")


class WAV(ArchivoAudio):
    def __init__(self, nombre, duracion_segundos, sample_rate_hz):
        super().__init__(nombre, duracion_segundos)
        self.sample_rate_hz = sample_rate_hz

    def reproducir(self):
        print(f"Reproduciendo WAV sin compresión ({self.sample_rate_hz}Hz): {self.nombre}")

    def info(self):
        print(f"[WAV] {self.nombre} - {self.duracion_segundos}s - {self.sample_rate_hz}Hz")


class FLAC(ArchivoAudio):
    def __init__(self, nombre, duracion_segundos, nivel_compresion):
        super().__init__(nombre, duracion_segundos)
        self.nivel_compresion = nivel_compresion

    def reproducir(self):
        print(f"Descomprimiendo FLAC (nivel {self.nivel_compresion}) sin pérdida: {self.nombre}")

    def info(self):
        print(f"[FLAC] {self.nombre} - {self.duracion_segundos}s - compresión nivel {self.nivel_compresion}")



playlist = [
    MP3("cancion1.mp3", 210, bitrate_kbps=320),
    WAV("cancion2.wav", 180, sample_rate_hz=44100),
    FLAC("cancion3.flac", 240, nivel_compresion=5),
]

for archivo in playlist:
    archivo.reproducir()
    archivo.info()
    print()

duracion_total = 0
for archivo in playlist:
    duracion_total += archivo.duracion_segundos

print(f"Duración total de la playlist: {duracion_total}s")
