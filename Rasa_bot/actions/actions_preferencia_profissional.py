# # https://rasa.com/docs/rasa/custom-actions

# # Traker memoria
# # Dispatcher mensagens
# # DomainDict regra de negocios

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction, REQUESTED_SLOT
# from rasa_sdk.types import DomainDict
# from API.services.routes import getHairDresser

# class ActionProcessarPreferencias(Action):
#     def name(self) -> Text:
#         return "action_processar_preferencias"

#     def run(self, dispatcher: CollectingDispatcher,
#             slots_mapped_in_domain: List[Text],
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         slots = slots_mapped_in_domain.copy()
#         if tracker.get_slot("tem_preferencia_profissional") is None:
#             return ["servico", "tem_preferencia_profissional"]
#         if tracker.get("tem_preferencia_profissional") is False:
#             porfissionais = getHairDresser()
#             dispatcher.utter_message(text=f"Vejá os porfissionais disponiveis: \n {porfissionais}")
#         if tracker.get("tem_preferencia_profissional") is True:
#             dispatcher.utter_message(text=f"Certo! Quem é seria?") # Só chegaria aqui caso ele respondesse com apenas (sim, claro...), caso ele já falasse (Sim, o Lucas) essa mensagem não deve ser enviada
