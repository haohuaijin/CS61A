##########################################################
#                     Calculator                         #
##########################################################

# 1.1
"""
>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
* (+ 1 2 3 4)

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
* (+ 1 (* 2 3))
"""


# 1.2
"""
(+ (- 2 4) 6 8)

i. Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))

ii. 
operator: +
the operator is p.first

iii. 
operands: (- 2 4) 6 8
the all operands is p.second
the first operands is p.second.first
"""


################################################################
#                      Evaluation                              #
################################################################

# 2.1
"""
> (+ 2 4 6 8)
calc_eval: 5 times
calc_apply: 1 time

> (+ 2 (* 4 (- 6 8)))
calc_eval: 9 times
calc_apply: 3 times

"""

# 2.2
"""
i. 
yes
because the < > = have the same struct like the + - * /

ii. 
!yes 
!because the and has the same struct like + - * /

iii.
exp.first == 'and'
"""


#####################################################
#                  List Quenstions                  #
#####################################################

# 3.1
"""
(define
    (replicate x n)
    (cond 
        ((equal? n 1) (cons x nil))
        (else 
            (cons x (replicate x (- n 1)))
        )
    )
)
"""


#! 3.2 haven't check the correct
"""
(define (my-append a b)
    (if (null? a) 
        b 
        (cons (car a) (my-append (cdr a) b))
    )
)

(define (uncompress s)
    (cond 
        ((equal? s nil) nil)
        (else
            (my-append (replicate s.first.first s.first.second) (uncompress s.second))
        )
    )
)
"""

#! 3.3
"""
(define (map fn lst)
    (cond 
        ((equal? lst nil) nil)    
        (else
            (cons (fn lst.first) (map fn lst.second))
        )
    )
)
"""

#! 3.4
"""
(define (make-tree label branches) (cons label branches)) 

(define (label tree) 
    tree.first
)

(define (branches tree)
    tree.second
)
"""


#! 3.5
"""
(define (tree-sum tree)
    (cond
        ((equal? (branches tree) nil) (label tree))
        (else 
            (helper (map tree-sum (branches tree)))
        ) 
    )

)
(define (helper lst)
    (cond
        ((equal? lst nil) 0)
        (else
            (+ lst.first (helper lst.second))
        )
    )
)
"""

