## Financement (Que révèlent ces chiffres sur la distribution du capital dans l’écosystème technologique ?)

Fbar = 25410171.813449025
Interprétation : si on partageait l'argent total à parts égales entre toutes les startups, chacune aurait environ 25 millions de dollars.

Mf = 10000000.0
Interprétation : la moitié des startups a levé moins de 10 millions de dollars, et l'autre moitié a levé plus.

sigma_F = 189634141.26567838
Interprétation : l'écart-type fait environ 190 millions de dollars, soit presque 8 fois la moyenne (25 millions). Les montants sont donc très éloignés les uns des autres : certaines startups ont levé très peu, d'autres des centaines de millions, voire des milliards.

Remarques :
- Mf < Fbar : la moyenne (25 millions) est bien plus haute que la médiane (10 millions). C'est parce que quelques très grosses startups (le maximum dépasse 5 milliards de dollars) tirent la moyenne vers le haut. La moyenne ne représente donc pas une startup typique.
- Conclusion : le capital n'est pas réparti de façon égale. Une majorité de startups lève des montants modestes, et quelques unes captent des sommes énormes.
- Limite : le financement total est cumulé jusqu'à la date de collecte des données, donc une startup plus ancienne a eu plus de temps pour lever de l'argent.

## Taille de l'équipe (remplacé par relationships)

Ebar = 7.7039045553145336
Interprétation : si toutes les startups avaient la même taille d'équipe, chacune aurait environ 7,7 relations (notre remplaçant de la taille d'équipe).

Me = 5.0
Interprétation : la moitié des startups a 5 relations ou moins, et l'autre moitié en a 5 ou plus.

sigma_E = 7.2628199126899595
Interprétation : l'écart-type fait environ 7,3, presque autant que la moyenne (7,7). Les tailles d'équipe sont donc très variées : certaines startups ont presque aucune relation, d'autres beaucoup (jusqu'à 63).

Remarques :
- Me < Ebar : la moyenne (7,7) est plus haute que la médiane (5) parce que quelques startups avec de très grosses équipes tirent la moyenne vers le haut. Comme pour le financement, mais en plus faible.
- Conclusion : la plupart des startups ont une petite équipe, et quelques-unes ont une équipe bien plus grande.

## Taux de succès
Tbar = 0.6464208242950108
Interprétation : environ 65 % des startups de l'échantillon ont réussi. Autrement dit, environ 6 startups sur 10 ont été rachetées, et 4 sur 10 ont fermé.

Mt = 1.0
Interprétation : la médiane vaut 1 (réussite) parce que plus de la moitié des startups ont réussi. Pour une colonne qui ne vaut que 0 ou 1, ce chiffre dit seulement quel cas est le plus fréquent.

sigma_T = 0.4780804767115779
Interprétation : l'écart-type (environ 0,48) est élevé pour une colonne qui ne vaut que 0 ou 1. C'est normal : il est maximal quand les deux cas sont à peu près aussi fréquents. Ici, réussites et échecs sont bien mélangés. Ce chiffre n'apporte pas d'information supplémentaire par rapport au 65 %.

Remarques :
- Dans ce dataset, "succès" veut dire "rachetée". Toutes les startups sont soit rachetées (597), soit fermées (326) : aucune n'est encore en activité.
- Limite : le taux de 65 % ne vaut que pour cet échantillon, qui ne contient que des startups dont l'histoire est terminée. Il ne dit pas que 65 % des startups en général réussissent.

## Les écarts sont-ils plus importants entre pays ou entre secteurs ?

Taux de succès par État : de 35 % (Pennsylvanie, PA) à 77 % (Massachusetts, MA), soit une étendue de 0,42 et un écart-type de 0,137. Les États qui réussissent le mieux sont le Massachusetts (77 %), New York (73 %) et le Colorado (74 %). La Californie, qui compte plus de la moitié des startups, est à 68 %. Les moins bons sont la Pennsylvanie (35 %), le groupe "Autres" (44 %) et l'Illinois (50 %).

Taux de succès par secteur : de 40 % (public_relations) à 84 % (analytics), soit une étendue de 0,44 et un écart-type de 0,136. Les secteurs qui réussissent le mieux sont analytics (84 %), security (79 %) et enterprise (77 %). Les moins bons sont public_relations (40 %), hardware (41 %) et cleantech (41 %).

