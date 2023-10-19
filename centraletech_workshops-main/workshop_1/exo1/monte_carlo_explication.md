## Méthode de Monte Carlo pour estimer π

La méthode de Monte Carlo est une technique d'approximation numérique qui permet d'estimer π en utilisant des nombres aléatoires. Elle est souvent utilisée pour résoudre des problèmes de probabilité, d'intégration numérique, ou de simulation.

### Illustration

![Cercle et Carré](https://media.geeksforgeeks.org/wp-content/uploads/MonteCarlo.png)

### Formules

Pour estimer π, nous utilisons les formules suivantes :

nous utiliserons un quart de cercle (le quart supérieur à droite) et un carré de longueur 1.

1. **Aire du Quart de Carré** : Si le côté du carré a une longueur de 1 (rayon du cercle), alors l'aire du quart de carré est donnée par : 

    $Aire_{quart\ de\ carré} = 1$

2. **Aire du Quart de Cercle** : Si le rayon du cercle est 1, alors l'aire du quart de cercle est donnée par :

   $Aire_{quart\ de\ cercle} = \frac{\pi}{4}$

Pour estimer π, nous allons générer un grand nombre de points aléatoires à l'intérieur du quart de carré, puis compter combien de ces points tombent à l'intérieur du quart de cercle. Ensuite, nous utiliserons la proportion de points dans le quart de cercle par rapport au nombre total de points pour estimer π.

### Étapes

1. Générez un grand nombre de points aléatoires à l'intérieur du quart de carré en utilisant des nombres aléatoires pour les coordonnées x et y.

2. Pour chaque point généré, vérifiez s'il se trouve à l'intérieur du quart de cercle en utilisant la formule de distance par rapport au centre du cercle. Si la distance du point au centre est inférieure ou égale à 1 (rayon du cercle), le point est à l'intérieur du quart de cercle on ajoute donc 1 au compteur 'nb_pts_interieurs' pour compter leur nombre

3. Utilisez la proportion de points dans le quart de cercle par rapport au nombre total de points générés pour estimer π en utilisant la formule simplifiée :

   $\pi \approx 4 \cdot \frac{Points\ dans\ le\ quart\ de\ cercle}{Total\ de\ points\ générés}$

4. Pour estimer l'écart entre la valeur réelle de π et la valeur estimée, vous pouvez utiliser la formule suivante :

    $\text{Pourcentage d'Écart} = \left|\frac{\pi - \text{Valeur estimée de }\pi}{\pi}\right| \cdot 100\%$
