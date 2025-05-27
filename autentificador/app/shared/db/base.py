
# Aquí se irán importando todos los demás modelos (Departamento, Ciudad, etc.)
from autentificador.app.models.paciente_model import Paciente
from autentificador.app.models.instituciones.fisioterapeuta_model import Fisioterapeuta
from autentificador.app.models.entidades_primarias.pais_model import Pais
from autentificador.app.models.entidades_primarias.departamento_model import Departamento
from autentificador.app.models.entidades_primarias.ciudad_model import Ciudad
from autentificador.app.models.entidades_primarias.estado_model import Estado
from autentificador.app.models.entidades_primarias.tipo_identificacion_model import TipoIdentificacion
from autentificador.app.models.instituciones.centro_rehabilitacion_model import CentroRehabilitacion
from autentificador.app.models.instituciones.sede_model import Sede
from autentificador.app.models.instituciones.tipo_sede_model import TipoSede
from autentificador.app.models.instituciones.fisioterapeuta_sede_model import FisioterapeutaSede