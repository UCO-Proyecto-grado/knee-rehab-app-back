from enum import Enum

class LogMessages:
    class Fisioterapeuta(str, Enum):
        CREATE_ATTEMPT = "Intentando crear fisioterapeuta"
        CREATE_SUCCESS = "Fisioterapeuta creado correctamente"
        CREATE_FAIL = "Error al crear fisioterapeuta"
        
        FETCH_ALL = "Listando todos los fisioterapeutas"
        FETCH_ALL_FAIL = "Error al listar fisioterapeutas"

        FETCH_BY_ID = "Buscando fisioterapeuta por ID"
        FETCH_BY_ID_FAIL = "Error al obtener fisioterapeuta por ID"

        UPDATE_ATTEMPT = "Intentando actualizar fisioterapeuta"
        UPDATE_SUCCESS = "Fisioterapeuta actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar fisioterapeuta"

        DELETE_ATTEMPT = "Intentando eliminar fisioterapeuta"
        DELETE_SUCCESS = "Fisioterapeuta eliminado correctamente"
        DELETE_FAIL = "Error al eliminar fisioterapeuta"

        NOT_FOUND = "Fisioterapeuta no encontrado"
        DUPLICATE = "Fisioterapeuta ya registrado"
    
    class Paciente(str, Enum):
        CREATE_ATTEMPT = "Intentando crear paciente"
        CREATE_SUCCESS = "Paciente creado correctamente"
        CREATE_FAIL = "Error al crear paciente"

        FETCH_ALL = "Listando todos los pacientes"
        FETCH_ALL_FAIL = "Error al listar pacientes"

        FETCH_BY_ID = "Buscando paciente por ID"
        FETCH_BY_ID_FAIL = "Error al obtener paciente por ID"

        FETCH_BY_SEDE_ID = "Buscando pacientes por ID de sede"
        FETCH_BY_SEDE_ID_FAIL = "Error al obtener pacientes por ID de sede"

        UPDATE_ATTEMPT = "Intentando actualizar paciente"
        UPDATE_SUCCESS = "Paciente actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar paciente"

        DELETE_ATTEMPT = "Intentando eliminar paciente"
        DELETE_SUCCESS = "Paciente eliminado correctamente"
        DELETE_FAIL = "Error al eliminar paciente"

        NOT_FOUND = "Paciente no encontrado"
        DUPLICATE = "Paciente ya registrado"
    
    class Ciudad(str, Enum):
        CREATE_ATTEMPT = "Intentando crear ciudad"
        CREATE_SUCCESS = "Ciudad creada correctamente"
        CREATE_FAIL = "Error al crear ciudad"

        FETCH_ALL = "Listando todas las ciudades"
        FETCH_ALL_FAIL = "Error al listar ciudades"

        FETCH_BY_ID = "Buscando ciudad por ID"
        FETCH_BY_ID_FAIL = "Error al obtener ciudad por ID"

        UPDATE_ATTEMPT = "Intentando actualizar ciudad"
        UPDATE_SUCCESS = "Ciudad actualizada correctamente"
        UPDATE_FAIL = "Error al actualizar ciudad"

        DELETE_ATTEMPT = "Intentando eliminar ciudad"
        DELETE_SUCCESS = "Ciudad eliminada correctamente"
        DELETE_FAIL = "Error al eliminar ciudad"

        NOT_FOUND = "Ciudad no encontrada"
        DUPLICATE = "La ciudad ya existe en ese departamento"
        DEPARTAMENTO_NOT_FOUND = "Departamento no encontrado"
    
    class Departamento(str, Enum):
        CREATE_ATTEMPT = "Intentando crear departamento"
        CREATE_SUCCESS = "Departamento creado correctamente"
        CREATE_FAIL = "Error al crear departamento"

        FETCH_ALL = "Listando todos los departamentos"
        FETCH_ALL_FAIL = "Error al listar departamentos"

        FETCH_BY_ID = "Buscando departamento por ID"
        FETCH_BY_ID_FAIL = "Error al obtener departamento por ID"

        UPDATE_ATTEMPT = "Intentando actualizar departamento"
        UPDATE_SUCCESS = "Departamento actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar departamento"

        DELETE_ATTEMPT = "Intentando eliminar departamento"
        DELETE_SUCCESS = "Departamento eliminado correctamente"
        DELETE_FAIL = "Error al eliminar departamento"

        NOT_FOUND = "Departamento no encontrado"
        DUPLICATE = "El departamento ya está registrado para este país"
        PAIS_NOT_FOUND = "País no encontrado"
    
    class Estado(str, Enum):
        CREATE_ATTEMPT = "Intentando crear estado"
        CREATE_SUCCESS = "Estado creado correctamente"
        CREATE_FAIL = "Error al crear estado"

        FETCH_ALL = "Listando todos los estados"
        FETCH_ALL_FAIL = "Error al listar estados"

        FETCH_BY_ID = "Buscando estado por ID"
        FETCH_BY_ID_FAIL = "Error al obtener estado por ID"

        UPDATE_ATTEMPT = "Intentando actualizar estado"
        UPDATE_SUCCESS = "Estado actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar estado"

        DELETE_ATTEMPT = "Intentando eliminar estado"
        DELETE_SUCCESS = "Estado eliminado correctamente"
        DELETE_FAIL = "Error al eliminar estado"

        NOT_FOUND = "Estado no encontrado"
        DUPLICATE = "El estado ya existe"

    class Pais(str, Enum):
        CREATE_ATTEMPT = "Intentando crear país"
        CREATE_SUCCESS = "País creado correctamente"
        CREATE_FAIL = "Error al crear país"

        FETCH_ALL = "Listando todos los países"
        FETCH_ALL_FAIL = "Error al listar países"

        FETCH_BY_ID = "Buscando país por ID"
        FETCH_BY_ID_FAIL = "Error al obtener país por ID"

        UPDATE_ATTEMPT = "Intentando actualizar país"
        UPDATE_SUCCESS = "País actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar país"

        DELETE_ATTEMPT = "Intentando eliminar país"
        DELETE_SUCCESS = "País eliminado correctamente"
        DELETE_FAIL = "Error al eliminar país"

        NOT_FOUND = "País no encontrado"
        DUPLICATE = "El país ya está registrado"
    
    class TipoIdentificacion(str, Enum):
        CREATE_ATTEMPT = "Intentando crear tipo de identificación"
        CREATE_SUCCESS = "Tipo de identificación creado correctamente"
        CREATE_FAIL = "Error al crear tipo de identificación"

        FETCH_ALL = "Listando todos los tipos de identificación"
        FETCH_ALL_FAIL = "Error al listar tipos de identificación"

        FETCH_BY_ID = "Buscando tipo de identificación por ID"
        FETCH_BY_ID_FAIL = "Error al obtener tipo de identificación por ID"

        UPDATE_ATTEMPT = "Intentando actualizar tipo de identificación"
        UPDATE_SUCCESS = "Tipo de identificación actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar tipo de identificación"

        DELETE_ATTEMPT = "Intentando eliminar tipo de identificación"
        DELETE_SUCCESS = "Tipo de identificación eliminado correctamente"
        DELETE_FAIL = "Error al eliminar tipo de identificación"

        NOT_FOUND = "Tipo de identificación no encontrado"
        DUPLICATE = "Tipo de identificación ya existe"
    
    class CentroRehabilitacion(str, Enum):
        CREATE_ATTEMPT = "Intentando crear centro de rehabilitación"
        CREATE_SUCCESS = "Centro de rehabilitación creado correctamente"
        CREATE_FAIL = "Error al crear centro de rehabilitación"

        FETCH_ALL = "Listando todos los centros de rehabilitación"
        FETCH_ALL_FAIL = "Error al listar centros de rehabilitación"

        FETCH_BY_ID = "Buscando centro de rehabilitación por ID"
        FETCH_BY_ID_FAIL = "Error al obtener centro de rehabilitación por ID"

        UPDATE_ATTEMPT = "Intentando actualizar centro de rehabilitación"
        UPDATE_SUCCESS = "Centro de rehabilitación actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar centro de rehabilitación"

        DELETE_ATTEMPT = "Intentando eliminar centro de rehabilitación"
        DELETE_SUCCESS = "Centro de rehabilitación eliminado correctamente"
        DELETE_FAIL = "Error al eliminar centro de rehabilitación"

        NOT_FOUND = "Centro de rehabilitación no encontrado"
        DUPLICATE_IDENTIFICACION = "Un centro con esta identificación ya existe"
        DUPLICATE_NOMBRE = "Un centro con este nombre ya existe"

    class Sede(str, Enum):
        CREATE_ATTEMPT = "Intentando crear sede"
        CREATE_SUCCESS = "Sede creada correctamente"
        CREATE_FAIL = "Error al crear sede"

        FETCH_ALL = "Listando todas las sedes"
        FETCH_ALL_FAIL = "Error al listar sedes"

        FETCH_BY_ID = "Buscando sede por ID"
        FETCH_BY_ID_FAIL = "Error al obtener sede por ID"

        UPDATE_ATTEMPT = "Intentando actualizar sede"
        UPDATE_SUCCESS = "Sede actualizada correctamente"
        UPDATE_FAIL = "Error al actualizar sede"

        DELETE_ATTEMPT = "Intentando eliminar sede"
        DELETE_SUCCESS = "Sede eliminada correctamente"
        DELETE_FAIL = "Error al eliminar sede"

        NOT_FOUND = "Sede no encontrada"

    class TipoSede(str, Enum):
        CREATE_ATTEMPT = "Intentando crear tipo de sede"
        CREATE_SUCCESS = "Tipo de sede creado correctamente"
        CREATE_FAIL = "Error al crear tipo de sede"

        FETCH_ALL = "Listando todos los tipos de sede"
        FETCH_ALL_FAIL = "Error al listar tipos de sede"

        FETCH_BY_ID = "Buscando tipo de sede por ID"
        FETCH_BY_ID_FAIL = "Error al obtener tipo de sede por ID"

        UPDATE_ATTEMPT = "Intentando actualizar tipo de sede"
        UPDATE_SUCCESS = "Tipo de sede actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar tipo de sede"

        DELETE_ATTEMPT = "Intentando eliminar tipo de sede"
        DELETE_SUCCESS = "Tipo de sede eliminado correctamente"
        DELETE_FAIL = "Error al eliminar tipo de sede"

        NOT_FOUND = "Tipo de sede no encontrado"
        DUPLICATE = "El tipo de sede ya está registrado"

    class Categoria(str, Enum):
        CREATE_ATTEMPT = "Intentando crear categoría"
        CREATE_SUCCESS = "Categoría creada correctamente"
        CREATE_FAIL = "Error al crear categoría"

        FETCH_ALL = "Listando todas las categorías"
        FETCH_ALL_FAIL = "Error al listar categorías"

        FETCH_BY_ID = "Buscando categoría por ID"
        FETCH_BY_ID_FAIL = "Error al obtener categoría por ID"

        UPDATE_ATTEMPT = "Intentando actualizar categoría"
        UPDATE_SUCCESS = "Categoría actualizada correctamente"
        UPDATE_FAIL = "Error al actualizar categoría"

        DELETE_ATTEMPT = "Intentando eliminar categoría"
        DELETE_SUCCESS = "Categoría eliminada correctamente"
        DELETE_FAIL = "Error al eliminar categoría"

        NOT_FOUND = "Categoría no encontrada"
        DUPLICATE = "La categoría ya existe"

    class CategoriaTipoLesion(str, Enum):
        CREATE_ATTEMPT = "Intentando crear relación entre categoría y lesión"
        CREATE_SUCCESS = "Relación creada correctamente"
        CREATE_FAIL = "Error al crear relación entre categoría y lesión"

        FETCH_ALL = "Listando relaciones entre categorías y lesiones"
        FETCH_ALL_FAIL = "Error al listar relaciones entre categorías y lesiones"

        DELETE_ATTEMPT = "Intentando eliminar relación entre categoría y lesión"
        DELETE_SUCCESS = "Relación eliminada correctamente"
        DELETE_FAIL = "Error al eliminar relación entre categoría y lesión"

        DUPLICATE = "La relación ya existe"
        NOT_FOUND = "Relación no encontrada"

    class TipoLesion(str, Enum):
        CREATE_ATTEMPT = "Intentando crear tipo de lesión"
        CREATE_SUCCESS = "Tipo de lesión creado correctamente"
        CREATE_FAIL = "Error al crear tipo de lesión"

        FETCH_ALL = "Listando todos los tipos de lesión"
        FETCH_ALL_FAIL = "Error al listar tipos de lesión"

        FETCH_BY_ID = "Buscando tipo de lesión por ID"
        FETCH_BY_ID_FAIL = "Error al obtener tipo de lesión por ID"

        UPDATE_ATTEMPT = "Intentando actualizar tipo de lesión"
        UPDATE_SUCCESS = "Tipo de lesión actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar tipo de lesión"

        DELETE_ATTEMPT = "Intentando eliminar tipo de lesión"
        DELETE_SUCCESS = "Tipo de lesión eliminado correctamente"
        DELETE_FAIL = "Error al eliminar tipo de lesión"

        NOT_FOUND = "Tipo de lesión no encontrado"
        DUPLICATE = "El tipo de lesión ya existe"

    class Ejercicio(str, Enum):
        CREATE_ATTEMPT = "Intentando crear ejercicio"
        CREATE_SUCCESS = "Ejercicio creado correctamente"
        CREATE_FAIL = "Error al crear ejercicio"

        FETCH_ALL = "Listando ejercicios por módulo"
        FETCH_ALL_FAIL = "Error al listar ejercicios"

        FETCH_BY_ID = "Buscando ejercicio por ID"
        FETCH_BY_ID_FAIL = "Error al obtener ejercicio por ID"

        FETCH_BY_CENTRO = "Listando ejercicios por centro de rehabilitación"
        FETCH_BY_CENTRO_FAIL = "Error al listar ejercicios por centro de rehabilitación"

        FETCH_BY_CENTRO_Y_MODULO = "Listando ejercicios por centro y módulo"
        FETCH_BY_CENTRO_Y_MODULO_FAIL = "Error al listar ejercicios por centro y módulo"

        UPDATE_ATTEMPT = "Intentando actualizar ejercicio"
        UPDATE_SUCCESS = "Ejercicio actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar ejercicio"

        DELETE_ATTEMPT = "Intentando eliminar ejercicio"
        DELETE_SUCCESS = "Ejercicio eliminado correctamente"
        DELETE_FAIL = "Error al eliminar ejercicio"

        NOT_FOUND = "Ejercicio no encontrado"

    class MaterialApoyo(str, Enum):
        CREATE_ATTEMPT = "Intentando crear material de apoyo"
        CREATE_SUCCESS = "Material de apoyo creado correctamente"
        CREATE_FAIL = "Error al crear material de apoyo"

        FETCH_ALL = "Listando materiales de apoyo por centro de rehabilitación"
        FETCH_ALL_FAIL = "Error al listar materiales de apoyo"

        FETCH_BY_ID = "Buscando material de apoyo por ID"
        FETCH_BY_ID_FAIL = "Error al obtener material de apoyo por ID"

        UPDATE_ATTEMPT = "Intentando actualizar material de apoyo"
        UPDATE_SUCCESS = "Material de apoyo actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar material de apoyo"

        DELETE_ATTEMPT = "Intentando eliminar material de apoyo"
        DELETE_SUCCESS = "Material de apoyo eliminado correctamente"
        DELETE_FAIL = "Error al eliminar material de apoyo"

        NOT_FOUND = "Material de apoyo no encontrado"

    class Modulo(str, Enum):
        CREATE_ATTEMPT = "Intentando crear módulo"
        CREATE_SUCCESS = "Módulo creado correctamente"
        CREATE_FAIL = "Error al crear módulo"

        FETCH_ALL = "Listando módulos por centro de rehabilitación"
        FETCH_ALL_FAIL = "Error al listar módulos"

        FETCH_BY_ID = "Buscando módulo por ID"
        FETCH_BY_ID_FAIL = "Error al obtener módulo por ID"

        UPDATE_ATTEMPT = "Intentando actualizar módulo"
        UPDATE_SUCCESS = "Módulo actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar módulo"

        DELETE_ATTEMPT = "Intentando eliminar módulo"
        DELETE_SUCCESS = "Módulo eliminado correctamente"
        DELETE_FAIL = "Error al eliminar módulo"

        NOT_FOUND = "Módulo no encontrado"

    class EstadoPlanRehabilitacionEjercicio(str, Enum):
        CREATE_ATTEMPT = "Intentando crear estado de plan de rehabilitación - ejercicio"
        CREATE_SUCCESS = "Estado creado correctamente"
        CREATE_FAIL = "Error al crear estado"

        FETCH_ALL = "Listando todos los estados de plan de rehabilitación - ejercicio"
        FETCH_ALL_FAIL = "Error al listar estados"

        FETCH_BY_ID = "Buscando estado por ID"
        FETCH_BY_ID_FAIL = "Error al obtener estado por ID"

        UPDATE_ATTEMPT = "Intentando actualizar estado"
        UPDATE_SUCCESS = "Estado actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar estado"

        DELETE_ATTEMPT = "Intentando eliminar estado"
        DELETE_SUCCESS = "Estado eliminado correctamente"
        DELETE_FAIL = "Error al eliminar estado"

        NOT_FOUND = "Estado no encontrado"

    class PacienteCategoriaTipoLesion(str, Enum):
        CREATE_ATTEMPT = "Intentando crear relación paciente - categoría tipo lesión"
        CREATE_SUCCESS = "Relación paciente - categoría tipo lesión creada correctamente"
        CREATE_FAIL = "Error al crear relación paciente - categoría tipo lesión"

        FETCH_ALL = "Listando todas las relaciones paciente - categoría tipo lesión"
        FETCH_ALL_FAIL = "Error al listar relaciones paciente - categoría tipo lesión"

        DELETE_ATTEMPT = "Intentando eliminar relación paciente - categoría tipo lesión"
        DELETE_SUCCESS = "Relación paciente - categoría tipo lesión eliminada correctamente"
        DELETE_FAIL = "Error al eliminar relación paciente - categoría tipo lesión"

        DUPLICATE = "La relación ya existe"
        NOT_FOUND = "Relación no encontrada"

    class PlanRehabilitacion(str, Enum):
        CREATE_ATTEMPT = "Intentando crear plan de rehabilitación"
        CREATE_SUCCESS = "Plan de rehabilitación creado correctamente"
        CREATE_FAIL = "Error al crear plan de rehabilitación"

        FETCH_ALL = "Listando todos los planes de rehabilitación"
        FETCH_ALL_FAIL = "Error al listar planes de rehabilitación"

        FETCH_BY_ID = "Buscando plan de rehabilitación por ID"
        FETCH_BY_ID_FAIL = "Error al obtener plan de rehabilitación por ID"

        UPDATE_ATTEMPT = "Intentando actualizar plan de rehabilitación"
        UPDATE_SUCCESS = "Plan de rehabilitación actualizado correctamente"
        UPDATE_FAIL = "Error al actualizar plan de rehabilitación"

        DELETE_ATTEMPT = "Intentando eliminar plan de rehabilitación"
        DELETE_SUCCESS = "Plan de rehabilitación eliminado correctamente"
        DELETE_FAIL = "Error al eliminar plan de rehabilitación"

        NOT_FOUND = "Plan de rehabilitación no encontrado"
