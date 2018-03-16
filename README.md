# Étude du réseau Véli'b : Comment optimiser la redistribution des vélos dans le réseau ?

n s'intéresse au problème de la redistribution des vélos dans les systèmes de vélo-partage comme celui des vélib's à Paris. Dans un tel système, des vélos sont proposés aux usagers, qui peuvent s'en servir et donc les déplacer entre les différentes stations. Le problème est que certaines stations peuvent se retrouver vides de vélos ou pleines de vélos, empêchant le bon fonctionnement du service. L'enjeu de cette redistribution est triple : économique, commercial, et écologique.
À Paris, l'entreprise JCDecaux, qui s'occupe de la gestion du système Vélib's, dispose de deux camions d'une capacité de 62 vélos, et de 23 camionnettes d'une capacité de 20 vélos pour assurer cette redistribution. 
Nous nous sommes intéressés à la redistribution en faisant l'hypothèse qu'aucun vélo n'est en cours d'utilisation.
 Dans ce TIPE, nous allons chercher des méthodes de redistribution respectant les deux conditions suivantes :

	- minimiser la distance parcourue par les camionnettes ;
 	- maximiser la qualité de la redistribution effectuée.

Nous allons traiter le problème statique et nocturne, c'est à dire pendant la nuit quand les mouvements des vélos dûs aux usagers sont minimes.

Pour cela, on travaille à partir de la liste des stations, et de données statistiques sur les trajets effectués : nous disposons des données de la ville de Londres.