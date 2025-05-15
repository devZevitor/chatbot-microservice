from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction, REQUESTED_SLOT
from rasa_sdk.types import DomainDict

class ValidateAgendamentoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_agendamento_form"

    async def required_slots(
            self,
            slots_mapped_in_domain: List[Text],
            dispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> List[Text]:

        required = ["servico", "tem_preferencia_profissional"]
        slot_profissional_preferencia = tracker.get_slot("tem_preferencia_profissional")

        if(tracker.get_slot("data") and not tracker.get_slot("profissional") and slot_profissional_preferencia is False):
            return required + ["profissional", "horario"]

        if(tracker.get_slot("data") and not tracker.get_slot("profissional") and slot_profissional_preferencia is True):
             # Chamar a API
            return required + ["profissional", "horario"]

        if(tracker.get_slot("horario") and not tracker.get_slot("profissional") and slot_profissional_preferencia is False):
            return required + ["tem_preferencia_profissional", "profissional", "horario"]

        if(tracker.get_slot("horario") and not tracker.get_slot("profissional") and slot_profissional_preferencia is True):
            # Chamar a API
            return required + ["tem_preferencia_profissional", "profissional", "horario"]


        if(tracker.get_slot("profissional") and not tracker.get_slot("horario")):
            return required + ["horario", "data"]

        if(tracker.get_slot("profissional") and not tracker.get_slot("data")):
            return required + ["data", "horario"]

        return required + ["profissional", "data", "horario", ] # caso senhuma condição atenda ele retorna todos os slots obrigatorios

    # async def validate_servico(
    #         self,
    #         slot_value: Any,
    #         tracker: Tracker,
    #         dispatcher: CollectingDispatcher,
    #         domain: DomainDict
    #     ) -> Dict[Text, Any]:

    #     servicos_validos = ["corte", "barba", "luzes"]
    #     if slot_value.lower() not in servicos_validos:
    #         dispatcher.utter_message("Desculpe, não trabalhamos com esse serviço")
    #         return {"servico": None}

    #     return {"servico": slot_value}

    async def validate_tem_preferencia_profissional(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> Dict[Text, Any]:

        if slot_value not in [True, False]:
            dispatcher.utter_message("Por favor, responda com 'sim' ou 'não'.")
            return {"tem_preferencia_profissional": None}
        return {"tem_preferencia_profissional": slot_value}

    async def validate_data(
            self,
            slot_value: Any,
            tracker: Tracker,
            dispatcher: CollectingDispatcher,
            domain: DomainDict
        ) -> Dict[Text, Any]:

        if(tracker.get_slot("profissional") and not  tracker.get_slot("data")):
            dispatcher.utter_message("Temos os seguintes dias 11/02, 11/02, 12/01 para este funcionario")

        if not slot_value:
            dispatcher.utter_message("Valor invalido ou vazio...")
            return {"data": None}

        # chamar a API para validar a data

        return {"data": slot_value}

    async def validate_horario(
            self,
            slot_value: Any,
            tracker: Tracker,
            dispatcher: CollectingDispatcher,
            domain: DomainDict
        ) -> Dict[Text, Any]:

        if(tracker.get_slot("profissional") and not tracker.get_slot("horario")):
            dispatcher.utter_message("Temos os seguintes horarios 11:00, 09:00, 07:00 para esse funcionario")

        if not slot_value:
            dispatcher.utter_message("Valor invalido ou vazio...")
            return {"horario": None}

        # chamar a API para validar o horario

        return {"horario": slot_value}

    async def validate_profissional(
            self,
            slot_value: Any,
            tracker: Tracker,
            dispatcher: CollectingDispatcher,
            domain: DomainDict
        ) -> Dict[Text, Any]:
        
        slot_profissional_preferencia = tracker.get_slot("tem_preferencia_profissional")

        if( tracker.get_slot("data") and not tracker.get_slot("profissional") and slot_profissional_preferencia is False):
            dispatcher.utter_message("Temos os seguintes funcionarios João, Carlos, Junior paraa esta data")

        if( tracker.get_slot("data") and not tracker.get_slot("profissional") and slot_profissional_preferencia is True):
            # Chamar a API
            dispatcher.utter_message("Chamando a API...")

        if(tracker.get_slot("horario") and not tracker.get_slot("profissional") and slot_profissional_preferencia is False):
            dispatcher.utter_message("Temos os seguintes funcionarios Andre, Carlos, Luan para este horario")

        if(tracker.get_slot("horario") and not tracker.get_slot("profissional") and slot_profissional_preferencia is True):
            # Chamar a API
            dispatcher.utter_message("Chamando a API...")

        if not slot_value:
            dispatcher.utter_message("Valor invalido ou vazio...")
            return {"profissional": None}

        # chamar a API para validar os profissionais
        profissionais_validos = ["joão", "carlos", "junior", "andre", "luan"]  # simulando o retorno da API
        if slot_value.lower() not in profissionais_validos:
            dispatcher.utter_message("Desculpe, esse profissional não está disponivel")
            return {"profissional": None}
        
        # listar os funcionarios que estão disponiveis da API
        for profissional in profissionais_validos:
           print(profissional)

        return {"profissional": slot_value}