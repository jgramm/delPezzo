# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:06:21 2016

@author: James
"""

\documentclass[12pt]{article}
\usepackage{amsfonts}

\title{WHAT IS MY TITLE}
\author{James Grammatikos}
\date{\today}



\begin{document}
\maketitle

\fontsize{14}{20}
\selectfont


Goal Check if $D_i = dP_n$ for any divisor $D_i$, where $dP_n$ indicates that the divisor is a del Pezzo structure of degree n, where $1 <= n <= 9$. We will not be looking at the trivial n = 9 case.

Definition: a divisor has a del Pezzo structure if it is a non-singular, projective algebraic surface with an ample anti-canonical divisor class. We can obtain these surfaces by blowing up $\mathbb{P}^2$ at n points, for $0 <= n <= 8$

Steps
\begin{itemize}
\item Get $D_i$ from (CY Intersection tensor from (Basis from Toric Divisors))

\item Find anti-canonical bundle $-K$

\item Check $K^2 = \displaystyle \int \limits_{X}(C_1^2(dP_n) \bigwedge dP_n) = 9 - n$

\item Check $\chi(dP_n) = \displaystyle \int \limits_{X} (C_2(dP_n) \bigwedge dP_n) = 3 + n$

\item Check $\chi_h(dP_n) = \displaystyle \int \limits_{X} (Td_2(dP_n) \bigwedge dP_n) = 1$

\item Check $\displaystyle \int \limits_{X} (C_1(dP_n) \bigwedge dP_n \bigwedge D_i) > 0$
\\
\\

\end{itemize}

Intermediate tools
\begin{itemize}
\item Wedge product 

\item Integrate over hypersurfaces

\item Get curves $C = D_i \cap S for D_i \neq S$
\end{itemize}


\end{document}Get curves C = D_i dot S for D_i != S