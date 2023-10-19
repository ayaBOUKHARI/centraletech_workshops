"""
L'objectif de cet exercice est d'utiliser une API pour récupérer des informations sur internet avec le module requests, l'API en question nous donne des faits aléatoires en anglais
API : (Application Programming Interface) ou (Interface de Programmation Applicative) est un moyen pour les logiciels de se parler et de collaborer pour accomplir des tâches spécifiques comme demander des informations ou effectuer des actions.
Pour utiliser l'api d'un service, nous aurons besoin de son url (chemin d'accès de service par internet), et d'une clef api (API Key), pour l'authentification (on aura pas besoin d'une clef pour l'api qu'on va utiliser)
On va utiliser le nodule requests qui permet de faire des requêtes http(s) et de recevoir les réponses, c'est comme si on accédait à un site avec notre navigateur web

(1) requests.get(<url>) : permet de faire une requête http(s) avec un lien et de récupérer sa réponse
(2) requests.text : renvoie le contenue de la réponse sous format texte
(3) requests.json : convertit un texte en format json (dictionnaire en python) pour exploiter les élement de la réponse
(4) requests.status_code : renvoie le code http de la réponse de la requête (200 -> ok / 404 -> introuvable)
"""