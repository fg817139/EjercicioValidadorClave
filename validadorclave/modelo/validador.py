from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __int__(self,longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def validar_longitud(self,clave):
        return len(clave)>self._longitud_esperada
    def continue_mayuscula(self,clave):
        return any(char.isupper() for char in clave)
    def continue_minuscula(self,clave):
        return any(char.isupper()for char in clave)
    def continue_numero(self,clave):
        return any(char.isupper()for char in clave)

    @abstractmethod
    def es_valida(self,clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __int__(self):
        super().__int__(8)
    def continue_caracter_especial(self,clave):
        return any(char in '@_#$%'for char in clave)
    def es_valida(self,clave):
        return (self.validar_longitud(clave)and
                self.continue_mayuscula(clave)and
                self.continue_minuscula(clave)and
                self.continue_numero(clave)and
                self.continue_caracter_especial(clave))

class ReglasValidacionCalisto(ReglaValidacion):
    def __int__(self):
        super().__int__(6)

    def continue_calisto(self,clave):
        for variant in [f'c{i}l{i}sto'for i in ['A','a']]:
            if clave.lower().find(variant)!=-1 and sum(c.insupper()for c in clave[clave.lower().find(variant):clave.lower().find(variant)+7])>=2:
                return True
            return False

    def es_valida(self,clave):
        return (self.validar_longitud(clave)and
                self.continue_numero(clave)and
                self.continue_calisto(clave))

class Validador:
    def __int__(self,regla):
        self._regla=regla
    def es_valida(self,clave):
        return self._regla.es_valida(clave)



