# Abstract
We present and analyze PackIt!, a turn-based game consisting of packing rectangles on an n × n grid. PackIt! can be easily played on paper, either as a competitive two-player game or in solitaire fashion. On the t-th turn, a rectangle of area t or t+1 must be placed in the grid. In the two-player format of PackIt! whichever player places a rectangle last wins, whereas the goal in the solitaire variant is to perfectly pack the n × n grid. We analyze necessary conditions for the existence of a perfect packing over n × n, then present an automated reasoning approach that allows finding perfect games of PackIt! up to n = 50 which includes a novel SAT-encoding technique of independent interest, and conclude by proving an NP-hardness result.

# Author's observation / insight
Thomas Garrison, Marijn J. H. Heule, and Bernardo Subercaseaux are the author of 'PackIt!: Gamified Rectangle Packing.' This problem arises when you sit in front of an empty, square board. You have a million dollars at steak to beat your opponent. You think to yourself, tic-tac-toe is a 'solved' game, meaning that there is always a perfect move you can make to win or tie the game. The same is true for connect four. But not all games are 'solved'. For example, Chess is not a solved game. Can 'PackIt!: Gamified Rectable Packing' be 'solved'? If so, can you ensure yourself victory? This game you are fixated on is a turn based game that starts on a n x n square and each player has to place a rectangle that is t or t + 1 in area. t is the amount of turns in the game so far. n can be up to 50, you won't know for sure. The winner of the game is the one who places the last rectangle in the square. There is also a single player version, where the rules are the same, but you win by perfectly fitting the square with your rectangles. 

### Full Version
https://arxiv.org/abs/2403.12195

### Authors Github
https://github.com/bsubercaseaux/packit

### Thomas Garrison, Marijn J. H. Heule, and Bernardo Subercaseaux. PackIt!: Gamified Rectangle Packing. In 12th International Conference on Fun with Algorithms (FUN 2024). Leibniz International Proceedings in Informatics (LIPIcs), Volume 291, pp. 14:1-14:19, Schloss Dagstuhl – Leibniz-Zentrum für Informatik (2024) https://doi.org/10.4230/LIPIcs.FUN.2024.14
