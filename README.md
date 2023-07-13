# Final-Project-Jedha
Projet final pour valider le bloc 6 de la certification et la fin de formation en Data Science chez Jedha. L'objectif est de creer et deployer un model de machine learning qui va predirer les retards sur les departs de vols aux USA.

Dans ce notebook, nous essayons de visualiser les vols des compagnies aeriennes americaines de janvier 2019 à décembre 2019 et essayons de développer un modèle pour prédire ou prévoir les retards des vols au décollage. Dans la visualisation, toutes les informations des données ne seront pas capturées par seulement quelques-unes car le chargement du dataset complet sera très lourd. Aussi pour la prédiction, nous allons essayer de développer les meilleurs modèles possible pour avoir un resultat effiscient sur notre apllication de prediction.

Le notebook est composé de trois parties : exploration, nettoyage et modélisation.

Préambule: vue d'ensemble, visualisation et informations descriptives du jeu de données

MONTH : Mois
DAY_OF_MONTH : Jour du mois (1-31)
DAY_OF_WEEK : 		Jour de la semaine
OP_UNIQUE_CARRIER : Code transporteur, correspond à OP_UNIQUE_CARRIER dans d'autres fichiers
TAIL_NUM : Numéro de queue unique, correspond à TAIL_NUM dans d'autres fichiers
OP_CARRIER_FL_NUM : Numéro de vol
ORIGIN_AIRPORT_ID : ID de l'aéroport, correspond à ORIGIN_AIRPORT_ID dans d'autres fichiers
ORIGIN : Abréviation de l'aéroport d'origine
ORIGIN_CITY_NAME : 	Nom de la ville d'origine
DEST_AIRPORT_ID : ID de l'aéroport de destination, correspond à l'ID de l'aéroport dans d'autres fichiers
DEST : Abréviation de l'aéroport de destination
DEST_CITY_NAME : 	Nom de la ville de destination
CRS_DEP_TIME : 		Heure de départ prévue
DEP_TIME : 		Heure de départ réelle
DEP_DELAY_NEW : Retard de départ en minutes
DEP_DEL15 : TARGET VARIABLE Binaire si retard de plus de 15 min, 1 est oui
DEP_TIME_BLK : Blocage de l'heure de départ
CRS_ARR_TIME :		Heure d'arrivée prévue
ARR_TIME :		Heure d'arrivée réelle
ARR_DELAY_NEW : retard à l'arrivée en minutes
ARR_TIME_BLK : Blocage de l'heure d'arrivée
CANCELLED :		Indicateur si le vol a été annulé
CANCELLATION_CODE :	Code d'annulation
CRS_ELAPSED_TIME :	Temps écoulé prévu pour le vol
ACTUAL_ELAPSED_TIME :	Temps écoulé réel du vol
DISTANCE : Distance du vol en miles
DISTANCE_GROUP :		Groupe de distance du vol
CARRIER_DELAY : Indicateur de retard du transporteur
WEATHER_DELAY : Indicateur de retard dû aux conditions météorologiques
NAS_DELAY : Indicateur pour un retard NAS
SECURITY_DELAY : Indicateur d'un retard lié à la sécurité
LATE_AIRCRAFT_DELAY : Indicateur d'un retard d'avion tardif
