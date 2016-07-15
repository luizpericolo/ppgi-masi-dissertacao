## Definitions ##

Can be found from pdf page 60 onwards (or dissertation page 48 onwards)

### Canidate Solution ###

Represents the value that maximizes the target function. If the candidate is an Integer, we can
represent it as an array of bits that it is made up of. The candidate can also be a list of integers
representing a permutation of graph nodes. In either case, we shall use N to represent the length of our
candidate solution.


### Mask ###

The mask M is a set of size |M|. Each step of our method deals with the possibility of changing the candidate
solution to enhance it using this mask.

### Transformation or Application ###

There will also exist *m* different transformations, or applications, of a given mask, which represents all the possible outcomes of a
betting event.
An application consists of an array that tells us if each element of the mask can be changed or not.

    Example:
    N = 10
    M = {2, 5, 7, 9}

Applying transformation T0 or application 0, to mask M will yield no possible positions to change.
Applying transformation T3, or application 3, to mask M will yield possibility to change positions 7 and 9 of the
candidate solution since 3 has the last two bits active in binary (0011) and the last two positions of mask M
are the indexes 7 and 9.

Each application shall yield a value, so each result is defined by its generating application Ti. The winning
Ti will be the one that yields the highest value among all possible i values (in the previous example T0, T1, T2, .., T15)

The masks and the applications, or transformations, are responsible for defining the choices the players will have to bet
on. They are responsible for directing the search for the best solution once they are always applied to the currently best
known candidate (**cbkc** for sort).

### Player ###

Each player is an algorithm or formula that decides the weights of a given Ti. This means that each player, given a mask M, and knowing the definition of the transformation T, must be able to calculate the weight *w* of each outcome. In practice this means that there will be *m* candidate solutions that will be created applying a transformation on the **cbkc** and one of them will be the winner.
Given the weights *w*1, ..., *w*m for each combination of *m*, the estimated probability p* for each result is

p*k = *w*k / SUM{i=1, w} *w*i

The way we calculate the weight can vary and it's probably the most important thing to define when applying this method to find
the solution to a problem.

(... more stuff ...)

### Algorithm - Phase 1 ###

selecione solução candidata aleatória e atribua a x*

    for cada iteracao do
        seleciona máscara aleatoria M de tamanho |M|
        for cada jogador i do conjunto P do
            for j de 1 a m do
                calcule o peso de wij
            end for
        end for
        for j de 1 a m do
            wj = SUM{i = 1, |P|} wij / SUM{k=1, m} SUM{i=1, |P|} wik
        end for
        for cada jogador i do conjunto P do
            for all k tal que wk > wik do
                p' = 1 / wik
                w = wk
                Bik = min(rho, max(Bmin, p'(w-1) / (w-1) * rho))
                aposte Bik no resultado k
            end for
        end for
        best = 0
        for cada mascara i em m do
            t = f(Ti)
            if t > best then
                best = t
                b = i
            end if
        end for
        for cada jogador i em P do
            if jogador apostou em b then
                rhoi = rhoi + Bib * wb
            end if
            if rhoi = 0 then
                remova jogador i do conjunto P
                crie um novo jogador e insira em P
            end if
        end for
        if best > f(x*) then
            x* = Tb
        end if
    end for

### Algorithm - Phase 2 ###

    for cada iteração do
        for cada jogador do
             crie solução s = 0
            for cada bit 1 <= i <= N do
                ative bit i de s com probabilidade p1i
            end for
            avalie f(s)
        end for
    end for
