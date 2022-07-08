from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    mensaje="""
        <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
        <h2>EP Ingeniería de Sistemas</h2>
        <h3>Bienvenidos</h3>
    """
    return HttpResponse(mensaje)

def UC3(request):
    mensaje = """
    <h1>Lenguaje de Programación III</h1>
    <h2>Evaluación de la Unidad de Competencia 3</h2>
    <h2>Docente: Mg. Flor Elizabeth Cerdán León</h2>
    <p>Integrantes: </p>
    <li>Alanya Villar Joel Edwin</li>
    <li>Cosme Hernandez Carlos Daniel</li>
    """
    return HttpResponse(mensaje)

def noticia(request):
    mensaje="""
        <h1>Noticia</h1>
        <h2>Periodistas de América TV se pronuncian sobre el secuestro de colegas en Cajamarca</h2>
        <div style="width:60%">
  
            <p style="text-align:justify">Anoche, a esta hora, se le exigió a América Televisión interrumpir su 
            programación para defender la vida de sus periodistas. Fuimos extorsionados por un grupo de ronderos que,
             abusando de su rol, secuestraron a un equipo periodístico de Cuarto Poder y para mantenerlos a salvo nos
              obligaron a transmitir en vivo la lectura de un manifiesto que pretendía desvirtuar una denuncia periodística
               por corrupción.  Este hecho, claramente, fue un acto de extorsión que no debe repetirse y que no avalaremos 
               permaneciendo en silencio. 
                En un país en el que impera el Estado de Derecho y se respeta la libertad de información, la extorsión 
                a un medio de comunicación es un delito que nos afecta a todos, que violenta nuestros derechos y libertades,
                 y no debe ser aceptado ni normalizado. Ello solo muestra la vulnerabilidad a las que estamos sometidos todos
                  los peruanos y no solo la prensa independiente que investiga y denuncia actos de corrupción. Como sociedad,
                   no podemos normalizar la delincuencia y la violencia. Debemos reaccionar y reconducir nuestro país antes de
                    que sea demasiado tarde, y defender nuestro estado libre y democrático.
            Frente a ustedes, nuestros televidentes, y ante todo el país, los periodistas de América Televisión reafirmamos
             nuestro compromiso con la verdad. Esto nos impulsa a seguir investigando este caso y no callaremos, así como todo 
             acto o decisión que atente contra los intereses del país, sin importar quién o quiénes estén involucrados.</p>
        </div>
        <a href="https://canaln.pe/actualidad/pronunciamiento-america-television-y-sus-periodistas-n448123">Pronunciamiento de America-Canal N</a>
    """
    return HttpResponse(mensaje)