Conclusion : les écarts sont à peu près les mêmes entre États et entre secteurs. L'étendue est un peu plus grande pour les secteurs (0,44 contre 0,42), mais l'écart type est presque identique (0,136 contre 0,137) : on ne peut pas dire que l'un varie nettement plus que l'autre.

## Représentez les distributions à l’aide d’histogrammes et de diagrammes à barres.
### Diagramme à barres : nombre de startups rachetées par État
La Californie concentre de loin le plus de startups rachetées (environ 330 sur 597, soit plus de la moitié). Viennent ensuite New York (environ 77) et le Massachusetts (environ 64). Ces trois États réunissent près de 80 % des startups rachetées. Les autres États (Washington, Texas, Colorado, Illinois, Pennsylvanie) en ont chacun moins de 25.
**Question de réflexion** : l'incubateur doit il s'installer en Californie, où il y a le plus de startups rachetées ?

### Diagramme à barres : taux de succès par État
Le Massachusetts (77 %), le Colorado (74 %) et New York (73 %) ont les meilleurs taux de succès, suivis de la Californie (68 %). Les moins bons sont la Pennsylvanie (35 %), le groupe "Autres" (44 %) et l'Illinois (50 %).

### Quelles zones géographiques concentrent le plus de startups performantes ?
La Californie, New York et le Massachusetts. La Californie en compte le plus parce qu'elle a le plus de startups (487 sur 922), pas parce qu'elle réussit nettement mieux. Son taux (68 %) est proche de la moyenne de l'échantillon (65 %). Le Massachusetts et New York ont un taux plus élevé avec moins de startups, une startup y a donc plus de chances d'être rachetée. Le Colorado a aussi un bon taux (74 %), mais avec seulement 19 startups, ce chiffre est peu fiable.
**Question de réflexion** : l'incubateur doit il aussi regarder des États comme le Massachusetts ou New York, où les startups réussissent plus souvent ?

### Que cela implique-t-il pour la stratégie de développement de l'incubateur ?
- Pour accéder au plus grand nombre de startups prometteuses et d'acheteurs potentiels, la Californie est l'endroit où il y a le plus de choix.
- Pour maximiser les chances de succès de chaque startup accompagnée, le Massachusetts et New York semblent plus favorables, et méritent une attention particulière.
- Prudence : on voit où les startups réussissent, mais pas pourquoi. L'État n'est peut être pas la cause du succès (secteur, financement ou taille d'équipe peuvent jouer). Le Colorado, l'Illinois et la Pennsylvanie ont trop peu de startups pour en tirer une conclusion.

### Histogramme de la répartition du financement total
la grande majorité des startups a levé des montants relativement petits, et quelques-unes très grosses étirent l’échelle. C’est ce qui explique la moyenne (25 millions) bien plus haute que la médiane (10 millions). Mais on ne distingue rien de la forme de la répartition parmi les petites startups : c’est pour ça qu’on a créé log_funding.
**Question de réflexion** : puisque quelques startups reçoivent beaucoup plus d'argent que les autres, l'incubateur doit il soutenir quelques grosses startups ou beaucoup de petites ?

### Histogramme de la répartition du logarithme du financement total
- 14 - environ 1 million de dollars, 16 - environ 9 millions, 18 - environ 65 millions, 20 - environ 500 millions.
- La majorisé des startups sont entre 15 et 18, avec un sommet vers 16-17 (environ 10 à 20 millions). C’est cohérent avec la médiane de 10 millions.
- Il y a un peu plus de startups à gauche (petits financements) qu’à droite, et une seule startup isolée tout à droite, vers 22 (plusieurs milliards), le maximum qu’on a vu.
**Question de réflexion** : quel montant d'investissement l'incubateur doit il viser pour une startup "normale" ?

### Histogramme de la taille d'équipe
la plupart des startups ont une petite équipe, quelques unes seulement (rares mais très éloignées des autres) ont une grande équipe. C’est ce qui explique la moyenne (7,7) plus haute que la médiane (5) : les quelques grandes équipes tirent la moyenne vers le haut. Même effet que pour le financement, en moins fort.
**Question de réflexion** : l'incubateur doit il soutenir surtout des petites équipes, puisque c'est la majorité des startups ?