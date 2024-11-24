# [Cryptanalyse] e=N - Write up

Grâce à :
```py
out += f"e = {pow(d, -1, φ)}\n"
```
que nous allons noter $x$, nous connaissons la valeur de N modulo $\varphi(N)$, i.e. nous avons :
```math
\begin{align*}
x &\equiv N \pmod{\varphi(N)} \\
x &= N + k\varphi(N), \quad k \in \mathbb{Z}
\end{align*}
```
Or, $N$ et $\varphi(N)$ sont très très proche l'un de l'autre, en effet, $\varphi(N) = (p-1) \times (q-1) \approx p*q \approx N$, il suffit donc de retirer une seule fois $\varphi(N)$ a $N$ pour obtenir $x$. Nous avons alors la relation :
```math
\begin{equation}
x = N - 1 \times \varphi(N)
\end{equation}
```
Grâce a cette relation, nous déduisons que $\varphi(N) = N - x$. Connaissant $\varphi(N)$, il est maintenant trivial de retrouver le flag ; une implémentation en python de cette solution est disponible dans le script `solve.py`.
