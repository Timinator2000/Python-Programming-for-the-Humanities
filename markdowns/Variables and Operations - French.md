<h1> <center>Cours : Variables et opérations </center></h1>

# Part One: Variables

A variable in computing allows you to keep data in memory (while the program is running) such as the result of a calculation or a word, a list or many other things.
To store a value in memory in a variable, we simply use the equal sign =.
For example:

```python
a=3
b=7
c=b+a+2
```

In this example, we have stored 3 variables. In a, we have stored the value 3, in b the value 7 and in c the value 12. Important note: what is stored is the result of the calculation and not the calculation. This means that if we change the value of a, the variable c will remain at 12.

To display the value of a variable, we use the function `print`. Press the Run button to see the effect of the code below:

```python runnable
a=3
b=7
c=b+a+2
print(c)
```

We see the value of c displayed.

A little subtlety with variables: We can use a certain variable a to do a calculation and store the answer again in a which will have the effect of making the first value of a disappear. This is very practical to avoid using too many different variables for example.

```python runnable
a=3
a=a+2
print(a)
a=a+a
print(a)
```

Petite explication des résultats affichés : Au début *a* vaut 3, on lui ajoute 2 et on stocke dans *a* donc maintenant *a* vaut 5, ce qu'on affiche en premier. Ensuite on calcule *a+a* donc 5+5=10 qu'on stocke de nouveau dans *a*, d'où l'affichage du 10 en deuxième.


# Part Two: Operations on Numerical Variables

In this part, we will see the basic operations that can be performed in Python on numbers.

* There are of course the four classic operations +, -, *, / with the usual operational priorities. For example:

```python runnable
  a=5
  b=3
  print(a+b)
  print(a-b)
  print(a*b)
  print(a/b)
  ```

+ Les deux autres opérations qu'on utilise couramment sont les puissances et la racine carrée.  
  - Pour les ***puissances***, on double simplement la multiplication. Ainsi $`x^n`$ s'obtiendra en écrivant `x**n`.  
  - Pour la ***racine carrée***, on va simplement utiliser une propriété mathématique : $`\sqrt x = x^{0.5}`$. Donc pour calculer la racine carrée d'un nombre x, il suffit d'écrire `x**0.5`.  
  Voici quelques exemples. On a rajouté des commentaires à coté des instructions d'affichage des calculs pour que ces instructions soient plus claires. Pour écrire un commentaire, il suffit de mettre un # devant. Tout ce qui suit le # ne sera pas executé par l'ordinateur et ne sert donc qu'à la personne qui lit le programme.

```python runnable
print(2**3) # Affiche le résultat de 2 puissance 3
print(3**2) # Affiche le résultat de 3 puissance 2
print(9**0.5) # Affiche la racine carrée de 9
print(2**0.5) # Affiche la racine carrée de 2
```

+ On peut aussi réaliser facilement des divisions euclidiennes (c'est à dire les divisions posées comme au primaire). 
  - Pour obtenir le ***quotient*** de la division de a par b, il suffit d'écrire `a//b`.
  - Pour obtenir le ***reste*** de la division de a par b, il suffit d'écrire `a%b`.  
  Remarque : La différence entre `a/b`et `a//b`est que le premier donne une valeur approchée décimale à 16 chiffres après la virgule alors que la deuxième nous donne l'***entier*** q tel que 0 <= a-bq < b.  
  Voici quelques exemples que vous pouvez modifier pour vérifier que vous avez bien compris.

```python runnable
a=17
b=3
print(a//b) # Affiche le quotient de la division euclidienne de a par b
print(a%b) # Affiche le reste de la division euclidienne de a par b
```

Remarque : Même si ces opérations sont finalement assez peu utilisée en cours de mathématiques, elles le sont beaucoup plus en informatique, principalement le calcul du reste de la division euclidienne. Par exemple pour déterminer si un nombre est pair, il suffit de regarder si `x%2` vaut 0. En effet, un nombre est pair si et seulement si son reste par la division par 2 est nul. On l'utilisera régulièrement dans les exercices.
  
# Troisième partie : QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1

```python
a=5
b=a-2
print(a*b)
```  

?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] -10
-[x] 15
-[ ] 23
-[ ] 3
-[ ] 8

---

###### QCM 2

```python
a=5
a=a-2
a=a*a+1
print(a)
```  

?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 16
-[ ] 26
-[ ] 12
-[x] 10

---

###### QCM 3

```python
a=7
b=a-1
print((b/2)**2)
```

?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 6.0
-[ ] 1.5
-[x] 9.0
-[ ] -0.25  

---

##### QCM 4
```python
a=3
b=a+1
print((a**2+b**2)**0.5)
```
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[x] 5.0
-[ ] 13.0
-[ ] 12.5
-[ ] 7.0

---

###### QCM 5
```python
a=22
b=5
print((a//b)+(a%b))

```
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 6.4
-[ ] 4.4
-[x] 6
-[ ] 114.4 

# Over to you!

###### Exercice 1 :

Le but de cet exercice est de suivre un programme de calcul en partant d'un entier ***n*** qui sera donné automatiquement.

Appuyez sur Run et suivez les instructions qui s'affichent.

N'effacez pas ce que vous avez fait juste. Il faut rajouter au fur et à mesure en dessous.

Quand on demande d'afficher, c'est avec `print`.

@[Programme de calcul]({"stubs": ["Variables_et_fonctions/Programme_calcul.py"], "command": "python3 Variables_et_fonctions/Programme_calcul_Test.py"})

---

###### Exercice 2 :

La consigne de cet exercice est identique au précédent.

Appuyez sur Run et suivez les instructions qui s'affichent.

N'effacez pas ce que vous avez fait juste. Il faut rajouter au fur et à mesure en dessous.

Quand on demande d'afficher, c'est avec `print`.

@[Programme de calcul]({"stubs": ["Variables_et_fonctions/Programme_calcul1.py"], "command": "python3 Variables_et_fonctions/Programme_calcul1_Test.py"})

---



